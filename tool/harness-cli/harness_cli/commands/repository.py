"""Auto-generated CLI commands for repository endpoints."""

import json

import click

from api_specification_client.api.repository import (
    archive,
    calculate_commit_divergence,
    code_owners_validate,
    commit_files,
    create_branch,
    create_repository,
    create_tag,
    delete_branch,
    delete_repository,
    delete_tag,
    diff_stats,
    find_general_settings,
    find_security_settings,
    fork_create,
    fork_sync_branch,
    get_blame,
    get_branch,
    get_commit,
    get_commit_diff,
    get_content,
    get_raw,
    get_repo_languages,
    get_repository,
    import_repository,
    linked_create,
    linked_sync,
    list_branches,
    list_commits,
    list_paths,
    list_repos,
    list_tags,
    merge_check,
    path_details,
    purge_repository,
    raw_diff,
    raw_diff_post,
    rebase_branch,
    restore_repository,
    squash_branch,
    summary,
    update_default_branch,
    update_general_settings,
    update_repository,
    update_security_settings,
)
from api_specification_client.models.fork_create_body import ForkCreateBody
from api_specification_client.models.fork_sync_branch_body import ForkSyncBranchBody
from api_specification_client.models.import_repository_body import ImportRepositoryBody
from api_specification_client.models.linked_create_body import LinkedCreateBody
from api_specification_client.models.linked_sync_body import LinkedSyncBody
from api_specification_client.models.openapi_calculate_commit_divergence_request import OpenapiCalculateCommitDivergenceRequest
from api_specification_client.models.openapi_commit_files_request import OpenapiCommitFilesRequest
from api_specification_client.models.openapi_create_branch_request import OpenapiCreateBranchRequest
from api_specification_client.models.openapi_create_repository_request import OpenapiCreateRepositoryRequest
from api_specification_client.models.openapi_create_tag_request import OpenapiCreateTagRequest
from api_specification_client.models.openapi_general_settings_request import OpenapiGeneralSettingsRequest
from api_specification_client.models.openapi_paths_details_request import OpenapiPathsDetailsRequest
from api_specification_client.models.openapi_restore_request import OpenapiRestoreRequest
from api_specification_client.models.openapi_security_settings_request import OpenapiSecuritySettingsRequest
from api_specification_client.models.openapi_update_default_branch_request import OpenapiUpdateDefaultBranchRequest
from api_specification_client.models.openapi_update_repo_request import OpenapiUpdateRepoRequest
from api_specification_client.models.rebase_branch_body import RebaseBranchBody
from api_specification_client.models.squash_branch_body import SquashBranchBody
from api_specification_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Repository operations (branches, commits, content, tags, diff, settings)."""
    pass


@group.command("archive")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("git_ref", metavar="GIT_REF")
@click.argument("format", metavar="FORMAT")
@click.option("--path", default=None, multiple=True)
@click.option("--prefix", default=None)
@click.option("--attributes", default=None)
@click.option("--time", default=None)
@click.option("--compression", default=None, type=int)
@click.pass_context
def archive_cmd(ctx, repo_identifier, git_ref, format, path, prefix, attributes, time, compression):
    """Download repo in archived format"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["git_ref"] = git_ref
    kwargs["format_"] = format
    kwargs["path"] = path if path is not None else UNSET
    kwargs["prefix"] = prefix if prefix is not None else UNSET
    kwargs["attributes"] = attributes if attributes is not None else UNSET
    kwargs["time"] = time if time is not None else UNSET
    kwargs["compression"] = compression if compression is not None else UNSET
    try:
        render(archive.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(archive, kwargs)


@group.command("calculate-commit-divergence")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def calculate_commit_divergence_cmd(ctx, repo_identifier, body_json):
    """Get commit divergence"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiCalculateCommitDivergenceRequest.from_dict(json.loads(body_json))
    try:
        render(calculate_commit_divergence.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(calculate_commit_divergence, kwargs)


@group.command("code-owners-validate")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--git-ref", default=None)
@click.pass_context
def code_owners_validate_cmd(ctx, repo_identifier, git_ref):
    """Validate code owners file"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["git_ref"] = git_ref if git_ref is not None else UNSET
    try:
        render(code_owners_validate.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(code_owners_validate, kwargs)


@group.command("commit-files")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def commit_files_cmd(ctx, repo_identifier, body_json):
    """Commit files"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiCommitFilesRequest.from_dict(json.loads(body_json))
    try:
        render(commit_files.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(commit_files, kwargs)


@group.command("create-branch")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def create_branch_cmd(ctx, repo_identifier, body_json):
    """Create branch"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiCreateBranchRequest.from_dict(json.loads(body_json))
    try:
        render(create_branch.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(create_branch, kwargs)


@group.command("create-repository")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def create_repository_cmd(ctx, body_json):
    """Create repository"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if body_json:
        kwargs["body"] = OpenapiCreateRepositoryRequest.from_dict(json.loads(body_json))
    try:
        render(create_repository.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(create_repository, kwargs)


@group.command("create-tag")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def create_tag_cmd(ctx, repo_identifier, body_json):
    """Create tag"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiCreateTagRequest.from_dict(json.loads(body_json))
    try:
        render(create_tag.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(create_tag, kwargs)


@group.command("delete-branch")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("branch_name", metavar="BRANCH_NAME")
@click.option("--bypass-rules/--no-bypass-rules", default=False)
@click.option("--dry-run-rules/--no-dry-run-rules", default=False)
@click.pass_context
def delete_branch_cmd(ctx, repo_identifier, branch_name, bypass_rules, dry_run_rules):
    """Delete branch"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["branch_name"] = branch_name
    kwargs["bypass_rules"] = bypass_rules
    kwargs["dry_run_rules"] = dry_run_rules
    try:
        render(delete_branch.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_branch, kwargs)


@group.command("delete-repository")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.pass_context
def delete_repository_cmd(ctx, repo_identifier):
    """Soft delete repository"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    try:
        render(delete_repository.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_repository, kwargs)


@group.command("delete-tag")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("tag_name", metavar="TAG_NAME")
@click.option("--bypass-rules/--no-bypass-rules", default=False)
@click.option("--dry-run-rules/--no-dry-run-rules", default=False)
@click.pass_context
def delete_tag_cmd(ctx, repo_identifier, tag_name, bypass_rules, dry_run_rules):
    """Delete tag"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["tag_name"] = tag_name
    kwargs["bypass_rules"] = bypass_rules
    kwargs["dry_run_rules"] = dry_run_rules
    try:
        render(delete_tag.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_tag, kwargs)


@group.command("diff-stats")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("range", metavar="RANGE")
@click.option("--path", default=None, multiple=True)
@click.pass_context
def diff_stats_cmd(ctx, repo_identifier, range, path):
    """Get diff stats"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["range_"] = range
    kwargs["path"] = path if path is not None else UNSET
    try:
        render(diff_stats.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(diff_stats, kwargs)


@group.command("find-general-settings")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.pass_context
def find_general_settings_cmd(ctx, repo_identifier):
    """Get general settings"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    try:
        render(find_general_settings.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(find_general_settings, kwargs)


@group.command("find-security-settings")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.pass_context
def find_security_settings_cmd(ctx, repo_identifier):
    """Get security settings"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    try:
        render(find_security_settings.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(find_security_settings, kwargs)


@group.command("fork-create")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def fork_create_cmd(ctx, repo_identifier, body_json):
    """Args:"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = ForkCreateBody.from_dict(json.loads(body_json))
    try:
        render(fork_create.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(fork_create, kwargs)


@group.command("fork-sync-branch")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def fork_sync_branch_cmd(ctx, repo_identifier, body_json):
    """Args:"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = ForkSyncBranchBody.from_dict(json.loads(body_json))
    try:
        render(fork_sync_branch.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(fork_sync_branch, kwargs)


@group.command("get-blame")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("path", metavar="PATH")
@click.option("--git-ref", default=None)
@click.option("--line-from", default=0, type=int)
@click.option("--line-to", default=0, type=int)
@click.pass_context
def get_blame_cmd(ctx, repo_identifier, path, git_ref, line_from, line_to):
    """Get git blame"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["path"] = path
    kwargs["git_ref"] = git_ref if git_ref is not None else UNSET
    if line_from is not None:
        kwargs["line_from"] = line_from
    if line_to is not None:
        kwargs["line_to"] = line_to
    try:
        render(get_blame.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_blame, kwargs)


@group.command("get-branch")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("branch_name", metavar="BRANCH_NAME")
@click.option("--include-checks/--no-include-checks", default=False)
@click.option("--include-rules/--no-include-rules", default=False)
@click.option("--include-pullreqs/--no-include-pullreqs", default=False)
@click.option("--max-divergence", default=None, type=int)
@click.pass_context
def get_branch_cmd(ctx, repo_identifier, branch_name, include_checks, include_rules, include_pullreqs, max_divergence):
    """Get branch"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["branch_name"] = branch_name
    kwargs["include_checks"] = include_checks
    kwargs["include_rules"] = include_rules
    kwargs["include_pullreqs"] = include_pullreqs
    kwargs["max_divergence"] = max_divergence if max_divergence is not None else UNSET
    try:
        render(get_branch.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_branch, kwargs)


@group.command("get-commit")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("commit_sha", metavar="COMMIT_SHA")
@click.pass_context
def get_commit_cmd(ctx, repo_identifier, commit_sha):
    """Get commit"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["commit_sha"] = commit_sha
    try:
        render(get_commit.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_commit, kwargs)


@group.command("get-commit-diff")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("commit_sha", metavar="COMMIT_SHA")
@click.pass_context
def get_commit_diff_cmd(ctx, repo_identifier, commit_sha):
    """Get raw git diff of a commit"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["commit_sha"] = commit_sha
    try:
        render(get_commit_diff.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_commit_diff, kwargs)


@group.command("get-content")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("path", metavar="PATH")
@click.option("--git-ref", default=None)
@click.option("--include-commit/--no-include-commit", default=False)
@click.option("--flatten-directories/--no-flatten-directories", default=False)
@click.pass_context
def get_content_cmd(ctx, repo_identifier, path, git_ref, include_commit, flatten_directories):
    """Get content of a file"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["path"] = path
    kwargs["git_ref"] = git_ref if git_ref is not None else UNSET
    kwargs["include_commit"] = include_commit
    kwargs["flatten_directories"] = flatten_directories
    try:
        render(get_content.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_content, kwargs)


@group.command("get-raw")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("path", metavar="PATH")
@click.option("--git-ref", default=None)
@click.pass_context
def get_raw_cmd(ctx, repo_identifier, path, git_ref):
    """Get raw file content"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["path"] = path
    kwargs["git_ref"] = git_ref if git_ref is not None else UNSET
    try:
        render(get_raw.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_raw, kwargs)


@group.command("get-repo-languages")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.pass_context
def get_repo_languages_cmd(ctx, repo_identifier):
    """Get repository language statistics"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    try:
        render(get_repo_languages.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_repo_languages, kwargs)


@group.command("get-repository")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.pass_context
def get_repository_cmd(ctx, repo_identifier):
    """Get repository"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    try:
        render(get_repository.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_repository, kwargs)


@group.command("import-repository")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def import_repository_cmd(ctx, body_json):
    """Import repository"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if body_json:
        kwargs["body"] = ImportRepositoryBody.from_dict(json.loads(body_json))
    try:
        render(import_repository.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(import_repository, kwargs)


@group.command("linked-create")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def linked_create_cmd(ctx, body_json):
    """Args:"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if body_json:
        kwargs["body"] = LinkedCreateBody.from_dict(json.loads(body_json))
    try:
        render(linked_create.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(linked_create, kwargs)


@group.command("linked-sync")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def linked_sync_cmd(ctx, repo_identifier, body_json):
    """Args:"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = LinkedSyncBody.from_dict(json.loads(body_json))
    try:
        render(linked_sync.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(linked_sync, kwargs)


@group.command("list-branches")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--include-commit/--no-include-commit", default=False)
@click.option("--query", default=None)
@click.option("--order", default=None)
@click.option("--sort", default=None)
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--include-checks/--no-include-checks", default=False)
@click.option("--include-rules/--no-include-rules", default=False)
@click.option("--include-pullreqs/--no-include-pullreqs", default=False)
@click.option("--max-divergence", default=None, type=int)
@click.pass_context
def list_branches_cmd(ctx, repo_identifier, include_commit, query, order, sort, page, limit, include_checks, include_rules, include_pullreqs, max_divergence):
    """List branches"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["include_commit"] = include_commit
    kwargs["query"] = query if query is not None else UNSET
    kwargs["order"] = order if order is not None else UNSET
    kwargs["sort"] = sort if sort is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["include_checks"] = include_checks
    kwargs["include_rules"] = include_rules
    kwargs["include_pullreqs"] = include_pullreqs
    kwargs["max_divergence"] = max_divergence if max_divergence is not None else UNSET
    try:
        render(list_branches.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_branches, kwargs)


@group.command("list-commits")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--git-ref", default=None)
@click.option("--after", default=None)
@click.option("--path", default="")
@click.option("--since", default=None, type=int)
@click.option("--until", default=None, type=int)
@click.option("--committer", default=None)
@click.option("--committer-id", default=None, type=int)
@click.option("--author", default=None)
@click.option("--author-id", default=None, type=int)
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--include-stats/--no-include-stats", default=False)
@click.pass_context
def list_commits_cmd(ctx, repo_identifier, git_ref, after, path, since, until, committer, committer_id, author, author_id, page, limit, include_stats):
    """List commits"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["git_ref"] = git_ref if git_ref is not None else UNSET
    kwargs["after"] = after if after is not None else UNSET
    if path is not None:
        kwargs["path"] = path
    kwargs["since"] = since if since is not None else UNSET
    kwargs["until"] = until if until is not None else UNSET
    kwargs["committer"] = committer if committer is not None else UNSET
    kwargs["committer_id"] = committer_id if committer_id is not None else UNSET
    kwargs["author"] = author if author is not None else UNSET
    kwargs["author_id"] = author_id if author_id is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["include_stats"] = include_stats
    try:
        render(list_commits.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_commits, kwargs)


@group.command("list-paths")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--git-ref", default=None)
@click.option("--include-directories/--no-include-directories", default=False)
@click.pass_context
def list_paths_cmd(ctx, repo_identifier, git_ref, include_directories):
    """List all paths"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["git_ref"] = git_ref if git_ref is not None else UNSET
    kwargs["include_directories"] = include_directories
    try:
        render(list_paths.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_paths, kwargs)


@group.command("list-repos")
@click.option("--query", default=None)
@click.option("--sort", default=None)
@click.option("--order", default=None)
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--only-favorites/--no-only-favorites", default=False)
@click.option("--recursive/--no-recursive", default=False)
@click.pass_context
def list_repos_cmd(ctx, query, sort, order, page, limit, only_favorites, recursive):
    """List repositories"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["query"] = query if query is not None else UNSET
    kwargs["sort"] = sort if sort is not None else UNSET
    kwargs["order"] = order if order is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["only_favorites"] = only_favorites
    kwargs["recursive"] = recursive
    try:
        render(list_repos.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_repos, kwargs)


@group.command("list-tags")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--include-commit/--no-include-commit", default=False)
@click.option("--query", default=None)
@click.option("--order", default=None)
@click.option("--sort", default=None)
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.pass_context
def list_tags_cmd(ctx, repo_identifier, include_commit, query, order, sort, page, limit):
    """List tags"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["include_commit"] = include_commit
    kwargs["query"] = query if query is not None else UNSET
    kwargs["order"] = order if order is not None else UNSET
    kwargs["sort"] = sort if sort is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    try:
        render(list_tags.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_tags, kwargs)


@group.command("merge-check")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("range", metavar="RANGE")
@click.option("--path", default=None, multiple=True)
@click.pass_context
def merge_check_cmd(ctx, repo_identifier, range, path):
    """Check mergeability"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["range_"] = range
    kwargs["path"] = path if path is not None else UNSET
    try:
        render(merge_check.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(merge_check, kwargs)


@group.command("path-details")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--git-ref", default=None)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def path_details_cmd(ctx, repo_identifier, git_ref, body_json):
    """Get commit details"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["git_ref"] = git_ref if git_ref is not None else UNSET
    if body_json:
        kwargs["body"] = OpenapiPathsDetailsRequest.from_dict(json.loads(body_json))
    try:
        render(path_details.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(path_details, kwargs)


@group.command("purge-repository")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--deleted-at", default=None, type=int)
@click.pass_context
def purge_repository_cmd(ctx, repo_identifier, deleted_at):
    """Purge repository"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if deleted_at is not None:
        kwargs["deleted_at"] = deleted_at
    try:
        render(purge_repository.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(purge_repository, kwargs)


@group.command("raw-diff")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("range", metavar="RANGE")
@click.option("--path", default=None, multiple=True)
@click.pass_context
def raw_diff_cmd(ctx, repo_identifier, range, path):
    """Get raw diff"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["range_"] = range
    kwargs["path"] = path if path is not None else UNSET
    try:
        render(raw_diff.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(raw_diff, kwargs)


@group.command("raw-diff-post")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("range", metavar="RANGE")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def raw_diff_post_cmd(ctx, repo_identifier, range, body_json):
    """Get raw diff"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["range_"] = range
    try:
        render(raw_diff_post.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(raw_diff_post, kwargs)


@group.command("rebase-branch")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def rebase_branch_cmd(ctx, repo_identifier, body_json):
    """Rebase a branch relative to another branch or a commit"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = RebaseBranchBody.from_dict(json.loads(body_json))
    try:
        render(rebase_branch.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(rebase_branch, kwargs)


@group.command("restore-repository")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--deleted-at", default=None, type=int)
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def restore_repository_cmd(ctx, repo_identifier, deleted_at, body_json):
    """Restore repository"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if deleted_at is not None:
        kwargs["deleted_at"] = deleted_at
    if body_json:
        kwargs["body"] = OpenapiRestoreRequest.from_dict(json.loads(body_json))
    try:
        render(restore_repository.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(restore_repository, kwargs)


@group.command("squash-branch")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def squash_branch_cmd(ctx, repo_identifier, body_json):
    """Squashes commits in a branch relative to another branch or a commit"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = SquashBranchBody.from_dict(json.loads(body_json))
    try:
        render(squash_branch.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(squash_branch, kwargs)


@group.command("summary")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.pass_context
def summary_cmd(ctx, repo_identifier):
    """Get repository summary"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    try:
        render(summary.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(summary, kwargs)


@group.command("update-default-branch")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_default_branch_cmd(ctx, repo_identifier, body_json):
    """Update default branch"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiUpdateDefaultBranchRequest.from_dict(json.loads(body_json))
    try:
        render(update_default_branch.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_default_branch, kwargs)


@group.command("update-general-settings")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_general_settings_cmd(ctx, repo_identifier, body_json):
    """Update general settings"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiGeneralSettingsRequest.from_dict(json.loads(body_json))
    try:
        render(update_general_settings.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_general_settings, kwargs)


@group.command("update-repository")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_repository_cmd(ctx, repo_identifier, body_json):
    """Update repository"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiUpdateRepoRequest.from_dict(json.loads(body_json))
    try:
        render(update_repository.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_repository, kwargs)


@group.command("update-security-settings")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_security_settings_cmd(ctx, repo_identifier, body_json):
    """Update security settings"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiSecuritySettingsRequest.from_dict(json.loads(body_json))
    try:
        render(update_security_settings.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_security_settings, kwargs)

