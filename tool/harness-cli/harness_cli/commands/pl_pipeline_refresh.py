"""Auto-generated CLI commands for pipeline_refresh endpoints."""

import click

from pipeline_service_api_reference_client.api.pipeline_refresh import (
    refresh_all_templates_inputs_in_pipeline,
    validate_template_inputs,
)
from pipeline_service_api_reference_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Pipeline template refresh."""
    pass


@group.command("refresh-all-templates-inputs-in-pipeline")
@click.option("--identifier", default=None)
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
@click.option("--load-from-cache", default="false")
@click.pass_context
def refresh_all_templates_inputs_in_pipeline_cmd(ctx, identifier, branch, repo_identifier, root_folder, file_path, commit_msg, last_object_id, resolved_conflict_commit_id, base_branch, connector_ref, last_commit_id, is_new_branch, is_harness_code_repo, load_from_cache):
    """This recursively refresh and update template inputs in pipeline"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["identifier"] = identifier if identifier is not None else UNSET
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
    if load_from_cache is not None:
        kwargs["load_from_cache"] = load_from_cache
    try:
        render(refresh_all_templates_inputs_in_pipeline.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(refresh_all_templates_inputs_in_pipeline, kwargs)


@group.command("validate-template-inputs")
@click.option("--identifier", default=None)
@click.option("--branch", default=None)
@click.option("--repo-identifier", default=None)
@click.option("--get-default-from-other-repo/--no-get-default-from-other-repo", default=False)
@click.option("--load-from-cache", default="false")
@click.pass_context
def validate_template_inputs_cmd(ctx, identifier, branch, repo_identifier, get_default_from_other_repo, load_from_cache):
    """Validates template inputs in a pipeline's YAML specification."""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["identifier"] = identifier if identifier is not None else UNSET
    kwargs["branch"] = branch if branch is not None else UNSET
    kwargs["repo_identifier"] = repo_identifier if repo_identifier is not None else UNSET
    kwargs["get_default_from_other_repo"] = get_default_from_other_repo if get_default_from_other_repo is not None else UNSET
    if load_from_cache is not None:
        kwargs["load_from_cache"] = load_from_cache
    try:
        render(validate_template_inputs.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(validate_template_inputs, kwargs)

