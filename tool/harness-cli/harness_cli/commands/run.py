"""Pipeline run command (custom, not auto-generated).

The SDK's execute endpoint uses input_set_references which doesn't support
passing branch directly. This command uses the /pipeline/execute/{id} endpoint
with Content-Type: application/yaml, which is the known working method.
"""

import sys

import click
import httpx

from harness_cli.output import http_error_message


@click.command()
@click.argument("pipeline")
@click.option("--branch", "-b", default="main", help="Branch to build")
@click.pass_context
def run(ctx, pipeline, branch):
    """Execute a pipeline on a branch.

    Example: harness-cli run main_release --branch main
    """
    account_id = ctx.obj["account_id"]
    org_id = ctx.obj["org_id"]
    project_id = ctx.obj["project_id"]
    api_key = ctx.obj["_api_key"]

    client = httpx.Client(
        base_url="https://app.harness.io/gateway/pipeline/api",
        headers={"x-api-key": api_key},
        timeout=30,
    )

    yaml_body = f"""pipeline:
  identifier: {pipeline}
  properties:
    ci:
      codebase:
        build:
          type: branch
          spec:
            branch: {branch}"""

    try:
        resp = client.post(
            f"/pipeline/execute/{pipeline}",
            params={
                "accountIdentifier": account_id,
                "orgIdentifier": org_id,
                "projectIdentifier": project_id,
                "moduleType": "CI",
            },
            content=yaml_body,
            headers={"Content-Type": "application/yaml"},
        )
    except httpx.HTTPError as e:
        click.echo(f"network error: {e}", err=True)
        sys.exit(1)

    if resp.status_code != 200:
        click.echo(http_error_message(resp), err=True)
        sys.exit(1)

    try:
        data = resp.json()
    except ValueError:
        click.echo(http_error_message(resp), err=True)
        sys.exit(1)

    execution = data.get("data", {}).get("planExecution", {})
    exec_id = execution.get("uuid", "unknown")
    status = execution.get("status", "unknown")
    run_seq = execution.get("metadata", {}).get("runSequence", "?")

    click.echo(f"Triggered: {exec_id}")
    click.echo(f"Run: #{run_seq}")
    click.echo(f"Status: {status}")
