"""Harness CLI — typed pass-through for Harness Code, Pipeline, and Platform APIs.

Command groups for the SDKs are built dynamically at import time by reflecting
over the installed SDKs (see ``loader.py``); there is no code-generation step.
The hand-written custom commands (``run``, ``logs``, ``ng-file-store``) are
registered below.
"""

import click

from harness_cli.config import HarnessConfig
from harness_cli.loader import register_all


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
@click.option("-f", "--format", "format_expr", default=None, help="jq-style filter for output (e.g., '.[].number, .[].state')")
@click.option("-v", "--verbose", is_flag=True, default=False, help="Show raw response bodies in error messages")
@click.pass_context
def cli(ctx, format_expr, verbose):
    """Harness CLI — typed pass-through for Harness Code and Pipeline APIs.

    Credentials resolved from environment variables:

      Pipeline:  HARNESS_ACCOUNT_ID, HARNESS_ORG_ID, HARNESS_PROJECT_ID, HARNESS_PASSWORD_API

      Local dev: POC_HARNESS_ACCOUNT_ID, POC_HARNESS_API_KEY"""
    ctx.ensure_object(dict)
    ctx.obj = LazyConfig()
    if format_expr is not None:
        ctx.obj["format"] = format_expr
    ctx.obj["verbose"] = verbose


# Auto-discovered SDK command groups (each built lazily on first access)
register_all(cli)

# Custom (hand-written) command groups
from harness_cli.commands.run import run as run_cmd
from harness_cli.commands.logs import logs as logs_group
from harness_cli.commands.ng_file_store import group as ng_file_store_group

cli.add_command(run_cmd, "run")
cli.add_command(logs_group, "logs")
cli.add_command(ng_file_store_group, "ng-file-store")


if __name__ == "__main__":
    cli()
