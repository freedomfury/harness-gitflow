"""Auto-generated CLI commands for pullreq endpoints."""

import json

import click

from api_specification_client.api.pullreq import (
    checks_pull_req,
    codeowners_pull_req,
    comment_apply_suggestions,
    comment_create_pull_req,
    comment_delete_pull_req,
    comment_status_pull_req,
    comment_update_pull_req,
    count_pull_req_space,
    create_pull_req,
    diff_pull_req,
    diff_pull_req_post,
    file_view_add_pull_req,
    file_view_delete_pull_req,
    file_view_list_pull_req,
    get_pull_req,
    list_pull_req,
    list_pull_req_activities,
    list_pull_req_commits,
    list_pull_req_space,
    merge_pull_req_op,
    pr_auto_merge_disable,
    pr_auto_merge_enable,
    pr_auto_merge_get,
    pr_candidates,
    pull_req_meta_data,
    restore_pull_req_source_branch,
    revert_pull_req_op,
    review_submit_pull_req,
    reviewer_add_pull_req,
    reviewer_combined_list_pull_req,
    reviewer_delete_pull_req,
    reviewer_list_pull_req,
    state_pull_req,
    update_pull_req,
    user_group_reviewer_add_pull_req,
    user_group_reviewer_delete_pull_req,
)
from api_specification_client.models.openapi_comment_apply_suggestionst_request import OpenapiCommentApplySuggestionstRequest
from api_specification_client.models.openapi_comment_create_pull_req_request import OpenapiCommentCreatePullReqRequest
from api_specification_client.models.openapi_comment_status_pull_req_request import OpenapiCommentStatusPullReqRequest
from api_specification_client.models.openapi_comment_update_pull_req_request import OpenapiCommentUpdatePullReqRequest
from api_specification_client.models.openapi_create_pull_req_request import OpenapiCreatePullReqRequest
from api_specification_client.models.openapi_file_view_add_pull_req_request import OpenapiFileViewAddPullReqRequest
from api_specification_client.models.openapi_merge_pull_req import OpenapiMergePullReq
from api_specification_client.models.openapi_review_submit_pull_req_request import OpenapiReviewSubmitPullReqRequest
from api_specification_client.models.openapi_reviewer_add_pull_req_request import OpenapiReviewerAddPullReqRequest
from api_specification_client.models.openapi_state_pull_req_request import OpenapiStatePullReqRequest
from api_specification_client.models.openapi_update_pull_req_request import OpenapiUpdatePullReqRequest
from api_specification_client.models.openapi_user_group_reviewer_add_request import OpenapiUserGroupReviewerAddRequest
from api_specification_client.models.pr_auto_merge_enable_body import PrAutoMergeEnableBody
from api_specification_client.models.restore_pull_req_source_branch_body import RestorePullReqSourceBranchBody
from api_specification_client.models.revert_pull_req_op_body import RevertPullReqOpBody
from api_specification_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Pull request operations (create, merge, review, comments)."""
    pass


@group.command("checks-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.pass_context
def checks_pull_req_cmd(ctx, repo_identifier, pullreq_number):
    """Get status checks"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(checks_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(checks_pull_req, kwargs)


@group.command("codeowners-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.pass_context
def codeowners_pull_req_cmd(ctx, repo_identifier, pullreq_number):
    """Get code owners"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(codeowners_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(codeowners_pull_req, kwargs)


@group.command("comment-apply-suggestions")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def comment_apply_suggestions_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Apply pull request code comment suggestions"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiCommentApplySuggestionstRequest.from_dict(json.loads(body_json))
    try:
        render(comment_apply_suggestions.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(comment_apply_suggestions, kwargs)


@group.command("comment-create-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def comment_create_pull_req_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Create new pull request comment"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiCommentCreatePullReqRequest.from_dict(json.loads(body_json))
    try:
        render(comment_create_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(comment_create_pull_req, kwargs)


@group.command("comment-delete-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.argument("pullreq_comment_id", metavar="PULLREQ_COMMENT_ID")
@click.pass_context
def comment_delete_pull_req_cmd(ctx, repo_identifier, pullreq_number, pullreq_comment_id):
    """Delete pull request comment"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    kwargs["pullreq_comment_id"] = pullreq_comment_id
    try:
        render(comment_delete_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(comment_delete_pull_req, kwargs)


@group.command("comment-status-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.argument("pullreq_comment_id", metavar="PULLREQ_COMMENT_ID")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def comment_status_pull_req_cmd(ctx, repo_identifier, pullreq_number, pullreq_comment_id, body_json):
    """Update status of pull request comment"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    kwargs["pullreq_comment_id"] = pullreq_comment_id
    if body_json:
        kwargs["body"] = OpenapiCommentStatusPullReqRequest.from_dict(json.loads(body_json))
    try:
        render(comment_status_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(comment_status_pull_req, kwargs)


@group.command("comment-update-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.argument("pullreq_comment_id", metavar="PULLREQ_COMMENT_ID")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def comment_update_pull_req_cmd(ctx, repo_identifier, pullreq_number, pullreq_comment_id, body_json):
    """Update pull request comment"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    kwargs["pullreq_comment_id"] = pullreq_comment_id
    if body_json:
        kwargs["body"] = OpenapiCommentUpdatePullReqRequest.from_dict(json.loads(body_json))
    try:
        render(comment_update_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(comment_update_pull_req, kwargs)


@group.command("count-pull-req-space")
@click.option("--state", default=None, multiple=True)
@click.option("--source-repo-ref", default=None)
@click.option("--source-branch", default=None)
@click.option("--target-branch", default=None)
@click.option("--query", default=None)
@click.option("--created-by", default=None, type=int)
@click.option("--created-lt", default=None, type=int)
@click.option("--created-gt", default=None, type=int)
@click.option("--updated-lt", default=None, type=int)
@click.option("--include-subspaces/--no-include-subspaces", default=False)
@click.option("--label-id", default=None, type=int)
@click.option("--value-id", default=None, type=int)
@click.option("--author-id", default=None, type=int)
@click.option("--commenter-id", default=None, type=int)
@click.option("--mentioned-id", default=None, type=int)
@click.option("--reviewer-id", default=None, type=int)
@click.option("--review-decision", default=None, multiple=True)
@click.option("--include-rules/--no-include-rules", default=False)
@click.pass_context
def count_pull_req_space_cmd(ctx, state, source_repo_ref, source_branch, target_branch, query, created_by, created_lt, created_gt, updated_lt, include_subspaces, label_id, value_id, author_id, commenter_id, mentioned_id, reviewer_id, review_decision, include_rules):
    """Count pull requests in account/org/project"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["state"] = state if state is not None else UNSET
    kwargs["source_repo_ref"] = source_repo_ref if source_repo_ref is not None else UNSET
    kwargs["source_branch"] = source_branch if source_branch is not None else UNSET
    kwargs["target_branch"] = target_branch if target_branch is not None else UNSET
    kwargs["query"] = query if query is not None else UNSET
    kwargs["created_by"] = created_by if created_by is not None else UNSET
    kwargs["created_lt"] = created_lt if created_lt is not None else UNSET
    kwargs["created_gt"] = created_gt if created_gt is not None else UNSET
    kwargs["updated_lt"] = updated_lt if updated_lt is not None else UNSET
    kwargs["include_subspaces"] = include_subspaces
    kwargs["label_id"] = label_id if label_id is not None else UNSET
    kwargs["value_id"] = value_id if value_id is not None else UNSET
    kwargs["author_id"] = author_id if author_id is not None else UNSET
    kwargs["commenter_id"] = commenter_id if commenter_id is not None else UNSET
    kwargs["mentioned_id"] = mentioned_id if mentioned_id is not None else UNSET
    kwargs["reviewer_id"] = reviewer_id if reviewer_id is not None else UNSET
    kwargs["review_decision"] = review_decision if review_decision is not None else UNSET
    kwargs["include_rules"] = include_rules
    try:
        render(count_pull_req_space.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(count_pull_req_space, kwargs)


@group.command("create-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def create_pull_req_cmd(ctx, repo_identifier, body_json):
    """Create pull request"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiCreatePullReqRequest.from_dict(json.loads(body_json))
    try:
        render(create_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(create_pull_req, kwargs)


@group.command("diff-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--path", default=None, multiple=True)
@click.pass_context
def diff_pull_req_cmd(ctx, repo_identifier, pullreq_number, path):
    """Get file changes"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    kwargs["path"] = path if path is not None else UNSET
    try:
        render(diff_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(diff_pull_req, kwargs)


@group.command("diff-pull-req-post")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def diff_pull_req_post_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Get file changes"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(diff_pull_req_post.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(diff_pull_req_post, kwargs)


@group.command("file-view-add-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def file_view_add_pull_req_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Mark file as viewed"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiFileViewAddPullReqRequest.from_dict(json.loads(body_json))
    try:
        render(file_view_add_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(file_view_add_pull_req, kwargs)


@group.command("file-view-delete-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.argument("file_path", metavar="FILE_PATH")
@click.pass_context
def file_view_delete_pull_req_cmd(ctx, repo_identifier, pullreq_number, file_path):
    """Remove file view"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    kwargs["file_path"] = file_path
    try:
        render(file_view_delete_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(file_view_delete_pull_req, kwargs)


@group.command("file-view-list-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.pass_context
def file_view_list_pull_req_cmd(ctx, repo_identifier, pullreq_number):
    """List viewed files"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(file_view_list_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(file_view_list_pull_req, kwargs)


@group.command("get-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.pass_context
def get_pull_req_cmd(ctx, repo_identifier, pullreq_number):
    """Get pull request"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(get_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_pull_req, kwargs)


@group.command("list-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--state", default=None, multiple=True)
@click.option("--source-repo-ref", default=None)
@click.option("--source-branch", default=None)
@click.option("--target-branch", default=None)
@click.option("--query", default=None)
@click.option("--created-by", default=None, type=int)
@click.option("--order", default=None)
@click.option("--sort", default=None)
@click.option("--created-lt", default=None, type=int)
@click.option("--created-gt", default=None, type=int)
@click.option("--updated-lt", default=None, type=int)
@click.option("--updated-gt", default=None, type=int)
@click.option("--exclude-description/--no-exclude-description", default=False)
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--label-id", default=None, type=int)
@click.option("--value-id", default=None, type=int)
@click.option("--author-id", default=None, type=int)
@click.option("--commenter-id", default=None, type=int)
@click.option("--mentioned-id", default=None, type=int)
@click.option("--reviewer-id", default=None, type=int)
@click.option("--review-decision", default=None, multiple=True)
@click.option("--include-git-stats/--no-include-git-stats", default=False)
@click.option("--include-checks/--no-include-checks", default=False)
@click.option("--include-rules/--no-include-rules", default=False)
@click.pass_context
def list_pull_req_cmd(ctx, repo_identifier, state, source_repo_ref, source_branch, target_branch, query, created_by, order, sort, created_lt, created_gt, updated_lt, updated_gt, exclude_description, page, limit, label_id, value_id, author_id, commenter_id, mentioned_id, reviewer_id, review_decision, include_git_stats, include_checks, include_rules):
    """List pull requests"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["state"] = state if state is not None else UNSET
    kwargs["source_repo_ref"] = source_repo_ref if source_repo_ref is not None else UNSET
    kwargs["source_branch"] = source_branch if source_branch is not None else UNSET
    kwargs["target_branch"] = target_branch if target_branch is not None else UNSET
    kwargs["query"] = query if query is not None else UNSET
    kwargs["created_by"] = created_by if created_by is not None else UNSET
    kwargs["order"] = order if order is not None else UNSET
    kwargs["sort"] = sort if sort is not None else UNSET
    kwargs["created_lt"] = created_lt if created_lt is not None else UNSET
    kwargs["created_gt"] = created_gt if created_gt is not None else UNSET
    kwargs["updated_lt"] = updated_lt if updated_lt is not None else UNSET
    kwargs["updated_gt"] = updated_gt if updated_gt is not None else UNSET
    kwargs["exclude_description"] = exclude_description
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["label_id"] = label_id if label_id is not None else UNSET
    kwargs["value_id"] = value_id if value_id is not None else UNSET
    kwargs["author_id"] = author_id if author_id is not None else UNSET
    kwargs["commenter_id"] = commenter_id if commenter_id is not None else UNSET
    kwargs["mentioned_id"] = mentioned_id if mentioned_id is not None else UNSET
    kwargs["reviewer_id"] = reviewer_id if reviewer_id is not None else UNSET
    kwargs["review_decision"] = review_decision if review_decision is not None else UNSET
    kwargs["include_git_stats"] = include_git_stats
    kwargs["include_checks"] = include_checks
    kwargs["include_rules"] = include_rules
    try:
        render(list_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_pull_req, kwargs)


@group.command("list-pull-req-activities")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--kind", default=None, multiple=True)
@click.option("--type", default=None, multiple=True)
@click.option("--after", default=None, type=int)
@click.option("--before", default=None, type=int)
@click.option("--limit", default=30, type=int)
@click.pass_context
def list_pull_req_activities_cmd(ctx, repo_identifier, pullreq_number, kind, type, after, before, limit):
    """List activities"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    kwargs["kind"] = kind if kind is not None else UNSET
    kwargs["type_"] = type if type is not None else UNSET
    kwargs["after"] = after if after is not None else UNSET
    kwargs["before"] = before if before is not None else UNSET
    if limit is not None:
        kwargs["limit"] = limit
    try:
        render(list_pull_req_activities.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_pull_req_activities, kwargs)


@group.command("list-pull-req-commits")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.pass_context
def list_pull_req_commits_cmd(ctx, repo_identifier, pullreq_number, page, limit):
    """List commits"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    try:
        render(list_pull_req_commits.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_pull_req_commits, kwargs)


@group.command("list-pull-req-space")
@click.option("--state", default=None, multiple=True)
@click.option("--source-repo-ref", default=None)
@click.option("--source-branch", default=None)
@click.option("--target-branch", default=None)
@click.option("--query", default=None)
@click.option("--created-by", default=None, type=int)
@click.option("--created-lt", default=None, type=int)
@click.option("--created-gt", default=None, type=int)
@click.option("--updated-lt", default=None, type=int)
@click.option("--exclude-description/--no-exclude-description", default=False)
@click.option("--include-subspaces/--no-include-subspaces", default=False)
@click.option("--limit", default=30, type=int)
@click.option("--label-id", default=None, type=int)
@click.option("--value-id", default=None, type=int)
@click.option("--author-id", default=None, type=int)
@click.option("--commenter-id", default=None, type=int)
@click.option("--mentioned-id", default=None, type=int)
@click.option("--reviewer-id", default=None, type=int)
@click.option("--review-decision", default=None, multiple=True)
@click.option("--include-git-stats/--no-include-git-stats", default=False)
@click.option("--include-checks/--no-include-checks", default=False)
@click.option("--include-rules/--no-include-rules", default=False)
@click.pass_context
def list_pull_req_space_cmd(ctx, state, source_repo_ref, source_branch, target_branch, query, created_by, created_lt, created_gt, updated_lt, exclude_description, include_subspaces, limit, label_id, value_id, author_id, commenter_id, mentioned_id, reviewer_id, review_decision, include_git_stats, include_checks, include_rules):
    """List pull requests in account/org/project"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["state"] = state if state is not None else UNSET
    kwargs["source_repo_ref"] = source_repo_ref if source_repo_ref is not None else UNSET
    kwargs["source_branch"] = source_branch if source_branch is not None else UNSET
    kwargs["target_branch"] = target_branch if target_branch is not None else UNSET
    kwargs["query"] = query if query is not None else UNSET
    kwargs["created_by"] = created_by if created_by is not None else UNSET
    kwargs["created_lt"] = created_lt if created_lt is not None else UNSET
    kwargs["created_gt"] = created_gt if created_gt is not None else UNSET
    kwargs["updated_lt"] = updated_lt if updated_lt is not None else UNSET
    kwargs["exclude_description"] = exclude_description
    kwargs["include_subspaces"] = include_subspaces
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["label_id"] = label_id if label_id is not None else UNSET
    kwargs["value_id"] = value_id if value_id is not None else UNSET
    kwargs["author_id"] = author_id if author_id is not None else UNSET
    kwargs["commenter_id"] = commenter_id if commenter_id is not None else UNSET
    kwargs["mentioned_id"] = mentioned_id if mentioned_id is not None else UNSET
    kwargs["reviewer_id"] = reviewer_id if reviewer_id is not None else UNSET
    kwargs["review_decision"] = review_decision if review_decision is not None else UNSET
    kwargs["include_git_stats"] = include_git_stats
    kwargs["include_checks"] = include_checks
    kwargs["include_rules"] = include_rules
    try:
        render(list_pull_req_space.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_pull_req_space, kwargs)


@group.command("merge-pull-req-op")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def merge_pull_req_op_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Merge"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiMergePullReq.from_dict(json.loads(body_json))
    try:
        render(merge_pull_req_op.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(merge_pull_req_op, kwargs)


@group.command("pr-auto-merge-disable")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.pass_context
def pr_auto_merge_disable_cmd(ctx, repo_identifier, pullreq_number):
    """Disable the auto-merge option for the pull request."""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(pr_auto_merge_disable.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(pr_auto_merge_disable, kwargs)


@group.command("pr-auto-merge-enable")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def pr_auto_merge_enable_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Enable the auto-merge option for the pull request."""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = PrAutoMergeEnableBody.from_dict(json.loads(body_json))
    try:
        render(pr_auto_merge_enable.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(pr_auto_merge_enable, kwargs)


@group.command("pr-auto-merge-get")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.pass_context
def pr_auto_merge_get_cmd(ctx, repo_identifier, pullreq_number):
    """Get the auto-merge option for the pull request."""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(pr_auto_merge_get.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(pr_auto_merge_get, kwargs)


@group.command("pr-candidates")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--limit", default=30, type=int)
@click.pass_context
def pr_candidates_cmd(ctx, repo_identifier, limit):
    """Args:"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if limit is not None:
        kwargs["limit"] = limit
    try:
        render(pr_candidates.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(pr_candidates, kwargs)


@group.command("pull-req-meta-data")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.pass_context
def pull_req_meta_data_cmd(ctx, repo_identifier, pullreq_number):
    """Get metadata"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(pull_req_meta_data.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(pull_req_meta_data, kwargs)


@group.command("restore-pull-req-source-branch")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def restore_pull_req_source_branch_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Restore source branch"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = RestorePullReqSourceBranchBody.from_dict(json.loads(body_json))
    try:
        render(restore_pull_req_source_branch.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(restore_pull_req_source_branch, kwargs)


@group.command("revert-pull-req-op")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def revert_pull_req_op_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Revert of a merged pull request"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = RevertPullReqOpBody.from_dict(json.loads(body_json))
    try:
        render(revert_pull_req_op.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(revert_pull_req_op, kwargs)


@group.command("review-submit-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def review_submit_pull_req_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Submit review"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiReviewSubmitPullReqRequest.from_dict(json.loads(body_json))
    try:
        render(review_submit_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(review_submit_pull_req, kwargs)


@group.command("reviewer-add-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def reviewer_add_pull_req_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Add reviewer"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiReviewerAddPullReqRequest.from_dict(json.loads(body_json))
    try:
        render(reviewer_add_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(reviewer_add_pull_req, kwargs)


@group.command("reviewer-combined-list-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.pass_context
def reviewer_combined_list_pull_req_cmd(ctx, repo_identifier, pullreq_number):
    """Args:"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(reviewer_combined_list_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(reviewer_combined_list_pull_req, kwargs)


@group.command("reviewer-delete-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.argument("pullreq_reviewer_id", metavar="PULLREQ_REVIEWER_ID")
@click.pass_context
def reviewer_delete_pull_req_cmd(ctx, repo_identifier, pullreq_number, pullreq_reviewer_id):
    """Remove reviewer"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    kwargs["pullreq_reviewer_id"] = pullreq_reviewer_id
    try:
        render(reviewer_delete_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(reviewer_delete_pull_req, kwargs)


@group.command("reviewer-list-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.pass_context
def reviewer_list_pull_req_cmd(ctx, repo_identifier, pullreq_number):
    """List reviewers"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    try:
        render(reviewer_list_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(reviewer_list_pull_req, kwargs)


@group.command("state-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def state_pull_req_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Update state of pull request"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiStatePullReqRequest.from_dict(json.loads(body_json))
    try:
        render(state_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(state_pull_req, kwargs)


@group.command("update-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_pull_req_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Update pull request"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiUpdatePullReqRequest.from_dict(json.loads(body_json))
    try:
        render(update_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_pull_req, kwargs)


@group.command("user-group-reviewer-add-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def user_group_reviewer_add_pull_req_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Args:"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiUserGroupReviewerAddRequest.from_dict(json.loads(body_json))
    try:
        render(user_group_reviewer_add_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(user_group_reviewer_add_pull_req, kwargs)


@group.command("user-group-reviewer-delete-pull-req")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.argument("user_group_id", metavar="USER_GROUP_ID")
@click.pass_context
def user_group_reviewer_delete_pull_req_cmd(ctx, repo_identifier, pullreq_number, user_group_id):
    """Args:"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    kwargs["user_group_id"] = user_group_id
    try:
        render(user_group_reviewer_delete_pull_req.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(user_group_reviewer_delete_pull_req, kwargs)

