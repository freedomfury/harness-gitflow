# Harness API Reference

Base URL for all calls: `https://app.harness.io/gateway`

Auth header on every request: `x-api-key: <POC_HARNESS_API_KEY>`

Common query params (required on most endpoints):
- `accountIdentifier=<your-account-id>`
- `orgIdentifier=default`
- `projectIdentifier=image_flow`

## Finding endpoint specs

The **Harness Code** OpenAPI spec is fetchable directly — this is the source of truth for all `/code/api/v1/...` endpoints:
```
GET https://app.harness.io/gateway/code/openapi.yaml
```
Returns the full OpenAPI 3.0 spec with every endpoint, its params, request body schemas, and responses. Grep this file first instead of guessing.

---

## Pipeline Executions

### List executions

```
POST /pipeline/api/pipelines/execution/summary
     ?accountIdentifier=...&orgIdentifier=...&projectIdentifier=...
     &pipelineIdentifier=dev_build&page=0&size=10
Content-Type: application/json

{"filterType": "PipelineExecution"}
```

Response: `data.content[]` — each item has:
- `planExecutionId` — the execution ID used everywhere else
- `status` — `Success | Failed | Running | Aborted | Expired`
- `startTs` / `endTs` — epoch milliseconds
- `runSequence` — sequential build number

---

### Get execution status

```
GET /pipeline/api/pipelines/execution/v2/{planExecutionId}
    ?accountIdentifier=...&orgIdentifier=...&projectIdentifier=...
```

Response: `data.pipelineExecutionSummary` with `status`, timestamps, trigger info.

---

### Get step-level execution graph (what failed and why)

```
GET /pipeline/api/pipelines/execution/getExecutionGraph/{planExecutionId}
    ?accountIdentifier=...&orgIdentifier=...&projectIdentifier=...
```

Response: `data.executionGraph.nodeMap` — a map of step UUIDs to step details.
Each node has:
- `name`, `identifier`, `status`
- `failureInfo.message` — the error message when a step fails
- `outcomes.output.outputVariables` — output variables the step exported
- `startTs`, `endTs`

This is the one to call when a run fails to see which step and what the error was.

---

### Execute a pipeline (manual trigger)

The body is **raw YAML** (not JSON), and `Content-Type` must be `application/yaml`.

```
POST /pipeline/api/pipeline/execute/{pipelineIdentifier}
     ?accountIdentifier=...&orgIdentifier=...&projectIdentifier=...
Content-Type: application/yaml

pipeline:
  identifier: dev_build
  properties:
    ci:
      codebase:
        build:
          type: branch
          spec:
            branch: dev/test-flow
```

For a PR build instead of a branch build:
```yaml
pipeline:
  identifier: dev_build
  properties:
    ci:
      codebase:
        build:
          type: PR
          spec:
            number: "42"
```

Response: `data.planExecutionId` — use this to poll status.

---

## Step Logs

Logs are not in the pipeline API. They are in a separate log service.

### Download step logs

First get the log key prefix. It follows this pattern:
```
{accountId}/pipeline/{pipelineId}/{runSequence}-{planExecutionId}/{stageId}/{stepId}
```

Then:
```
POST /log-service/blob/download?accountID=...&prefix=<encoded-prefix>
Content-Type: application/json

{}
```

Response: `data.downloadLink` — a signed URL to the raw log file.

---

## Harness Code (Git) API

Base: `/gateway/code/api/v1/accounts/{acct}/orgs/{org}/projects/{proj}`

### List branch rules
```
GET .../repos/image-build/rules
```

### Create branch rule
```
POST .../repos/image-build/rules
Content-Type: application/json

{
  "identifier": "protect_stg_0_1_0",
  "type": "branch",
  "state": "active",
  "pattern": {"include": ["stg-0.1.0"]},
  "definition": {
    "bypass": {"repo_owners": true},
    "pullreq": {
      "approvals": {"require_minimum_count": 1},
      "comments": {},
      "status_checks": {"require_uids": ["dev_build"]},
      "merge": {},
      "reviewers": {}
    }
  }
}
```

Field names that are NOT obvious:
- `require_minimum_count` (not `required_count`)
- `require_uids` (not `require_identifiers`)
- `delete_forbidden: true` (not `delete: true`) to block branch deletion

### Delete branch rule
```
DELETE .../repos/image-build/rules/{identifier}
```

### Create branch
```
POST .../repos/image-build/branches
Content-Type: application/json

{"name": "stg-0.2.0", "target": "main"}
```

Returns 201 on success, 409 if already exists.

### Read file
```
GET .../repos/image-build/raw/{path}?ref={branch}
```

Returns raw file content (200). The `/contents/{path}` endpoint redirects (307) — use `/raw/` instead.

### List pull requests
```
GET .../repos/image-build/pullreq
    ?state=open|closed|merged (repeatable)
    &source_branch=...&target_branch=...
    &include_checks=true&include_rules=true
```

### Create pull request
```
POST .../repos/image-build/pullreq
Content-Type: application/json

{
  "source_branch": "dev/test-flow",
  "target_branch": "stg-0.1.0",
  "title": "test: initial flow exercise",
  "description": "optional markdown body",
  "is_draft": false
}
```
Returns 201 with the new PR object including `number` (the PR number used in subsequent calls).

### Get pull request
```
GET .../repos/image-build/pullreq/{pullreq_number}
    ?include_checks=true&include_rules=true
```

### Check PR mergeability / status checks
```
GET .../repos/image-build/pullreq/{pullreq_number}/checks
```
Returns the status check results attached to the PR (including `dev_build` outcome).

### Merge pull request
```
POST .../repos/image-build/pullreq/{pullreq_number}/merge
Content-Type: application/json

{
  "method": "merge",
  "delete_source_branch": true,
  "dry_run": false
}
```
`method` is one of: `fast-forward`, `merge`, `rebase`, `squash`. Returns 200 on success, 422 if a rule is violated (response has `TypesMergeViolations`), 409 on conflict.

### Create or update file
```
PUT .../repos/image-build/contents/{path}
Content-Type: application/json

{
  "message": "commit message",
  "content": "<base64 encoded content>",
  "branch": "stg-0.2.0"
}
```

For updates, include `"sha": "<current file sha>"`. Get the sha from:
```
GET .../repos/image-build/contents/{path}?ref={branch}
```
(Follow the redirect — the JSON response includes `"sha"`.)
