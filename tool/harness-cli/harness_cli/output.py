"""Shared output formatting for CLI commands."""

import json
import sys

import click

try:
    import jq as _jq
except ImportError:
    _jq = None

from api_specification_client.models.usererror_error import UsererrorError

try:
    from pipeline_service_api_reference_client.models.error import Error as PipelineError
    from pipeline_service_api_reference_client.models.failure import Failure as PipelineFailure
except ImportError:
    PipelineError = None
    PipelineFailure = None


def read_body(body_json):
    """Parse a --body value into a dict.

    Accepts an inline JSON string, or ``@path/to/file.json`` to read JSON
    from a file (``@-`` reads from stdin). Returns the parsed object.
    """
    if body_json is None:
        return None
    raw = body_json
    if isinstance(body_json, str) and body_json.startswith("@"):
        path = body_json[1:]
        if path == "-":
            raw = sys.stdin.read()
        else:
            with open(path, "r") as fh:
                raw = fh.read()
    try:
        return json.loads(raw)
    except (ValueError, TypeError) as exc:
        click.echo(f"Invalid JSON body: {exc}", err=True)
        sys.exit(1)


def get_format():
    """Get format expression from current Click context."""
    ctx = click.get_current_context(silent=True)
    if ctx and "format" in ctx.obj:
        return ctx.obj.get("format")
    return None


def apply_format(data, format_expr):
    """Apply jq-style filter to JSON data."""
    if not format_expr:
        return data

    # Try jq Python module first (if installed)
    if _jq is not None:
        try:
            compiled = _jq.compile(format_expr)
            result = compiled.input(data)
            output = result.text()
            return output
        except Exception:
            pass

    # Fallback: subprocess jq (if installed as CLI tool)
    import shutil
    import subprocess
    if shutil.which("jq"):
        try:
            result = subprocess.run(
                ["jq", format_expr],
                input=json.dumps(data),
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            click.echo(f"jq filter failed: {e.stderr if e.stderr else format_expr}", err=True)

    # Final fallback: simple dot notation
    try:
        return _simple_dot_filter(data, format_expr)
    except Exception as e:
        click.echo(f"Format expression not supported (jq not available): {format_expr}", err=True)
        return data


def _simple_dot_filter(data, expr):
    """Simple dot-notation fallback when jq is unavailable."""
    # Support: .field, .[].field, .[0].field
    # Extract multiple comma-separated fields
    parts = [p.strip() for p in expr.split(",")]
    results = []

    for part in parts:
        # Remove leading dot if present
        part = part.lstrip(".")
        # Handle array indexing .[] or .[0]
        if part.startswith("[]"):
            # Apply to all items in list
            field = part[2:]
            if isinstance(data, list):
                results.extend([_get_nested(item, field) for item in data])
        elif part.startswith("[") and "]" in part:
            # Index into list
            bracket_end = part.index("]")
            try:
                idx = int(part[1:bracket_end])
            except ValueError:
                continue
            rest = part[bracket_end + 1:].lstrip(".") if bracket_end + 1 < len(part) else ""
            if isinstance(data, list) and 0 <= idx < len(data):
                results.append(_get_nested(data[idx], rest))
        else:
            # Simple field access
            results.append(_get_nested(data, part))

    if len(results) == 1:
        return str(results[0])
    return "\n".join(str(r) for r in results)


def _get_nested(obj, path):
    """Get nested value from object using dot path."""
    if not path:
        return obj
    current = obj
    for key in path.split("."):
        if key and isinstance(current, dict):
            current = current.get(key)
        elif key and isinstance(current, list):
            try:
                current = current[int(key)]
            except (ValueError, IndexError):
                return ""
    return current if current is not None else ""


def render(response, expected_status=None):
    """Render an SDK response as JSON. Exit with error on failure."""
    format_expr = get_format()
    try:
        status = response.status_code.value
    except Exception:
        status = getattr(response, 'status_code', '???')

    if expected_status and status not in expected_status:
        _print_error(status, response)
        sys.exit(1)

    # Try parsed response first, fall back to raw content if parsing fails
    try:
        parsed = response.parsed
    except Exception:
        # Model parsing failed — output raw JSON from the response
        try:
            import json as _json
            raw = _json.loads(response.content)
            _output(raw, format_expr)
        except Exception:
            click.echo(response.content.decode() if response.content else f"HTTP {status}")
        return
    if parsed is None:
        # Raw content fallback
        try:
            content = response.content.decode()
            if format_expr:
                click.echo(content)
            else:
                click.echo(content)
        except Exception:
            click.echo(f"HTTP {status} (no parseable body)")
        return

    if isinstance(parsed, UsererrorError):
        click.echo(json.dumps({"error": parsed.message, "status": status}, indent=2), err=True)
        sys.exit(1)

    if PipelineError and isinstance(parsed, PipelineError):
        click.echo(json.dumps(_to_dict(parsed), indent=2, default=str), err=True)
        sys.exit(1)

    if PipelineFailure and isinstance(parsed, PipelineFailure):
        click.echo(json.dumps(_to_dict(parsed), indent=2, default=str), err=True)
        sys.exit(1)

    if isinstance(parsed, list):
        data = [_to_dict(item) for item in parsed]
    else:
        data = _to_dict(parsed)

    _output(data, format_expr)


def _output(data, format_expr):
    """Output data, applying format filter if provided."""
    if format_expr:
        formatted = apply_format(data, format_expr)
        click.echo(formatted)
    else:
        click.echo(json.dumps(data, indent=2, default=str))


def render_raw(sdk_module, kwargs):
    """Fallback: re-execute the request via raw httpx when SDK model parsing fails."""
    format_expr = get_format()
    client = kwargs.pop("client")
    # Reconstruct the request using the SDK's _get_kwargs
    try:
        request_kwargs = sdk_module._get_kwargs(**kwargs)
        httpx_client = client.get_httpx_client()
        response = httpx_client.request(**request_kwargs)
        try:
            data = response.json()
            _output(data, format_expr)
        except Exception:
            click.echo(response.text)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def _to_dict(obj):
    """Convert an SDK model to a dict, handling attrs and dataclass objects."""
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    if isinstance(obj, dict):
        return obj
    return str(obj)


def _print_error(status, response):
    """Print error details to stderr."""
    parsed = response.parsed
    if isinstance(parsed, UsererrorError):
        click.echo(json.dumps({"error": parsed.message, "status": status}, indent=2), err=True)
    else:
        try:
            click.echo(f"HTTP {status}: {response.content.decode()}", err=True)
        except Exception:
            click.echo(f"HTTP {status}", err=True)
