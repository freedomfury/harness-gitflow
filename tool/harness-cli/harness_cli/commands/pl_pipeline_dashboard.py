"""Auto-generated CLI commands for pipeline_dashboard endpoints."""

import click

from pipeline_service_api_reference_client.api.pipeline_dashboard import (
    get_pipeline_execution,
)

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Pipeline dashboard."""
    pass


@group.command("get-pipeline-execution")
@click.option("--pipeline-identifier", default=None)
@click.option("--module-info", default=None)
@click.option("--start-time", default=None, type=int)
@click.option("--end-time", default=None, type=int)
@click.pass_context
def get_pipeline_execution_cmd(ctx, pipeline_identifier, module_info, start_time, end_time):
    """Fetch Execution Details for an Interval"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    if module_info is not None:
        kwargs["module_info"] = module_info
    if start_time is not None:
        kwargs["start_time"] = start_time
    if end_time is not None:
        kwargs["end_time"] = end_time
    try:
        render(get_pipeline_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_pipeline_execution, kwargs)

