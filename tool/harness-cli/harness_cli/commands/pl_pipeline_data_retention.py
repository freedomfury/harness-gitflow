"""Auto-generated CLI commands for pipeline_data_retention endpoints."""

import click

from pipeline_service_api_reference_client.api.pipeline_data_retention import (
    get_retention_period_in_months,
)

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Data retention settings."""
    pass


@group.command("get-retention-period-in-months")
@click.pass_context
def get_retention_period_in_months_cmd(ctx):
    """Get retention period for pipeline executions"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    try:
        render(get_retention_period_in_months.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_retention_period_in_months, kwargs)

