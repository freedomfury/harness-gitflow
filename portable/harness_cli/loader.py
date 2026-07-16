"""Build Click commands dynamically from the installed Harness SDKs.

This replaces the old ``generate.py`` codegen. Instead of writing Python source
files by string concatenation, we reflect over each SDK endpoint's
``sync_detailed`` signature at runtime and construct real ``click.Command``
objects in memory. The SDK is the single source of truth — no regeneration
step, no generated files, no ``lines.append(...)``.

The discovery helpers (``get_api_groups`` / ``get_endpoints``), the ``SDKS``
config, and the parameter-classification rules are ported from the former
``generate.py`` so that the dynamically-built commands accept the same flags
and produce the same ``kwargs`` as the files the generator used to emit.
"""

import importlib
import inspect
import os
import typing

import click

from harness_cli.output import read_body, render, render_raw


# --- SDK Definitions (ported verbatim from generate.py) ---

SDKS = {
    "code": {
        "api_pkg": "api_specification_client.api",
        "models_pkg": "api_specification_client.models",
        "types_pkg": "api_specification_client.types",
        "prefix": "",  # no prefix for code (original SDK)
        "group_aliases": {
            "repository": "repos",
            "pullreq": "pr",
            "status_checks": "checks",
            "webhook": "webhooks",
        },
        "group_descriptions": {
            "repository": "Repository operations (branches, commits, content, tags, diff, settings)",
            "pullreq": "Pull request operations (create, merge, review, comments)",
            "rules": "Branch/tag protection rules",
            "webhook": "Webhook management and execution history",
            "status_checks": "Status check operations",
            "labels": "Label management",
            "upload": "Artifact upload and download",
            "principals": "Principal/user lookup",
            "resource": "Git resources (gitignore, licenses)",
            "settings": "Space-level settings",
            "user": "User favorites",
            "usergroups": "User group lookup",
        },
    },
    "platform": {
        "api_pkg": "harness_next_gen_software_delivery_platform_api_reference_client.api",
        "models_pkg": "harness_next_gen_software_delivery_platform_api_reference_client.models",
        "types_pkg": "harness_next_gen_software_delivery_platform_api_reference_client.types",
        "prefix": "ng_",
        "cli_prefix": "ng-",
        "client_key": "platform_client",
        # Only surface groups listed here — the Platform spec is huge and most
        # of it is managed by Terraform. file_store is hand-written
        # (commands/ng_file_store.py) because its multipart content field
        # cannot be represented by the generated model.
        "include_groups": [],
        "group_aliases": {
            "file_store": "file-store",
        },
        "group_descriptions": {
            "file_store": "Harness Platform File Store (config files, mutex locks)",
        },
    },
    "pipeline": {
        "api_pkg": "pipeline_service_api_reference_client.api",
        "models_pkg": "pipeline_service_api_reference_client.models",
        "types_pkg": "pipeline_service_api_reference_client.types",
        "prefix": "pl_",  # file prefix to avoid name collisions with code SDK
        "cli_prefix": "pl-",
        "group_aliases": {
            "pipeline_execute": "execute",
            "pipeline_execution_details": "executions",
            "pipeline_input_set": "input-sets",
            "pipeline_dashboard": "dashboard",
            "pipeline_data_retention": "retention",
            "pipeline_refresh": "refresh",
            "queued_pipeline_executions": "queued",
            "triggers_events": "trigger-events",
            "webhook_triggers": "webhook-triggers",
            "filter_": "filters",
            "branch_sequences": "branch-sequences",
        },
        "group_descriptions": {
            "pipeline": "Pipeline CRUD operations",
            "pipeline_execute": "Pipeline execution (run, retry, rerun, stages)",
            "pipeline_execution_details": "Execution details (status, graph, logs, list)",
            "pipeline_input_set": "Pipeline input sets",
            "pipeline_dashboard": "Pipeline dashboard",
            "pipeline_data_retention": "Data retention settings",
            "pipeline_refresh": "Pipeline template refresh",
            "queued_pipeline_executions": "Queued pipeline executions",
            "triggers": "Pipeline triggers",
            "triggers_events": "Trigger event history",
            "webhook_triggers": "Webhook trigger processing",
            "filter_": "Pipeline filters",
            "branch_sequences": "Branch sequences",
            "approvals": "Approval operations",
        },
    },
}

# Common params injected from config — never exposed as CLI flags
COMMON_PARAMS = {"account_identifier", "org_identifier", "project_identifier", "client"}

# SDK defaults that break the live API — override with UNSET
BAD_DEFAULTS = {
    "max_divergence": 0,
}

# Placeholder strings the spec uses for "server decides" — override with UNSET
PLACEHOLDER_DEFAULTS = ["{Repository Default Branch}"]

# Body model types we never construct (the raw request is sent instead)
_SKIP_BODY_TYPES = {"Unset", "Any", "None"}


# --- Discovery (ported from generate.py) ---

def get_api_groups(sdk_config):
    """Discover all API groups in the SDK."""
    api_dir = os.path.join(
        os.path.dirname(importlib.import_module(sdk_config["api_pkg"]).__file__)
    )
    return sorted(
        d for d in os.listdir(api_dir)
        if os.path.isdir(os.path.join(api_dir, d)) and d != "__pycache__"
    )


def get_endpoints(sdk_config, group):
    """Get all endpoint modules in a group."""
    group_pkg = f"{sdk_config['api_pkg']}.{group}"
    group_dir = os.path.dirname(importlib.import_module(group_pkg).__file__)
    return sorted(
        f[:-3] for f in os.listdir(group_dir)
        if f.endswith(".py") and f != "__init__.py"
    )


# --- Parameter classification (mirrors generate.py's analyze/param_to_click) ---

def _type_components(ann):
    """Flatten an annotation into its component types (e.g. ``int | Unset`` -> ``(int, Unset)``)."""
    if ann is None:
        return ()
    args = typing.get_args(ann)
    return args if args else (ann,)


def _is_unset_annotation(comps):
    """True if the annotation references the SDK's Unset sentinel type."""
    return any(getattr(c, "__name__", "") == "Unset" for c in comps)


def _needs_unset(name, has_default, default):
    """Replicates generate.py's needs_unset: when to send UNSET rather than a value/default."""
    if not has_default:
        return False
    if name in BAD_DEFAULTS and default == BAD_DEFAULTS[name]:
        return True
    if isinstance(default, str) and default in PLACEHOLDER_DEFAULTS:
        return True
    # Non-primitive defaults (the UNSET sentinel, enums, models, ...) must be overridden
    if type(default).__name__ not in ("int", "float", "str", "bool", "NoneType"):
        return True
    return False


def _resolve_body_class(ann):
    """Extract the request-body model class from a body annotation, or None."""
    for c in _type_components(ann):
        if isinstance(c, type) and c.__name__ not in _SKIP_BODY_TYPES:
            return c
    return None


def _classify(name, param):
    """Classify one ``sync_detailed`` parameter.

    Returns the SDK name, the Click-facing name, the decorator kind, and the
    kwargs-assignment kind. The two "kind" chains are independent on purpose,
    matching the generator: a parameter can be decorated as one thing (e.g. a
    list with ``multiple=True``) while its kwargs are assigned another way (e.g.
    ``x if x is not None else UNSET`` when it also ``needs_unset``).
    """
    ann = param.annotation if param.annotation is not inspect.Parameter.empty else None
    comps = _type_components(ann)
    has_default = param.default is not inspect.Parameter.empty
    default = param.default if has_default else None

    is_bool = bool in comps
    is_int = int in comps and not is_bool
    is_list = any(typing.get_origin(c) is list or c is list for c in comps)
    is_unset = _is_unset_annotation(comps)
    needs_unset = _needs_unset(name, has_default, default)

    clean_name = name.rstrip("_")  # range_ -> range, format_ -> format

    is_positional = (
        not has_default
        and param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        and name != "body"
        and not is_bool
        and not is_unset
    )

    # Decorator kind — precedence: positional(argument) > bool > int > list > str
    if is_positional:
        decor = "argument"
    elif is_bool:
        decor = "bool"
    elif is_int:
        decor = "int"
    elif is_list:
        decor = "list"
    else:
        decor = "str"

    # Kwargs kind — precedence: positional > unset > bool > list > default
    if is_positional:
        kw = "positional"
    elif needs_unset:
        kw = "unset"
    elif is_bool:
        kw = "bool"
    elif is_list:
        kw = "list"
    else:
        kw = "default"

    return {
        "sdk_name": name,
        "clean_name": clean_name,
        "cli_name": clean_name.replace("_", "-"),
        "has_default": has_default,
        "default": default,
        "needs_unset": needs_unset,
        "decor": decor,
        "kw": kw,
    }


def _click_param(c):
    """Build the ``click.Option`` / ``click.Argument`` for one classified param."""
    if c["decor"] == "argument":
        return click.Argument(
            [c["clean_name"]],
            metavar=c["clean_name"].upper().replace("-", "_"),
        )

    flag = f"--{c['cli_name']}"
    if c["decor"] == "bool":
        default = c["default"] if (c["has_default"] and isinstance(c["default"], bool)) else False
        return click.Option([f"{flag}/--no-{c['cli_name']}"], default=default)
    if c["decor"] == "int":
        default = c["default"] if (c["has_default"] and not c["needs_unset"]) else None
        return click.Option([flag], default=default, type=int)
    if c["decor"] == "list":
        return click.Option([flag], default=None, multiple=True)

    # str / default
    if c["has_default"] and not c["needs_unset"]:
        dv = c["default"]
        if isinstance(dv, str):
            pass
        elif dv is None or str(dv).startswith("<"):
            dv = None
    else:
        dv = None
    return click.Option([flag], default=dv)


# --- Command + group construction ---

def build_command(op_module, client_key, unset):
    """Reflect over ``op_module.sync_detailed`` and return a ``click.Command``."""
    func = getattr(op_module, "sync_detailed", None)
    if func is None:
        return None

    sig = inspect.signature(func)
    short_name = op_module.__name__.rsplit(".", 1)[-1]
    doc = (func.__doc__ or "").strip()
    help_text = doc.split("\n")[0] if doc else short_name.replace("_", " ").title()
    cmd_name = short_name.replace("_", "-")

    classified = []
    for pname, param in sig.parameters.items():
        if pname in COMMON_PARAMS or pname == "body":
            continue
        classified.append(_classify(pname, param))

    body_param = sig.parameters.get("body")
    body_cls = None
    body_required = False
    if body_param is not None:
        ann = body_param.annotation if body_param.annotation is not inspect.Parameter.empty else None
        body_cls = _resolve_body_class(ann)
        body_required = body_param.default is inspect.Parameter.empty

    # If the endpoint takes a body we can't model (e.g. `body: Any` for raw
    # uploads), the reflected command can't build it correctly — skip it rather
    # than advertise a --body that's silently dropped. Hand-write it instead
    # (see commands/ng_file_store.py for the pattern).
    if body_param is not None and body_cls is None:
        click.echo(
            f"warning: skipping {short_name}: unresolvable request-body type "
            "(needs a hand-written command)",
            err=True,
        )
        return None

    # Positional arguments first (parsed in this order), then options, then body.
    click_params = [_click_param(c) for c in classified if c["decor"] == "argument"]
    click_params += [_click_param(c) for c in classified if c["decor"] != "argument"]
    if body_param is not None:
        body_help = "JSON request body (or @file.json, or - for stdin)"
        if body_required:
            click_params.append(click.Option(["--body", "body_json"], required=True, help=body_help))
        else:
            click_params.append(click.Option(["--body", "body_json"], default=None, help=body_help))

    # Capture in closure to keep the callback self-contained.
    rules = classified
    bcls = body_cls
    breq = body_required
    has_body = body_param is not None

    def callback(ctx, **opts):
        kwargs = {
            "client": ctx.obj[client_key],
            "account_identifier": ctx.obj["account_id"],
        }
        if ctx.obj["org_id"]:
            kwargs["org_identifier"] = ctx.obj["org_id"]
        if ctx.obj["project_id"]:
            kwargs["project_identifier"] = ctx.obj["project_id"]
        for c in rules:
            val = opts.get(c["clean_name"])
            kind = c["kw"]
            if kind == "positional":
                kwargs[c["sdk_name"]] = val
            elif kind == "unset":
                kwargs[c["sdk_name"]] = val if val is not None else unset
            elif kind == "bool":
                kwargs[c["sdk_name"]] = val
            elif kind == "list":
                if val:
                    kwargs[c["sdk_name"]] = list(val)
            else:  # default
                if val is not None:
                    kwargs[c["sdk_name"]] = val

        if has_body and bcls is not None:
            body_json = opts.get("body_json")
            if breq or body_json:
                kwargs["body"] = bcls.from_dict(read_body(body_json))

        try:
            render(func(**kwargs))
        except (ValueError, TypeError, KeyError, AttributeError):
            render_raw(op_module, kwargs)

    callback = click.pass_context(callback)
    return click.Command(name=cmd_name, params=click_params, callback=callback, help=help_text)


class LazyGroup(click.Group):
    """A ``click.Group`` that builds its commands on first access.

    Keeping endpoint import + command construction lazy means ``harness-cli --help``
    only walks the SDK directories for group names, and a single invocation only
    imports the endpoints of the group it touches.
    """

    def __init__(self, *args, loader=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._loader = loader
        self._loaded = False

    def _ensure_loaded(self):
        if not self._loaded:
            self._loaded = True
            if self._loader:
                for cmd in self._loader():
                    self.add_command(cmd)

    def list_commands(self, ctx):
        self._ensure_loaded()
        return super().list_commands(ctx)

    def get_command(self, ctx, cmd_name):
        self._ensure_loaded()
        return super().get_command(ctx, cmd_name)

    def resolve_command(self, ctx, args):
        self._ensure_loaded()
        return super().resolve_command(ctx, args)


def _client_key_for(sdk_name):
    cfg = SDKS[sdk_name]
    return cfg.get("client_key", "pipeline_client" if sdk_name == "pipeline" else "client")


def _make_loader(sdk_name, group):
    """Return a zero-arg callable that builds every command for one group."""
    sdk_config = SDKS[sdk_name]
    client_key = _client_key_for(sdk_name)
    types_pkg = sdk_config["types_pkg"]
    api_pkg = sdk_config["api_pkg"]

    def load():
        try:
            unset = getattr(importlib.import_module(types_pkg), "UNSET")
        except (ImportError, AttributeError):
            unset = None
        commands = []
        for endpoint in get_endpoints(sdk_config, group):
            try:
                op = importlib.import_module(f"{api_pkg}.{group}.{endpoint}")
            except Exception as e:
                click.echo(f"warning: skipped endpoint {group}.{endpoint}: {e}", err=True)
                continue
            cmd = build_command(op, client_key, unset)
            if cmd is not None:
                commands.append(cmd)
        return commands

    return load


def register_all(cli):
    """Discover every SDK group and register a ``LazyGroup`` for each on ``cli``."""
    for sdk_name, sdk_config in SDKS.items():
        # Skip SDKs that aren't installed (e.g. the Platform client).
        try:
            importlib.import_module(sdk_config["api_pkg"])
        except ImportError:
            continue

        aliases = sdk_config["group_aliases"]
        descriptions = sdk_config.get("group_descriptions", {})
        include_groups = sdk_config.get("include_groups")
        cli_prefix = sdk_config.get("cli_prefix", "")

        for group in get_api_groups(sdk_config):
            if include_groups is not None and group not in include_groups:
                continue

            cli_name = aliases.get(group, group).replace("_", "-")
            if cli_prefix and not cli_name.startswith(cli_prefix):
                cli_name = f"{cli_prefix}{cli_name}"
            description = descriptions.get(group, f"{group} operations")

            cli.add_command(
                LazyGroup(name=cli_name, help=description, loader=_make_loader(sdk_name, group)),
                cli_name,
            )
