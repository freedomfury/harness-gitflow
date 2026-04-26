"""Auto-generated CLI commands for approvals endpoints."""

import json

import click

from pipeline_service_api_reference_client.api.approvals import (
    add_harness_approval_activity,
)
from pipeline_service_api_reference_client.models.harness_approval_activity_request import HarnessApprovalActivityRequest

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Approval operations."""
    pass


@group.command("add-harness-approval-activity")
@click.argument("approval_instance_id", metavar="APPROVAL_INSTANCE_ID")
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def add_harness_approval_activity_cmd(ctx, approval_instance_id, body_json):
    """Approve or Reject a Pipeline Execution"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["approval_instance_id"] = approval_instance_id
    kwargs["body"] = HarnessApprovalActivityRequest.from_dict(json.loads(body_json))
    try:
        render(add_harness_approval_activity.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(add_harness_approval_activity, kwargs)

