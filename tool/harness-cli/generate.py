#!/usr/bin/env python3
"""Auto-generate Click CLI commands from generated Harness SDKs.

Usage:
    python generate.py                    # generates all groups from all SDKs
    python generate.py --sdk code         # generates only Code SDK groups
    python generate.py --sdk pipeline     # generates only Pipeline SDK groups
    python generate.py --sdk code repos   # generates only the repository group from Code

Output goes to harness_cli/commands/<prefix>_<group>.py, overwriting any existing file.
Also regenerates harness_cli/main.py to wire up all groups.
"""

import argparse
import importlib
import inspect
import os
import re
import sys


# --- SDK Definitions ---

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
        # Only generate commands for these groups — the Platform spec is huge (1.4MB)
        # and most of it is managed by Terraform. Add groups here as needed.
        # file_store is intentionally omitted: its multipart content field requires
        # a custom command (harness_cli/commands/ng_file_store.py) — see notes there.
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

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "harness_cli", "commands")
MAIN_PY = os.path.join(os.path.dirname(__file__), "harness_cli", "main.py")

# Common params injected from config — never exposed as CLI flags
COMMON_PARAMS = {"account_identifier", "org_identifier", "project_identifier", "client"}

# SDK defaults that break the live API — override with UNSET
BAD_DEFAULTS = {
    "max_divergence": 0,
}

# Placeholder strings the spec uses for "server decides" — override with UNSET
PLACEHOLDER_DEFAULTS = ["{Repository Default Branch}"]


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


def analyze_endpoint(sdk_config, group, endpoint_name):
    """Analyze an endpoint's sync_detailed signature."""
    mod = importlib.import_module(f"{sdk_config['api_pkg']}.{group}.{endpoint_name}")
    func = getattr(mod, "sync_detailed", None)
    if func is None:
        return None

    sig = inspect.signature(func)
    params = []
    for name, param in sig.parameters.items():
        if name in COMMON_PARAMS:
            continue
        info = {
            "name": name,
            "kind": param.kind,
            "has_default": param.default is not inspect.Parameter.empty,
            "default": param.default if param.default is not inspect.Parameter.empty else None,
            "annotation": str(param.annotation) if param.annotation != inspect.Parameter.empty else None,
        }
        params.append(info)

    # Get docstring for description
    doc = func.__doc__ or ""
    first_line = doc.strip().split("\n")[0] if doc.strip() else endpoint_name.replace("_", " ").title()

    # Detect body parameter and its type
    body_param = None
    body_type = None
    for p in params:
        if p["name"] == "body":
            body_param = p
            ann = p["annotation"] or ""
            # Try patterns: "module.ClassName | Unset", "module.ClassName", "<class 'module.ClassName'>"
            match = re.search(r"(\w+\.(\w+))\s*\|", ann)
            if not match:
                match = re.search(r"(\w+\.(\w+))'>", ann)
            if not match:
                match = re.search(r"(\w+\.(\w+))$", ann.strip())
            if match:
                body_type = match.group(2)
            break

    return {
        "module": endpoint_name,
        "description": first_line,
        "params": params,
        "body_param": body_param,
        "body_type": body_type,
    }


def param_to_click(p):
    """Convert an SDK parameter to Click option/argument info."""
    name = p["name"]
    clean_name = name.rstrip("_")  # range_ -> range

    ann = p["annotation"] or ""
    is_bool = "bool" in ann
    is_int = "int" in ann and "bool" not in ann
    is_list = "list[" in ann
    is_enum = "Enum" in ann or (".models." in ann and "bool" not in ann and "int" not in ann and "str" not in ann)
    is_unset = "Unset" in ann

    needs_unset = False
    if name in BAD_DEFAULTS and p["has_default"] and p["default"] == BAD_DEFAULTS[name]:
        needs_unset = True
    if p["has_default"] and isinstance(p["default"], str) and p["default"] in PLACEHOLDER_DEFAULTS:
        needs_unset = True
    if p["has_default"]:
        default_type = type(p["default"]).__name__
        if default_type not in ("int", "float", "str", "bool", "NoneType"):
            needs_unset = True

    is_positional = (
        not p["has_default"]
        and p["kind"] == inspect.Parameter.POSITIONAL_OR_KEYWORD
        and name != "body"
        and not is_bool
        and not is_unset
    )

    return {
        "name": name,
        "clean_name": clean_name,
        "cli_name": clean_name.replace("_", "-"),
        "is_positional": is_positional,
        "is_bool": is_bool,
        "is_int": is_int,
        "is_list": is_list,
        "is_enum": is_enum,
        "has_default": p["has_default"],
        "default": p["default"],
        "needs_unset": needs_unset,
    }


def generate_command(endpoint_info, sdk_config, sdk_name):
    """Generate a Click command function for an endpoint."""
    mod_name = endpoint_info["module"]
    cmd_name = mod_name.replace("_", "-")
    description = endpoint_info["description"]
    params = [param_to_click(p) for p in endpoint_info["params"] if p["name"] != "body"]

    # Each SDK may specify its own client key; default to "client" (Code API)
    client_key = SDKS[sdk_name].get("client_key", "pipeline_client" if sdk_name == "pipeline" else "client")

    lines = []
    python_func_name = f"{mod_name}_cmd"

    lines.append(f'@group.command("{cmd_name}")')

    for p in params:
        if p["is_positional"]:
            metavar = p["clean_name"].upper().replace("-", "_")
            lines.append(f'@click.argument("{p["clean_name"]}", metavar="{metavar}")')

    for p in params:
        if p["is_positional"]:
            continue
        flag = f'--{p["cli_name"]}'
        opts = []
        if p["is_bool"]:
            opts.append(f'"--{p["cli_name"]}/--no-{p["cli_name"]}"')
            default = p["default"] if p["has_default"] and isinstance(p["default"], bool) else False
            opts.append(f"default={default}")
        elif p["is_int"]:
            opts.append(f'"{flag}"')
            if p["has_default"] and not p["needs_unset"]:
                opts.append(f"default={p['default']}")
            else:
                opts.append("default=None")
            opts.append("type=int")
        elif p["is_list"]:
            opts.append(f'"{flag}"')
            opts.append("default=None")
            opts.append("multiple=True")
        else:
            opts.append(f'"{flag}"')
            if p["has_default"] and not p["needs_unset"]:
                default = p["default"]
                if isinstance(default, str):
                    opts.append(f'default="{default}"')
                elif default is None or str(default).startswith("<"):
                    opts.append("default=None")
                else:
                    opts.append(f"default={default}")
            else:
                opts.append("default=None")
        lines.append(f'@click.option({", ".join(opts)})')

    has_body = endpoint_info["body_param"] is not None
    body_required = has_body and not endpoint_info["body_param"]["has_default"]
    if has_body:
        if body_required:
            lines.append('@click.option("--body", "body_json", required=True, help="JSON request body (or @file.json, or - for stdin)")')
        else:
            lines.append('@click.option("--body", "body_json", default=None, help="JSON request body (or @file.json, or - for stdin)")')

    lines.append("@click.pass_context")

    func_params = ["ctx"]
    for p in params:
        if p["is_positional"]:
            func_params.append(p["clean_name"])
    for p in params:
        if not p["is_positional"]:
            func_params.append(p["clean_name"])
    if has_body:
        func_params.append("body_json")

    lines.append(f'def {python_func_name}({", ".join(func_params)}):')
    lines.append(f'    """{description}"""')

    lines.append("    kwargs = {")
    lines.append(f'        "client": ctx.obj["{client_key}"],')
    lines.append('        "account_identifier": ctx.obj["account_id"],')
    lines.append('        "org_identifier": ctx.obj["org_id"],')
    lines.append('        "project_identifier": ctx.obj["project_id"],')
    lines.append("    }")

    for p in params:
        if p["is_positional"]:
            if p["name"] != p["clean_name"]:
                lines.append(f'    kwargs["{p["name"]}"] = {p["clean_name"]}')
            else:
                lines.append(f'    kwargs["{p["name"]}"] = {p["name"]}')
        elif p["needs_unset"]:
            lines.append(f'    kwargs["{p["name"]}"] = {p["clean_name"]} if {p["clean_name"]} is not None else UNSET')
        elif p["is_bool"]:
            lines.append(f'    kwargs["{p["name"]}"] = {p["clean_name"]}')
        elif p["is_list"]:
            lines.append(f'    if {p["clean_name"]}:')
            lines.append(f'        kwargs["{p["name"]}"] = list({p["clean_name"]})')
        else:
            lines.append(f'    if {p["clean_name"]} is not None:')
            lines.append(f'        kwargs["{p["name"]}"] = {p["clean_name"]}')

    if has_body:
        body_type = endpoint_info["body_type"]
        skip_types = {"Unset", "Any", "None"}
        if body_type and body_type not in skip_types:
            if body_required:
                lines.append(f'    kwargs["body"] = {body_type}.from_dict(read_body(body_json))')
            else:
                lines.append(f"    if body_json:")
                lines.append(f'        kwargs["body"] = {body_type}.from_dict(read_body(body_json))')

    lines.append(f"    try:")
    lines.append(f"        render({mod_name}.sync_detailed(**kwargs))")
    lines.append(f"    except (ValueError, TypeError, KeyError, AttributeError):")
    lines.append(f"        render_raw({mod_name}, kwargs)")
    lines.append("")

    return "\n".join(lines)


def generate_group_file(sdk_config, group, sdk_name):
    """Generate the full commands file for an API group."""
    aliases = sdk_config["group_aliases"]
    descriptions = sdk_config["group_descriptions"]
    api_pkg = sdk_config["api_pkg"]
    models_pkg = sdk_config["models_pkg"]
    types_pkg = sdk_config["types_pkg"]

    cli_name = aliases.get(group, group)
    description = descriptions.get(group, f"{group} operations")
    endpoints = get_endpoints(sdk_config, group)

    endpoint_infos = []
    for ep in endpoints:
        info = analyze_endpoint(sdk_config, group, ep)
        if info:
            endpoint_infos.append(info)

    if not endpoint_infos:
        return None

    sdk_imports = set()
    model_imports = set()
    needs_json = False

    for info in endpoint_infos:
        sdk_imports.add(info["module"])
        skip_types = {"Unset", "Any", "None"}
        if info["body_type"] and info["body_type"] not in skip_types:
            needs_json = True
            body_type = info["body_type"]
            # Look up actual module name from SDK models package
            try:
                models_mod = importlib.import_module(models_pkg)
                cls = getattr(models_mod, body_type, None)
                if cls and hasattr(cls, "__module__"):
                    snake = cls.__module__.split(".")[-1]
                else:
                    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", body_type).lower()
            except (ImportError, AttributeError):
                snake = re.sub(r"(?<!^)(?=[A-Z])", "_", body_type).lower()
            model_imports.add((snake, body_type))

    needs_unset = any(
        param_to_click(p)["needs_unset"]
        for info in endpoint_infos
        for p in info["params"]
        if p["name"] != "body"
    )

    lines = []
    lines.append(f'"""Auto-generated CLI commands for {group} endpoints."""')
    lines.append("")

    if needs_json:
        lines.append("import json")
        lines.append("")

    lines.append("import click")
    lines.append("")

    lines.append(f"from {api_pkg}.{group} import (")
    for imp in sorted(sdk_imports):
        lines.append(f"    {imp},")
    lines.append(")")

    if model_imports:
        for mod_name, class_name in sorted(model_imports):
            lines.append(f"from {models_pkg}.{mod_name} import {class_name}")

    if needs_unset:
        lines.append(f"from {types_pkg} import UNSET")

    lines.append("")
    lines.append("from harness_cli.output import read_body, render, render_raw")
    lines.append("")
    lines.append("")

    lines.append("@click.group()")
    lines.append("def group():")
    lines.append(f'    """{description}."""')
    lines.append("    pass")
    lines.append("")
    lines.append("")

    for info in endpoint_infos:
        cmd_code = generate_command(info, sdk_config, sdk_name)
        lines.append(cmd_code)
        lines.append("")

    return "\n".join(lines)


def generate_main_py(all_groups_by_sdk):
    """Generate main.py that wires up all groups from all SDKs."""
    lines = []
    lines.append('"""Harness CLI — auto-generated typed pass-through for Harness APIs."""')
    lines.append("")
    lines.append("import click")
    lines.append("")
    lines.append("from harness_cli.config import HarnessConfig")
    lines.append("")

    # Collect all (file_name, cli_name, var_name) tuples
    registrations = []
    for sdk_name, groups in all_groups_by_sdk.items():
        sdk_config = SDKS[sdk_name]
        prefix = sdk_config["prefix"]
        aliases = sdk_config["group_aliases"]
        for group in groups:
            file_name = f"{prefix}{group}"
            cli_name = aliases.get(group, group).replace("_", "-")
            cli_prefix = sdk_config.get("cli_prefix", "pl-" if prefix else "")
            if cli_prefix and not cli_name.startswith(cli_prefix):
                cli_name = f"{cli_prefix}{cli_name}"
            var_name = f"{file_name}_group"
            registrations.append((file_name, cli_name, var_name))
            lines.append(f"from harness_cli.commands.{file_name} import group as {var_name}")

    lines.append("")
    lines.append("")
    lines.append("class LazyConfig(dict):")
    lines.append('    """Lazily resolves Harness config on first access, so --help works without credentials."""')
    lines.append("")
    lines.append("    _resolved = False")
    lines.append("")
    lines.append("    def _resolve(self):")
    lines.append("        if not self._resolved:")
    lines.append("            config = HarnessConfig.from_env()")
    lines.append('            self["client"] = config.get_client()')
    lines.append('            self["pipeline_client"] = config.get_pipeline_client()')
    lines.append('            self["platform_client"] = config.get_platform_client()')
    lines.append('            self["account_id"] = config.account_id')
    lines.append('            self["org_id"] = config.org_id')
    lines.append('            self["project_id"] = config.project_id')
    lines.append('            self["_api_key"] = config.api_key')
    lines.append("            self._resolved = True")
    lines.append("")
    lines.append("    def __getitem__(self, key):")
    lines.append("        self._resolve()")
    lines.append("        return super().__getitem__(key)")
    lines.append("")
    lines.append("")
    lines.append("@click.group()")
    lines.append("@click.option(\"-f\", \"--format\", \"format_expr\", default=None, help=\"jq-style filter for output (e.g., '.[].number, .[].state')\")")
    lines.append("@click.pass_context")
    lines.append("def cli(ctx, format_expr):")
    lines.append('    """Harness CLI — typed pass-through for Harness Code and Pipeline APIs.')
    lines.append("")
    lines.append("    Credentials resolved from environment variables:")
    lines.append("")
    lines.append("      Pipeline:  HARNESS_ACCOUNT_ID, HARNESS_ORG_ID, HARNESS_PROJECT_ID, HARNESS_PASSWORD_API")
    lines.append("")
    lines.append('      Local dev: POC_HARNESS_ACCOUNT_ID, POC_HARNESS_API_KEY"""')
    lines.append("    ctx.ensure_object(dict)")
    lines.append("    ctx.obj = LazyConfig()")
    lines.append("    if format_expr is not None:")
    lines.append('        ctx.obj["format"] = format_expr')
    lines.append("")
    lines.append("")

    for file_name, cli_name, var_name in sorted(registrations, key=lambda x: x[1]):
        lines.append(f'cli.add_command({var_name}, "{cli_name}")')

    # Custom (non-generated) commands
    lines.append("")
    lines.append("# Custom commands (not auto-generated)")
    lines.append("from harness_cli.commands.logs import logs as logs_group")
    lines.append('cli.add_command(logs_group, "logs")')
    lines.append("from harness_cli.commands.run import run as run_cmd")
    lines.append('cli.add_command(run_cmd, "run")')
    lines.append("from harness_cli.commands.ng_file_store import group as ng_file_store_group")
    lines.append('cli.add_command(ng_file_store_group, "ng-file-store")')

    lines.append("")
    lines.append("")
    lines.append('if __name__ == "__main__":')
    lines.append("    cli()")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate Harness CLI from SDKs")
    parser.add_argument("--sdk", choices=[*SDKS.keys(), "all"], default="all",
                        help="Which SDK to generate from (default: all)")
    parser.add_argument("groups", nargs="*", help="Specific groups to generate (default: all)")
    args = parser.parse_args()

    sdk_names = list(SDKS.keys()) if args.sdk == "all" else [args.sdk]

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_groups_by_sdk = {}

    for sdk_name in sdk_names:
        sdk_config = SDKS[sdk_name]
        prefix = sdk_config["prefix"]
        aliases = sdk_config["group_aliases"]
        alias_reverse = {v: k for k, v in aliases.items()}

        all_groups = get_api_groups(sdk_config)

        include_groups = sdk_config.get("include_groups")

        if args.groups:
            groups_to_gen = []
            for r in args.groups:
                if r in alias_reverse:
                    groups_to_gen.append(alias_reverse[r])
                elif r in all_groups:
                    groups_to_gen.append(r)
                else:
                    print(f"Unknown group in {sdk_name}: {r}", file=sys.stderr)
            if not groups_to_gen:
                continue
        elif include_groups is not None:
            # SDK has a whitelist — only generate the listed groups
            groups_to_gen = [g for g in all_groups if g in include_groups]
        else:
            groups_to_gen = all_groups

        print(f"\n=== {sdk_name.upper()} SDK ===")
        generated = []
        for grp in groups_to_gen:
            print(f"  Generating {grp}...", end=" ")
            content = generate_group_file(sdk_config, grp, sdk_name)
            if content is None:
                print("skipped (no endpoints)")
                continue

            file_name = f"{prefix}{grp}"
            out_path = os.path.join(OUTPUT_DIR, f"{file_name}.py")
            with open(out_path, "w") as f:
                f.write(content)
            endpoints = get_endpoints(sdk_config, grp)
            print(f"{len(endpoints)} endpoints -> {file_name}.py")
            generated.append(grp)

        all_groups_by_sdk[sdk_name] = [
            g for g in all_groups
            if os.path.exists(os.path.join(OUTPUT_DIR, f"{prefix}{g}.py"))
        ]

    # Regenerate main.py with all existing groups from all SDKs
    main_content = generate_main_py(all_groups_by_sdk)
    with open(MAIN_PY, "w") as f:
        f.write(main_content)

    total = sum(len(g) for g in all_groups_by_sdk.values())
    print(f"\nGenerated main.py with {total} groups across {len(all_groups_by_sdk)} SDKs")
    print("Done!")


if __name__ == "__main__":
    main()
