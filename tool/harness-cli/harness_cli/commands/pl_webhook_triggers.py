"""Auto-generated CLI commands for webhook_triggers endpoints."""

import click

from pipeline_service_api_reference_client.api.webhook_triggers import (
    fetch_webhook_details,
    fetch_webhook_execution_details,
    fetch_webhook_execution_details_v2,
    process_custom_webhook_event,
    process_custom_webhook_event_v2,
    process_custom_webhook_event_v3,
    process_webhook_event,
)
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Webhook trigger processing."""
    pass


@group.command("fetch-webhook-details")
@click.option("--event-id", default=None)
@click.pass_context
def fetch_webhook_details_cmd(ctx, event_id):
    """Gets webhook event processing details for input eventId."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if event_id is not None:
        kwargs["event_id"] = event_id
    try:
        render(fetch_webhook_details.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(fetch_webhook_details, kwargs)


@group.command("fetch-webhook-execution-details")
@click.argument("event_id", metavar="EVENT_ID")
@click.pass_context
def fetch_webhook_execution_details_cmd(ctx, event_id):
    """Gets webhook event processing details for input eventId."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["event_id"] = event_id
    try:
        render(fetch_webhook_execution_details.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(fetch_webhook_execution_details, kwargs)


@group.command("fetch-webhook-execution-details-v2")
@click.argument("event_id", metavar="EVENT_ID")
@click.pass_context
def fetch_webhook_execution_details_v2_cmd(ctx, event_id):
    """Gets webhook event processing details for input eventId when the trigger is queued and has not"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["event_id"] = event_id
    try:
        render(fetch_webhook_execution_details_v2.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(fetch_webhook_execution_details_v2, kwargs)


@group.command("process-custom-webhook-event")
@click.option("--pipeline-identifier", default=None)
@click.option("--trigger-identifier", default=None)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def process_custom_webhook_event_cmd(ctx, pipeline_identifier, trigger_identifier, body_json):
    """Handles event payload for custom webhook triggers."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier if pipeline_identifier is not None else UNSET
    kwargs["trigger_identifier"] = trigger_identifier if trigger_identifier is not None else UNSET
    try:
        render(process_custom_webhook_event.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(process_custom_webhook_event, kwargs)


@group.command("process-custom-webhook-event-v2")
@click.option("--pipeline-identifier", default=None)
@click.option("--trigger-identifier", default=None)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def process_custom_webhook_event_v2_cmd(ctx, pipeline_identifier, trigger_identifier, body_json):
    """Handles event payload for custom webhook triggers."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier if pipeline_identifier is not None else UNSET
    kwargs["trigger_identifier"] = trigger_identifier if trigger_identifier is not None else UNSET
    try:
        render(process_custom_webhook_event_v2.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(process_custom_webhook_event_v2, kwargs)


@group.command("process-custom-webhook-event-v3")
@click.argument("webhook_token", metavar="WEBHOOK_TOKEN")
@click.option("--pipeline-identifier", default=None)
@click.option("--trigger-identifier", default=None)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def process_custom_webhook_event_v3_cmd(ctx, webhook_token, pipeline_identifier, trigger_identifier, body_json):
    """Handles event payload for custom webhook triggers."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["webhook_token"] = webhook_token
    kwargs["pipeline_identifier"] = pipeline_identifier if pipeline_identifier is not None else UNSET
    kwargs["trigger_identifier"] = trigger_identifier if trigger_identifier is not None else UNSET
    try:
        render(process_custom_webhook_event_v3.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(process_custom_webhook_event_v3, kwargs)


@group.command("process-webhook-event")
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def process_webhook_event_cmd(ctx, body_json):
    """Handles event payload for webhook triggers."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    try:
        render(process_webhook_event.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(process_webhook_event, kwargs)

