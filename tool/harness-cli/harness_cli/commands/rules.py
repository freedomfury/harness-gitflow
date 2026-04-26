"""Auto-generated CLI commands for rules endpoints."""

import json

import click

from api_specification_client.api.rules import (
    repo_rule_add,
    repo_rule_delete,
    repo_rule_get,
    repo_rule_list,
    repo_rule_update,
    space_rule_add,
    space_rule_delete,
    space_rule_get,
    space_rule_list,
    space_rule_update,
)
from api_specification_client.models.repo_rule_add_body import RepoRuleAddBody
from api_specification_client.models.repo_rule_update_body import RepoRuleUpdateBody
from api_specification_client.models.space_rule_add_body import SpaceRuleAddBody
from api_specification_client.models.space_rule_update_body import SpaceRuleUpdateBody
from api_specification_client.types import UNSET

from harness_cli.output import render, render_raw


@click.group()
def group():
    """Branch/tag protection rules."""
    pass


@group.command("repo-rule-add")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def repo_rule_add_cmd(ctx, repo_identifier, body_json):
    """Add repo protection rule"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    if body_json:
        kwargs["body"] = RepoRuleAddBody.from_dict(json.loads(body_json))
    try:
        render(repo_rule_add.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(repo_rule_add, kwargs)


@group.command("repo-rule-delete")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("rule_identifier", metavar="RULE_IDENTIFIER")
@click.pass_context
def repo_rule_delete_cmd(ctx, repo_identifier, rule_identifier):
    """Delete repo protection rule"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["rule_identifier"] = rule_identifier
    try:
        render(repo_rule_delete.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(repo_rule_delete, kwargs)


@group.command("repo-rule-get")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("rule_identifier", metavar="RULE_IDENTIFIER")
@click.pass_context
def repo_rule_get_cmd(ctx, repo_identifier, rule_identifier):
    """Get repo protection rule"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["rule_identifier"] = rule_identifier
    try:
        render(repo_rule_get.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(repo_rule_get, kwargs)


@group.command("repo-rule-list")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.option("--query", default=None)
@click.option("--order", default=None)
@click.option("--sort", default=None)
@click.option("--type", default=None, multiple=True)
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--inherited/--no-inherited", default=False)
@click.pass_context
def repo_rule_list_cmd(ctx, repo_identifier, query, order, sort, type, page, limit, inherited):
    """List repo protection rules"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["query"] = query if query is not None else UNSET
    kwargs["order"] = order if order is not None else UNSET
    kwargs["sort"] = sort if sort is not None else UNSET
    kwargs["type_"] = type if type is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["inherited"] = inherited
    try:
        render(repo_rule_list.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(repo_rule_list, kwargs)


@group.command("repo-rule-update")
@click.argument("repo_identifier", metavar="REPO_IDENTIFIER")
@click.argument("rule_identifier", metavar="RULE_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def repo_rule_update_cmd(ctx, repo_identifier, rule_identifier, body_json):
    """Update repo protection rule"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["repo_identifier"] = repo_identifier
    kwargs["rule_identifier"] = rule_identifier
    if body_json:
        kwargs["body"] = RepoRuleUpdateBody.from_dict(json.loads(body_json))
    try:
        render(repo_rule_update.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(repo_rule_update, kwargs)


@group.command("space-rule-add")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def space_rule_add_cmd(ctx, body_json):
    """Add acc/org/proj protection rule"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    if body_json:
        kwargs["body"] = SpaceRuleAddBody.from_dict(json.loads(body_json))
    try:
        render(space_rule_add.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(space_rule_add, kwargs)


@group.command("space-rule-delete")
@click.argument("rule_identifier", metavar="RULE_IDENTIFIER")
@click.pass_context
def space_rule_delete_cmd(ctx, rule_identifier):
    """Delete acc/org/proj protection rule"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["rule_identifier"] = rule_identifier
    try:
        render(space_rule_delete.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(space_rule_delete, kwargs)


@group.command("space-rule-get")
@click.argument("rule_identifier", metavar="RULE_IDENTIFIER")
@click.pass_context
def space_rule_get_cmd(ctx, rule_identifier):
    """Get acc/org/proj protection rule"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["rule_identifier"] = rule_identifier
    try:
        render(space_rule_get.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(space_rule_get, kwargs)


@group.command("space-rule-list")
@click.option("--query", default=None)
@click.option("--type", default=None, multiple=True)
@click.option("--order", default=None)
@click.option("--sort", default=None)
@click.option("--page", default=1, type=int)
@click.option("--limit", default=30, type=int)
@click.option("--inherited/--no-inherited", default=False)
@click.pass_context
def space_rule_list_cmd(ctx, query, type, order, sort, page, limit, inherited):
    """List acc/org/proj protection rules"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["query"] = query if query is not None else UNSET
    kwargs["type_"] = type if type is not None else UNSET
    kwargs["order"] = order if order is not None else UNSET
    kwargs["sort"] = sort if sort is not None else UNSET
    if page is not None:
        kwargs["page"] = page
    if limit is not None:
        kwargs["limit"] = limit
    kwargs["inherited"] = inherited
    try:
        render(space_rule_list.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(space_rule_list, kwargs)


@group.command("space-rule-update")
@click.argument("rule_identifier", metavar="RULE_IDENTIFIER")
@click.option("--body", "body_json", default=None, help="JSON request body")
@click.pass_context
def space_rule_update_cmd(ctx, rule_identifier, body_json):
    """Update acc/org/proj protection rule"""
    kwargs = {
        "client": ctx.obj["client"],
        "account_identifier": ctx.obj["account_id"],
        "org_identifier": ctx.obj["org_id"],
        "project_identifier": ctx.obj["project_id"],
    }
    kwargs["rule_identifier"] = rule_identifier
    if body_json:
        kwargs["body"] = SpaceRuleUpdateBody.from_dict(json.loads(body_json))
    try:
        render(space_rule_update.sync_detailed(**kwargs))
    except (ValueError, TypeError, KeyError, AttributeError):
        render_raw(space_rule_update, kwargs)

