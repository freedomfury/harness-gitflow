"""Auto-generated CLI commands for pipeline_execution_details endpoints."""

import json

import click

from pipeline_service_api_reference_client.api.pipeline_execution_details import (
    can_retry_execution,
    get_annotation_full_content,
    get_execution_data,
    get_execution_detail,
    get_execution_detail_v2,
    get_execution_graph,
    get_execution_sub_graph_for_node_execution,
    get_execution_url,
    get_inputset_yaml_v2,
    get_list_of_execution_identifier,
    get_list_of_executions,
    get_list_of_executions_outline,
    get_notes_for_execution,
    get_pipeline_execution_annotations,
    get_ppolicy_evaluation,
    get_workflow_graph,
    update_notes_for_execution,
)
from pipeline_service_api_reference_client.models.filter_properties import FilterProperties
from pipeline_service_api_reference_client.models.pipeline_execution_filter_properties import PipelineExecutionFilterProperties
from pipeline_service_api_reference_client.models.pipeline_execution_outline_filter_dto import PipelineExecutionOutlineFilterDTO
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Execution details (status, graph, logs, list)."""
    pass


@group.command("can-retry-execution")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.pass_context
def can_retry_execution_cmd(ctx, plan_execution_id):
    """Validate if Execution can be retried"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    try:
        render(can_retry_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(can_retry_execution, kwargs)


@group.command("get-annotation-full-content")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.argument("context_id", metavar="CONTEXT_ID")
@click.option("--pipeline-identifier", default=None)
@click.pass_context
def get_annotation_full_content_cmd(ctx, plan_execution_id, context_id, pipeline_identifier):
    """Fetch Full Annotation Content"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    kwargs["context_id"] = context_id
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    try:
        render(get_annotation_full_content.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_annotation_full_content, kwargs)


@group.command("get-execution-data")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.pass_context
def get_execution_data_cmd(ctx, plan_execution_id):
    """Get execution metadata of a pipeline execution"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    try:
        render(get_execution_data.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_execution_data, kwargs)


@group.command("get-execution-detail")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--stage-node-id", default=None)
@click.option("--stage-node-execution-id", default=None)
@click.pass_context
def get_execution_detail_cmd(ctx, plan_execution_id, stage_node_id, stage_node_execution_id):
    """Fetch Execution Details"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    kwargs["stage_node_id"] = stage_node_id if stage_node_id is not None else UNSET
    kwargs["stage_node_execution_id"] = stage_node_execution_id if stage_node_execution_id is not None else UNSET
    try:
        render(get_execution_detail.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_execution_detail, kwargs)


@group.command("get-execution-detail-v2")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--stage-node-id", default=None)
@click.option("--stage-node-execution-id", default=None)
@click.option("--child-stage-node-id", default=None)
@click.option("--render-full-bottom-graph/--no-render-full-bottom-graph", default=False)
@click.pass_context
def get_execution_detail_v2_cmd(ctx, plan_execution_id, stage_node_id, stage_node_execution_id, child_stage_node_id, render_full_bottom_graph):
    """Fetch Execution Details"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    kwargs["stage_node_id"] = stage_node_id if stage_node_id is not None else UNSET
    kwargs["stage_node_execution_id"] = stage_node_execution_id if stage_node_execution_id is not None else UNSET
    kwargs["child_stage_node_id"] = child_stage_node_id if child_stage_node_id is not None else UNSET
    kwargs["render_full_bottom_graph"] = render_full_bottom_graph if render_full_bottom_graph is not None else UNSET
    try:
        render(get_execution_detail_v2.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_execution_detail_v2, kwargs)


@group.command("get-execution-graph")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.pass_context
def get_execution_graph_cmd(ctx, plan_execution_id):
    """Fetch Execution Graph"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    try:
        render(get_execution_graph.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_execution_graph, kwargs)


@group.command("get-execution-sub-graph-for-node-execution")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.argument("node_execution_id", metavar="NODE_EXECUTION_ID")
@click.pass_context
def get_execution_sub_graph_for_node_execution_cmd(ctx, plan_execution_id, node_execution_id):
    """Fetch Execution SubGraph for a Given Retried StepGroup NodeExecution ID"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    kwargs["node_execution_id"] = node_execution_id
    try:
        render(get_execution_sub_graph_for_node_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_execution_sub_graph_for_node_execution, kwargs)


@group.command("get-execution-url")
@click.option("--pipeline-identifier", default=None)
@click.option("--plan-execution-id", default=None)
@click.option("--modules", default=None, multiple=True)
@click.pass_context
def get_execution_url_cmd(ctx, pipeline_identifier, plan_execution_id, modules):
    """Fetch Execution Url"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    if plan_execution_id is not None:
        kwargs["plan_execution_id"] = plan_execution_id
    kwargs["modules"] = modules if modules is not None else UNSET
    try:
        render(get_execution_url.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_execution_url, kwargs)


@group.command("get-inputset-yaml-v2")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--resolve-expressions/--no-resolve-expressions", default=False)
@click.option("--resolve-expressions-type", default="UNKNOWN")
@click.pass_context
def get_inputset_yaml_v2_cmd(ctx, plan_execution_id, resolve_expressions, resolve_expressions_type):
    """Get the Input Set YAML used for given Plan Execution"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    kwargs["resolve_expressions"] = resolve_expressions
    if resolve_expressions_type is not None:
        kwargs["resolve_expressions_type"] = resolve_expressions_type
    try:
        render(get_inputset_yaml_v2.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_inputset_yaml_v2, kwargs)


@group.command("get-list-of-execution-identifier")
@click.option("--pipeline-identifier", default=None)
@click.option("--page", default=0, type=int)
@click.option("--size", default=10, type=int)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--filter-identifier", default=None)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def get_list_of_execution_identifier_cmd(ctx, pipeline_identifier, page, size, branch, repo_identifier, get_default_from_other_repo, filter_identifier, body_json):
    """List Execution Identifier"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier if pipeline_identifier is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    kwargs["filter_identifier"] = filter_identifier if filter_identifier is not None else UNSET
    if body_json:
        kwargs["body"] = FilterProperties.from_dict(json.loads(body_json))
    try:
        render(get_list_of_execution_identifier.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_list_of_execution_identifier, kwargs)


@group.command("get-list-of-executions")
@click.option("--search-term", default=None)
@click.option("--pipeline-identifier", default=None)
@click.option("--page", default=0, type=int)
@click.option("--size", default=10, type=int)
@click.option("--sort", default=None, multiple=True)
@click.option("--filter-identifier", default=None)
@click.option("--show-all-executions/--no-show-all-executions", default=False)
@click.option("--module", default=None)
@click.option("--status", default=None, multiple=True)
@click.option("--my-deployments/--no-my-deployments", default=False)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def get_list_of_executions_cmd(ctx, search_term, pipeline_identifier, page, size, sort, filter_identifier, show_all_executions, module, status, my_deployments, branch, repo_identifier, get_default_from_other_repo, body_json):
    """List Executions"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["search_term"] = search_term if search_term is not None else UNSET
    kwargs["pipeline_identifier"] = pipeline_identifier if pipeline_identifier is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if size is not None:
        kwargs["size"] = size
    kwargs["sort"] = sort if sort is not None else UNSET
    kwargs["filter_identifier"] = filter_identifier if filter_identifier is not None else UNSET
    kwargs["show_all_executions"] = show_all_executions
    kwargs["module"] = module if module is not None else UNSET
    kwargs["status"] = status if status is not None else UNSET
    kwargs["my_deployments"] = my_deployments if my_deployments is not None else UNSET
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    if body_json:
        kwargs["body"] = PipelineExecutionFilterProperties.from_dict(json.loads(body_json))
    try:
        render(get_list_of_executions.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_list_of_executions, kwargs)


@group.command("get-list-of-executions-outline")
@click.option("--last-seen-execution-id", default=None)
@click.option("--last-seen-start-time", default=None, type=int)
@click.option("--size", default=10, type=int)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def get_list_of_executions_outline_cmd(ctx, last_seen_execution_id, last_seen_start_time, size, body_json):
    """List Executions Outline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["last_seen_execution_id"] = last_seen_execution_id if last_seen_execution_id is not None else UNSET
    kwargs["last_seen_start_time"] = last_seen_start_time if last_seen_start_time is not None else UNSET
    if size is not None:
        kwargs["size"] = size
    if body_json:
        kwargs["body"] = PipelineExecutionOutlineFilterDTO.from_dict(json.loads(body_json))
    try:
        render(get_list_of_executions_outline.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_list_of_executions_outline, kwargs)


@group.command("get-notes-for-execution")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.pass_context
def get_notes_for_execution_cmd(ctx, plan_execution_id):
    """Get Notes for a pipelineExecution"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    try:
        render(get_notes_for_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_notes_for_execution, kwargs)


@group.command("get-pipeline-execution-annotations")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--pipeline-identifier", default=None)
@click.pass_context
def get_pipeline_execution_annotations_cmd(ctx, plan_execution_id, pipeline_identifier):
    """Fetch Pipeline Execution Annotations"""
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
        render(get_pipeline_execution_annotations.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_pipeline_execution_annotations, kwargs)


@group.command("get-ppolicy-evaluation")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--page", default=0, type=int)
@click.option("--size", default=None, type=int)
@click.pass_context
def get_ppolicy_evaluation_cmd(ctx, plan_execution_id, page, size):
    """Gets the policy evaluated used for given Plan Execution"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    if page is not None:
        kwargs["page"] = page
    kwargs["size"] = size if size is not None else UNSET
    try:
        render(get_ppolicy_evaluation.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_ppolicy_evaluation, kwargs)


@group.command("get-workflow-graph")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--node-execution-id", default=None)
@click.option("--depth", default=10, type=int)
@click.pass_context
def get_workflow_graph_cmd(ctx, plan_execution_id, node_execution_id, depth):
    """Get workflow graph for visualization"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    kwargs["node_execution_id"] = node_execution_id if node_execution_id is not None else UNSET
    if depth is not None:
        kwargs["depth"] = depth
    try:
        render(get_workflow_graph.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_workflow_graph, kwargs)


@group.command("update-notes-for-execution")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--notes-for-pipeline-execution", default=None)
@click.pass_context
def update_notes_for_execution_cmd(ctx, plan_execution_id, notes_for_pipeline_execution):
    """Updates Notes for a pipelineExecution"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    if notes_for_pipeline_execution is not None:
        kwargs["notes_for_pipeline_execution"] = notes_for_pipeline_execution
    try:
        render(update_notes_for_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_notes_for_execution, kwargs)

