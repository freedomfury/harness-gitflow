"""Auto-generated CLI commands for filter_ endpoints."""

import json

import click

from pipeline_service_api_reference_client.api.filter_ import (
    delete_filter,
    get_filter,
    get_filter_list,
    post_filter,
    update_filter,
)
from pipeline_service_api_reference_client.models.filter_ import Filter
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Pipeline filters."""
    pass


@group.command("delete-filter")
@click.argument("identifier", metavar="IDENTIFIER")
@click.option("--type", default=None)
@click.pass_context
def delete_filter_cmd(ctx, identifier, type):
    """Delete a Filter"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["identifier"] = identifier
    if type is not None:
        kwargs["type_"] = type
    try:
        render(delete_filter.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_filter, kwargs)


@group.command("get-filter")
@click.argument("identifier", metavar="IDENTIFIER")
@click.option("--type", default=None)
@click.pass_context
def get_filter_cmd(ctx, identifier, type):
    """Return Filter Details"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["identifier"] = identifier
    if type is not None:
        kwargs["type_"] = type
    try:
        render(get_filter.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_filter, kwargs)


@group.command("get-filter-list")
@click.option("--page-index", default=0, type=int)
@click.option("--page-size", default=100, type=int)
@click.option("--type", default=None)
@click.option("--search-term", default=None)
@click.pass_context
def get_filter_list_cmd(ctx, page_index, page_size, type, search_term):
    """List Filters"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if page_index is not None:
        kwargs["page_index"] = page_index
    if page_size is not None:
        kwargs["page_size"] = page_size
    if type is not None:
        kwargs["type_"] = type
    kwargs["search_term"] = search_term if search_term is not None else UNSET
    try:
        render(get_filter_list.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_filter_list, kwargs)


@group.command("post-filter")
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def post_filter_cmd(ctx, body_json):
    """Create a Filter"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["body"] = Filter.from_dict(json.loads(body_json))
    try:
        render(post_filter.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(post_filter, kwargs)


@group.command("update-filter")
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def update_filter_cmd(ctx, body_json):
    """Update a Filter"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["body"] = Filter.from_dict(json.loads(body_json))
    try:
        render(update_filter.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_filter, kwargs)

