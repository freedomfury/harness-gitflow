"""Auto-generated CLI commands for resource endpoints."""

import click

from api_specification_client.api.resource import (
    list_gitignore,
    list_licenses,
)

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Git resources (gitignore, licenses)."""
    pass


@group.command("list-gitignore")
@click.pass_context
def list_gitignore_cmd(ctx):
    """List available gitignore names"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    try:
        render(list_gitignore.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_gitignore, kwargs)


@group.command("list-licenses")
@click.pass_context
def list_licenses_cmd(ctx):
    """List available license names"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    try:
        render(list_licenses.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_licenses, kwargs)

