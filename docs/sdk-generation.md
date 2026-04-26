# Harness Python SDK — Generation Guide

This documents how to generate typed Python SDKs and a CLI from Harness's OpenAPI specs. The process is fully repeatable: fetch specs, run generator, install.

## What We Built

| Component | Location | Endpoints | Status |
|-----------|----------|-----------|--------|
| Code SDK | `repo/tool/harness-code-api-client/` | 141 | Clean — no parsing issues |
| Pipeline SDK | `repo/tool/harness-pipeline-api-client/` | 86 | Working — some model parsing bugs, handled by `render_raw` fallback |
| CLI | `repo/tool/harness-cli/` | 225 (26 groups) | Auto-generated from both SDKs |
| CLI generator | `repo/tool/harness-cli/generate.py` | — | Reads SDK function signatures, outputs Click commands |

### CLI Command Groups

**Code API** (no prefix): `repos`, `pr`, `rules`, `checks`, `webhooks`, `labels`, `settings`, `upload`, `principals`, `resource`, `user`, `usergroups`

**Pipeline API** (`pl-` prefix): `pl-pipeline`, `pl-execute`, `pl-executions`, `pl-triggers`, `pl-trigger-events`, `pl-webhook-triggers`, `pl-input-sets`, `pl-filters`, `pl-queued`, `pl-dashboard`, `pl-refresh`, `pl-retention`, `pl-branch-sequences`, `pl-approvals`

## Prerequisites

```bash
pip install openapi-python-client
```

No Java required. Python 3.10+.

## Step 1: Fetch the OpenAPI Specs

Harness is split into separate microservices, each with its own OpenAPI spec at `https://app.harness.io/gateway/{service}/api/openapi.yaml`. You need an API key to fetch them.

```bash
source exports  # sets POC_HARNESS_API_KEY

# Code API (repos, branches, PRs, rules, webhooks, status checks)
curl -s "https://app.harness.io/gateway/code/openapi.yaml" \
  -H "x-api-key: $POC_HARNESS_API_KEY" > harness-code-openapi.yaml

# Pipeline API (pipeline CRUD, execute, triggers, execution details)
curl -s "https://app.harness.io/gateway/pipeline/api/openapi.yaml" \
  -H "x-api-key: $POC_HARNESS_API_KEY" > harness-pipeline-openapi.yaml
```

### All Available Specs

Confirmed reachable with an API key (as of 2026-04-13):

| Service | Path | Size | In use? |
|---------|------|------|---------|
| Code | `gateway/code/openapi.yaml` | 379KB | Yes |
| Pipeline | `gateway/pipeline/api/openapi.yaml` | 748KB | Yes |
| Platform (ng) | `gateway/ng/api/openapi.yaml` | 1.4MB | No — Terraform handles this |
| Template | `gateway/template/api/openapi.yaml` | 256KB | No |
| Resource Group | `gateway/resourcegroup/api/openapi.yaml` | 264KB | No |
| Auth/RBAC | `gateway/authz/api/openapi.yaml` | 264KB | No |
| Audit | `gateway/audit/api/openapi.yaml` | 110KB | No |
| CCM (Cloud Cost) | `gateway/ccm/api/openapi.yaml` | 633KB | No |

Services that returned 404/401: CD, CI, STO, CF, CE, IACM, log-service, gitops, gateway.

### Adding a New API

To add a new service (e.g., Platform):

1. Fetch the spec
2. Generate the SDK: `openapi-python-client generate --path <spec> --output-path repo/tool/harness-<name>-api-client --config config.yaml`
3. Add a new entry to the `SDKS` dict in `generate.py`
4. Run `python generate.py --sdk <name>`

New commands appear in the CLI automatically.

## Step 2: Generate the SDKs

```bash
# Code SDK — generates cleanly
openapi-python-client generate \
  --path harness-code-openapi.yaml \
  --output-path repo/tool/harness-code-api-client

# Pipeline SDK — needs literal_enums config
cat > /tmp/opc-config.yaml << 'EOF'
literal_enums: true
EOF
openapi-python-client generate \
  --path harness-pipeline-openapi.yaml \
  --output-path repo/tool/harness-pipeline-api-client \
  --config /tmp/opc-config.yaml
```

### Known Generation Issues

**Code spec (clean):**
- `archive` endpoint skipped (binary response types)
- Two webhook list endpoints skipped (enum default mismatch)
- No impact on core functionality

**Pipeline spec (has bugs):**
- Duplicate enum values — requires `literal_enums: true` config
- `WorkflowGraph` schema skipped (duplicate model name)
- Some `application/yaml` request bodies skipped
- Model parsing fails on some responses (e.g., `PMSPipelineSummaryResponse.filters`) — the CLI's `render_raw` fallback handles this by re-executing with raw httpx

**Bad defaults in both specs (handled by CLI generator):**
- `max_divergence=0` — API requires positive integer → CLI passes `UNSET`
- `git_ref="{Repository Default Branch}"` — literal placeholder → CLI passes `UNSET`
- Enum defaults (sort, order) → CLI passes `UNSET` to let server decide
- Boolean defaults that are Unset objects → CLI defaults to `False`

**Additional generator bugs fixed:**
- Required body params had `default=None` → generator detects `has_default=False` and adds `required=True` to Click option
- `<class '...'>` annotation format for required (non-optional) body params → matched via `'>` regex pattern
- Function name collisions (e.g., function `list_repos` shadows SDK import `list_repos`) → all Click handler functions suffixed with `_cmd`
- Generator overwrites `main.py` on every run → preserves custom `logs` and `run` commands and `_api_key` in LazyConfig

## Step 3: Install the SDKs

```bash
pip install -e repo/tool/harness-code-api-client
pip install -e repo/tool/harness-pipeline-api-client
```

## Step 4: Generate and Install the CLI

```bash
cd repo/tool/harness-cli

# Generate all groups from all SDKs
python generate.py

# Or target specific SDKs
python generate.py --sdk code
python generate.py --sdk pipeline

# Install
pip install -e .
```

The generator introspects SDK function signatures and auto-generates Click commands. It handles bad defaults globally and uses `render_raw` fallback for Pipeline SDK model parsing failures.

## Usage

### SDK (for code — imageflow, scripts, etc.)

```python
from api_specification_client import AuthenticatedClient
from api_specification_client.api.repository import list_branches, create_branch
from api_specification_client.models import OpenapiCreateBranchRequest

# Code API client
client = AuthenticatedClient(
    base_url="https://app.harness.io/gateway/code/api/v1",
    token="your-api-key",
    prefix="",
    auth_header_name="x-api-key",
)

resp = list_branches.sync_detailed(
    "image-build",
    client=client,
    account_identifier="your-account-id",
    org_identifier="default",
    project_identifier="image_flow",
)
```

```python
from pipeline_service_api_reference_client import AuthenticatedClient
from pipeline_service_api_reference_client.api.pipeline import get_pipeline_list

# Pipeline API client (different base URL)
client = AuthenticatedClient(
    base_url="https://app.harness.io/gateway/pipeline/api",
    token="your-api-key",
    prefix="",
    auth_header_name="x-api-key",
)
```

### CLI (for humans, troubleshooting, one-offs, AI assistant use)

```bash
source exports

# Code API
harness-cli repos list-repos
harness-cli repos list-branches image-build
harness-cli repos get-raw image-build VERSION
harness-cli repos create-branch image-build my-branch --target main
harness-cli pr list-pull-req image-build
harness-cli rules repo-rule-list image-build
harness-cli checks list-status-check-recent image-build

# Pipeline API
harness-cli pl-pipeline get-pipeline-list
harness-cli pl-executions get-list-of-executions --pipeline-identifier dev_build
harness-cli pl-triggers get-list-for-target --target-identifier dev_build
```

### Custom Commands

Two commands are hand-written and not auto-generated. The generator always emits them so they survive regeneration.

```bash
# Trigger a pipeline on a branch (SDK execute endpoint doesn't pass branch correctly)
harness-cli run main_release --branch main

# Pipeline step logs
harness-cli logs latest main_release               # list steps for latest run
harness-cli logs latest main_release --step close_sprint  # fetch logs for a step
harness-cli logs find <exec-id>                    # list steps for a specific execution
harness-cli logs get <exec-id> <step-id> -p main_release  # logs for specific exec + step
```

## Auth Differences Between APIs

| | Code API | Pipeline API |
|---|----------|-------------|
| Base URL | `/gateway/code/api/v1` | `/gateway/pipeline/api` |
| Account ID | `accountIdentifier` query param | `accountIdentifier` query param |
| Org/Project | Query params | Query params |
| API Key | `x-api-key` header | `x-api-key` header |

The `config.py` in `harness-cli` creates separate clients for each API via `get_client()` and `get_pipeline_client()`. Credentials are shared — resolved from `HARNESS_PASSWORD_API` (pipeline env) or `POC_HARNESS_API_KEY` (local dev).

## When to Use What

| Layer | When |
|-------|------|
| **CLI** | One-off commands in pipeline YAML, interactive troubleshooting, AI assistant checking state |
| **SDK** | `imageflow` invoke tasks that compose multiple API calls with logic |
| **Terraform** | Permanent infrastructure (projects, repos, pipelines, triggers, permanent branch rules) |

## Regenerating After API Changes

```bash
# Re-fetch specs
source exports
curl -s "https://app.harness.io/gateway/code/openapi.yaml" \
  -H "x-api-key: $POC_HARNESS_API_KEY" > harness-code-openapi.yaml
curl -s "https://app.harness.io/gateway/pipeline/api/openapi.yaml" \
  -H "x-api-key: $POC_HARNESS_API_KEY" > harness-pipeline-openapi.yaml

# Regenerate SDKs (--overwrite replaces existing)
openapi-python-client generate \
  --path harness-code-openapi.yaml \
  --output-path repo/tool/harness-code-api-client \
  --overwrite

openapi-python-client generate \
  --path harness-pipeline-openapi.yaml \
  --output-path repo/tool/harness-pipeline-api-client \
  --config /tmp/opc-config.yaml \
  --overwrite

# Regenerate CLI
cd repo/tool/harness-cli && python generate.py

# Reinstall
pip install -e repo/tool/harness-code-api-client
pip install -e repo/tool/harness-pipeline-api-client
pip install -e repo/tool/harness-cli
```
