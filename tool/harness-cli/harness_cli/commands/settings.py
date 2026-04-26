"""Auto-generated CLI commands for settings endpoints."""

import json

import click

from api_specification_client.api.settings import (
    find_space_general_settings,
    update_space_general_settings,
)
from api_specification_client.models.settings_general_settings_space import SettingsGeneralSettingsSpace

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Space-level settings."""
    pass


@group.command("find-space-general-settings")
@click.pass_context
def find_space_general_settings_cmd(ctx):
    """Find general settings of the account, organization, or project."""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    try:
        render(find_space_general_settings.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(find_space_general_settings, kwargs)


@group.command("update-space-general-settings")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def update_space_general_settings_cmd(ctx, body_json):
    """Update general settings of the account, organization, or project."""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if body_json:
        kwargs["body"] = SettingsGeneralSettingsSpace.from_dict(json.loads(body_json))
    try:
        render(update_space_general_settings.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(update_space_general_settings, kwargs)

