"""Auto-generated CLI commands for pipeline_input_set endpoints."""

import json

import click

from pipeline_service_api_reference_client.api.pipeline_input_set import (
    delete_input_set,
    get_batch_input_sets_metadata,
    get_bulk_input_sets,
    get_input_set,
    get_overlay_input_set,
    list_input_set,
    merge_input_sets,
    post_overlay_input_set,
    put_overlay_input_set,
    runtime_input_template,
    update_input_set_git_details,
)
from pipeline_service_api_reference_client.models.batch_input_sets_api_request import BatchInputSetsAPIRequest
from pipeline_service_api_reference_client.models.bulk_input_sets_api_request import BulkInputSetsAPIRequest
from pipeline_service_api_reference_client.models.input_set_template_request import InputSetTemplateRequest
from pipeline_service_api_reference_client.models.merge_input_set_request import MergeInputSetRequest
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Pipeline input sets."""
    pass


@group.command("delete-input-set")
@click.argument("input_set_identifier", metavar="INPUT_SET_IDENTIFIER")
@click.option("--pipeline-identifier", default=None)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--root-folder", default=None)
@click.option("--file-path", default=None)
@click.option("--commit-msg", default=None)
@click.option("--last-object-id", default=None)
@click.option("--if-match", default=None)
@click.pass_context
def delete_input_set_cmd(ctx, input_set_identifier, pipeline_identifier, branch, repo_identifier, root_folder, file_path, commit_msg, last_object_id, if_match):
    """Delete an Input Set"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["input_set_identifier"] = input_set_identifier
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["root_folder"] = root_folder if root_folder is not None else UNSET
    kwargs["file_path"] = file_path if file_path is not None else UNSET
    kwargs["commit_msg"] = commit_msg if commit_msg is not None else UNSET
    kwargs["last_object_id"] = last_object_id if last_object_id is not None else UNSET
    kwargs["if_match"] = if_match if if_match is not None else UNSET
    try:
        render(delete_input_set.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_input_set, kwargs)


@group.command("get-batch-input-sets-metadata")
@click.option("--page-index", default=0, type=int)
@click.option("--page-size", default=20, type=int)
@click.option("--search-term", default=None)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def get_batch_input_sets_metadata_cmd(ctx, page_index, page_size, search_term, body_json):
    """List regular Input Sets for multiple pipelines (excludes overlay input sets)"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if page_index is not None:
        kwargs["page_index"] = page_index
    if page_size is not None:
        kwargs["page_size"] = page_size
    kwargs["search_term"] = search_term if search_term is not None else UNSET
    if body_json:
        kwargs["body"] = BatchInputSetsAPIRequest.from_dict(json.loads(body_json))
    try:
        render(get_batch_input_sets_metadata.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_batch_input_sets_metadata, kwargs)


@group.command("get-bulk-input-sets")
@click.option("--pipeline-identifier", default=None)
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def get_bulk_input_sets_cmd(ctx, pipeline_identifier, body_json):
    """Get multiple input sets by identifiers (non-deleted only)"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["body"] = BulkInputSetsAPIRequest.from_dict(json.loads(body_json))
    try:
        render(get_bulk_input_sets.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_bulk_input_sets, kwargs)


@group.command("get-input-set")
@click.argument("input_set_identifier", metavar="INPUT_SET_IDENTIFIER")
@click.option("--pipeline-identifier", default=None)
@click.option("--pipeline-branch", default=None)
@click.option("--pipeline-repo-id", default=None)
@click.option("--load-from-fallback-branch/--no-load-from-fallback-branch", default=False)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--load-from-cache", default="false")
@click.pass_context
def get_input_set_cmd(ctx, input_set_identifier, pipeline_identifier, pipeline_branch, pipeline_repo_id, load_from_fallback_branch, branch, repo_identifier, get_default_from_other_repo, load_from_cache):
    """Fetch an Input Set"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["input_set_identifier"] = input_set_identifier
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["pipeline_branch"] = pipeline_branch if pipeline_branch is not None else UNSET
    kwargs["pipeline_repo_id"] = pipeline_repo_id if pipeline_repo_id is not None else UNSET
    kwargs["load_from_fallback_branch"] = load_from_fallback_branch
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    if load_from_cache is not None:
        kwargs["load_from_cache"] = load_from_cache
    try:
        render(get_input_set.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_input_set, kwargs)


@group.command("get-overlay-input-set")
@click.argument("input_set_identifier", metavar="INPUT_SET_IDENTIFIER")
@click.option("--pipeline-identifier", default=None)
@click.option("--pipeline-branch", default=None)
@click.option("--pipeline-repo-id", default=None)
@click.option("--load-from-fallback-branch/--no-load-from-fallback-branch", default=False)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--load-from-cache", default="false")
@click.pass_context
def get_overlay_input_set_cmd(ctx, input_set_identifier, pipeline_identifier, pipeline_branch, pipeline_repo_id, load_from_fallback_branch, branch, repo_identifier, get_default_from_other_repo, load_from_cache):
    """Gets an Overlay Input Set by identifier"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["input_set_identifier"] = input_set_identifier
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["pipeline_branch"] = pipeline_branch if pipeline_branch is not None else UNSET
    kwargs["pipeline_repo_id"] = pipeline_repo_id if pipeline_repo_id is not None else UNSET
    kwargs["load_from_fallback_branch"] = load_from_fallback_branch
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    if load_from_cache is not None:
        kwargs["load_from_cache"] = load_from_cache
    try:
        render(get_overlay_input_set.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_overlay_input_set, kwargs)


@group.command("list-input-set")
@click.option("--page-index", default=0, type=int)
@click.option("--page-size", default=100, type=int)
@click.option("--pipeline-identifier", default=None)
@click.option("--input-set-type", default="ALL")
@click.option("--search-term", default=None)
@click.option("--sort-orders", default=None, multiple=True)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.pass_context
def list_input_set_cmd(ctx, page_index, page_size, pipeline_identifier, input_set_type, search_term, sort_orders, branch, repo_identifier, get_default_from_other_repo):
    """List Input Sets"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if page_index is not None:
        kwargs["page_index"] = page_index
    if page_size is not None:
        kwargs["page_size"] = page_size
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    if input_set_type is not None:
        kwargs["input_set_type"] = input_set_type
    kwargs["search_term"] = search_term if search_term is not None else UNSET
    kwargs["sort_orders"] = sort_orders if sort_orders is not None else UNSET
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    try:
        render(list_input_set.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_input_set, kwargs)


@group.command("merge-input-sets")
@click.option("--pipeline-identifier", default=None)
@click.option("--pipeline-branch", default=None)
@click.option("--pipeline-repo-id", default=None)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--load-from-cache", default="false")
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def merge_input_sets_cmd(ctx, pipeline_identifier, pipeline_branch, pipeline_repo_id, branch, repo_identifier, get_default_from_other_repo, load_from_cache, body_json):
    """Merge given Input Sets into a single Runtime Input YAML"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["pipeline_branch"] = pipeline_branch if pipeline_branch is not None else UNSET
    kwargs["pipeline_repo_id"] = pipeline_repo_id if pipeline_repo_id is not None else UNSET
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    if load_from_cache is not None:
        kwargs["load_from_cache"] = load_from_cache
    kwargs["body"] = MergeInputSetRequest.from_dict(json.loads(body_json))
    try:
        render(merge_input_sets.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(merge_input_sets, kwargs)


@group.command("post-overlay-input-set")
@click.option("--pipeline-identifier", default=None)
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
def post_overlay_input_set_cmd(ctx, pipeline_identifier, branch, repo_identifier, root_folder, file_path, commit_msg, is_new_branch, base_branch, connector_ref, store_type, repo_name, is_harness_code_repo, body_json):
    """Create an Overlay Input Set for a pipeline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
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
        render(post_overlay_input_set.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(post_overlay_input_set, kwargs)


@group.command("put-overlay-input-set")
@click.argument("input_set_identifier", metavar="INPUT_SET_IDENTIFIER")
@click.option("--pipeline-identifier", default=None)
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
def put_overlay_input_set_cmd(ctx, input_set_identifier, pipeline_identifier, branch, repo_identifier, root_folder, file_path, commit_msg, last_object_id, resolved_conflict_commit_id, base_branch, connector_ref, last_commit_id, is_new_branch, is_harness_code_repo, if_match, body_json):
    """Update an Overlay Input Set for a pipeline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["input_set_identifier"] = input_set_identifier
    if pipeline_identifier is not None:
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
        render(put_overlay_input_set.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(put_overlay_input_set, kwargs)


@group.command("runtime-input-template")
@click.option("--pipeline-identifier", default=None)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--load-from-cache", default="false")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def runtime_input_template_cmd(ctx, pipeline_identifier, branch, repo_identifier, get_default_from_other_repo, load_from_cache, body_json):
    """Fetch Runtime Input Template"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    if load_from_cache is not None:
        kwargs["load_from_cache"] = load_from_cache
    if body_json:
        kwargs["body"] = InputSetTemplateRequest.from_dict(json.loads(body_json))
    try:
        render(runtime_input_template.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(runtime_input_template, kwargs)


@group.command("update-input-set-git-details")
@click.argument("input_set_identifier", metavar="INPUT_SET_IDENTIFIER")
@click.option("--pipeline-identifier", default=None)
@click.option("--connector-ref", default=None)
@click.option("--repo-name", default=None)
@click.option("--file-path", default=None)
@click.pass_context
def update_input_set_git_details_cmd(ctx, input_set_identifier, pipeline_identifier, connector_ref, repo_name, file_path):
    """Update git-metadata in remote input-set"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["input_set_identifier"] = input_set_identifier
    if pipeline_identifier is not None:
        kwargs["pipeline_identifier"] = pipeline_identifier
    kwargs["connector_ref"] = connector_ref if connector_ref is not None else UNSET
    kwargs["repo_name"] = repo_name if repo_name is not None else UNSET
    kwargs["file_path"] = file_path if file_path is not None else UNSET
    try:
        render(update_input_set_git_details.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_input_set_git_details, kwargs)

