# The Full Picture — What We Have and What We're Missing

Last updated: 2026-04-16 (post-full-flow sprints 0.3.0–0.10.0 confirmed).

---

## Triggers Configured in Terraform

| Trigger | Event type | Branch filter | Fires pipeline |
|---------|-----------|--------------|---------------|
| `dev_build_push` | Push | `dev/*` | `dev_build` |
| `dev_build_branch_create` | Branch Create | `dev/*` | `dev_build` |
| `dev_build_pr` | Pull Request (Create/Reopen/Update) | `dev/*` source | `dev_build` |
| `stg_merge_push` | Push | `stg-*` | `stg_merge` |
| `main_release_push` | Push | `main` | `main_release` |
| `ops_build_push` | Push | `ops/*` | `ops_build` |

**Note:** every `terraform apply -replace=harness_platform_pipeline.*` disconnects that pipeline's triggers — they must be `-replace`'d alongside the pipeline or re-applied separately.

---

## Branch Rules

| Branch | Rule name | Requires | Blocks deletion |
|--------|-----------|---------|----------------|
| `main` | `protect_main` | PR + 1 approval + `stg_merge-promote` status check | Yes |
| `stg-*` | `protect_stg_X_Y_Z` (created by `main_release` CLI) | PR + 1 approval + `dev_build-validate` status check | No |

Both rules have `bypass: repo_owners = true`.

---

## Pipeline Status

### `dev_build` — fully working ✓

Pipeline variables (with defaults for push builds):
- `pr_event` — `"push"` by default; PR trigger sets to `"pull_request"`
- `pr_target_branch` — `""` by default; PR trigger sets to `<+trigger.targetBranch>`

Steps:
1. `branch_check` — validates branch namespace (`dev/*`, `stg-*`, `main`, `ops/*`)
2. `flow_check` — reads `$EVENT`; skips on push; validates PR target on PR events: `dev/*` → `stg-*`, `stg-*` → `main`, `ops/*` → `main`
3. `version_precheck` — reads `$EVENT`; skips on push; fetches stg branch VERSION via `harness-cli repos get-raw`, enforces `dev > stg AND dev <= target` using `scripts/version-check.py`
4. `mock_build` — content hash excluding VERSION, MinIO cache check, 2s mock build on miss
5. `mock_short_tests` — 2s mock test suite
6. `tag_artifact` — tags artifact URL with VERSION + content hash
7. `publish_artifact` — publishes to Harness Artifacts tab

Status check `dev_build-validate` is set on every commit.

### `stg_merge` — fully working ✓

Steps:
1. `version_change_check` — detects VERSION-only commits using `git diff --name-only "$BEFORE" HEAD` (where `$BEFORE` = `$DRONE_COMMIT_BEFORE`); on branch creation events (`DRONE_COMMIT_BEFORE = 0000...0000`), skips the entire run
2. `mock_long_tests` — reads `build.env`, skips if VERSION-only, otherwise 2s mock integration suite, pushes artifact to `staging/<branch>/artifact.stub` in MinIO

Status check `stg_merge-promote` is set on every stg-* push.

### `main_release` — fully working ✓

Steps:
1. `read_version` — reads VERSION, guards against pre-release, computes NEXT_VERSION and NEXT_STG
2. `tag_release_artifact` — promotes artifact from `staging/stg-X.Y.Z/` to `releases/X.Y.Z/` in MinIO (stub fallback if staging artifact missing)
3. `close_sprint` — creates next stg-* branch, sets VERSION, creates `protect_stg_X_Y_Z` branch rule

### `ops_build` — deployed ✓

Steps:
1. `branch_check` — validates branch is `ops/*`
2. `code_check` — fetches main, diffs against HEAD, rejects changes to image code paths (`VERSION`, `scripts/`)

Status check `ops_build-ops` is set on every ops/* push.

**Note:** `require_status_checks` uses AND semantics (all listed checks must pass). Since `ops/*` branches will never have `stg_merge-promote`, ops/* merges to main require repo-owner bypass (`bypass_rules: true`). This is by design — the repo owner acts as the human gate.

---

## Event-by-Event: What Happens

### Push to `dev/*` (or branch create)
- `dev_build` fires; all steps run
- Content hash excludes VERSION — VERSION-only pushes hit build cache
- `dev_build-validate` status check set on commit

### Open / Update PR from `dev/*` to `stg-*`
- `dev_build` fires again (PR trigger)
- `flow_check` runs and validates target branch
- `version_precheck` enforces VERSION ordering vs stg-* branch
- `dev_build-validate` status check updated on PR head

### Merge PR `dev/*` → `stg-*`
- `stg_merge` fires on the push to stg-*
- VERSION-only merge skips long tests
- Artifact promoted to `staging/<stg-branch>/artifact.stub`
- `stg_merge-promote` status check set

### Open PR from `stg-*` to `main`
- No pipeline fires; status checks already set from prior merges

### Merge PR `stg-*` → `main`
- `main_release` fires
- Artifact promoted from `staging/` to `releases/`
- Next stg-* branch + branch protection rule created automatically

### Push to `ops/*`
- `ops_build` fires
- `branch_check` validates ops/* namespace
- `code_check` validates no image code in diff
- `ops_build-ops` status check set on commit

### Open PR from `ops/*` to `main`
- No pipeline fires; status check already set from push
- Merge blocked by `protect_main` (requires `stg_merge-promote` which ops/* never has)
- Repo owner merges with `bypass_rules: true` — human reviews diff, confirms no image code

---

## CLI Tooling

The `harness-cli` provides typed access to Harness Code (141 endpoints) and Pipeline (86 endpoints) APIs. Auto-generated from OpenAPI specs with two custom commands (`run`, `logs`).

### Global `--format` flag

All commands support `--format` / `-f` for jq-style output filtering:

```bash
# Extract specific fields
harness-cli --format '.[].identifier' rules repo-rule-list image-build
harness-cli -f '.[].name, .[].sha' repos list-branches image-build --limit 5

# Works with all command groups
harness-cli -f '.[].number' pr list-pull-req image-build --limit 3
harness-cli -f '.[].planExecutionId' pl-executions list-executions --pipeline-id dev_build --size 5
```

**Implementation:**
- Uses `jq.py` Python library (bindings for jq 1.7.1) — no external `jq` binary required, no subprocess overhead
- Full jq syntax supported via `jq.compile()` and `.input()/.text()`
- Falls back to simple dot-notation extractor if `jq.py` fails
- Must come **before** the subcommand: `harness-cli -f '...' repos list-branches`

**See `docs/cli.md` for full CLI reference.**

---

## Open Gaps

### ~~Gap 1~~ — `ops/*` merge path (resolved 2026-04-15)

`ops_build` pipeline is deployed and working. `require_status_checks` confirmed AND semantics — ops/* merges to main use repo-owner bypass by design. No code change needed; the human gate is the intended control.

---

### Gap 2 — PR creation is manual

After `dev_build` passes, the developer manually opens the PR to stg-*. After `stg_merge` passes, manually opens PR to main. The CLI supports this but it's not automated.

This is the `imageflow` Python workflow layer — not started.

---

## What's Working End to End (confirmed sprints 0.3.0–0.10.0)

- Push to `dev/*` → build + MinIO cache → status check set
- PR to `stg-*` → `dev_build` reruns with `flow_check` + `version_precheck`
- Merge to `stg-*` → `stg_merge` → artifact in `staging/` MinIO
- Merge to `main` → `main_release` → artifact in `releases/` MinIO → next sprint branch + rule created
- VERSION-only commits: `dev_build` hits cache (no rebuild), `stg_merge` skips long tests
- Branch creation guard: `stg_merge` skips when `DRONE_COMMIT_BEFORE = 0000...0000`
- Pre-release VERSION guard: `main_release` blocks if VERSION contains `-`
- MinIO artifact lifecycle: `dev/` → `staging/` → `releases/`
- `ops/*` push → `ops_build` validates + reports status check → repo-owner bypass to merge to main
