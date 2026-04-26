"""Auto-generated CLI commands for webhook endpoints."""

import json

import click

from api_specification_client.api.webhook import (
    create_repo_webhook,
    create_space_webhook,
    delete_repo_webhook,
    delete_space_webhook,
    get_repo_webhook,
    get_repo_webhook_execution,
    get_space_webhook,
    get_space_webhook_execution,
    list_repo_webhook_executions,
    list_space_webhook_executions,
    retrigger_repo_webhook_execution,
    retrigger_space_webhook_execution,
    update_repo_webhook,
    update_space_webhook,
)
from api_specification_client.models.openapi_create_repo_webhook_request import OpenapiCreateRepoWebhookRequest
from api_specification_client.models.openapi_update_repo_webhook_request import OpenapiUpdateRepoWebhookRequest
from api_specification_client.models.openapi_update_space_webhook_request import OpenapiUpdateSpaceWebhookRequest
from api_specification_client.models.types_webhook_create_input import TypesWebhookCreateInput

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Webhook management and execution history."""
    pass


@group.command("create-repo-webhook")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def create_repo_webhook_cmd(ctx, repo_identifier, body_json):
    """Create repo webhook"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = OpenapiCreateRepoWebhookRequest.from_dict(json.loads(body_json))
    try:
        render(create_repo_webhook.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(create_repo_webhook, kwargs)


@group.command("create-space-webhook")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def create_space_webhook_cmd(ctx, body_json):
    """Create acc, org or proj webhook"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if body_json:
        kwargs["body"] = TypesWebhookCreateInput.from_dict(json.loads(body_json))
    try:
        render(create_space_webhook.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(create_space_webhook, kwargs)


@group.command("delete-repo-webhook")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.pass_context
def delete_repo_webhook_cmd(ctx, repo_identifier, webhook_identifier):
    """Delete repo webhook"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["webhook_identifier"] = webhook_identifier
    try:
        render(delete_repo_webhook.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_repo_webhook, kwargs)


@group.command("delete-space-webhook")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.pass_context
def delete_space_webhook_cmd(ctx, webhook_identifier):
    """Delete acc, org or proj webhook"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["webhook_identifier"] = webhook_identifier
    try:
        render(delete_space_webhook.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_space_webhook, kwargs)


@group.command("get-repo-webhook")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.pass_context
def get_repo_webhook_cmd(ctx, repo_identifier, webhook_identifier):
    """Get repo webhook"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["webhook_identifier"] = webhook_identifier
    try:
        render(get_repo_webhook.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_repo_webhook, kwargs)


@group.command("get-repo-webhook-execution")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.argument("webhook_execution_id", metavar="WEBHOOK_EXECUTION_ID")
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.pass_context
def get_repo_webhook_execution_cmd(ctx, repo_identifier, webhook_identifier, webhook_execution_id, page, limit):
    """Get repo webhook execution"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["webhook_identifier"] = webhook_identifier
    kwargs["webhook_execution_id"] = webhook_execution_id
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    try:
        render(get_repo_webhook_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_repo_webhook_execution, kwargs)


@group.command("get-space-webhook")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.pass_context
def get_space_webhook_cmd(ctx, webhook_identifier):
    """Get acc, org or proj webhook"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["webhook_identifier"] = webhook_identifier
    try:
        render(get_space_webhook.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_space_webhook, kwargs)


@group.command("get-space-webhook-execution")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.argument("webhook_execution_id", metavar="WEBHOOK_EXECUTION_ID")
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.pass_context
def get_space_webhook_execution_cmd(ctx, webhook_identifier, webhook_execution_id, page, limit):
    """Get acc, org or proj webhook execution"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["webhook_identifier"] = webhook_identifier
    kwargs["webhook_execution_id"] = webhook_execution_id
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    try:
        render(get_space_webhook_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_space_webhook_execution, kwargs)


@group.command("list-repo-webhook-executions")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.pass_context
def list_repo_webhook_executions_cmd(ctx, repo_identifier, webhook_identifier, page, limit):
    """List repo webhook executions"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["webhook_identifier"] = webhook_identifier
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    try:
        render(list_repo_webhook_executions.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_repo_webhook_executions, kwargs)


@group.command("list-space-webhook-executions")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.pass_context
def list_space_webhook_executions_cmd(ctx, webhook_identifier, page, limit):
    """List acc, org or proj webhook executions"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["webhook_identifier"] = webhook_identifier
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    try:
        render(list_space_webhook_executions.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_space_webhook_executions, kwargs)


@group.command("retrigger-repo-webhook-execution")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.argument("webhook_execution_id", metavar="WEBHOOK_EXECUTION_ID")
@click.pass_context
def retrigger_repo_webhook_execution_cmd(ctx, repo_identifier, webhook_identifier, webhook_execution_id):
    """Retrigger repo webhook execution"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["webhook_identifier"] = webhook_identifier
    kwargs["webhook_execution_id"] = webhook_execution_id
    try:
        render(retrigger_repo_webhook_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(retrigger_repo_webhook_execution, kwargs)


@group.command("retrigger-space-webhook-execution")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.argument("webhook_execution_id", metavar="WEBHOOK_EXECUTION_ID")
@click.pass_context
def retrigger_space_webhook_execution_cmd(ctx, webhook_identifier, webhook_execution_id):
    """Retrigger acc, org or proj webhook execution"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["webhook_identifier"] = webhook_identifier
    kwargs["webhook_execution_id"] = webhook_execution_id
    try:
        render(retrigger_space_webhook_execution.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(retrigger_space_webhook_execution, kwargs)


@group.command("update-repo-webhook")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_repo_webhook_cmd(ctx, repo_identifier, webhook_identifier, body_json):
    """Update repo webhook"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["webhook_identifier"] = webhook_identifier
    if body_json:
        kwargs["body"] = OpenapiUpdateRepoWebhookRequest.from_dict(json.loads(body_json))
    try:
        render(update_repo_webhook.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_repo_webhook, kwargs)


@group.command("update-space-webhook")
@click.argument("webhook_identifier", metavar="WEBHOOK_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_space_webhook_cmd(ctx, webhook_identifier, body_json):
    """Update acc, org or proj webhook"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["webhook_identifier"] = webhook_identifier
    if body_json:
        kwargs["body"] = OpenapiUpdateSpaceWebhookRequest.from_dict(json.loads(body_json))
    try:
        render(update_space_webhook.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_space_webhook, kwargs)

