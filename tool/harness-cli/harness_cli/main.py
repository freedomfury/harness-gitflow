"""Harness CLI — auto-generated typed pass-through for Harness APIs."""

import click

from harness_cli.config import HarnessConfig

from harness_cli.commands.labels import group as labels_group
from harness_cli.commands.principals import group as principals_group
from harness_cli.commands.pullreq import group as pullreq_group
from harness_cli.commands.repository import group as repository_group
from harness_cli.commands.resource import group as resource_group
from harness_cli.commands.rules import group as rules_group
from harness_cli.commands.settings import group as settings_group
from harness_cli.commands.status_checks import group as status_checks_group
from harness_cli.commands.upload import group as upload_group
from harness_cli.commands.user import group as user_group
from harness_cli.commands.usergroups import group as usergroups_group
from harness_cli.commands.webhook import group as webhook_group
from harness_cli.commands.ng_file_store import group as ng_file_store_group
from harness_cli.commands.pl_approvals import group as pl_approvals_group
from harness_cli.commands.pl_branch_sequences import group as pl_branch_sequences_group
from harness_cli.commands.pl_filter_ import group as pl_filter__group
from harness_cli.commands.pl_pipeline import group as pl_pipeline_group
from harness_cli.commands.pl_pipeline_dashboard import group as pl_pipeline_dashboard_group
from harness_cli.commands.pl_pipeline_data_retention import group as pl_pipeline_data_retention_group
from harness_cli.commands.pl_pipeline_execute import group as pl_pipeline_execute_group
from harness_cli.commands.pl_pipeline_execution_details import group as pl_pipeline_execution_details_group
from harness_cli.commands.pl_pipeline_input_set import group as pl_pipeline_input_set_group
from harness_cli.commands.pl_pipeline_refresh import group as pl_pipeline_refresh_group
from harness_cli.commands.pl_queued_pipeline_executions import group as pl_queued_pipeline_executions_group
from harness_cli.commands.pl_triggers import group as pl_triggers_group
from harness_cli.commands.pl_triggers_events import group as pl_triggers_events_group
from harness_cli.commands.pl_webhook_triggers import group as pl_webhook_triggers_group


class LazyConfig(dict):
    """Lazily resolves Harness config on first access, so --help works without credentials."""

    _resolved = False

    def _resolve(self):
        if not self._resolved:
            config = HarnessConfig.from_env()
            self["client"] = config.get_client()
            self["pipeline_client"] = config.get_pipeline_client()
            self["platform_client"] = config.get_platform_client()
            self["account_id"] = config.account_id
            self["org_id"] = config.org_id
            self["project_id"] = config.project_id
            self["_api_key"] = config.api_key
            self._resolved = True

    def __getitem__(self, key):
        self._resolve()
        return super().__getitem__(key)


@click.group()
@click.option("--format", "-f", "format_expr", default=None,
              help="jq-style filter for output (e.g., '.[].number, .[].state')")
@click.pass_context
def cli(ctx, format_expr):
    """Harness CLI — typed pass-through for Harness Code and Pipeline APIs.

    Credentials resolved from environment variables:

      Pipeline:  HARNESS_ACCOUNT_ID, HARNESS_ORG_ID, HARNESS_PROJECT_ID, HARNESS_PASSWORD_API

      Local dev: POC_HARNESS_ACCOUNT_ID, POC_HARNESS_API_KEY"""
    ctx.ensure_object(dict)
    ctx.obj = LazyConfig()
    ctx.obj["format"] = format_expr


cli.add_command(status_checks_group, "checks")
cli.add_command(labels_group, "labels")
cli.add_command(ng_file_store_group, "ng-file-store")
cli.add_command(pl_approvals_group, "pl-approvals")
cli.add_command(pl_branch_sequences_group, "pl-branch-sequences")
cli.add_command(pl_pipeline_dashboard_group, "pl-dashboard")
cli.add_command(pl_pipeline_execute_group, "pl-execute")
cli.add_command(pl_pipeline_execution_details_group, "pl-executions")
cli.add_command(pl_filter__group, "pl-filters")
cli.add_command(pl_pipeline_input_set_group, "pl-input-sets")
cli.add_command(pl_pipeline_group, "pl-pipeline")
cli.add_command(pl_queued_pipeline_executions_group, "pl-queued")
cli.add_command(pl_pipeline_refresh_group, "pl-refresh")
cli.add_command(pl_pipeline_data_retention_group, "pl-retention")
cli.add_command(pl_triggers_events_group, "pl-trigger-events")
cli.add_command(pl_triggers_group, "pl-triggers")
cli.add_command(pl_webhook_triggers_group, "pl-webhook-triggers")
cli.add_command(pullreq_group, "pr")
cli.add_command(principals_group, "principals")
cli.add_command(repository_group, "repos")
cli.add_command(resource_group, "resource")
cli.add_command(rules_group, "rules")
cli.add_command(settings_group, "settings")
cli.add_command(upload_group, "upload")
cli.add_command(user_group, "user")
cli.add_command(usergroups_group, "usergroups")
cli.add_command(webhook_group, "webhooks")

# Custom commands (not auto-generated)
from harness_cli.commands.logs import logs as logs_group
cli.add_command(logs_group, "logs")
from harness_cli.commands.run import run as run_cmd
cli.add_command(run_cmd, "run")
from harness_cli.commands.ng_file_store import group as ng_file_store_group
cli.add_command(ng_file_store_group, "ng-file-store")


if __name__ == "__main__":
    cli()
