# harness-cli

> **📦 Portable build — self-contained.** The SDKs in `vendor/` are already
> generated, so this folder runs on its own (no `tool/`, siblings, Dockerfile,
> or wheels). Just:
>
> ```bash
> uv sync
> uv run harness-cli --help                       # no credentials needed
> cp .env.example .env   &&   $EDITOR .env        # add your Harness creds
> uv run --env-file .env harness-cli repos get-branch image-build main
> ```
>
> To regenerate the SDKs (e.g. after a Harness API change): put your API key in
> `.env`, then `./scripts/vendor.sh` — it downloads the OpenAPI specs fresh from
> Harness and rebuilds `vendor/`. (Needs network + API key; `specs/` is gitignored.)

A typed pass-through CLI for the Harness Code, Pipeline, and Platform APIs.
Command groups are built dynamically at import time by reflecting over the
installed SDKs — there is no code-generation step. A few hand-written
commands (`run`, `logs`, `ng-file-store`) are layered on top.

This directory is a **self-contained, standalone project**: `scripts/vendor.sh`
downloads the OpenAPI specs for the three Harness APIs from Harness itself and
generates the SDKs, and `uv.lock` pins a full dependency graph. It runs
anywhere `uv` + Python 3.11+ are available. The generated SDKs (`vendor/`) and
the fetched specs (`specs/`) are produced locally by `scripts/vendor.sh` — they
are not committed and not shipped.

> **No credentials ship with this project.** The CLI reads credentials only
> from environment variables at runtime and writes nothing to disk. Every
> value in the examples below is a placeholder or a generic project slug.

---

## Table of contents

- [Quick start](#quick-start)
- [Unpackaging the tarball](#unpackaging-the-tarball)
- [Credentials](#credentials)
- [Using the CLI](#using-the-cli)
  - [Discovering commands](#discovering-commands)
  - [Repositories (`repos`)](#repositories-repos)
  - [Pull requests (`pr`)](#pull-requests-pr)
  - [Output formatting (`-f`)](#output-formatting--f)
  - [Running a pipeline (`run`)](#running-a-pipeline-run)
  - [Execution logs (`logs`)](#execution-logs-logs)
  - [File Store (`ng-file-store`)](#file-store-ng-file-store)
  - [Pipeline SDK groups (`pl-*`)](#pipeline-sdk-groups-pl-)
- [Request bodies](#request-bodies)
- [What's vendored](#whats-vendored)
- [Packaging (building the tarball)](#packaging-building-the-tarball)
- [Project layout](#project-layout)
- [Development](#development)

---

## Quick start

```bash
cd portable                # this folder (vendor/ is already generated)
./scripts/vendor.sh        # optional — regenerate SDKs (downloads specs; needs API key in .env + network)
uv sync                    # creates .venv, installs CLI + generated SDKs from uv.lock
uv run harness-cli --help  # works with no credentials — --help never calls the API
```

Don't have `uv`? Install it once:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Unpackaging the tarball

The distributable archive is a small gzipped tarball (`harness-cli.tar.gz`)
containing the CLI source + `scripts/vendor.sh` (no specs, no SDKs — both are
produced locally). Setup is: unpack, add credentials, generate the SDKs.

```bash
# 1. Unpack anywhere
tar -xzf harness-cli.tar.gz
cd harness-cli

# 2. Add credentials FIRST — vendor.sh needs the API key to download the specs
cp .env.example .env        # then edit .env and replace the <...> placeholders

# 3. Generate the SDKs: downloads the specs from Harness + runs openapi-python-client.
#    Needs network + the API key from .env.
./scripts/vendor.sh

# 4. Install + run
uv sync
uv run --env-file .env harness-cli repos get-branch image-build main
```

`vendor/` is generated locally and gitignored; it never ships. `uv sync` reads
`uv.lock` and builds an identical environment every time. To avoid repeating
`uv run`, drop into the environment shell:

```bash
uv run bash          # now `harness-cli ...` works directly
# or activate the venv the classic way:
source .venv/bin/activate
```

## Credentials

The CLI never reads a credential file and never writes one. It resolves four
values from the environment on first use (not on `--help`):

| Value          | Pipeline-injected var     | Local-dev var (takes priority) |
|----------------|---------------------------|-------------------------------|
| Account ID     | `HARNESS_ACCOUNT_ID`      | `POC_HARNESS_ACCOUNT_ID`       |
| API key        | `HARNESS_PASSWORD_API`    | `POC_HARNESS_API_KEY`          |
| Org ID         | `HARNESS_ORG_ID`          | (defaults to `default`)        |
| Project ID     | `HARNESS_PROJECT_ID`      | (no default; set for project-scoped commands) |

Either set works — the local-dev names override the pipeline names. Example:

```bash
# Minimal set for local dev (org defaults to "default"; set HARNESS_PROJECT_ID
# for project-scoped commands like repos/PRs/pipelines)
export POC_HARNESS_ACCOUNT_ID=<your-account-id>
export POC_HARNESS_API_KEY=<your-api-key>

# Equivalent, using the Harness-pipeline names explicitly
export HARNESS_ACCOUNT_ID=<your-account-id>
export HARNESS_ORG_ID=default
export HARNESS_PROJECT_ID=image_flow
export HARNESS_PASSWORD_API=<your-api-key>
```

If either account ID or API key is missing, the CLI prints the required
variable names and exits without making any API call.

**Alternative: a `.env` file.** Instead of exporting vars in every shell, keep
them in a `.env` file and let `uv run` load it with `--env-file`:

```bash
cp .env.example .env        # the template ships with the tarball
# edit .env and replace the <...> placeholders with your real values
uv run --env-file .env harness-cli repos get-branch image-build main
```

`.env` is gitignored and excluded from the tarball — it never leaves your
machine. `.env.example` (placeholder template only) is the sole credential-ish
file that ships; recipients copy it to `.env` and fill in their own keys.

---

## Using the CLI

The examples below use `image-build` as the Harness Code repository
identifier and `image_flow` as the project — substitute your own. Every
command also accepts `--help`.

### Discovering commands

`harness-cli --help` lists every command group. Help works at three levels:

```bash
harness-cli --help              # all groups (repos, pr, logs, run, pl-*, ...)
harness-cli repos --help        # every subcommand under `repos`
harness-cli repos get-branch --help   # args + flags for one command
```

Commands mirror the underlying REST API, so a command's flags are exactly the
endpoint's query/path parameters. The base URL is the public Harness SaaS
gateway (`https://app.harness.io/gateway`).

### Repositories (`repos`)

Source: Harness Code SDK. Backed by the `image-build` repo in these examples.

```bash
# Read branch metadata
harness-cli repos get-branch image-build main

# List tags
harness-cli repos list-tags image-build

# Create a branch (body schema is the Harness Code create-branch request)
harness-cli repos create-branch image-build \
  --body '{"target_branch":"main"}'

# Commit files (body carries the files + commit message)
harness-cli repos commit-files image-build --body @changes.json

# Branch protection rules
harness-cli rules --help
```

### Pull requests (`pr`)

```bash
# List open PRs
harness-cli pr list-pull-req image-build

# Get one PR by number
harness-cli pr get-pull-req image-build 42

# Status checks on a PR
harness-cli pr checks-pull-req image-build 42

# Create a PR (body is the Harness Code create-PR request)
harness-cli pr create-pull-req image-build \
  --body '{"target_branch":"main","source_branch":"dev/add-feature","title":"Add feature"}'
```

### Output formatting (`-f`)

Every command prints pretty JSON by default. Pass `-f` (before the group) for
a [`jq`](https://stedolan.github.io/jq/)-style filter to pull out just what
you need:

```bash
# Just PR numbers and states, one per line
harness-cli -f '.[].number, .[].state' pr list-pull-req image-build

# A single field from a single object
harness-cli -f '.branch.commit.sha' repos get-branch image-build main
```

If the Python `jq` module and the `jq` binary are both unavailable, the CLI
falls back to a simple dot/index filter (`.field`, `.[].field`, `.[0].field`).

### Running a pipeline (`run`)

Hand-written command that triggers a pipeline execution on a branch:

```bash
# Trigger the release pipeline on main
harness-cli run main_release --branch main

# Trigger a dev validation build
harness-cli run dev_build --branch dev/add-feature
```

`main_release` / `dev_build` are example pipeline identifiers — use yours.

### Execution logs (`logs`)

Hand-written commands over the log-service API. The default stage is
`release`; pass `-s validate` for `dev_build` or `-s promote` for `stg_merge`.

```bash
# Most recent execution of a pipeline (lists its steps + statuses)
harness-cli logs latest main_release

# Fetch a specific step's logs from the latest execution
harness-cli logs latest main_release --stage release --step <step_id>

# A known execution ID (lists steps)
harness-cli logs find <execution_id>

# Fetch one step's logs from a known execution
harness-cli logs get <execution_id> <step_id> -p main_release -s release
```

### File Store (`ng-file-store`)

Hand-written commands for the Harness Platform File Store (config files,
mutex locks). The multipart create endpoint is hand-written because the
generated model cannot represent the raw `content` field.

```bash
# List files and folders
harness-cli ng-file-store list

# Get metadata for one file
harness-cli ng-file-store get-file release_lock

# Download raw content to stdout
harness-cli ng-file-store download-file release_lock > release.lock

# Create a file (identifiers use underscores, not dashes)
harness-cli ng-file-store create release_lock \
  --name "Release lock" --type FILE --parent-identifier Root \
  --content "held-by: build-42"

# Create a folder
harness-cli ng-file-store create sprint_config \
  --name "Sprint config" --type FOLDER --parent-identifier Root

# Delete
harness-cli ng-file-store delete-file release_lock
```

`create` exits `1` on `DUPLICATE_FIELD` (e.g. a lock already held) and `2` on
other errors — handy for using the File Store as a mutex.

### Pipeline SDK groups (`pl-*`)

The Pipeline SDK groups are prefixed `pl-` to avoid name collisions with the
Code SDK:

```bash
harness-cli pl-pipeline --help        # Pipeline CRUD
harness-cli pl-execute --help         # Execute / retry / rerun
harness-cli pl-executions --help      # Execution details, graph, list
harness-cli pl-triggers --help        # Triggers
harness-cli pl-input-sets --help      # Input sets
```

These are full pass-throughs — same `--body` / `-f` conventions as above.

---

## Request bodies

Write commands accept a request body via `--body` in three forms:

```bash
--body '{"key":"value"}'        # inline JSON
--body @path/to/body.json       # read from a file
--body -                        # read from stdin (pipe something in)
```

The exact JSON schema for each body is the Harness API's request model —
check the corresponding REST endpoint. Storing bodies in `*.json` files (kept
outside this project) keeps complex payloads readable and versionable.

---

## What's vendored

The three Harness SDK packages are generated from OpenAPI specs and are **not
on PyPI**. Neither the generated code nor the specs are committed —
`scripts/vendor.sh` downloads the specs fresh from Harness each run and
generates the SDKs. Both `vendor/` and `specs/` are gitignored and excluded
from the tarball; the recipient (or developer) produces them locally:

```bash
./scripts/vendor.sh        # download specs from Harness + generate vendor/ (via uvx)
```

The generated dirs and their import packages:

| Generated dir (`vendor/…`)       | Import package                                           |
|----------------------------------|----------------------------------------------------------|
| `harness-code-api-client`        | `api_specification_client`                               |
| `harness-pipeline-api-client`    | `pipeline_service_api_reference_client`                  |
| `harness-platform-api-client`    | `harness_next_gen_software_delivery_platform_api_reference_client` |

The mapping (distribution name → generated path) lives in `[tool.uv.sources]`
in `pyproject.toml`. All three are hard dependencies: `main.py` constructs all
three API clients eagerly on first use, so the Platform SDK is required for
the CLI to function (it is not optional in practice, despite defensive
try/except in the source). After regenerating, run `uv lock` if the generated
versions changed, then `uv sync`.

---

## Packaging (building the tarball)

```bash
./package.sh                  # -> ../harness-cli.tar.gz  (small; specs only, no vendor/)
./package.sh /tmp/out.tar.gz  # custom output path
```

The tarball ships the CLI source, `scripts/`, `pyproject.toml`,
`uv.lock`, `.python-version`, and `.env.example`. It **excludes** `vendor/`
and `specs/` (the recipient fetches specs + regenerates `vendor/` via
`scripts/vendor.sh`) plus all dynamic/generated artifacts:

- `vendor/`, `specs/` — generated/fetched locally by `scripts/vendor.sh`
- `__pycache__/`, `*.pyc` — Python bytecode
- `.venv/`, `venv/` — virtual environments (each user creates their own via `uv sync`)
- `*.egg-info/`, `build/`, `dist/` — build metadata
- `.pytest_cache/`, `.coverage`, `htmlcov/` — test artifacts
- `.ruff_cache/` — linter cache
- `.env` — real credentials (only the `.env.example` template ships)

`uv.lock` **is** shipped — it fully reproduces the environment once `vendor/`
is generated. No credential material of any kind is included.

---

## Project layout

```
harness-cli/
├── pyproject.toml        # project + [tool.uv.sources] → vendor/
├── uv.lock               # pinned full dependency graph (shipped)
├── .python-version       # 3.12
├── .gitignore            # vendor/, .env, dynamic-artifact exclusions
├── package.sh            # tarball builder (excludes vendor/)
├── README.md             # this file
├── harness_cli/          # CLI source (hand-written)
│   ├── main.py           #   entry point + lazy config
│   ├── loader.py         #   reflects over SDKs to build Click commands
│   ├── config.py         #   env-based credential resolution + client factory
│   ├── output.py         #   JSON rendering + jq formatting
│   └── commands/         #   hand-written: run.py, logs.py, ng_file_store.py
├── specs/                # OpenAPI specs (gitignored; fetched from Harness by vendor.sh)
├── scripts/
│   └── vendor.sh         # fetch specs from Harness + generate vendor/ (via openapi-python-client)
├── vendor/               # generated SDKs (gitignored, not shipped; built by vendor.sh)
└── tests/                # CLI test suite (uv sync --extra dev → pytest)
```

---

## Development

```bash
uv sync --extra dev       # adds pytest, pytest-mock
uv run pytest             # run the test suite
```

The SDK command groups are discovered at runtime from `loader.py`; the
hand-written commands live in `harness_cli/commands/`. To rebuild the venv
from scratch at any time: `rm -rf .venv && uv sync`.
