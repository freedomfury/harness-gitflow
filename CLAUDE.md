# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Harness CI/CD proof-of-concept for a golden image build pipeline with multi-branch release workflow, running on the **Harness Free Tier**. Infrastructure is managed with Terraform; pipelines are defined in YAML and triggered by webhooks from Harness Code (built-in git hosting).

## Session Setup

```bash
cd path/to/harness-poc
source activate
harness-cli --help
```

That's it. `activate` loads the venv and credentials. `harness-cli` is ready.

See **[docs/cli.md](docs/cli.md)** for common commands, output filtering, and troubleshooting.

## Workspace Boundary

Only `repo/` is mirrored to Harness Code (`image-build`) and visible to pipeline execution as repository content.

Everything outside `repo/` is local control-plane material for operating the project:
- Terraform (`infra/`)
- pipeline definitions (`pipelines/`)
- credentials/bootstrap (`exports`, installers)
- generated specs and project documentation (`docs/`)

Rule of thumb: if a change must affect Harness repository behavior at runtime, it must land under `repo/`.

**Current status:** Flow proven end-to-end through sprints 0.3.0–0.10.0. Image build steps are intentionally mocked (2-second sleeps + MinIO stubs); the POC is about proving the multi-branch flow, not the build.

## Documents

| File | What it contains |
|------|-----------------|
| `README.md` (root) | Project overview, quickstart, status, doc index |
| `docs/design.md` | **The heart.** Branch strategy, VERSION file, artifact lifecycle, ASCII flow diagrams |
| `docs/events.md` | Event map: triggers, branch rules, what fires when |
| `docs/cli.md` | `harness-cli` setup, common commands, `--format` filtering |
| `docs/sdk-generation.md` | How to regenerate the SDKs and CLI from OpenAPI specs |
| `docs/lessons-learned.md` | Hard-won lessons from fighting Harness webhooks, triggers, and infra setup |
| `docs/endpoints.md` | Raw API reference with curl examples (fallback when SDK doesn't cover) |
| `docs/invoke-project-guide.md` | Python Invoke layout — reference for the future `imageflow` workflow layer |
| `docs/architecture.drawio` | Visual diagram of the full system |

## Git Workflow

```
dev/* push/PR → dev_build (validate) → PR to stg-* → merge → stg_merge (promote) → PR to main → merge → main_release
```

## Key Files

| Path | Purpose |
|------|---------|
| `pipelines/*.yaml` | Pipeline definitions (Terraform reads these via `file(...)`) |
| `infra/*.tf` | Terraform: project, repo, pipelines, triggers, branch rules |
| `repo/` | Local clone of `image-build` Harness Code repo |
| `exports` | Credentials: `source exports` before running CLI or Terraform |

### SDK and CLI

| Path | Purpose |
|------|---------|
| `harness-code-openapi.yaml` | Harness Code OpenAPI spec |
| `harness-pipeline-openapi.yaml` | Harness Pipeline OpenAPI spec |
| `tool/harness-code-api-client/` | Generated Code SDK (141 endpoints) |
| `tool/harness-pipeline-api-client/` | Generated Pipeline SDK (86 endpoints) |
| `tool/harness-platform-api-client/` | Generated Platform (NG) SDK — large spec, only `ng-file-store` wired into the CLI |
| `tool/harness-cli/` | Auto-generated CLI (`main.py` + command files are git-ignored/regenerated; only `run`, `logs`, `output.py`, `generate.py` are tracked) |
| `tool/harness-cli/generate.py` | CLI generator — `python generate.py` regenerates everything |
| `tool/harness-cli/harness_cli/commands/logs.py` | Custom: `logs latest/find/get` |
| `tool/harness-cli/harness_cli/commands/run.py` | Custom: `run <pipeline> --branch <branch>` |
| `tool/Dockerfile` | Container image (`freedomfury/imageflow`) |
| `tool/BUILD.md` | Container build/push instructions |

> **Note:** `tool/` is at the project root, **not** inside `repo/`. It is local control-plane tooling and is intentionally excluded from the Harness Code remote. The venv and credentials are auto-loaded via `/etc/sandbox-persistent.sh` — `harness-cli` is available immediately in any new shell session without any setup.

## Three-Layer Tool Architecture

| Layer | When to use | Example |
|-------|-------------|---------|
| **CLI** (`harness-cli`) | One-off commands, troubleshooting, pipeline YAML one-liners | `harness-cli repos create-branch image-build stg-0.5.0` |
| **SDK** (Python import) | `imageflow` invoke tasks composing multiple calls with logic | `from api_specification_client.api.repository import create_branch` |
| **Terraform** | Permanent infrastructure that persists across sprints | Projects, repos, pipelines, triggers, `protect_main` rule |

**Responsibility split:**
- **Terraform** — stateful, permanent: projects, repos, pipeline definitions, triggers, permanent branch rules
- **SDK/CLI** — dynamic, runtime: ephemeral stg branches, VERSION files, sprint-scoped rules, PRs, status checks

## Running Terraform

```bash
source exports
export HARNESS_ACCOUNT_ID=$POC_HARNESS_ACCOUNT_ID
export HARNESS_PLATFORM_API_KEY=$POC_HARNESS_API_KEY
terraform apply \
  -var="code_api_key=$POC_HARNESS_API_KEY" \
  -var="minio_url=$MINIO_URL" \
  -var="minio_user=$MINIO_USER" \
  -var="minio_pass=$MINIO_PASS"
```

**Critical:** replacing a pipeline disconnects its triggers. Always `-replace` the pipeline's triggers in the same apply:

```bash
terraform apply \
  -replace=harness_platform_pipeline.dev_build \
  -replace=harness_platform_triggers.dev_build_push \
  -replace=harness_platform_triggers.dev_build_branch_create \
  -replace=harness_platform_triggers.dev_build_pr
```

## SDK Generation (Quick Reference)

```bash
source exports

# Fetch specs
curl -s "https://app.harness.io/gateway/code/openapi.yaml" -H "x-api-key: $POC_HARNESS_API_KEY" > harness-code-openapi.yaml
curl -s "https://app.harness.io/gateway/pipeline/api/openapi.yaml" -H "x-api-key: $POC_HARNESS_API_KEY" > harness-pipeline-openapi.yaml

# Generate SDKs
openapi-python-client generate --path harness-code-openapi.yaml --output-path tool/harness-code-api-client
openapi-python-client generate --path harness-pipeline-openapi.yaml --output-path tool/harness-pipeline-api-client --config <(echo 'literal_enums: true')

# Generate CLI
cd tool/harness-cli && python generate.py

# Install (use uv into project venv)
uv pip install -e tool/harness-code-api-client -e tool/harness-pipeline-api-client -e tool/harness-cli
```

## Container

```bash
cd tool
docker build -t freedomfury/imageflow:latest .
docker push freedomfury/imageflow:latest
```

Base: `almalinux/9-minimal:9.7`. Contains: Python 3.12, pip, git, envsubst, both SDKs, CLI.

## Critical Harness Gotchas

- **Webhook trigger YAML** requires exact 4-level nesting (`source.spec.spec.spec`)
- **Push events** use `targetBranch`, PR events use `sourceBranch`
- **Status check IDs** are `{pipelineId}-{stageId}` (e.g., `dev_build-validate`)
- **Pipeline execute API** expects raw YAML body with `Content-Type: application/yaml`
- **`$DRONE_OUTPUT`** is per-container — use workspace files or Harness `outputVariables` instead
- **Pipeline SDK** has model parsing bugs — CLI uses `render_raw` fallback
- **PR merge API** requires `source_sha` field (not `source_commit_sha`)
- **`Pipeline Rollback: NotStarted`** in logs output is normal — it's Harness's built-in rollback stage, only activates on failure

## Custom CLI Commands

**`harness-cli run <pipeline> --branch <branch>`** — triggers a pipeline execution via `/pipeline/execute/{id}` with `Content-Type: application/yaml`.

**`harness-cli logs latest/find/get`** — fetches step logs from the log-service API:
- `logs latest <pipeline>` — list steps for most recent execution
- `logs latest <pipeline> --step <step_id> --stage <stage_id>` — fetch step logs
- `logs find <exec_id>` — list steps for a specific execution
- `logs get <exec_id> <step_id> -p <pipeline> -s <stage>` — fetch logs for specific step

Default `--stage` is `release`. Override with `-s promote` for stg_merge, `-s validate` for dev_build.
