"""Auto-generated CLI commands for triggers endpoints."""

import json

import click

from pipeline_service_api_reference_client.api.triggers import (
    create_trigger,
    delete_trigger,
    get_list_for_target,
    get_trigger,
    get_trigger_catalog,
    get_trigger_details,
    trigger_event_history,
    update_trigger,
)
from pipeline_service_api_reference_client.models.trigger_filter_properties import TriggerFilterProperties
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Pipeline triggers."""
    pass


@group.command("create-trigger")
@click.option("--target-identifier", default=None)
@click.option("--ignore-error/--no-ignore-error", default=False)
@click.option("--with-service-v2/--no-with-service-v2", default=False)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def create_trigger_cmd(ctx, target_identifier, ignore_error, with_service_v2, body_json):
    """Creates Trigger for triggering target pipeline identifier."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if target_identifier is not None:
        kwargs["target_identifier"] = target_identifier
    kwargs["ignore_error"] = ignore_error
    kwargs["with_service_v2"] = with_service_v2
    try:
        render(create_trigger.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(create_trigger, kwargs)


@group.command("delete-trigger")
@click.argument("trigger_identifier", metavar="TRIGGER_IDENTIFIER")
@click.option("--target-identifier", default=None)
@click.option("--if-match", default=None)
@click.pass_context
def delete_trigger_cmd(ctx, trigger_identifier, target_identifier, if_match):
    """Deletes Trigger by identifier."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["trigger_identifier"] = trigger_identifier
    if target_identifier is not None:
        kwargs["target_identifier"] = target_identifier
    kwargs["if_match"] = if_match if if_match is not None else UNSET
    try:
        render(delete_trigger.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_trigger, kwargs)


@group.command("get-list-for-target")
@click.option("--target-identifier", default=None)
@click.option("--filter", default=None)
@click.option("--page", default=0, type=int)
@click.option("--size", default=25, type=int)
@click.option("--sort", default=None, multiple=True)
@click.option("--search-term", default=None)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def get_list_for_target_cmd(ctx, target_identifier, filter, page, size, sort, search_term, body_json):
    """Gets the paginated list of triggers for accountIdentifier, orgIdentifier, projectIdentifier,"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if target_identifier is not None:
        kwargs["target_identifier"] = target_identifier
    kwargs["filter_"] = filter if filter is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    kwargs["sort"] = sort if sort is not None else UNSET
    kwargs["search_term"] = search_term if search_term is not None else UNSET
    if body_json:
        kwargs["body"] = TriggerFilterProperties.from_dict(json.loads(body_json))
    try:
        render(get_list_for_target.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_list_for_target, kwargs)


@group.command("get-trigger")
@click.argument("trigger_identifier", metavar="TRIGGER_IDENTIFIER")
@click.option("--target-identifier", default=None)
@click.pass_context
def get_trigger_cmd(ctx, trigger_identifier, target_identifier):
    """Gets the trigger by accountIdentifier, orgIdentifier, projectIdentifier, targetIdentifier and"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["trigger_identifier"] = trigger_identifier
    if target_identifier is not None:
        kwargs["target_identifier"] = target_identifier
    try:
        render(get_trigger.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_trigger, kwargs)


@group.command("get-trigger-catalog")
@click.pass_context
def get_trigger_catalog_cmd(ctx):
    """Lists all Triggers"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    try:
        render(get_trigger_catalog.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_trigger_catalog, kwargs)


@group.command("get-trigger-details")
@click.argument("trigger_identifier", metavar="TRIGGER_IDENTIFIER")
@click.option("--target-identifier", default=None)
@click.pass_context
def get_trigger_details_cmd(ctx, trigger_identifier, target_identifier):
    """Fetches Trigger details for a specific accountIdentifier, orgIdentifier, projectIdentifier,"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["trigger_identifier"] = trigger_identifier
    if target_identifier is not None:
        kwargs["target_identifier"] = target_identifier
    try:
        render(get_trigger_details.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_trigger_details, kwargs)


@group.command("trigger-event-history")
@click.argument("trigger_identifier", metavar="TRIGGER_IDENTIFIER")
@click.option("--target-identifier", default=None)
@click.option("--search-term", default=None)
@click.option("--page", default=0, type=int)
@click.option("--size", default=10, type=int)
@click.option("--sort", default=None, multiple=True)
@click.pass_context
def trigger_event_history_cmd(ctx, trigger_identifier, target_identifier, search_term, page, size, sort):
    """Get event history for a trigger"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["trigger_identifier"] = trigger_identifier
    if target_identifier is not None:
        kwargs["target_identifier"] = target_identifier
    kwargs["search_term"] = search_term if search_term is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    kwargs["sort"] = sort if sort is not None else UNSET
    try:
        render(trigger_event_history.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(trigger_event_history, kwargs)


@group.command("update-trigger")
@click.argument("trigger_identifier", metavar="TRIGGER_IDENTIFIER")
@click.option("--target-identifier", default=None)
@click.option("--ignore-error/--no-ignore-error", default=False)
@click.option("--if-match", default=None)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def update_trigger_cmd(ctx, trigger_identifier, target_identifier, ignore_error, if_match, body_json):
    """Updates trigger for pipeline with target pipeline identifier."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["trigger_identifier"] = trigger_identifier
    if target_identifier is not None:
        kwargs["target_identifier"] = target_identifier
    kwargs["ignore_error"] = ignore_error
    kwargs["if_match"] = if_match if if_match is not None else UNSET
    try:
        render(update_trigger.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_trigger, kwargs)

