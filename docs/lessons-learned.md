# Harness POC — Lessons Learned

Session 1 parked on **2026-04-12**. Session 2 parked on **2026-04-14**. This file captures hard-won lessons from fighting Harness webhooks, trigger nesting, pipeline behavior, and the SDK/CLI toolchain. Session 1 covers initial scaffolding; see the bottom for session 2+ additions.

---

## TL;DR

Scaffolding is complete. Auto-triggers work end-to-end from `dev/*` push through `stg_merge` via real webhooks. The only remaining failure is the `main_release` pipeline's `create_next_stg` step — it tries to `apt-get install curl` and hit the Harness Code API from inside a stripped-down Ubuntu container, and that path is a debugging sinkhole.

**The next move is NOT to patch more bash into pipeline YAML. The next move is to build a Python/invoke CLI tool** (`imageflow`) that wraps the Harness APIs with typed functions, ship it inside the `image-build` repo under `tool/`, and replace every raw curl in the pipelines with `invoke <task>` calls.

---

## Current State of the System

### Harness resources (live, managed by Terraform)

| Resource | Identifier | Notes |
|---|---|---|
| Project | `image_flow` | |
| Repo (Harness Code) | `image-build` | Default branch `main` |
| Branch rule | `protect_main` | Requires `stg_merge-promote` check, PR + 1 approval, blocks deletion |
| Pipeline | `dev_build` | Inline, runs on dev/* branches, stage `validate` |
| Pipeline | `stg_merge` | Inline, runs on stg-* pushes, stage `promote` |
| Pipeline | `main_release` | Inline, runs on main pushes, stage `release` (**broken**) |
| Trigger | `dev_build_push` | Push event to `dev/*` — **works via webhook** |
| Trigger | `dev_build_branch_create` | Branch Create event to `dev/*` — **works via webhook** |
| Trigger | `stg_merge_push` | Push event to `stg-*` — **works via webhook** |
| Trigger | `main_release_push` | Push event to `main` — enabled but upstream step fails |

### Harness resources (out-of-band, created via API)

| Resource | Notes |
|---|---|
| `protect_stg_0_1_0` branch rule | Requires `dev_build-validate` check. Not in Terraform — created via Harness Code API. |

### Repo state (in `repo/` clone of `image-build`)

- `main`: has README.md, VERSION = `0.0.1-rc.1`, notes.txt, plus the original VERSION seed
- `stg-0.1.0`: merged to main via PR #3, still exists on origin (source branch not deleted on merge)
- `dev/branch-create-test`: test probe from the trigger debugging session, still exists
- No `.harness/` directory — pipelines are inline, not git-backed

### Local state (in this POC root)

- `infra/` — Terraform, fully applied. **Freeze this. Don't touch it unless adding new permanent scaffolding.**
- `pipelines/` — Source of truth for the three pipeline YAMLs. Terraform reads them via `file(...)`.
- `endpoints.md` — Validated API endpoint reference. Every endpoint here has been tested with curl at least once.
- `repo/` — Local git clone of the `image-build` Harness Code repo.
- `exports` — Creds (POC_HARNESS_ACCOUNT_ID, POC_HARNESS_API_KEY). `source` it before any API work.
- `harness-code-openapi.yaml` — Full Harness Code OpenAPI spec. Grep this when in doubt about Harness Code endpoints; it's the authoritative source.

---

## What Works End-to-End

1. Developer creates `dev/foo` branch locally, commits, pushes → `dev_build_branch_create` trigger fires (webhook) → `dev_build` pipeline runs on `dev/foo`.
2. Developer pushes more commits to `dev/foo` → `dev_build_push` trigger fires (webhook) → `dev_build` runs again.
3. PR opened `dev/foo` → `stg-0.1.0`. Status check `dev_build-validate` from the latest push is attached to the PR.
4. PR merge (via API or UI with `bypass_rules: true` since we have no second reviewer) → push event lands on `stg-0.1.0` → `stg_merge_push` trigger fires (webhook) → `stg_merge` pipeline runs.
5. PR opened `stg-0.1.0` → `main`. Status check `stg_merge-promote` attached.
6. PR merge to main → push event lands on main → `main_release_push` trigger fires (webhook) → `main_release` pipeline runs → **fails at `create_next_stg` step** (see below).

Steps 1–5 are clean. Step 6 is where we stopped.

---

## What's Broken

`main_release.yaml` has four steps that do real API work (`create_next_stg`, `set_version_next_stg`, `create_stg_rule`, plus `read_version` / `tag_release_artifact` that don't). Every API-calling step:

1. Runs `apt-get install -y -qq curl` at the top because `ubuntu:resolute` has no curl.
2. Builds a curl command inline with shell variable interpolation and JSON body escaping.
3. Parses the response with `grep`/`cut` or `python3 -c`.
4. Has no log visibility when it breaks — the Harness log-service API returned "operation not permitted" when we tried to fetch step logs.

Last observed failure: `create_next_stg` exited with status 1 after curl install succeeded. We never saw which line failed because fetching step logs required more API fighting.

**Do not try to fix this with more bash.** The fix is in the CLI tool plan below.

---

## Lessons Learned

These are the things we rediscovered the hard way. Don't rediscover them again.

### Harness Platform (pipelines / triggers)

1. **Free Tier does not support `store_type = "REMOTE"` for NEW pipeline creation via Terraform.** The provider sends `pipeline_yaml: ""` to the platform API, which responds with "No content to map" or NullPointerException. The existing `dev_build` pipeline "works" as REMOTE in Terraform state only because it was created earlier; the platform actually stores it inline (`git_details: null` in the v1 API response). Use `yaml = file(...)` and omit `git_details` for new pipelines. See `feedback_harness_remote_pipelines.md` in memory.

2. **Harness Code webhook trigger YAML needs four levels of `spec`/`type` nesting.** The Terraform provider accepts flatter structures without error but those triggers never register webhooks and never fire. Correct shape:
   ```yaml
   source:
     type: Webhook
     spec:
       type: Harness
       spec:
         type: Push          # or Branch
         spec:
           repoName: image-build
           payloadConditions: [...]
           actions: []         # required; empty for Push, [Create] for Branch
   ```
   Ground truth: create a throwaway trigger in the UI, view YAML, copy the structure.

3. **For Push events the payload condition key is `targetBranch`, not `sourceBranch`.** `sourceBranch` is for PullRequest events. This is the second thing that makes a trigger silently never fire.

4. **Push triggers do NOT fire on the initial push that creates a branch on origin.** The first `git push origin new-branch` is a Branch/Create event. You need a second trigger (`type: Branch`, `actions: [Create]`) to catch it. Dev/stg branches both need this; main does not.

5. **Status check identifiers are `{pipelineId}-{stageId}`**, not the pipeline identifier alone. `dev_build` pipeline with stage `validate` reports as `dev_build-validate`. Branch rules with `require_uids: ["dev_build"]` do not match anything.

6. **The `main` branch rule shouldn't require `dev_build-validate`** because `dev_build` only runs on dev branches, not on stg branches. The gate for main is `stg_merge-promote`. We fixed this mid-session.

7. **Pipeline execute API wants raw YAML as the body, `Content-Type: application/yaml`.** Not JSON with an `inputYaml` field. We burned a pipeline run discovering this.

8. **Pipeline execution API paths have three generations** that aren't interchangeable:
   - `/gateway/ng/api/pipeline/executions` — returns 404
   - `/gateway/pipeline/api/pipelines/execution/summary` — works, POST with `{"filterType": "PipelineExecution"}` body
   - `/gateway/v1/orgs/{org}/projects/{proj}/pipelines` — wants `pipeline_yaml` as a string field, errors if empty
   Always double-check the path against `endpoints.md`.

9. **Execute summary POST body must include `filterType: "PipelineExecution"`** or the API 400s with "missing type id property 'filterType'".

10. **Every pipeline run in this project so far is `triggerType: MANUAL` except the last batch** — the webhook plumbing was broken until we fixed the trigger YAML. If you're debugging whether a trigger fired, check `executionTriggerInfo.triggerType` on the execution, not just whether a new run appeared.

11. **Trigger event history is reachable at** `/gateway/pipeline/api/triggers/{id}/eventHistory?targetIdentifier={pipelineId}&...`. This is how you verify "did the webhook reach the trigger" independent of "did a pipeline run start."

### Harness Code (the git service)

12. **The Harness Code OpenAPI spec is fetchable directly** at `https://app.harness.io/gateway/code/openapi.yaml` with `x-api-key`. Grep it when in doubt. This was the single biggest productivity unlock of the session.

13. **Field names in the branch protection rule API are not intuitive:**
    - `require_minimum_count` (not `required_count`)
    - `require_uids` (not `require_identifiers` — though responses include both)
    - `delete_forbidden: true` / `update_forbidden: true` to block branch deletion (not `delete: true`)
    - `pattern.default: true` for the default branch (not `default_branch: true`)

14. **File content API (`/contents/{path}`) redirects (307)** to a CDN URL for the actual content. Use `/raw/{path}?ref={branch}` to get raw content in one call, or follow the 307 with `-L`.

15. **PR merge API requires `source_sha` in the request body** in addition to the PR number in the URL. "Source SHA must be provided" is the error when you forget.

16. **Bypass flag is `bypass_rules: true` + `bypass_message: "..."`** at merge time. This is how to merge without a second approver in a solo POC.

17. **Merging a PR via the API DOES generate a push webhook event** on the target branch. We briefly thought it didn't, but that was actually just the broken trigger YAML from lesson 2.

### Terraform provider (`harness/harness`)

18. **The Terraform provider lies about remote pipelines.** It happily accepts `git_details` with `store_type = "REMOTE"`, stores it in state, and reports no drift — but the platform doesn't actually use it. Don't rely on Terraform state matching Harness state for pipeline storage type.

19. **`harness_platform_triggers` with `type: Harness` webhook** is the correct type for Harness Code repos. Don't try `Custom` or other SCM providers.

20. **`bypass { repo_owners = true }` is required on branch rules.** Omitting it is a provider-level error, not a runtime one.

### Environment / runtime

21. **`ubuntu:resolute` has no curl, no python3, no jq.** Every step that needs them has to `apt-get install`. This alone adds 10–20 seconds to every step and makes bash scripts fragile. It's the main reason we're pivoting to a CLI tool in a proper image.

22. **`HARNESS_PASSWORD_API` is injected into pipeline step env** and is the service account API key. It has permissions to do Harness Code API calls from inside a pipeline. Don't hardcode tokens.

23. **`$DRONE_OUTPUT` is the env-var file** pipeline steps use to pass values to downstream steps. `echo "KEY=value" >> "$DRONE_OUTPUT"`. Downstream steps can read with `grep KEY "$DRONE_OUTPUT" | cut -d= -f2`.

24. **`$DRONE_SOURCE_BRANCH`, `$DRONE_TARGET_BRANCH`, `$DRONE_BUILD_EVENT`, `$DRONE_COMMIT_SHA`** are the git context env vars. They're injected by Harness CI and work reliably. Use these instead of Harness expressions in bash.

---

## Where We Failed (Don't Repeat)

This section is explicit about the wrong turns so they don't happen again.

1. **Spent real time trying to make git-backed (REMOTE) pipelines work.** Multiple terraform apply cycles, multiple API payloads, multiple NullPointerExceptions. Free Tier does not support this for new pipelines. Go inline from the start.

2. **Hand-wrote trigger YAML with the wrong nesting.** Created, applied, tested, saw zero events, assumed the webhook system was broken, spent ages looking at webhook registration and trying to find an OpenAPI spec for the pipeline service. The actual fix was mechanical: make a UI trigger, copy its YAML shape. We should have done that in the first 10 minutes.

3. **Used `sourceBranch` as the payload condition key for Push events.** Semantically misleading; Harness uses `targetBranch` for the branch a push landed on. We mixed this up with PR semantics.

4. **Used `["dev_build"]` as the branch rule status check requirement.** Harness actually reports `dev_build-validate`. The mismatch meant the branch rule was perpetually pending. We discovered this only when opening PR #1.

5. **Put raw curl calls in pipeline step bash.** This is the single biggest mistake of the session in terms of time cost. Every iteration is: edit YAML → terraform apply → trigger run → wait 30–60s for the container → apt-get → curl → fail → no logs → guess at the cause → edit YAML. **Total wall-clock cost was at least an hour.** The fix is a CLI tool that you iterate on locally in seconds.

6. **Tried to fetch step logs via the log-service API.** Hit "operation not permitted" with the obvious key format, tried variations, gave up and added `set -x` and echo debugging to the step itself. Still haven't resolved how to reach logs from the API cleanly. Next session: check the Harness UI's Network tab when viewing logs to see what call it actually makes.

7. **Retyped the same curl commands over and over.** Create PR, merge PR, poll execution, list executions, list triggers — each one rediscovered the correct shape, auth, body format each time. Should have captured them in a tool the moment we knew they'd be called twice.

8. **Pushed directly to main multiple times to fix pipeline YAML.** Each push would normally fire `main_release_push` and kick off a run we didn't want. We worked around it by disabling the trigger during cleanup, but it cost us the purity of the protected-branch story. A CLI tool running locally avoids this entirely.

9. **Used the wrong trigger event type for the first push to a new branch.** Spent a full cycle convinced Harness just "doesn't fire on branch creation" until the user pointed out that `type: Branch` with `actions: [Create]` is a separate event type. Lesson: when an event "doesn't fire," check the UI's trigger event list for what types exist.

10. **Fetched pipeline OpenAPI spec at multiple URLs that require browser session auth.** `/pipeline/api/openapi.json`, `/ng/api/swagger.json` — all return HTML redirects to the signin page with API keys. The Harness Code spec is special in being directly reachable. Don't assume all Harness services expose OpenAPI via API key.

---

## The Plan For Next Session

**Do not** resume by debugging `main_release.yaml`. **Do not** apt-get install anything from a pipeline step again.

1. **Build `imageflow` — a Python CLI tool** under `repo/tool/` (committed to the image-build Harness Code repo so pipeline checkouts get it automatically). Use `invoke-layout` as the template. Structure:
   ```
   tool/
     pyproject.toml
     imageflow/
       __init__.py
       __main__.py         # invoke entrypoint
       config.py           # read exports / env, resolve creds + account/org/project
       client.py           # shared HTTP client with retry, auth, error formatting
       tasks/
         code.py           # branches, files, rules, PRs, webhooks (harness CLI layer)
         pipeline.py       # execute, list runs, status, logs (harness CLI layer)
         flow.py           # close_sprint, open_hotfix, gc (imageflow verbs)
   ```

### Two layers, one tool

The tool should expose **two distinct layers** of commands, both backed by the same Python client. The user pointed this out explicitly: we were fighting raw curl against the Harness API all session, and we also need high-level workflow verbs. They are separate responsibilities and should be separate namespaces.

- **Layer 1 — the "Harness CLI" (`invoke code.*`, `invoke pipeline.*`)** is a thin, typed wrapper around one API endpoint per command. This replaces raw curl for interactive work. Examples:
  ```
  invoke code.branch-create   --repo image-build --name stg-0.2.0 --target main
  invoke code.file-put        --repo image-build --branch stg-0.2.0 --path VERSION --content 0.1.0
  invoke code.rule-create     --repo image-build --pattern stg-0.2.0 --require-check stg_merge-promote
  invoke code.pr-create       --repo image-build --source dev/foo --target stg-0.1.0 --title "..."
  invoke code.pr-merge        --repo image-build --number 3 --method merge --bypass
  invoke pipeline.run         --pipeline dev_build --branch dev/foo
  invoke pipeline.status      --exec $EXEC_ID
  invoke pipeline.logs        --exec $EXEC_ID --step create_next_stg
  invoke pipeline.list-runs   --pipeline dev_build --limit 5
  ```
  These are what we reach for when we just need to "hit the Harness API and see what happens" — no curl, no bash escaping, no forgetting the filterType field. Each command is 20 lines of Python with good error messages.

- **Layer 2 — the "imageflow verbs" (`invoke flow.*`)** compose Layer 1 into the workflow operations the design actually cares about. Examples:
  ```
  invoke flow.close-sprint                    # new stg branch + VERSION + rule
  invoke flow.open-hotfix --target 0.1.1
  invoke flow.gc-stale-stg-rules
  invoke flow.sprint-simulate                 # the full test harness from the original plan
  ```
  These are the commands pipelines and humans call when they want to do something meaningful. Layer 2 never reaches `requests.post()` directly — it always goes through Layer 1, which means a Layer 2 test with a mocked client naturally tests the whole composition.

- **Same mocking discipline for both layers.** Layer 1 tests exercise "given these args, expect this HTTP call, feed this mock response, assert the parsed result." Layer 2 tests exercise "given this starting state, expect this sequence of Layer 1 calls, assert the final state." Layer 2 tests don't touch HTTP at all — they mock the Layer 1 functions.

2. **Three layers, with pull-based discipline on the top two.**

   - **Layer 0 — generated Harness Code client (`harness_code_client/`).** One-shot `openapi-python-client generate --path harness-code-openapi.yaml`, commit the output, never hand-edit. Produces typed httpx-based functions for all ~40 Harness Code endpoints with correct field names (the `require_uids` / `targetBranch` / `delete_forbidden` discoveries become dataclass fields automatically). Regenerate only when Harness ships new endpoints. This is **not** speculative building — it's a dependency-like artifact. The unused generated modules are inert until a Layer 1 task imports them.

     Chosen generator: [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client) (v0.28.3, Feb 2026, 102 releases, very active). Produces clean typed Python per tag. Runtime dependency is just `httpx`. Error handling flag `raise_on_unexpected_status` gives us exceptions on non-2xx with decoded body. Git-friendly, commit alongside hand-written code.

   - **Layer 1 — hand-written invoke tasks (`imageflow/tasks/code.py`, `imageflow/tasks/pipeline.py`).** Pull-based. Add one task at a time, only when you reach for curl. Each Layer 1 task is ~10 lines wrapping a Layer 0 function (for Harness Code) or a hand-written httpx call (for pipeline execution, which has no public OpenAPI spec). Every task ships with a mocked-client state-machine test in the same commit.

     Workflow: continue the normal work → the moment you reach for curl, stop → write one Layer 1 task + its test → commit as `tool: add <task-name>` → use the new task to finish the original work → repeat on the next curl temptation.

   - **Layer 2 — flow verbs (`imageflow/tasks/flow.py`).** Pull-based, same discipline. Composes Layer 1 tasks into workflow operations. First verb is `flow.close-sprint` because it's blocking the end-to-end test. Subsequent verbs only get added when they're similarly pulled.

   **Hand-written pipeline endpoints (~8):** execute, execution/summary, execution/v2/{id}, execution/getExecutionGraph/{id}, triggers/{id}/eventHistory, plus anything we discover we need. These live directly in Layer 1 because there's no public OpenAPI spec for the pipeline service (the Harness Platform auth redirects block API-key access to `/pipeline/api/openapi.json`).

   **Reference but don't build on:** [`ljw4010/harness_python_SDK`](https://github.com/ljw4010/harness_python_SDK) — Swagger-Codegen client that doesn't cover Harness Code or pipeline execution. Useful only as a structural reference.

3. **Build Layer 2 verbs in `tasks/flow.py` the same way — pulled, not pushed.** The first Layer 2 verb is `flow.close-sprint`, because that's the one blocking the end-to-end test. We build it only after the three Layer 1 commands it depends on (`code.branch-create`, `code.file-put`, `code.rule-create`) have been added, tested, and committed. `flow.close-sprint` then gets its own commit and its own state-machine test set. After that it goes into `main-release.yaml` and we confirm the end-to-end loop. No other `flow.*` verbs get built until they're similarly pulled by a concrete need.

4. **Replace curl in `main-release.yaml`** with:
   ```yaml
   command: |-
     pip install -e /harness/${CI_REPO_NAME}/tool > /dev/null
     invoke flow.close-sprint
   ```
   Three lines. Pipeline logic moves entirely into Python where we can unit test it.

5. **Manually test `invoke flow.close-sprint` locally first.** No pipeline in the loop. Run, fix, run. Once it works on a laptop, push the tool to the repo, update the pipeline YAML, run it once to confirm the container install + invoke path works.

### Mocking strategy — the real reason this fixes the slow loop

The whole point of moving into Python is that we can iterate **without hitting real Harness at all** for most of the debug cycle. Three layers of test isolation, cheapest first:

- **`--dry-run` on every state-mutating task.** Prints the intended HTTP method, URL, headers (redacted), and body. Exits without calling anything. This becomes the default mode for interactive debugging: `invoke flow.close-sprint --dry-run` shows the full plan in under a second. Ship this before any real execution path.

- **Injectable HTTP client for unit tests.** Tasks must NOT call `requests.post()` directly. They call `client.code.create_branch(name=..., target=...)` on a client object passed in via the task's context or module-level singleton. In tests we replace the client with a stub that returns canned responses or raises canned errors. `unittest.mock.MagicMock` or `pytest-mock` is enough for the POC — no need for `responses` or `vcr.py` unless we actually record real traffic.

- **`invoke.MockContext` for subprocess-heavy tasks.** If a task shells out (`c.run("git push ...")`), invoke ships `MockContext` specifically for this. Pre-program expected commands and return values, run the task in-process, assert the sequence. Docs: https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext

**Minimum viable test setup:**
```
tool/
  tests/
    test_code.py        # one test per Harness Code API wrapper
    test_pipeline.py    # one test per pipeline API wrapper
    test_flow.py        # close_sprint with a mocked client, assert the call sequence
    conftest.py         # shared fixtures: fake client, sample responses
```

**The key discipline:** when a real Harness call fails in weird ways (and it will), the first move is to add a test that reproduces it against the mock client, fix it in the mock-driven loop, then run it for real once. Never loop on real pipeline runs to debug Python logic.

### Test shape — "given / expected call / mock response / continue or fail"

The tests should read like a state machine walkthrough of the flow, not just "did it call requests.post once". For each step in a task:

1. **Given** — the starting state and input parameters
2. **Expected call** — the HTTP method, URL, and body we should have made
3. **Mock response** — the canned API response we feed back
4. **Assertion** — did the task continue to the next step, fail loudly, warn and continue, or skip?

Concrete example for `flow.close_sprint` step 1:

```python
def test_close_sprint_creates_next_branch(fake_client):
    # Given: current release is 0.1.0
    fake_client.version_on_main.return_value = "0.1.0"

    # Mock response: branch create returns 201
    fake_client.code.create_branch.return_value = MockResponse(201, {"name": "stg-0.2.0"})

    close_sprint(fake_client)

    # Expected call
    fake_client.code.create_branch.assert_called_once_with(
        repo="image-build", name="stg-0.2.0", target="main"
    )

def test_close_sprint_tolerates_existing_branch(fake_client):
    # Given: stg-0.2.0 was already created (hotfix in flight)
    fake_client.code.create_branch.return_value = MockResponse(409, {"message": "exists"})

    # Assertion: continues past the create step, does not raise
    close_sprint(fake_client)
    assert fake_client.code.set_file.called  # moved on to step 2

def test_close_sprint_fails_loudly_on_500(fake_client):
    fake_client.code.create_branch.return_value = MockResponse(500, {})
    with pytest.raises(HarnessAPIError):
        close_sprint(fake_client)
```

Each decision point in the task — "201 continues, 409 tolerates, 500 fails" — is one test. The walkthrough **is** the spec. If tomorrow Harness starts returning 422 for a new edge case, we add a test, watch it fail, then decide what `close_sprint` should do about it, then make the test pass. That's how we stop rediscovering the same quirks.

Same shape applies at every level: atomic API wrappers (`test_code.py`), high-level flow verbs (`test_flow.py`), and eventually the sprint simulator from the original plan. The flow tasks compose the atomic ones, so their tests are just assertions about the sequence of calls on the mocked client, not about HTTP specifics.

**What this explicitly replaces:** the debug loop we actually spent today — edit YAML → terraform apply → trigger run → wait 60s → read partial logs → guess → repeat. That loop is ~2 minutes per cycle. The mocked loop is ~2 seconds per cycle. 60x speedup on the step that eats most of the session.

6. **Resume the end-to-end flow test** from where we left off: PR #3 merged stg-0.1.0 → main, main_release is the only piece that hasn't completed cleanly. Once the tool-backed version works, create the next flow (dev/feature-2 → stg-0.2.0 → main) to confirm the whole loop runs on auto-triggers with no hand-holding.

7. **Then consider the Python/invoke test harness from the original plan** (`tasks/sprint.py`, helpers, etc.) — but that's a phase on top of the tool, not a replacement for it.

---

## One-Liners Worth Keeping

```bash
# Source creds at the start of every session
source ./exports  # from project root
export HARNESS_PLATFORM_API_KEY=$POC_HARNESS_API_KEY
export TF_VAR_account_id=$POC_HARNESS_ACCOUNT_ID

# Fetch the Harness Code OpenAPI spec (authoritative reference)
curl -s "https://app.harness.io/gateway/code/openapi.yaml" \
  -H "x-api-key: $POC_HARNESS_API_KEY" > harness-code-openapi.yaml

# List recent executions for a pipeline
curl -s -X POST \
  "https://app.harness.io/gateway/pipeline/api/pipelines/execution/summary?accountIdentifier=${POC_HARNESS_ACCOUNT_ID}&orgIdentifier=default&projectIdentifier=image_flow&pipelineIdentifier=dev_build&page=0&size=5" \
  -H "x-api-key: ${POC_HARNESS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"filterType": "PipelineExecution"}'

# Manually execute a pipeline on a branch (YAML body, not JSON)
curl -s -X POST \
  "https://app.harness.io/gateway/pipeline/api/pipeline/execute/dev_build?accountIdentifier=${POC_HARNESS_ACCOUNT_ID}&orgIdentifier=default&projectIdentifier=image_flow" \
  -H "x-api-key: ${POC_HARNESS_API_KEY}" \
  -H "Content-Type: application/yaml" \
  -d 'pipeline:
  identifier: dev_build
  properties:
    ci:
      codebase:
        build:
          type: branch
          spec:
            branch: dev/my-branch'

# Check trigger event history (did the webhook fire?)
curl -s \
  "https://app.harness.io/gateway/pipeline/api/triggers/dev_build_push/eventHistory?accountIdentifier=${POC_HARNESS_ACCOUNT_ID}&orgIdentifier=default&projectIdentifier=image_flow&targetIdentifier=dev_build" \
  -H "x-api-key: ${POC_HARNESS_API_KEY}"
```

All of these should become `imageflow` subcommands. They're listed here so the first hour of next session doesn't start by rediscovering them.

---

## Parking Brake (Session 1 — now resolved)

Everything below was the session 1 state. All items have since been resolved.

- `main_release` was rewritten using the CLI tool; `close_sprint` and all three steps work.
- Full end-to-end flow (sprints 0.3.0–0.8.0) confirmed.

---

## Session 2+ Lessons

These cover what was learned during the sprint-cycle testing phase (sessions 2+), after the SDK and CLI were built.

### PR gate variables — `DRONE_BUILD_EVENT` is never `pull_request`

25. **Harness CI never sets `DRONE_BUILD_EVENT=pull_request` for PR builds** because the codebase build type in the trigger's `inputYaml` is `type: branch`, not `type: PR`. (Using `type: PR` makes the clone fail with exit 128 because Harness Code doesn't expose `refs/pull/N/head` git refs.) The correct pattern is to pass PR context via **pipeline variables**:
    - Declare `pr_event` (default `"push"`) and `pr_target_branch` (default `""`) as pipeline-level variables with `<+input>.default(...)`.
    - PR trigger's `inputYaml` sets `pr_event: "pull_request"` and `pr_target_branch: <+trigger.targetBranch>`.
    - Steps bind `EVENT: <+pipeline.variables.pr_event>` in `envVariables` and check `$EVENT`.
    - Push builds never set these, so steps see `$EVENT = "push"` and skip PR-only logic.

### `git show --name-only HEAD` is wrong on merge commits

26. **`git show --name-only HEAD` on a merge commit uses combined diff format**, which only shows files that differ from *all* parents simultaneously. For a standard merge commit this is typically empty. `git diff --name-only "$BEFORE" HEAD` is the correct approach — it compares the pre-merge SHA against HEAD and lists every file touched by the incoming branch.

### Version fetch from other branches inside a pipeline

27. **`git fetch origin <branch>` fails inside pipeline containers** — the cloned workspace has no stored git credentials for the Harness Code remote. Use `harness-cli repos get-raw <repo> <path> --git-ref <branch>` with an API key injected via `envVariables`. This is both credential-safe and simpler than configuring git credentials inside a container.

### Terraform trigger state drift after pipeline replacement

28. **After using `curl -X PUT` to update a pipeline YAML directly** (to avoid disconnecting triggers), Terraform state is stale — it holds the old pipeline YAML. A subsequent `terraform apply` without `-replace` will try to reconcile toward the stale state. The pipeline YAML in Harness is correct; the stale state is the problem. Always `-replace` the pipeline *and* all its triggers together when you do touch Terraform. See the "Known Infrastructure Quirks" section in `status.md` for the `curl -X PUT` pattern.

### Harness Code does not support `type: PR` codebase builds

29. **Do not set `build.type: PR` in trigger `inputYaml`** even though the Harness UI suggests it for PR events. Harness Code does not expose `refs/pull/N/head` — the git clone step exits 128 immediately. Use `type: branch` with `branch: <+trigger.sourceBranch>` and pass PR context through pipeline variables (see lesson 25).

### `git stash -u` sweeps untracked directories

30. **`git stash -u` (untracked) will stash and remove the `tool/` directory** because it is not committed to the `image-build` repo. Recovering it requires `git checkout stash@{N}^3 -- tool/`. To avoid losing the built SDK and CLI: either commit `tool/` to the repo or never use `git stash -u` in the image-build clone. The safest recovery path if stashed: `git stash list` to find the entry, then restore the untracked tree from `stash^3`.

## Locking Mechanism Fixes

### Bug A — `close_sprint` writes VERSION without trailing newline (2026-04-14)

31. **`harness-cli repos commit-files` writes the `payload` field exactly as-is, byte-for-byte.** If you pass `"0.9.0"` (5 bytes) the server stores 5 bytes — no trailing newline added. Every other edit to VERSION (dev branches, bump scripts, CLI tools) writes the file with a trailing newline because editors and `echo` both add one. Result: git sees the stg-side commit and the dev-side commit as modifying the same line to different byte sequences ("0.9.0" vs "0.9.0\n") and flags a content conflict on the first merge to the fresh stg branch. Observed as `Merge blocked by conflicting files: [VERSION]` even when the values are logically identical.

**Fix**: change the payload in `pipelines/main-release.yaml` line 121 from `"$RELEASE_VERSION"` to `"$RELEASE_VERSION\n"`. The literal `\n` in the JSON string becomes a real newline when the API parses the body. Deploy via `make replace-main-release`.

**Always include trailing `\n` in any `commit-files` payload for text files.** The API does not auto-append it. If you're writing a file that humans or other tools will edit later, a missing newline creates a phantom diff against every future commit.

### Locking primitive research (2026-04-14)

32. **The Harness CI pipeline has no native serialization/locking primitive.** Before committing to File Store as the Item 7 mutex, we evaluated six options:

| Option | Verdict |
|---|---|
| Pipeline-level concurrency=1 | Serializes the whole pipeline, including long tests. User rejected — we want parallel tests, serialized bumps only. |
| `.VERSION.lock` file committed to stg via `commit-files` | Works mechanically but pollutes git history with lock/unlock commits, and orphaned locks from killed pipelines need manual cleanup. User rejected the idea of putting lock state in git. |
| Harness CD Queue Step | Documented under `x-platform-cd-features` only. CI docs never mention it. Untested but strong evidence it's CD-only. |
| Git LFS Locking API (`git lfs lock`) | Not implemented in Harness Code. Gitness source at `/app/api/handler/lfs` has only `download.go`, `transfer.go`, `upload.go` — no locks handler. Harness LFS docs only describe storage/transfer features. |
| Harness CI Barriers / Resource Constraints | Do not exist in CI. Harness docs have no "flow control" page for CI pipelines. |
| **Harness Platform File Store POST** | **Works.** Atomic create-or-fail. Verified via `tests/file-store-lock-test.sh` — duplicate POST returns HTTP 400 `DUPLICATE_FIELD`, winner's content preserved, DELETE returns 200, N=[2,5,10] concurrent POSTs each return exactly 1 success / N-1 conflict. |

**Takeaway**: for any future CI-side serialization need, Harness Platform File Store is the working primitive. The pattern is: POST a marker file with a hierarchical path, handle HTTP 400 DUPLICATE_FIELD as "lock held", DELETE to release. `tests/file-store-lock-test.sh` is the regression test.

**File Store identifier quirk**: identifiers must be alphanumeric + underscore + `$`, and cannot start with a number or `$`. Dashes are rejected (first attempt at `identifier=image-build` returned `INVALID_REQUEST`). The `name` field is separate and accepts any display string. So `identifier=image_build` with `name=image-build` is the pattern.

### Item 7 auto-bump deployment (2026-04-14)

33. **Terraform `harness_platform_triggers` silently drops creations after a paired pipeline `-replace`.** During the Item 7 deploy, `terraform apply -replace=pipeline.X -replace=trigger.Y` reported `Creation complete after 5s` for every trigger, exit 0, no errors. But a subsequent `harness-cli pl-triggers get-list-for-target` returned `totalItems: 0` for every affected pipeline, and the next dev_build push fired no webhook. Terraform state held the "created" triggers; the Harness API had nothing. A second `terraform apply` (no args) detected the drift, planned 5 triggers as `will be created`, and this time they actually persisted.

**Fix**: after any pipeline `-replace`, always run a plain `terraform apply` immediately after to reconcile drift. Don't trust the replace's own output — verify triggers exist via `harness-cli pl-triggers get-list-for-target --target-identifier <pipeline>` before assuming webhooks will fire. **Webhook events pushed to a pipeline during the drift window are lost**, so also plan to push an empty retrigger commit (`git commit --allow-empty`) after re-applying.

34. **Container image rebuild is part of the deploy, not a separate concern.** The stg_merge bump_version step calls `harness-cli ng-file-store create/delete-file/download-file`. These CLI subcommands existed in the source tree but had never been baked into `freedomfury/imageflow:latest` on Docker Hub — the registry image was from 2026-04-13, before `ng_file_store.py` was written. Pipeline execution would have failed with `No such command 'ng-file-store'`. The fix is always: `docker build && docker push` the container **before** the terraform apply. Verify with `docker pull freedomfury/imageflow:latest && docker run --rm freedomfury/imageflow:latest harness-cli <subcommand> --help` — if the CLI help output doesn't include the expected command, the image is stale.

35. **The PR-creation trigger fires a second dev_build run.** Creating a PR with `harness-cli pr create-pull-req` fires `dev_build_pr` even if `dev_build_push` already ran against the same commit. The two runs both produce a `dev_build-validate` status check and the later one overwrites the earlier. This is not a bug — it's how the trigger set is designed — but it means the "dev_build already passed, PR is ready" state is transient: opening the PR always restarts the check. Wait for the post-PR run to finish before merging, don't merge based on the pre-PR check.

36. **`harness-cli pr merge-pull-req-op` with `bypass_rules: true` echoes the violation list back in the response, but still merges.** The response body contains the rule violations that were bypassed; the presence of a `violations` array does not mean the merge failed. Always re-fetch the PR (`harness-cli pr get-pull-req image-build N`) to confirm `state: merged` rather than trusting the merge response to tell you.

### Item 3 ops_build verification (2026-04-15)

37. **Harness Code `require_status_checks` uses AND semantics.** When a branch rule lists multiple status checks (e.g. `["stg_merge-promote", "ops_build-ops"]`), all of them must pass before the PR can merge. There is no OR mode. This means you cannot use a single branch rule to accept "either check A or check B." The merge attempt returns `pullreq.status_checks.required_identifiers` listing only the checks that haven't passed yet.

38. **`ops_build` pipeline `code_check` step needs an image with git.** The original pipeline used `ubuntu:resolute` which doesn't have `git` installed. The `git fetch` and `git diff` commands fail with exit code 127. Fixed by switching the `code_check` step image to `freedomfury/imageflow:latest` (AlmaLinux 9-based, has git). The `branch_check` step doesn't need git and can stay on any image.
