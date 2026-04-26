"""Auto-generated CLI commands for status_checks endpoints."""

import json

import click

from api_specification_client.api.status_checks import (
    list_status_check_recent,
    list_status_check_recent_space,
    list_status_check_results,
    report_status_check_results,
)
from api_specification_client.models.report_status_check_results_body import ReportStatusCheckResultsBody
from api_specification_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Status check operations."""
    pass


@group.command("list-status-check-recent")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--query", default=None)
@click.option("--since", default=None, type=int)
@click.pass_context
def list_status_check_recent_cmd(ctx, repo_identifier, query, since):
    """List recent status check"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["query"] = query if query is not None else UNSET
    kwargs["since"] = since if since is not None else UNSET
    try:
        render(list_status_check_recent.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_status_check_recent, kwargs)


@group.command("list-status-check-recent-space")
@click.option("--query", default=None)
@click.option("--since", default=None, type=int)
@click.option("--recursive/--no-recursive", default=False)
@click.pass_context
def list_status_check_recent_space_cmd(ctx, query, since, recursive):
    """List recent status check for acc, org or proj"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["query"] = query if query is not None else UNSET
    kwargs["since"] = since if since is not None else UNSET
    kwargs["recursive"] = recursive
    try:
        render(list_status_check_recent_space.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_status_check_recent_space, kwargs)


@group.command("list-status-check-results")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("commit_sha", metavar="COMMIT_SHA")
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--query", default=None)
@click.pass_context
def list_status_check_results_cmd(ctx, repo_identifier, commit_sha, page, limit, query):
    """List status check results"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["commit_sha"] = commit_sha
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["query"] = query if query is not None else UNSET
    try:
        render(list_status_check_results.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_status_check_results, kwargs)


@group.command("report-status-check-results")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("commit_sha", metavar="COMMIT_SHA")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def report_status_check_results_cmd(ctx, repo_identifier, commit_sha, body_json):
    """Report status check results"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["commit_sha"] = commit_sha
    if body_json:
        kwargs["body"] = ReportStatusCheckResultsBody.from_dict(json.loads(body_json))
    try:
        render(report_status_check_results.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(report_status_check_results, kwargs)

