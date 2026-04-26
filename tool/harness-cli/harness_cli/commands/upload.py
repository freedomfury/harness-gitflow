"""Auto-generated CLI commands for upload endpoints."""

import click

from api_specification_client.api.upload import (
    repo_artifact_download,
    repo_artifact_upload,
)

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Artifact upload and download."""
    pass


@group.command("repo-artifact-download")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("file_ref", metavar="FILE_REF")
@click.pass_context
def repo_artifact_download_cmd(ctx, repo_identifier, file_ref):
    """Repo artifact download"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["file_ref"] = file_ref
    try:
        render(repo_artifact_download.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(repo_artifact_download, kwargs)


@group.command("repo-artifact-upload")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", required=True, help="JSON request body")
@click.pass_context
def repo_artifact_upload_cmd(ctx, repo_identifier, body_json):
    """Repo artifact upload"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    try:
        render(repo_artifact_upload.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(repo_artifact_upload, kwargs)

