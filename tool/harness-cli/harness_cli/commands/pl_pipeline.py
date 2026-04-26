"""Auto-generated CLI commands for pipeline endpoints."""

import json

import click

from pipeline_service_api_reference_client.api.pipeline import (
    convert_pipeline_to_dag,
    create_pipeline_execution_annotations,
    delete_pipeline,
    download_file_using_file_path,
    get_file,
    get_pipeline,
    get_pipeline_list,
    get_pipeline_summary,
    import_pipeline,
    import_pipeline_1,
    post_pipeline,
    update_pipeline,
    update_pipeline_git_details,
)
from pipeline_service_api_reference_client.models.create_annotations_request import CreateAnnotationsRequest
from pipeline_service_api_reference_client.models.pipeline_filter_properties import PipelineFilterProperties
from pipeline_service_api_reference_client.models.pipeline_import_request import PipelineImportRequest
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Pipeline CRUD operations."""
    pass


@group.command("convert-pipeline-to-dag")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.pass_context
def convert_pipeline_to_dag_cmd(ctx, pipeline_identifier):
    """Convert existing pipeline to DAG format"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    try:
        render(convert_pipeline_to_dag.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(convert_pipeline_to_dag, kwargs)


@group.command("create-pipeline-execution-annotations")
@click.option("--account-id", default=None)
@click.option("--plan-execution-id", default=None)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def create_pipeline_execution_annotations_cmd(ctx, account_id, plan_execution_id, body_json):
    """Create/Update Pipeline Annotations"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if account_id is not None:
        kwargs["account_id"] = account_id
    if plan_execution_id is not None:
        kwargs["plan_execution_id"] = plan_execution_id
    kwargs["body"] = CreateAnnotationsRequest.from_dict(json.loads(body_json))
    try:
        render(create_pipeline_execution_annotations.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(create_pipeline_execution_annotations, kwargs)


@group.command("delete-pipeline")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--root-folder", default=None)
@click.option("--file-path", default=None)
@click.option("--commit-msg", default=None)
@click.option("--last-object-id", default=None)
@click.option("--if-match", default=None)
@click.pass_context
def delete_pipeline_cmd(ctx, pipeline_identifier, branch, repo_identifier, root_folder, file_path, commit_msg, last_object_id, if_match):
    """Delete a Pipeline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["root_folder"] = root_folder if root_folder is not None else UNSET
    kwargs["file_path"] = file_path if file_path is not None else UNSET
    kwargs["commit_msg"] = commit_msg if commit_msg is not None else UNSET
    kwargs["last_object_id"] = last_object_id if last_object_id is not None else UNSET
    kwargs["if_match"] = if_match if if_match is not None else UNSET
    try:
        render(delete_pipeline.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_pipeline, kwargs)


@group.command("download-file-using-file-path")
@click.option("--file-path", default=None)
@click.pass_context
def download_file_using_file_path_cmd(ctx, file_path):
    """Download file from GCS using filePath"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if file_path is not None:
        kwargs["file_path"] = file_path
    try:
        render(download_file_using_file_path.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(download_file_using_file_path, kwargs)


@group.command("get-file")
@click.argument("plan_execution_id", metavar="PLAN_EXECUTION_ID")
@click.option("--node-execution-id", default=None)
@click.option("--file-name", default=None)
@click.pass_context
def get_file_cmd(ctx, plan_execution_id, node_execution_id, file_name):
    """Returns a file uploaded or filtered based on the fileIdentifier provided for a given nodeExecutionId"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["plan_execution_id"] = plan_execution_id
    if node_execution_id is not None:
        kwargs["node_execution_id"] = node_execution_id
    if file_name is not None:
        kwargs["file_name"] = file_name
    try:
        render(get_file.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_file, kwargs)


@group.command("get-pipeline")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--get-templates-resolved-pipeline/--no-get-templates-resolved-pipeline", default=False)
@click.option("--load-from-fallback-branch/--no-load-from-fallback-branch", default=False)
@click.option("--validate-async/--no-validate-async", default=False)
@click.option("--load-from-cache", default="false")
@click.pass_context
def get_pipeline_cmd(ctx, pipeline_identifier, branch, repo_identifier, get_default_from_other_repo, get_templates_resolved_pipeline, load_from_fallback_branch, validate_async, load_from_cache):
    """Fetch a Pipeline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    kwargs["get_templates_resolved_pipeline"] = get_templates_resolved_pipeline
    kwargs["load_from_fallback_branch"] = load_from_fallback_branch
    kwargs["validate_async"] = validate_async
    if load_from_cache is not None:
        kwargs["load_from_cache"] = load_from_cache
    try:
        render(get_pipeline.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_pipeline, kwargs)


@group.command("get-pipeline-list")
@click.option("--page", default=0, type=int)
@click.option("--size", default=25, type=int)
@click.option("--sort", default=None, multiple=True)
@click.option("--search-term", default=None)
@click.option("--module", default=None)
@click.option("--filter-identifier", default=None)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--get-distinct-from-branches/--no-get-distinct-from-branches", default=False)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def get_pipeline_list_cmd(ctx, page, size, sort, search_term, module, filter_identifier, branch, repo_identifier, get_default_from_other_repo, get_distinct_from_branches, body_json):
    """List Pipelines"""
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
    kwargs["sort"] = sort if sort is not None else UNSET
    kwargs["search_term"] = search_term if search_term is not None else UNSET
    kwargs["module"] = module if module is not None else UNSET
    kwargs["filter_identifier"] = filter_identifier if filter_identifier is not None else UNSET
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    kwargs["get_distinct_from_branches"] = get_distinct_from_branches if get_distinct_from_branches is not None else UNSET
    if body_json:
        kwargs["body"] = PipelineFilterProperties.from_dict(json.loads(body_json))
    try:
        render(get_pipeline_list.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_pipeline_list, kwargs)


@group.command("get-pipeline-summary")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--load-from-fallback-branch/--no-load-from-fallback-branch", default=False)
@click.option("--load-from-cache", default="false")
@click.pass_context
def get_pipeline_summary_cmd(ctx, pipeline_identifier, branch, repo_identifier, get_default_from_other_repo, load_from_fallback_branch, load_from_cache):
    """Fetch Pipeline Summary"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    kwargs["load_from_fallback_branch"] = load_from_fallback_branch
    if load_from_cache is not None:
        kwargs["load_from_cache"] = load_from_cache
    try:
        render(get_pipeline_summary.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_pipeline_summary, kwargs)


@group.command("import-pipeline")
@click.option("--connector-ref", default=None)
@click.option("--repo-name", default=None)
@click.option("--branch", default=None)
@click.option("--file-path", default=None)
@click.option("--is-force-import/--no-is-force-import", default=False)
@click.option("--is-harness-code-repo/--no-is-harness-code-repo", default=False)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def import_pipeline_cmd(ctx, connector_ref, repo_name, branch, file_path, is_force_import, is_harness_code_repo, body_json):
    """Import and Create Pipeline from Git Repository"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["connector_ref"] = connector_ref if connector_ref is not None else UNSET
    if repo_name is not None:
        kwargs["repo_name"] = repo_name
    if branch is not None:
        kwargs["branch"] = branch
    if file_path is not None:
        kwargs["file_path"] = file_path
    kwargs["is_force_import"] = is_force_import
    kwargs["is_harness_code_repo"] = is_harness_code_repo if is_harness_code_repo is not None else UNSET
    if body_json:
        kwargs["body"] = PipelineImportRequest.from_dict(json.loads(body_json))
    try:
        render(import_pipeline.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(import_pipeline, kwargs)


@group.command("import-pipeline-1")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.option("--connector-ref", default=None)
@click.option("--repo-name", default=None)
@click.option("--branch", default=None)
@click.option("--file-path", default=None)
@click.option("--is-force-import/--no-is-force-import", default=False)
@click.option("--is-harness-code-repo/--no-is-harness-code-repo", default=False)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def import_pipeline_1_cmd(ctx, pipeline_identifier, connector_ref, repo_name, branch, file_path, is_force_import, is_harness_code_repo, body_json):
    """Import and Create Pipeline from Git Repository"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["connector_ref"] = connector_ref if connector_ref is not None else UNSET
    if repo_name is not None:
        kwargs["repo_name"] = repo_name
    if branch is not None:
        kwargs["branch"] = branch
    if file_path is not None:
        kwargs["file_path"] = file_path
    kwargs["is_force_import"] = is_force_import
    kwargs["is_harness_code_repo"] = is_harness_code_repo if is_harness_code_repo is not None else UNSET
    if body_json:
        kwargs["body"] = PipelineImportRequest.from_dict(json.loads(body_json))
    try:
        render(import_pipeline_1.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(import_pipeline_1, kwargs)


@group.command("post-pipeline")
@click.option("--enable-dag/--no-enable-dag", default=False)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--root-folder", default=None)
@click.option("--file-path", default=None)
@click.option("--commit-msg", default=None)
@click.option("--is-new-branch/--no-is-new-branch", default=False)
@click.option("--base-branch", default=None)
@click.option("--connector-ref", default=None)
@click.option("--store-type", default=None)
@click.option("--repo-name", default=None)
@click.option("--is-harness-code-repo/--no-is-harness-code-repo", default=False)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def post_pipeline_cmd(ctx, enable_dag, branch, repo_identifier, root_folder, file_path, commit_msg, is_new_branch, base_branch, connector_ref, store_type, repo_name, is_harness_code_repo, body_json):
    """Create a Pipeline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["enable_dag"] = enable_dag
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["root_folder"] = root_folder if root_folder is not None else UNSET
    kwargs["file_path"] = file_path if file_path is not None else UNSET
    kwargs["commit_msg"] = commit_msg if commit_msg is not None else UNSET
    kwargs["is_new_branch"] = is_new_branch
    kwargs["base_branch"] = base_branch if base_branch is not None else UNSET
    kwargs["connector_ref"] = connector_ref if connector_ref is not None else UNSET
    kwargs["store_type"] = store_type if store_type is not None else UNSET
    kwargs["repo_name"] = repo_name if repo_name is not None else UNSET
    kwargs["is_harness_code_repo"] = is_harness_code_repo if is_harness_code_repo is not None else UNSET
    try:
        render(post_pipeline.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(post_pipeline, kwargs)


@group.command("update-pipeline")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--root-folder", default=None)
@click.option("--file-path", default=None)
@click.option("--commit-msg", default=None)
@click.option("--last-object-id", default=None)
@click.option("--resolved-conflict-commit-id", default=None)
@click.option("--base-branch", default=None)
@click.option("--connector-ref", default=None)
@click.option("--last-commit-id", default=None)
@click.option("--is-new-branch/--no-is-new-branch", default=False)
@click.option("--is-harness-code-repo/--no-is-harness-code-repo", default=False)
@click.option("--if-match", default=None)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def update_pipeline_cmd(ctx, pipeline_identifier, branch, repo_identifier, root_folder, file_path, commit_msg, last_object_id, resolved_conflict_commit_id, base_branch, connector_ref, last_commit_id, is_new_branch, is_harness_code_repo, if_match, body_json):
    """Update a Pipeline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["root_folder"] = root_folder if root_folder is not None else UNSET
    kwargs["file_path"] = file_path if file_path is not None else UNSET
    kwargs["commit_msg"] = commit_msg if commit_msg is not None else UNSET
    kwargs["last_object_id"] = last_object_id if last_object_id is not None else UNSET
    kwargs["resolved_conflict_commit_id"] = resolved_conflict_commit_id if resolved_conflict_commit_id is not None else UNSET
    kwargs["base_branch"] = base_branch if base_branch is not None else UNSET
    kwargs["connector_ref"] = connector_ref if connector_ref is not None else UNSET
    kwargs["last_commit_id"] = last_commit_id if last_commit_id is not None else UNSET
    kwargs["is_new_branch"] = is_new_branch
    kwargs["is_harness_code_repo"] = is_harness_code_repo if is_harness_code_repo is not None else UNSET
    kwargs["if_match"] = if_match if if_match is not None else UNSET
    try:
        render(update_pipeline.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_pipeline, kwargs)


@group.command("update-pipeline-git-details")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.option("--connector-ref", default=None)
@click.option("--repo-name", default=None)
@click.option("--file-path", default=None)
@click.pass_context
def update_pipeline_git_details_cmd(ctx, pipeline_identifier, connector_ref, repo_name, file_path):
    """Update git-metadata in remote pipeline Entity"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["connector_ref"] = connector_ref if connector_ref is not None else UNSET
    kwargs["repo_name"] = repo_name if repo_name is not None else UNSET
    kwargs["file_path"] = file_path if file_path is not None else UNSET
    try:
        render(update_pipeline_git_details.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_pipeline_git_details, kwargs)

