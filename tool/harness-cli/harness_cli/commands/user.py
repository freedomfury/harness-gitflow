"""Auto-generated CLI commands for user endpoints."""

import json

import click

from api_specification_client.api.user import (
    create_favorite,
    delete_favorite,
)
from api_specification_client.models.types_favorite_resource import TypesFavoriteResource
from api_specification_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """User favorites."""
    pass


@group.command("create-favorite")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def create_favorite_cmd(ctx, body_json):
    """Create favorite"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if body_json:
        kwargs["body"] = TypesFavoriteResource.from_dict(json.loads(body_json))
    try:
        render(create_favorite.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(create_favorite, kwargs)


@group.command("delete-favorite")
@click.argument("resource_id", metavar="RESOURCE_ID")
@click.option("--resource-type", default=None)
@click.pass_context
def delete_favorite_cmd(ctx, resource_id, resource_type):
    """Delete favorite"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["resource_id"] = resource_id
    kwargs["resource_type"] = resource_type if resource_type is not None else UNSET
    try:
        render(delete_favorite.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_favorite, kwargs)

