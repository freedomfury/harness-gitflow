"""CLI commands for Harness Platform File Store.

Custom (hand-written) command group. The auto-generator cannot handle the
File Store multipart API correctly because the OpenAPI spec types the `content`
field as an opaque InputStream, and the generated model JSON-encodes it instead
of sending raw bytes. This file wraps the Platform SDK for simple operations
and uses the authenticated httpx client directly for create/update.
"""

import json
import sys

import click
import httpx

from harness_next_gen_software_delivery_platform_api_reference_client.api.file_store import (
    download_file,
    get_file,
    list_files_and_folders,
)

from harness_cli.output import http_error_message, render, render_raw


@click.group("ng-file-store")
def group():
    """Harness Platform File Store (config files, mutex locks)."""
    pass


# ---------------------------------------------------------------------------
# create — POST /file-store (multipart)
# ---------------------------------------------------------------------------

@group.command("create")
@click.argument("identifier")
@click.option("--name", required=True, help="Display name of the file or folder")
@click.option("--type", "type_", required=True, type=click.Choice(["FILE", "FOLDER"]), help="FILE or FOLDER")
@click.option("--parent-identifier", required=True, help="Parent folder identifier (Root for top-level)")
@click.option("--file-usage", default="CONFIG", show_default=True, help="fileUsage field (e.g. CONFIG)")
@click.option("--content", default=None, help="File content (plain text). Omit for folders.")
@click.option("--format", "-f", "format_expr", default=None, help="jq-style filter for output")
@click.pass_context
def create_cmd(ctx, identifier, name, type_, parent_identifier, file_usage, content, format_expr):
    """Create a FILE or FOLDER in the File Store.

    IDENTIFIER is the unique identifier for the file or folder.
    Identifiers may only contain alphanumeric characters, underscores and $.
    Dashes in branch/repo names must be replaced with underscores.

    Exits 0 on success, 1 on DUPLICATE_FIELD (lock already held), 2 on other error.
    """
    if format_expr is not None:
        ctx.obj["format"] = format_expr
    cfg = ctx.obj
    platform_client = cfg["platform_client"]
    account_id = cfg["account_id"]
    org_id = cfg["org_id"]
    project_id = cfg["project_id"]

    # Derive the base URL from the public httpx client attribute (not the SDK's
    # private _base_url field, which could be renamed on regeneration).
    httpx_client = platform_client.get_httpx_client()
    base_url = str(httpx_client.base_url).rstrip("/")

    params = {"accountIdentifier": account_id}
    if org_id:
        params["orgIdentifier"] = org_id
    if project_id:
        params["projectIdentifier"] = project_id

    fields = [
        ("identifier", (None, identifier.encode(), "text/plain")),
        ("name", (None, name.encode(), "text/plain")),
        ("type", (None, type_.encode(), "text/plain")),
        ("parentIdentifier", (None, parent_identifier.encode(), "text/plain")),
        ("fileUsage", (None, file_usage.encode(), "text/plain")),
    ]
    if content is not None:
        fields.append(("content", (None, content.encode("utf-8"), "text/plain")))

    try:
        resp = httpx_client.post(
            f"{base_url}/file-store",
            params=params,
            files=fields,
        )
    except httpx.HTTPError as e:
        click.echo(f"network error: {e}", err=True)
        sys.exit(2)

    if resp.status_code in (200, 201):
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        click.echo(json.dumps(data, indent=2))
    elif resp.status_code == 400:
        try:
            body = resp.json()
        except Exception:
            body = {"raw": resp.text}
        code = body.get("code", "")
        if code == "DUPLICATE_FIELD":
            click.echo(f"conflict: {body.get('message', 'file already exists')}", err=True)
            sys.exit(1)
        click.echo(f"error 400: {json.dumps(body)}", err=True)
        sys.exit(2)
    else:
        click.echo(http_error_message(resp), err=True)
        sys.exit(2)


# ---------------------------------------------------------------------------
# delete-file — DELETE /file-store/{identifier}
# ---------------------------------------------------------------------------

@group.command("delete-file")
@click.argument("identifier")
@click.option("--format", "-f", "format_expr", default=None, help="jq-style filter for output")
@click.pass_context
def delete_file_cmd(ctx, identifier, format_expr):
    """Delete a File or Folder by identifier."""
    if format_expr is not None:
        ctx.obj["format"] = format_expr
    cfg = ctx.obj
    platform_client = cfg["platform_client"]
    httpx_client = platform_client.get_httpx_client()
    base_url = str(httpx_client.base_url).rstrip("/")

    params = {"accountIdentifier": cfg["account_id"]}
    if cfg["org_id"]:
        params["orgIdentifier"] = cfg["org_id"]
    if cfg["project_id"]:
        params["projectIdentifier"] = cfg["project_id"]
    try:
        resp = httpx_client.delete(
            f"{base_url}/file-store/{identifier}",
            params=params,
        )
    except httpx.HTTPError as e:
        click.echo(f"network error: {e}", err=True)
        sys.exit(1)
    if resp.status_code not in (200, 201, 204):
        click.echo(http_error_message(resp), err=True)
        sys.exit(1)
    try:
        data = resp.json()
    except Exception:
        data = {"raw": resp.text}
    click.echo(json.dumps(data, indent=2))


# ---------------------------------------------------------------------------
# download-file — GET /file-store/files/{identifier}/download
# ---------------------------------------------------------------------------

@group.command("download-file")
@click.argument("identifier")
@click.option("--format", "-f", "format_expr", default=None, help="jq-style filter (no-op for raw content)")
@click.pass_context
def download_file_cmd(ctx, identifier, format_expr):
    """Download file content by identifier. Prints raw content to stdout."""
    if format_expr is not None:
        ctx.obj["format"] = format_expr
    cfg = ctx.obj
    dl_kwargs = {
        "identifier": identifier,
        "client": cfg["platform_client"],
        "account_identifier": cfg["account_id"],
    }
    if cfg["org_id"]:
        dl_kwargs["org_identifier"] = cfg["org_id"]
    if cfg["project_id"]:
        dl_kwargs["project_identifier"] = cfg["project_id"]
    try:
        resp = download_file.sync_detailed(**dl_kwargs)
    except httpx.HTTPError as e:
        click.echo(f"network error: {e}", err=True)
        sys.exit(1)
    try:
        status = resp.status_code.value
    except Exception:
        status = resp.status_code
    # Don't write an error body to stdout as though it were file content.
    if status not in (200, 201):
        click.echo(http_error_message(resp), err=True)
        sys.exit(1)
    sys.stdout.buffer.write(resp.content)


# ---------------------------------------------------------------------------
# get-file — GET /file-store/{identifier}
# ---------------------------------------------------------------------------

@group.command("get-file")
@click.argument("identifier")
@click.option("--format", "-f", "format_expr", default=None, help="jq-style filter for output")
@click.pass_context
def get_file_cmd(ctx, identifier, format_expr):
    """Get File or Folder metadata by identifier."""
    if format_expr is not None:
        ctx.obj["format"] = format_expr
    cfg = ctx.obj
    gf_kwargs = {
        "identifier": identifier,
        "client": cfg["platform_client"],
        "account_identifier": cfg["account_id"],
    }
    if cfg["org_id"]:
        gf_kwargs["org_identifier"] = cfg["org_id"]
    if cfg["project_id"]:
        gf_kwargs["project_identifier"] = cfg["project_id"]
    try:
        render(get_file.sync_detailed(**gf_kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_file, gf_kwargs)


# ---------------------------------------------------------------------------
# list — GET /file-store
# ---------------------------------------------------------------------------

@group.command("list")
@click.option("--page-index", default=None, type=int, help="Page index (0-based)")
@click.option("--page-size", default=None, type=int, help="Page size")
@click.option("--format", "-f", "format_expr", default=None, help="jq-style filter for output")
@click.pass_context
def list_cmd(ctx, page_index, page_size, format_expr):
    """List Files and Folders in the File Store."""
    if format_expr is not None:
        ctx.obj["format"] = format_expr
    cfg = ctx.obj
    kwargs = {
        "client": cfg["platform_client"],
        "account_identifier": cfg["account_id"],
    }
    if cfg["org_id"]:
        kwargs["org_identifier"] = cfg["org_id"]
    if cfg["project_id"]:
        kwargs["project_identifier"] = cfg["project_id"]
    if page_index is not None:
        kwargs["page_index"] = page_index
    if page_size is not None:
        kwargs["page_size"] = page_size
    try:
        render(list_files_and_folders.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_files_and_folders, kwargs)
