"""Auto-generated CLI commands for labels endpoints."""

import json

import click

from api_specification_client.api.labels import (
    assign_label,
    define_repo_label,
    define_repo_label_value,
    define_space_label,
    define_space_label_value,
    delete_repo_label,
    delete_repo_label_value,
    delete_space_label,
    delete_space_label_value,
    list_pull_req_labels,
    list_repo_label_values,
    list_repo_labels,
    list_space_label_values,
    list_space_labels,
    save_repo_label,
    save_space_label,
    unassign_label,
    update_repo_label,
    update_repo_label_value,
    update_space_label,
    update_space_label_value,
)
from api_specification_client.models.define_repo_label_body import DefineRepoLabelBody
from api_specification_client.models.define_repo_label_value_body import DefineRepoLabelValueBody
from api_specification_client.models.define_space_label_body import DefineSpaceLabelBody
from api_specification_client.models.define_space_label_value_body import DefineSpaceLabelValueBody
from api_specification_client.models.openapi_pull_req_assign_label_input import OpenapiPullReqAssignLabelInput
from api_specification_client.models.save_repo_label_body import SaveRepoLabelBody
from api_specification_client.models.save_space_label_body import SaveSpaceLabelBody
from api_specification_client.models.update_repo_label_body import UpdateRepoLabelBody
from api_specification_client.models.update_repo_label_value_body import UpdateRepoLabelValueBody
from api_specification_client.models.update_space_label_body import UpdateSpaceLabelBody
from api_specification_client.models.update_space_label_value_body import UpdateSpaceLabelValueBody
from api_specification_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Label management."""
    pass


@group.command("assign-label")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def assign_label_cmd(ctx, repo_identifier, pullreq_number, body_json):
    """Assign label to pull request"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    if body_json:
        kwargs["body"] = OpenapiPullReqAssignLabelInput.from_dict(json.loads(body_json))
    try:
        render(assign_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(assign_label, kwargs)


@group.command("define-repo-label")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def define_repo_label_cmd(ctx, repo_identifier, body_json):
    """Create label at repo level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = DefineRepoLabelBody.from_dict(json.loads(body_json))
    try:
        render(define_repo_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(define_repo_label, kwargs)


@group.command("define-repo-label-value")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("key", metavar="KEY")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def define_repo_label_value_cmd(ctx, repo_identifier, key, body_json):
    """Create label value at repo level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["key"] = key
    if body_json:
        kwargs["body"] = DefineRepoLabelValueBody.from_dict(json.loads(body_json))
    try:
        render(define_repo_label_value.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(define_repo_label_value, kwargs)


@group.command("define-space-label")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def define_space_label_cmd(ctx, body_json):
    """Create label at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if body_json:
        kwargs["body"] = DefineSpaceLabelBody.from_dict(json.loads(body_json))
    try:
        render(define_space_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(define_space_label, kwargs)


@group.command("define-space-label-value")
@click.argument("key", metavar="KEY")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def define_space_label_value_cmd(ctx, key, body_json):
    """Create label value at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["key"] = key
    if body_json:
        kwargs["body"] = DefineSpaceLabelValueBody.from_dict(json.loads(body_json))
    try:
        render(define_space_label_value.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(define_space_label_value, kwargs)


@group.command("delete-repo-label")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("key", metavar="KEY")
@click.pass_context
def delete_repo_label_cmd(ctx, repo_identifier, key):
    """Delete label at repo level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["key"] = key
    try:
        render(delete_repo_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_repo_label, kwargs)


@group.command("delete-repo-label-value")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("key", metavar="KEY")
@click.argument("value", metavar="VALUE")
@click.pass_context
def delete_repo_label_value_cmd(ctx, repo_identifier, key, value):
    """Delete label value at repo level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["key"] = key
    kwargs["value"] = value
    try:
        render(delete_repo_label_value.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_repo_label_value, kwargs)


@group.command("delete-space-label")
@click.argument("key", metavar="KEY")
@click.pass_context
def delete_space_label_cmd(ctx, key):
    """Delete label at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["key"] = key
    try:
        render(delete_space_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_space_label, kwargs)


@group.command("delete-space-label-value")
@click.argument("key", metavar="KEY")
@click.argument("value", metavar="VALUE")
@click.pass_context
def delete_space_label_value_cmd(ctx, key, value):
    """Delete label value at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["key"] = key
    kwargs["value"] = value
    try:
        render(delete_space_label_value.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_space_label_value, kwargs)


@group.command("list-pull-req-labels")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--assignable/--no-assignable", default=False)
@click.option("--query", default=None)
@click.pass_context
def list_pull_req_labels_cmd(ctx, repo_identifier, pullreq_number, page, limit, assignable, query):
    """List labels assigned to pull request"""
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
    kwargs["assignable"] = assignable
    kwargs["query"] = query if query is not None else UNSET
    try:
        render(list_pull_req_labels.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_pull_req_labels, kwargs)


@group.command("list-repo-label-values")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("key", metavar="KEY")
@click.pass_context
def list_repo_label_values_cmd(ctx, repo_identifier, key):
    """List label values at repo level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["key"] = key
    try:
        render(list_repo_label_values.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_repo_label_values, kwargs)


@group.command("list-repo-labels")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--inherited/--no-inherited", default=False)
@click.option("--query", default=None)
@click.pass_context
def list_repo_labels_cmd(ctx, repo_identifier, page, limit, inherited, query):
    """List labels at repo level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["inherited"] = inherited
    kwargs["query"] = query if query is not None else UNSET
    try:
        render(list_repo_labels.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_repo_labels, kwargs)


@group.command("list-space-label-values")
@click.argument("key", metavar="KEY")
@click.pass_context
def list_space_label_values_cmd(ctx, key):
    """List label values at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["key"] = key
    try:
        render(list_space_label_values.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_space_label_values, kwargs)


@group.command("list-space-labels")
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--inherited/--no-inherited", default=False)
@click.option("--query", default=None)
@click.pass_context
def list_space_labels_cmd(ctx, page, limit, inherited, query):
    """List labels at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["inherited"] = inherited
    kwargs["query"] = query if query is not None else UNSET
    try:
        render(list_space_labels.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_space_labels, kwargs)


@group.command("save-repo-label")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def save_repo_label_cmd(ctx, repo_identifier, body_json):
    """Save label and values at repo level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = SaveRepoLabelBody.from_dict(json.loads(body_json))
    try:
        render(save_repo_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(save_repo_label, kwargs)


@group.command("save-space-label")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def save_space_label_cmd(ctx, body_json):
    """Save label and values at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if body_json:
        kwargs["body"] = SaveSpaceLabelBody.from_dict(json.loads(body_json))
    try:
        render(save_space_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(save_space_label, kwargs)


@group.command("unassign-label")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("pullreq_number", metavar="PULLREQ_NUMBER")
@click.argument("label_id", metavar="LABEL_ID")
@click.pass_context
def unassign_label_cmd(ctx, repo_identifier, pullreq_number, label_id):
    """Unassign label from pull request"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["pullreq_number"] = pullreq_number
    kwargs["label_id"] = label_id
    try:
        render(unassign_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(unassign_label, kwargs)


@group.command("update-repo-label")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("key", metavar="KEY")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_repo_label_cmd(ctx, repo_identifier, key, body_json):
    """Update label at repo level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["key"] = key
    if body_json:
        kwargs["body"] = UpdateRepoLabelBody.from_dict(json.loads(body_json))
    try:
        render(update_repo_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_repo_label, kwargs)


@group.command("update-repo-label-value")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("key", metavar="KEY")
@click.argument("value", metavar="VALUE")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_repo_label_value_cmd(ctx, repo_identifier, key, value, body_json):
    """Update label value at repo level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["key"] = key
    kwargs["value"] = value
    if body_json:
        kwargs["body"] = UpdateRepoLabelValueBody.from_dict(json.loads(body_json))
    try:
        render(update_repo_label_value.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_repo_label_value, kwargs)


@group.command("update-space-label")
@click.argument("key", metavar="KEY")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_space_label_cmd(ctx, key, body_json):
    """Update label at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["key"] = key
    if body_json:
        kwargs["body"] = UpdateSpaceLabelBody.from_dict(json.loads(body_json))
    try:
        render(update_space_label.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_space_label, kwargs)


@group.command("update-space-label-value")
@click.argument("key", metavar="KEY")
@click.argument("value", metavar="VALUE")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_space_label_value_cmd(ctx, key, value, body_json):
    """Update label value at account, org or project level"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["key"] = key
    kwargs["value"] = value
    if body_json:
        kwargs["body"] = UpdateSpaceLabelValueBody.from_dict(json.loads(body_json))
    try:
        render(update_space_label_value.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_space_label_value, kwargs)

