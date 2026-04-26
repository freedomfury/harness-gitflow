"""Auto-generated CLI commands for principals endpoints."""

import click

from api_specification_client.api.principals import (
    list_principals,
)
from api_specification_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Principal/user lookup."""
    pass


@group.command("list-principals")
@click.option("--query", default=None)
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--type", default=None, multiple=True)
@click.pass_context
def list_principals_cmd(ctx, query, page, limit, type):
    """Args:"""
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
    kwargs["type_"] = type if type is not None else UNSET
    try:
        render(list_principals.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_principals, kwargs)

