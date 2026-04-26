"""Auto-generated CLI commands for usergroups endpoints."""

import click

from api_specification_client.api.usergroups import (
    list_usergroups,
)
from api_specification_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """User group lookup."""
    pass


@group.command("list-usergroups")
@click.option("--query", default=None)
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.pass_context
def list_usergroups_cmd(ctx, query, page, limit):
    """List usergroups at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["query"] = query if query is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    try:
        render(list_usergroups.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_usergroups, kwargs)

