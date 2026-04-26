"""Auto-generated CLI commands for pipeline_execute endpoints."""

import json

import click

from pipeline_service_api_reference_client.api.pipeline_execute import (
    handle_stage_interrupt,
    mark_manual_execution,
    post_execute_stages,
    post_pipeline_execute_with_input_set_list,
    put_handle_interrupt,
    retry_history,
    retry_pipeline_v2,
)
from pipeline_service_api_reference_client.models.manual_execution_request import ManualExecutionRequest
from pipeline_service_api_reference_client.models.merge_input_set_request import MergeInputSetRequest
from pipeline_service_api_reference_client.models.retry_pipeline_request import RetryPipelineRequest
from pipeline_service_api_reference_client.models.run_stage_request import RunStageRequest
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Pipeline execution (run, retry, rerun, stages)."""
    pass


@group.command("handle-stage-interrupt")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.argument("node_execution_id", metavar="NODE_EXECUTION_ID")
@click.option("--interrupt-type", default=None)
@click.pass_context
def handle_stage_interrupt_cmd(ctx, plan_execution_id, node_execution_id, interrupt_type):
    """Handles the interrupt for a given stage in a pipeline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    kwargs["node_execution_id"] = node_execution_id
    if interrupt_type is not None:
        kwargs["interrupt_type"] = interrupt_type
    try:
        render(handle_stage_interrupt.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(handle_stage_interrupt, kwargs)


@group.command("mark-manual-execution")
@click.argument("node_execution_id", metavar="NODE_EXECUTION_ID")
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def mark_manual_execution_cmd(ctx, node_execution_id, body_json):
    """Marks the Manual Execution as fail or resume"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["node_execution_id"] = node_execution_id
    kwargs["body"] = ManualExecutionRequest.from_dict(json.loads(body_json))
    try:
        render(mark_manual_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(mark_manual_execution, kwargs)


@group.command("post-execute-stages")
@click.argument("identifier", metavar="IDENTIFIER")
@click.option("--module-type", default=None)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--use-fqn-if-error/--no-use-fqn-if-error", default=False)
@click.option("--notes-for-pipeline-execution", default="")
@click.option("--input-set-identifiers", default=None, multiple=True)
@click.option("--async-plan-creation/--no-async-plan-creation", default=False)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def post_execute_stages_cmd(ctx, identifier, module_type, branch, repo_identifier, get_default_from_other_repo, use_fqn_if_error, notes_for_pipeline_execution, input_set_identifiers, async_plan_creation, body_json):
    """Execute given Stages of a Pipeline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["identifier"] = identifier
    kwargs["module_type"] = module_type if module_type is not None else UNSET
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    kwargs["use_fqn_if_error"] = use_fqn_if_error
    if notes_for_pipeline_execution is not None:
        kwargs["notes_for_pipeline_execution"] = notes_for_pipeline_execution
    kwargs["input_set_identifiers"] = input_set_identifiers if input_set_identifiers is not None else UNSET
    kwargs["async_plan_creation"] = async_plan_creation
    if body_json:
        kwargs["body"] = RunStageRequest.from_dict(json.loads(body_json))
    try:
        render(post_execute_stages.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(post_execute_stages, kwargs)


@group.command("post-pipeline-execute-with-input-set-list")
@click.argument("identifier", metavar="IDENTIFIER")
@click.option("--module-type", default=None)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--use-fqn-if-error/--no-use-fqn-if-error", default=False)
@click.option("--notes-for-pipeline-execution", default="")
@click.option("--async-plan-creation/--no-async-plan-creation", default=False)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def post_pipeline_execute_with_input_set_list_cmd(ctx, identifier, module_type, branch, repo_identifier, get_default_from_other_repo, use_fqn_if_error, notes_for_pipeline_execution, async_plan_creation, body_json):
    """Execute a Pipeline with Input Set References"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["identifier"] = identifier
    kwargs["module_type"] = module_type if module_type is not None else UNSET
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    kwargs["use_fqn_if_error"] = use_fqn_if_error
    if notes_for_pipeline_execution is not None:
        kwargs["notes_for_pipeline_execution"] = notes_for_pipeline_execution
    kwargs["async_plan_creation"] = async_plan_creation
    kwargs["body"] = MergeInputSetRequest.from_dict(json.loads(body_json))
    try:
        render(post_pipeline_execute_with_input_set_list.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(post_pipeline_execute_with_input_set_list, kwargs)


@group.command("put-handle-interrupt")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--interrupt-type", default=None)
@click.pass_context
def put_handle_interrupt_cmd(ctx, plan_execution_id, interrupt_type):
    """Execute an Interrupt"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    if interrupt_type is not None:
        kwargs["interrupt_type"] = interrupt_type
    try:
        render(put_handle_interrupt.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(put_handle_interrupt, kwargs)


@group.command("retry-history")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--pipeline-identifier", default=None)
@click.pass_context
def retry_history_cmd(ctx, plan_execution_id, pipeline_identifier):
    """Retry History for a given execution"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    try:
        render(retry_history.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(retry_history, kwargs)


@group.command("retry-pipeline-v2")
@click.argument("identifier", metavar="IDENTIFIER")
@click.option("--module-type", default=None)
@click.option("--plan-execution-id", default=None)
@click.option("--retry-stages", default=None, multiple=True)
@click.option("--run-all-stages/--no-run-all-stages", default=True)
@click.option("--notes-for-pipeline-execution", default="")
@click.option("--async-plan-creation/--no-async-plan-creation", default=False)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def retry_pipeline_v2_cmd(ctx, identifier, module_type, plan_execution_id, retry_stages, run_all_stages, notes_for_pipeline_execution, async_plan_creation, body_json):
    """Retry a executed pipeline with Runtime Input YAML V2"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["identifier"] = identifier
    kwargs["module_type"] = module_type if module_type is not None else UNSET
    if plan_execution_id is not None:
        kwargs["plan_execution_id"] = plan_execution_id
    if retry_stages:
        kwargs["retry_stages"] = list(retry_stages)
    kwargs["run_all_stages"] = run_all_stages
    if notes_for_pipeline_execution is not None:
        kwargs["notes_for_pipeline_execution"] = notes_for_pipeline_execution
    kwargs["async_plan_creation"] = async_plan_creation
    if body_json:
        kwargs["body"] = RetryPipelineRequest.from_dict(json.loads(body_json))
    try:
        render(retry_pipeline_v2.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(retry_pipeline_v2, kwargs)

