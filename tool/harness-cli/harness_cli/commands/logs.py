"""Pipeline step log commands (log-service API, not part of generated SDK)."""

import json
import re
import sys

import click
import httpx

from harness_cli.output import http_error_message


def _make_client(ctx):
    """Create an httpx client for direct API calls."""
    return httpx.Client(
        base_url="https://app.harness.io/gateway",
        headers={"x-api-key": ctx.obj["_api_key"]},
        timeout=30,
    )


def _common_params(ctx):
    """Return the standard query params."""
    return {
        "accountIdentifier": ctx.obj["account_id"],
        "orgIdentifier": ctx.obj["org_id"],
        "projectIdentifier": ctx.obj["project_id"],
    }


def _die(msg):
    """Echo an error to stderr and exit non-zero."""
    click.echo(msg, err=True)
    sys.exit(1)


def _json_or_die(resp):
    """Parse a JSON body, exiting clearly on non-JSON responses.

    The common trigger is an expired/invalid API key, for which the Harness
    gateway returns its HTML sign-in page (HTTP 200, non-JSON).
    """
    try:
        return resp.json()
    except ValueError:
        _die(http_error_message(resp))


def _fetch_build_num(client, ctx, pipeline, execution_id):
    """Look up runSequence for a given execution_id from the summary API."""
    params = _common_params(ctx)
    params.update({"pipelineIdentifier": pipeline, "page": 0, "size": 10})

    try:
        resp = client.post(
            "/pipeline/api/pipelines/execution/summary",
            params=params,
            json={"filterType": "PipelineExecution"},
        )
    except httpx.HTTPError as e:
        _die(f"network error: {e}")

    if resp.status_code != 200:
        _die(http_error_message(resp))

    data = _json_or_die(resp)
    for ex in data.get("data", {}).get("content", []):
        if ex.get("planExecutionId") == execution_id:
            return ex.get("runSequence")
    _die(f"Execution {execution_id} not found in recent runs.")


def _fetch_latest_execution(client, ctx, pipeline):
    """Return (planExecutionId, runSequence) for the most recent execution of a pipeline."""
    params = _common_params(ctx)
    params.update({"pipelineIdentifier": pipeline, "page": 0, "size": 1})

    try:
        resp = client.post(
            "/pipeline/api/pipelines/execution/summary",
            params=params,
            json={"filterType": "PipelineExecution"},
        )
    except httpx.HTTPError as e:
        _die(f"network error: {e}")

    if resp.status_code != 200:
        _die(http_error_message(resp))

    content = _json_or_die(resp).get("data", {}).get("content", [])
    if not content:
        _die(f"No executions found for pipeline '{pipeline}'.")

    entry = content[0]
    return entry.get("planExecutionId"), entry.get("runSequence")


def _print_step_logs(client, account_id, execution_id, pipeline, run_sequence, step_id, stage):
    """Fetch and print logs for a single step."""
    log_key = f"{account_id}/pipeline/{pipeline}/{run_sequence}/-{execution_id}/{stage}/{step_id}"

    try:
        resp = client.get(
            "/log-service/blob",
            params={"accountID": account_id, "key": log_key},
        )
    except httpx.HTTPError as e:
        _die(f"network error: {e}")

    if resp.status_code != 200:
        _die(http_error_message(resp))

    text = resp.text.strip()
    if not text:
        click.echo("No logs found.")
        return

    for line in text.split("\n"):
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            clean = re.sub(r"\x1b\[[0-9;]*m", "", entry.get("out", ""))
            if clean.strip():
                click.echo(clean, nl=False)
        except json.JSONDecodeError:
            click.echo(line)


def _print_step_list(client, ctx, execution_id):
    """Fetch and print all steps for an execution."""
    try:
        resp = client.get(
            f"/pipeline/api/pipelines/execution/v2/{execution_id}",
            params=_common_params(ctx),
        )
    except httpx.HTTPError as e:
        _die(f"network error: {e}")

    if resp.status_code != 200:
        _die(http_error_message(resp))

    layout = (
        _json_or_die(resp)
        .get("data", {})
        .get("pipelineExecutionSummary", {})
        .get("layoutNodeMap", {})
    )
    if not layout:
        click.echo("No layout data found in execution.")
        return

    for _nid, node in layout.items():
        identifier = node.get("nodeIdentifier", node.get("nodeUuid", "?"))
        name = node.get("name", "?")
        status = node.get("status", "?")
        fail_msg = ""
        fi = node.get("failureInfo")
        if fi:
            fail_msg = fi.get("message", "")
        click.echo(f"{identifier} ({name}): {status}")
        if fail_msg:
            click.echo(f"  Error: {fail_msg.strip()[:300]}")


@click.group()
def logs():
    """Pipeline step logs."""
    pass


@logs.command()
@click.argument("execution_id")
@click.argument("step_id")
@click.option("--pipeline", "-p", required=True, help="Pipeline identifier")
@click.option("--stage", "-s", default="release", help="Stage identifier")
@click.pass_context
def get(ctx, execution_id, step_id, pipeline, stage):
    """Fetch logs for a pipeline step.

    Example: harness-cli logs get <exec-id> close_sprint -p main_release
    """
    account_id = ctx.obj["account_id"]
    client = _make_client(ctx)

    run_sequence = _fetch_build_num(client, ctx, pipeline, execution_id)
    if run_sequence is None:
        _die("Could not find build number for execution.")

    _print_step_logs(client, account_id, execution_id, pipeline, run_sequence, step_id, stage)


@logs.command("find")
@click.argument("execution_id")
@click.pass_context
def find_cmd(ctx, execution_id):
    """List steps and their statuses for an execution.

    Example: harness-cli logs find <exec-id>
    """
    client = _make_client(ctx)
    _print_step_list(client, ctx, execution_id)


@logs.command()
@click.argument("pipeline")
@click.option("--step", "-S", default=None, help="Step identifier to fetch logs for")
@click.option("--stage", "-s", default="release", help="Stage identifier")
@click.pass_context
def latest(ctx, pipeline, step, stage):
    """Show latest execution for a pipeline.

    Without --step, lists all steps. With --step, fetches that step's logs.

    Example: harness-cli logs latest main_release
    Example: harness-cli logs latest main_release --step close_sprint
    """
    account_id = ctx.obj["account_id"]
    client = _make_client(ctx)

    execution_id, run_sequence = _fetch_latest_execution(client, ctx, pipeline)
    if not execution_id:
        _die("Could not determine latest execution.")

    if step:
        if run_sequence is None:
            _die("Could not determine run sequence for latest execution.")
        _print_step_logs(client, account_id, execution_id, pipeline, run_sequence, step, stage)
    else:
        _print_step_list(client, ctx, execution_id)
