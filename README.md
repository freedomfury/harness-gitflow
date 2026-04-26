# harness-poc

A proof-of-concept CI/CD pipeline for golden image builds, running on **Harness Free Tier**. The goal is to prove a multi-branch release flow built on one principle:

> **Build once. Test progressively. Promote through gates. Never rebuild unless code actually changed.**

This repo is also an experiment in division of labor: a human (me) designed the workflow, branch strategy, VERSION file mechanics, and pipeline gates; an AI assistant generated the SDKs, the CLI, the Terraform, and most of the pipeline YAML from that design. The `docs/lessons-learned.md` file is a record of where the AI learned the hard way.

## Status

Flow proven end-to-end across 8 sprints (0.3.0 → 0.10.0). The four pipelines are live, the branch protection rules enforce the gates, the VERSION file is server-owned with a Harness File Store mutex, and `main_release` automatically creates the next sprint branch.

The image build itself is **intentionally mocked** — every "build" and "test" step is a short sleep plus a MinIO artifact stub. The POC is about proving the **flow**, not the build. The mocked steps are simple enough to swap for real Packer/AMI work without touching the orchestration.

Two things remain unfinished and are flagged below.

## The branch flow

```
                                 ┌────────────────────────────────┐
                                 │              main              │
                                 │  permanent, production record  │
                                 │  ●─0.10.0─●─0.11.0─●─0.12.0──  │
                                 └─────┬─────────────────┬────────┘
                                       │                 │
                  auto-created from main│                 │ ops/* merge
                                       ▼                 │ (human gate)
                ┌──────────────────────────────────┐     │
                │           stg-X.Y.Z              │     │
                │   ephemeral, one per sprint      │     │
                │   VERSION owned by stg_merge     │     │
                │   File Store mutex serializes    │     │
                └────────────┬─────────────────────┘     │
                             │ PR + status check          │
                             ▼                            │
                       ┌─────────────┐                    │
                       │     main    │◀───────────────────┘
                       └─────────────┘

       ┌──────────────────────────────┐    ┌──────────────────────────────┐
       │       dev/* branches         │    │       ops/* branches         │
       │   one per feature, build +   │    │   pipeline/infra changes,    │
       │   short tests, merge to stg  │    │   no image code, repo-owner  │
       │                              │    │   bypass to land on main     │
       └──────────────────────────────┘    └──────────────────────────────┘
```

Code flows unidirectionally toward release. The VERSION file (and merge-conflict mechanics on it) prevent stale work from landing on the wrong branch. See [`docs/design.md`](docs/design.md) for the full architecture, six ASCII diagrams, and the FAQ.

## The four pipelines

| Pipeline | Trigger | What it does | Status check |
|----------|---------|--------------|--------------|
| **`dev_build`** | push / PR / branch-create on `dev/*` | Validate branch, content-hash cache, mock build + short tests, tag artifact | `dev_build-validate` |
| **`stg_merge`** | push to `stg-*` (after merge) | Skip if VERSION-only; mock long tests; promote to `staging/`; bump VERSION under File Store mutex | `stg_merge-promote` |
| **`main_release`** | push to `main` (after merge) | Promote to `releases/`; auto-create next `stg-X.Y.Z` branch + protection rule | — |
| **`ops_build`** | push to `ops/*` | Validate no image-code in diff; repo-owner bypass merges to main | `ops_build-ops` |

Defined in [`pipelines/*.yaml`](pipelines), wired up by Terraform in [`infra/`](infra). Event-by-event behavior in [`docs/events.md`](docs/events.md).

## Repo layout

```
harness-poc/
├── README.md                      this file
├── CLAUDE.md                      project guide for AI assistants
├── Makefile                       Terraform plan/apply/destroy + per-pipeline replace targets
├── activate                       source to load venv + credentials
├── exports                        local credentials (gitignored)
│
├── docs/                          design + reference
│   ├── design.md                    the heart — branch strategy, VERSION mechanics, diagrams
│   ├── events.md                    trigger map: what fires when
│   ├── cli.md                       harness-cli reference
│   ├── sdk-generation.md            how to regenerate SDKs and CLI
│   ├── lessons-learned.md           where the AI learned the hard way
│   ├── endpoints.md                 raw API reference (fallback)
│   ├── invoke-project-guide.md      style guide for the future imageflow layer
│   └── architecture.drawio          visual diagram
│
├── pipelines/                     four pipeline YAML definitions
├── infra/                         Terraform: project, repo, pipelines, triggers, branch rules
│   └── triggers/                    extracted trigger templates
│
├── repo/                          mirrored to Harness Code (image-build) — VERSION + scripts
├── tool/                          local control-plane tooling (NOT pushed to Harness Code)
│   ├── Dockerfile                   freedomfury/imageflow runner image
│   ├── harness-cli/                 generated CLI + custom run/logs commands
│   ├── harness-code-api-client/     generated SDK (141 endpoints)
│   └── harness-pipeline-api-client/ generated SDK (86 endpoints)
│
├── examples/                      reference OpenAPI specs + env var list
├── extras/                        delegate install script
└── tests/                         File Store mutex regression test
```

Only `repo/` is mirrored to Harness Code. Everything outside is local control-plane material — Terraform, pipelines, docs, tooling.

## Quickstart

```bash
cd harness-poc
source activate                    # loads venv + credentials from ./exports
harness-cli --help                 # 225 commands, autogenerated

# Terraform
make plan                          # see what would change
make apply                         # provision project, repo, pipelines, triggers, rules
make replace-dev-build             # replace pipeline AND its triggers atomically (see Gotchas)
```

Credentials live in `./exports` (gitignored). Template:

```bash
export POC_HARNESS_ACCOUNT_ID=...
export POC_HARNESS_API_KEY=...
export MINIO_URL=...
export MINIO_USER=...
export MINIO_PASS=...
```

To set up the delegate host, see [`extras/install-delegate.sh`](extras/install-delegate.sh) (requires `HARNESS_ACCOUNT_ID` and `HARNESS_DELEGATE_TOKEN` exported).

Terraform handles the project, repo, four pipelines, six triggers, and `protect_main`. Pipeline updates use the `replace-*` Makefile targets so the pipeline and its triggers go in the same apply — replacing one without the other drops the webhooks.

## What's hand-written vs generated

| Layer | Source | Written by |
|-------|--------|-----------|
| Branch strategy + VERSION mechanics | conversation + [`docs/design.md`](docs/design.md) | human |
| Pipeline YAML | [`pipelines/*.yaml`](pipelines) | AI (from design) |
| Terraform | [`infra/*.tf`](infra) | AI (from design) |
| Custom Docker image | [`tool/Dockerfile`](tool/Dockerfile) | AI |
| Python SDKs (227 endpoints total) | `tool/harness-{code,pipeline}-api-client/` | `openapi-python-client` (generated) |
| CLI (225 commands) | `tool/harness-cli/` | [`tool/harness-cli/generate.py`](tool/harness-cli/generate.py) (generated) |
| CLI custom commands (`run`, `logs`) | `tool/harness-cli/harness_cli/commands/{run,logs}.py` | hand-written, generator-preserved |
| File Store mutex regression test | [`tests/file-store-lock-test.sh`](tests/file-store-lock-test.sh) | AI |

The three-layer tooling split is deliberate:

- **Terraform** owns permanent state (project, repo, pipelines, triggers, branch rules).
- **CLI** is for humans, troubleshooting, and pipeline YAML one-liners.
- **SDK** is for code — the not-yet-built `imageflow` invoke layer will compose multi-step workflows on top of it.

## Notable design points

- **Server-owned VERSION** — only `stg_merge` writes the VERSION file. Concurrent merges serialize through a Harness File Store mutex (`POST` returns `400 DUPLICATE_FIELD` for the loser; loser retries with exponential backoff and force-deletes locks older than 10 minutes). Mechanism validated in [`tests/file-store-lock-test.sh`](tests/file-store-lock-test.sh).
- **Content-hash caching** — VERSION is excluded from the build hash. VERSION-only commits hit the cache and skip the rebuild.
- **Conflict-trap enforcement** — Git itself enforces "stale work can't merge" via VERSION conflicts. No human policing.
- **Trigger templates** — webhook trigger YAMLs live in [`infra/triggers/*.tpl.yml`](infra/triggers) with `templatefile()` interpolation, not inline heredocs.
- **`replace-*` Makefile targets** — replacing a pipeline silently disconnects its triggers in Harness state. The Makefile pairs both in a single `terraform apply` to avoid this. The ordering matters; see the comment in the Makefile and lesson 33 in [`docs/lessons-learned.md`](docs/lessons-learned.md).

## What's next

1. **`imageflow` workflow layer** — Python invoke tasks that automate the currently manual PR-creation steps (`dev/* → stg-*` and `stg-* → main`). The CLI supports it; nothing wires it together. See [`docs/invoke-project-guide.md`](docs/invoke-project-guide.md) for the planned structure.
2. **Real builds** — swap the mocked sleeps in `dev_build` and `stg_merge` for actual Packer/AMI work. Pipeline structure stays.
3. **Nightly automation** — `ops/gc-YYYY-MM-DD` branches on a timer for garbage collection and continuous security scanning.

## Documentation map

| Doc | What's in it |
|-----|--------------|
| [`docs/design.md`](docs/design.md) | Branch strategy, VERSION rules, security gate, artifact lifecycle, ASCII diagrams, FAQ |
| [`docs/events.md`](docs/events.md) | What fires when — trigger-by-trigger event map |
| [`docs/cli.md`](docs/cli.md) | `harness-cli` setup, command groups, output formatting |
| [`docs/sdk-generation.md`](docs/sdk-generation.md) | Regenerating the SDKs and CLI from OpenAPI specs |
| [`docs/lessons-learned.md`](docs/lessons-learned.md) | Hard-won lessons from fighting Harness webhooks, triggers, and the toolchain |
| [`docs/endpoints.md`](docs/endpoints.md) | Raw API reference with curl examples (fallback) |
| [`docs/invoke-project-guide.md`](docs/invoke-project-guide.md) | Python Invoke style guide for the future imageflow layer |
| [`docs/architecture.drawio`](docs/architecture.drawio) | Visual diagram |
| [`CLAUDE.md`](CLAUDE.md) | Project guide for AI assistants working in this repo |
