# Task: Add a `logs` command group to the Harness CLI

## Context

We have a Click-based CLI at `harness_cli/` that wraps two auto-generated Python SDKs for the Harness CI/CD platform. The CLI exposes ~225 auto-generated commands for the Code API and Pipeline API.

However, **pipeline step logs** come from a separate Harness service (the "log-service") that has **no OpenAPI spec** and is not covered by either SDK. We need a hand-written `logs` command group.

## Architecture

- **CLI framework:** Click
- **HTTP client:** httpx (already a dependency)
- **Auth:** `x-api-key` header with an API key
- **Config:** The Click context (`ctx.obj`) provides:
  - `ctx.obj["account_id"]` — Harness account ID
  - `ctx.obj["org_id"]` — org identifier (usually `"default"`)
  - `ctx.obj["project_id"]` — project identifier (usually `"image_flow"`)
  - `ctx.obj["_api_key"]` — raw API key string
  - `ctx.obj["client"]` — Code SDK authenticated client (not needed for logs)
  - `ctx.obj["pipeline_client"]` — Pipeline SDK authenticated client (not needed for logs)

## What to build

Create `harness_cli/commands/logs.py` with a Click group called `logs` containing these commands:

### 1. `harness-cli logs find <execution-id>`

Lists all steps in a pipeline execution with their status.

**API call:**
```
GET https://app.harness.io/gateway/pipeline/api/pipelines/execution/v2/{execution_id}
Query params: accountIdentifier, orgIdentifier, projectIdentifier
Header: x-api-key
```

**Response structure (JSON):**
```json
{
  "data": {
    "pipelineExecutionSummary": {
      "layoutNodeMap": {
        "<node-uuid>": {
          "name": "close sprint",
          "nodeIdentifier": "close_sprint",
          "status": "Failed",
          "nodeType": "Run",
          "failureInfo": {
            "message": "exit status 1"
          }
        }
      }
    }
  }
}
```

**Output format (plain text, one line per step):**
```
close_sprint (close sprint): Failed
  Error: exit status 1
read_version (read version): Success
tag_release_artifact (tag release artifact): Success
```

### 2. `harness-cli logs get <execution-id> <step-id> -p <pipeline> [-s <stage>]`

Fetches the actual stdout/stderr logs for a specific pipeline step.

**Step 1: Get the build number.** The log key requires a `runSequence` number. Fetch it from:
```
POST https://app.harness.io/gateway/pipeline/api/pipelines/execution/summary
Query params: accountIdentifier, orgIdentifier, projectIdentifier, pipelineIdentifier={pipeline}, page=0, size=10
Header: x-api-key
Body (JSON): {"filterType": "PipelineExecution"}
```

Response has `data.content[]` — find the entry where `planExecutionId == execution_id` and extract `runSequence`.

**Step 2: Fetch the logs.** The log key format is:
```
{account_id}/pipeline/{pipeline}/{runSequence}/-{execution_id}/{stage}/{step_id}
```

Note the `-` before the execution ID.

```
GET https://app.harness.io/gateway/log-service/blob
Query params: accountID={account_id}, key={log_key}
Header: x-api-key
```

**Response format:** JSONL (one JSON object per line):
```json
{"level":"info","pos":0,"out":"\u001b[1;33msome log output\u001b[0m\n","time":"2026-04-13T13:44:26Z","args":null}
{"level":"info","pos":1,"out":"next line\n","time":"2026-04-13T13:44:26Z","args":null}
```

**Output:** Strip ANSI escape codes from the `out` field and print each line. Use this regex to strip ANSI: `\x1b\[[0-9;]*m`

**Options:**
- `--pipeline` / `-p` (required) — pipeline identifier (e.g., `main_release`)
- `--stage` / `-s` (default: `release`) — stage identifier

### 3. `harness-cli logs latest <pipeline> [--step <step-id>]`

Convenience command: gets the most recent execution for a pipeline and shows either the step list or a specific step's logs.

**Step 1:** Fetch the latest execution:
```
POST https://app.harness.io/gateway/pipeline/api/pipelines/execution/summary
Query params: accountIdentifier, orgIdentifier, projectIdentifier, pipelineIdentifier={pipeline}, page=0, size=1
Body: {"filterType": "PipelineExecution"}
```

Extract `planExecutionId` and `runSequence` from `data.content[0]`.

**Step 2:** If `--step` is provided, fetch that step's logs (same as `logs get`). If not, list all steps (same as `logs find`).

## File structure

```python
# harness_cli/commands/logs.py

import json
import re

import click
import httpx


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


@click.group()
def logs():
    """Pipeline step logs."""
    pass


# ... commands here ...
```

## Wiring

The `logs` group is already imported in `main.py`:
```python
from harness_cli.commands.logs import logs as logs_group
# ...
cli.add_command(logs_group, "logs")
```

And `ctx.obj["_api_key"]` is already exposed in the LazyConfig.

## Error handling

- If an API call returns non-200, print `HTTP {status}: {body[:500]}` to stderr and return
- If the execution ID is not found in the summary list, print a clear error message
- If the log key returns no data, print "No logs found"

## Testing

Test against a real Harness instance:
```bash
source exports  # sets POC_HARNESS_ACCOUNT_ID and POC_HARNESS_API_KEY

# List steps for a known execution
harness-cli logs find BflGhqkmSkyPBbnHmfSRCA

# Get logs for a specific step
harness-cli logs get BflGhqkmSkyPBbnHmfSRCA close_sprint -p main_release

# Get latest execution's steps
harness-cli logs latest main_release

# Get latest execution's specific step logs
harness-cli logs latest main_release --step close_sprint
```
