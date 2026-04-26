"""Auto-generated CLI commands for branch_sequences endpoints."""

import click

from pipeline_service_api_reference_client.api.branch_sequences import (
    delete_branch_sequence,
    delete_branch_sequences,
    get_branch_sequence,
    list_branch_sequences,
    set_branch_sequence,
)

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Branch sequences."""
    pass


@group.command("delete-branch-sequence")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.option("--repo-url", default=None)
@click.option("--branch", default=None)
@click.pass_context
def delete_branch_sequence_cmd(ctx, pipeline_identifier, repo_url, branch):
    """Delete Branch Sequence"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    if repo_url is not None:
        kwargs["repo_url"] = repo_url
    if branch is not None:
        kwargs["branch"] = branch
    try:
        render(delete_branch_sequence.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_branch_sequence, kwargs)


@group.command("delete-branch-sequences")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.pass_context
def delete_branch_sequences_cmd(ctx, pipeline_identifier):
    """Delete Branch Sequences"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    try:
        render(delete_branch_sequences.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(delete_branch_sequences, kwargs)


@group.command("get-branch-sequence")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.option("--repo-url", default=None)
@click.option("--branch", default=None)
@click.pass_context
def get_branch_sequence_cmd(ctx, pipeline_identifier, repo_url, branch):
    """Get Branch Sequence"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    if repo_url is not None:
        kwargs["repo_url"] = repo_url
    if branch is not None:
        kwargs["branch"] = branch
    try:
        render(get_branch_sequence.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(get_branch_sequence, kwargs)


@group.command("list-branch-sequences")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.pass_context
def list_branch_sequences_cmd(ctx, pipeline_identifier):
    """List Branch Sequences"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    try:
        render(list_branch_sequences.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(list_branch_sequences, kwargs)


@group.command("set-branch-sequence")
@click.argument("pipeline_identifier", metavar="PIPELINE_IDENTIFIER")
@click.option("--repo-url", default=None)
@click.option("--branch", default=None)
@click.option("--sequence-id", default=None, type=int)
@click.pass_context
def set_branch_sequence_cmd(ctx, pipeline_identifier, repo_url, branch, sequence_id):
    """Set Branch Sequence"""
    kwargs = {
        "client": ctx.obj["pipeline_client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["pipeline_identifier"] = pipeline_identifier
    if repo_url is not None:
        kwargs["repo_url"] = repo_url
    if branch is not None:
        kwargs["branch"] = branch
    if sequence_id is not None:
        kwargs["sequence_id"] = sequence_id
    try:
        render(set_branch_sequence.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(set_branch_sequence, kwargs)

