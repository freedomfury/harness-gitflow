"""Auto-generated CLI commands for triggers_events endpoints."""

import click

from pipeline_service_api_reference_client.api.triggers_events import (
    polled_response_trigger_identifier,
    trigger_event_history_build_source_type,
    trigger_event_history_new,
    trigger_event_history_using_filters,
    trigger_history_event_correlation,
    trigger_history_event_correlation_v2,
)
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Trigger event history."""
    pass


@group.command("polled-response-trigger-identifier")
@click.argument("trigger_identifier", metavar="TRIGGER_IDENTIFIER")
@click.option("--target-identifier", default=None)
@click.pass_context
def polled_response_trigger_identifier_cmd(ctx, trigger_identifier, target_identifier):
    """Get all the polled response for a given trigger"""
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
        render(polled_response_trigger_identifier.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(polled_response_trigger_identifier, kwargs)


@group.command("trigger-event-history-build-source-type")
@click.option("--target-identifier", default=None)
@click.option("--artifact-type", default=None)
@click.option("--search-term", default=None)
@click.option("--page", default=0, type=int)
@click.option("--size", default=10, type=int)
@click.option("--sort", default=None, multiple=True)
@click.pass_context
def trigger_event_history_build_source_type_cmd(ctx, target_identifier, artifact_type, search_term, page, size, sort):
    """Get artifact and manifest trigger event history based on build source type"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["target_identifier"] = target_identifier if target_identifier is not None else UNSET
    kwargs["artifact_type"] = artifact_type if artifact_type is not None else UNSET
    kwargs["search_term"] = search_term if search_term is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    kwargs["sort"] = sort if sort is not None else UNSET
    try:
        render(trigger_event_history_build_source_type.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(trigger_event_history_build_source_type, kwargs)


@group.command("trigger-event-history-new")
@click.argument("trigger_identifier", metavar="TRIGGER_IDENTIFIER")
@click.option("--target-identifier", default=None)
@click.option("--search-term", default=None)
@click.option("--page", default=0, type=int)
@click.option("--size", default=10, type=int)
@click.option("--sort", default=None, multiple=True)
@click.option("--should-send-trigger-payload/--no-should-send-trigger-payload", default=True)
@click.pass_context
def trigger_event_history_new_cmd(ctx, trigger_identifier, target_identifier, search_term, page, size, sort, should_send_trigger_payload):
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
    kwargs["should_send_trigger_payload"] = should_send_trigger_payload
    try:
        render(trigger_event_history_new.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(trigger_event_history_new, kwargs)


@group.command("trigger-event-history-using-filters")
@click.option("--target-identifier", default=None)
@click.option("--trigger-identifier", default=None)
@click.option("--status", default=None, multiple=True)
@click.option("--trigger-type", default=None)
@click.option("--page", default=0, type=int)
@click.option("--size", default=10, type=int)
@click.pass_context
def trigger_event_history_using_filters_cmd(ctx, target_identifier, trigger_identifier, status, trigger_type, page, size):
    """Get event history for a trigger using filters."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if target_identifier is not None:
        kwargs["target_identifier"] = target_identifier
    kwargs["trigger_identifier"] = trigger_identifier if trigger_identifier is not None else UNSET
    kwargs["status"] = status if status is not None else UNSET
    kwargs["trigger_type"] = trigger_type if trigger_type is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    try:
        render(trigger_event_history_using_filters.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(trigger_event_history_using_filters, kwargs)


@group.command("trigger-history-event-correlation")
@click.argument("event_correlation_id", metavar="EVENT_CORRELATION_ID")
@click.option("--page", default=0, type=int)
@click.option("--size", default=10, type=int)
@click.option("--sort", default=None, multiple=True)
@click.pass_context
def trigger_history_event_correlation_cmd(ctx, event_correlation_id, page, size, sort):
    """Get Trigger history event correlation"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["event_correlation_id"] = event_correlation_id
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    kwargs["sort"] = sort if sort is not None else UNSET
    try:
        render(trigger_history_event_correlation.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(trigger_history_event_correlation, kwargs)


@group.command("trigger-history-event-correlation-v2")
@click.argument("event_correlation_id", metavar="EVENT_CORRELATION_ID")
@click.option("--page", default=0, type=int)
@click.option("--size", default=10, type=int)
@click.option("--sort", default=None, multiple=True)
@click.pass_context
def trigger_history_event_correlation_v2_cmd(ctx, event_correlation_id, page, size, sort):
    """Get Trigger history event correlation V2"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["event_correlation_id"] = event_correlation_id
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    kwargs["sort"] = sort if sort is not None else UNSET
    try:
        render(trigger_history_event_correlation_v2.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(trigger_history_event_correlation_v2, kwargs)

