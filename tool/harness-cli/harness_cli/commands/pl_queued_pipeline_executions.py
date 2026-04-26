"""Auto-generated CLI commands for queued_pipeline_executions endpoints."""

import json

import click

from pipeline_service_api_reference_client.api.queued_pipeline_executions import (
    bulk_abort_queued_pipelines,
    list_queued_pipelines,
)
from pipeline_service_api_reference_client.models.queued_pipeline_bulk_abort_request import QueuedPipelineBulkAbortRequest
from pipeline_service_api_reference_client.models.queued_pipeline_filter import QueuedPipelineFilter
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Queued pipeline executions."""
    pass


@group.command("bulk-abort-queued-pipelines")
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def bulk_abort_queued_pipelines_cmd(ctx, body_json):
    """Bulk Abort Queued Pipelines"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["body"] = QueuedPipelineBulkAbortRequest.from_dict(json.loads(body_json))
    try:
        render(bulk_abort_queued_pipelines.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(bulk_abort_queued_pipelines, kwargs)


@group.command("list-queued-pipelines")
@click.option("--page", default=0, type=int)
@click.option("--size", default=20, type=int)
@click.option("--search-term", default=None)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def list_queued_pipelines_cmd(ctx, page, size, search_term, body_json):
    """List Queued Pipelines"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    kwargs["search_term"] = search_term if search_term is not None else UNSET
    if body_json:
        kwargs["body"] = QueuedPipelineFilter.from_dict(json.loads(body_json))
    try:
        render(list_queued_pipelines.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_queued_pipelines, kwargs)

