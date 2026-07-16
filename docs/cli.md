# harness-cli Reference

`harness-cli` is a typed CLI for the Harness Code and Pipeline APIs, auto-generated from OpenAPI specs with two hand-written custom commands (`run`, `logs`).

## Setup (every session)

```bash
cd path/to/harness-poc
source activate
harness-cli --help
```

`activate` loads the Python venv and credentials. That's it — nothing else needed.

**If `harness-cli` gives `ModuleNotFoundError`:** the venv `.pth` files are stale. Reinstall:
```bash
uv pip install -e tool/harness-code-api-client -e tool/harness-pipeline-api-client -e tool/harness-cli
```

## Tool location

```
tool/
  harness-cli/            ← CLI source (Click-based, command groups built at runtime from the SDKs + 3 hand-written groups)
  harness-code-api-client/    ← Code API SDK (141 endpoints)
  harness-pipeline-api-client/ ← Pipeline API SDK (86 endpoints)
  harness-platform-api-client/ ← Platform (NG) SDK — large spec, only `ng-file-store` wired into the CLI
```

> **How the CLI is built:** command groups are **not** generated files. At startup, `harness_cli/loader.py` reflects over each SDK's `sync_detailed` signatures and builds the Click groups in memory (lazily, per group). All of `harness_cli/` is tracked source — `main.py`, `loader.py`, `output.py`, `config.py`, and the hand-written custom groups (`run.py`, `logs.py`, `ng_file_store.py`). To change how a param maps to a flag, edit one function in `loader.py`; there is nothing to regenerate.

> **`--body` accepts `@file`:** any command taking `--body` accepts inline JSON, `@path/to/file.json`, or `@-` for stdin (handled by `read_body` in `output.py`).

`tool/` is at the **project root**, not inside `repo/`. It is never synced to Harness Code. No git checkout needed to access it.

## Credentials

All commands read from environment variables (loaded by `source activate`):

| Variable | Used for |
|----------|----------|
| `POC_HARNESS_API_KEY` | All API calls |
| `POC_HARNESS_ACCOUNT_ID` | Account scope |
| `POC_HARNESS_ORG_ID` | Org scope (default: `default`) |
| `POC_HARNESS_PROJECT_ID` | Project scope (default: `image_flow`) |

## Command groups

| Group | API | What it does |
|-------|-----|--------------|
| `repos` | Code | Branches, files, raw content |
| `pr` | Code | Pull requests (create, merge, list, checks) |
| `rules` | Code | Branch protection rules |
| `checks` | Code | Status check results |
| `run` | Pipeline | Trigger a pipeline on a branch *(custom)* |
| `logs` | Pipeline | Fetch step logs *(custom)* |
| `pl-executions` | Pipeline | Execution details and status |
| `pl-pipeline` | Pipeline | Pipeline definitions |

## Common commands

### Branches
```bash
# List branches matching a pattern
harness-cli repos list-branches image-build --query stg --limit 10

# Get raw file content from a branch
harness-cli repos get-raw image-build VERSION --git-ref main
harness-cli repos get-raw image-build VERSION --git-ref stg-0.9.0

# Create a branch
harness-cli repos create-branch image-build --body '{"name":"stg-0.9.0","target":"main"}'

# Delete a branch
harness-cli repos delete-branch image-build <branch-name>
```

### Pull requests
```bash
# List recent PRs
harness-cli pr list-pull-req image-build --limit 5

# Get a specific PR
harness-cli pr get-pull-req image-build <number>

# Create a PR
harness-cli pr create-pull-req image-build \
  --body '{"title":"feat: my feature","source_branch":"dev/my-feature","target_branch":"stg-0.9.0","description":"..."}'

# Merge a PR (bypass_rules=true acts as repo-owner bypass)
harness-cli pr merge-pull-req-op image-build <number> \
  --body '{"method":"merge","source_sha":"<commit-sha>","bypass_rules":true}'
```

### Status checks
```bash
# What status check UIDs exist in this repo
harness-cli checks list-status-check-recent image-build

# Status check results for a specific commit
harness-cli checks list-status-check-results image-build <commit-sha>
```

### Branch protection rules
```bash
# List all rules
harness-cli rules repo-rule-list image-build

# Get a specific rule's definition
harness-cli rules repo-rule-get image-build protect_stg_0_9_0
```

### Pipelines (custom commands)
```bash
# Trigger a pipeline on a branch
harness-cli run dev_build --branch dev/feature-0.9.0
harness-cli run stg_merge --branch stg-0.9.0
harness-cli run main_release --branch main

# Latest execution status for a pipeline
harness-cli logs latest dev_build
harness-cli logs latest stg_merge
harness-cli logs latest main_release

# Specific step logs from latest execution
harness-cli logs latest dev_build --step version_precheck --stage validate
harness-cli logs latest stg_merge --step version_change_check --stage promote
harness-cli logs latest main_release --step close_sprint --stage release

# Find steps in a specific execution
harness-cli logs find <execution-id>

# Get logs for a specific step in a specific execution
harness-cli logs get <execution-id> <step-id> -p <pipeline-id> -s <stage-id>
```

## Output Formatting

All commands return raw JSON by default. Use the global `--format` / `-f` flag to filter output with jq-style expressions:

```bash
# Extract specific fields (uses jq if available, falls back to dot notation)
harness-cli --format '.[].identifier' rules repo-rule-list image-build
harness-cli -f '.[] | {number, title, state, source: .source_branch, target: .target_branch}' pr list-pull-req image-build --limit 3
harness-cli -f '.[].id, .[].status' checks list-status-check-results image-build <sha>

# Multiple comma-separated fields return one per line
harness-cli -f '.[].name' repos list-branches image-build --limit 5
harness-cli -f '.[].number, .[].title' pr list-pull-req image-build --limit 3
```

**Note:** The `--format` flag must come **before** the subcommand (Click standard pattern):
```bash
harness-cli --format '.[].name' repos list-branches image-build  # ✓
harness-cli repos list-branches image-build --format '.[].name'    # ✗ invalid option
```

**Implementation:** Uses `jq.py` Python library (bindings for jq 1.7.1). Full jq syntax supported — no external `jq` binary required, no subprocess overhead. If `jq.py` fails to parse an expression, it falls back to a simple dot-notation extractor for basic paths.

## Regenerating the CLI

After updating OpenAPI specs:
```bash
cd path/to/harness-poc

# Fetch latest specs
source activate
curl -s "https://app.harness.io/gateway/code/openapi.yaml" -H "x-api-key: $POC_HARNESS_API_KEY" > harness-code-openapi.yaml
curl -s "https://app.harness.io/gateway/pipeline/api/openapi.yaml" -H "x-api-key: $POC_HARNESS_API_KEY" > harness-pipeline-openapi.yaml

# Regenerate SDKs
openapi-python-client generate --path harness-code-openapi.yaml --output-path tool/harness-code-api-client
openapi-python-client generate --path harness-pipeline-openapi.yaml --output-path tool/harness-pipeline-api-client --config <(echo 'literal_enums: true')

# No CLI regeneration needed — commands are built at runtime from the SDKs

# Reinstall
cd path/to/harness-poc
uv pip install -e tool/harness-code-api-client -e tool/harness-pipeline-api-client -e tool/harness-cli
```
