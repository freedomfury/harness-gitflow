# Architecture, Rationale, and Implementation Guide

---

## Table of Contents

1. [Overview](#overview)
2. [Why This Exists](#why-this-exists)
3. [Branch Architecture](#branch-architecture)
4. [The VERSION File](#the-version-file)
5. [The Full Flow](#the-full-flow)
6. [Pipeline Behavior by Branch Type](#pipeline-behavior-by-branch-type)
7. [The Merge Conflict Trap](#the-merge-conflict-trap)
8. [Security Gate](#security-gate)
9. [Artifact Lifecycle and Tagging](#artifact-lifecycle-and-tagging)
10. [Nightly Automation and Garbage Collection](#nightly-automation-and-garbage-collection)
11. [ASCII Flow Diagrams](#ascii-flow-diagrams)
12. [Rules Reference](#rules-reference)
13. [FAQ](#faq)

---

## Overview

This document describes the Git branching strategy, pipeline design, and artifact lifecycle management for the golden image build system. The system produces a set of 16 AMIs across 4 seed image families, released on a scheduled two-week sprint cadence with support for hotfixes and nightly patch builds. Although this document uses AWS as its reference implementation, these concepts apply to any cloud or on-prem environment that supports image registration and artifact tagging.

The core principle is simple:

> **Build once. Test progressively. Promote through gates. Never rebuild unless code actually changed.**

---

## Why This Exists

### The Problem We Are Solving

The previous pipeline had the following chronic failure modes:

**Every failure meant starting from scratch.** Whether a flaky integration test, a deploy timeout, or a security scan finding — any failure at any stage restarted the entire pipeline including the most expensive steps. A multi-hour Kickstart and hardening build would be discarded because of a network blip during a test.

**No separation between build events and release events.** The pipeline conflated "did the image build successfully" with "is this image approved to ship." A failed deploy did not mean the image was wrong — it meant the deploy mechanism hiccupped. But the system treated both identically.

**Human compliance was the enforcement mechanism.** The release process relied on developers remembering to create release branches, bump version files, and follow a documented workflow. Operations-oriented developers with different mental models from software development lifecycle concepts could not consistently follow the process without constant reminders.

**A manual "finalized" step caused double builds on urgent releases.** When no code changes had occurred for two weeks, a separate branch had to be created to trigger a rebuild. For urgent releases, this meant running the full pipeline twice — once for the actual change, once for the finalization step.

**Cleanup lived inside the pipeline.** When the pipeline failed, cleanup never ran. Over time, orphaned AMIs accumulated in AWS — potentially petabytes of abandoned artifacts generating storage costs with no operational value.

**Security gates will block releases for problems nobody can fix.** Without separation between compliance checks and vulnerability scanning, a scan that fails on a CVE with no available vendor patch will block a release that is otherwise perfectly safe — and that may contain other security improvements. This is a predictable failure mode of any pipeline that treats vulnerability findings as binary pass/fail gates.

### The Design Principles Behind This Solution

**Idempotency over resumability.** Rather than trying to make the pipeline resume from a specific failed step, every stage checks whether its output already exists for the current inputs by content hash. If the code changed, the hash changes, and the stage re-executes. If the code did not change, the cached result is reused. A pipeline rerun after a code fix rebuilds everything that depends on the changed inputs. A pipeline rerun after a non-code failure (flaky test, network timeout) skips the expensive build and retests the same artifact.

**Artifact immutability.** Once an artifact is built and passes its gate, it is immutable. No downstream failure can invalidate it. A failed deploy retries the deploy against the same artifact. A flaky test retries the test against the same artifact. Only a code change produces a new artifact.

**Technical enforcement over human compliance.** Every process rule that previously relied on a developer remembering to do something is now enforced by Git conflict mechanics or pipeline pre-checks. Developers cannot accidentally violate the process — Git tells them immediately.

**Separation of build, test, and promote.** These are three distinct activities that happen at different cadences and have different failure modes. They should not be chained into a single pipeline where failure in one destroys the work of the others.

**Security as continuous monitoring, not a point-in-time gate.** Vulnerability scanning at deployment time provides false assurance — a CVE can be published two hours after the scan passes. Continuous nightly scanning against production provides real coverage. The security gate at promotion time catches configuration issues and newly available patches; it does not block releases for problems that cannot be fixed.

---

## Branch Architecture

There are four types of branches. Three for the image release flow, one for operational automation.

```
main          Permanent. Production record only.
              Every commit on main is a tagged release or an ops merge.
              Never worked in directly.
              Receives image code from stg-* branches only.
              Receives pipeline/infrastructure code from ops/* branches.
              Nightly automation runs from main.

stg-X.Y.Z     Ephemeral staging branch. One per release cycle.
              Named after the release target version.
              Created automatically when the previous release merges to main.
              If the next stg branch already exists (e.g., during a hotfix),
              creation is skipped with a warning — the operation is idempotent.
              Deleted after merge to main.
              Never builds images — only promotes artifacts from dev branches.
              Runs long integration tests against real cloud instances.

dev/*         Ephemeral feature branches. One per feature/fix.
              Named anything under the dev/ prefix.
              Branched from the current stg-* branch.
              Where all image builds happen.
              Runs short tests only (local QEMU/KVM simulation).
              Deleted after merge to stg-*.

ops/*         Ephemeral operational branches. Two uses:
              1. Pipeline maintenance — branched from main, merged back to main
                 directly. Bypasses stg entirely. No builds, no tests, no
                 versioning. Code-reviewed to prevent image code from slipping
                 through. Pipeline infrastructure changes only.
              2. Nightly automation — created from main on a timer
                 (e.g., ops/gc-2026-04-12). Push triggers operational jobs.
                 Fire and forget — results do not affect main's status.
                 Cleaned up by subsequent runs.
```

### Why This Maps to Dev/Stage/Prod

This is not an exotic branching model. It is standard Dev/Stage/Prod with two improvements: the stage branch carries a version number and is recreated each sprint rather than being permanent, and there is no shared dev integration branch — features meet each other for the first time on the stg branch when they merge.

```
Classic model:     dev (shared) → stage (permanent) → prod
This model:        dev/* (isolated) → stg-X.Y.Z (versioned, ephemeral) → main
```

The versioned stage branch solves the ambiguity problem of a permanent stage branch: at any moment it is completely clear what changes are in scope for the current release, because the branch exists only for that release. A permanent stage branch accumulates changes continuously and it is never obvious what "this release" actually contains.

The isolated dev branches mean features are built and tested independently before integration. Two features that work fine individually may conflict when they both land on stg — the long integration tests on stg are where this is caught.

### Why the Flow Is Unidirectional

Classic Git flow requires backward merges — hotfixes on main merge back into develop, develop merges back into feature branches. This is where human process breaks down. Code flows in the wrong direction and everyone inherits merge conflicts from changes they did not make.

In this model, code only flows toward release: dev → stg → main. A developer's only obligation is staying current with their target stg branch. Hotfixes that land on main between releases are cherry-picked forward into the active stg branch — still toward release, never backward. The VERSION file enforces this mechanically: stale work cannot merge because the version conflict catches it.

### Branch Naming Convention

```
main                        Production record
stg-0.12.0                  Stage branch targeting release 0.12.0
stg-0.12.1                  Stage branch for a hotfix against 0.12.0
dev/fix-boot-failure        Feature branch (name is free-form under dev/)
dev/add-monitoring-agent    Feature branch
dev/johns-experiment        Feature branch — naming is not policed
ops/gc-2026-04-12           Nightly garbage collection run
ops/fix-deploy-timeout      Pipeline maintenance (merges to main directly)
```

---

## The VERSION File

A single file named `VERSION` lives at the root of the repository. It is the single source of truth for release identity.

### Ownership: Server-Side Only

VERSION is owned and written exclusively by the `stg_merge` pipeline. Developers never touch it. There is no bump script, no pre-merge obligation, no version conflict to resolve.

When a dev branch merges to stg, `stg_merge` runs the full test suite, then automatically computes and commits the next VERSION value. Two concurrent merges cannot produce duplicate or conflicting VERSION values because the bump step runs under a File Store mutex — only one pipeline can hold the lock at a time.

This eliminates the race condition from the original dev-owned model, where two developers could bump independently to the same value before either merged.

### Version Numbering Rules

Two rules govern version numbering. No exceptions.

**Minor versions are scheduled sprint releases.** Every sprint release increments the minor version and the patch is always zero: `0.11.0 → 0.12.0 → 0.13.0`. Even a no-change sprint bumps the minor version. This keeps the release cadence predictable and unambiguous.

**Patch versions are unscheduled hotfix releases only.** A non-zero patch version always means an out-of-band release: `0.11.1`, `0.11.2`. If you see a patch version on main, something was fixed in production outside of the normal sprint cycle.

### Pre-release Labels

Two pre-release labels are used. The automation determines which one to apply based on the stg branch name.

**`rc.N` — release candidate.** Used on sprint branches (`stg-X.Y.0`). Indicates in-progress work toward the next scheduled release.

**`hotfix.N` — hotfix candidate.** Used on hotfix branches (`stg-X.Y.Z` where Z > 0). Indicates in-progress work toward an unscheduled patch release.

SemVer sorts these correctly: `hotfix.N < rc.N < solid release`.

### VERSION Value Semantics

The VERSION file uses SemVer with a pre-release suffix for in-progress work. The branch name is the target; the VERSION value tracks the current base.

```
Branch: stg-0.12.0 (target: next scheduled release)

Value               Meaning
─────────────────────────────────────────────────────────────
0.11.0              Base version, stg branch just created from main
0.11.1-rc.0         First feature merged to stg-0.12.0
0.11.1-rc.1         Second feature merged
0.11.1-rc.6         Sixth feature merged, sprint in progress
  ↓ hotfix 0.11.1 ships out of band, cherry-picked into stg
0.11.1              Hotfix landed, base moved forward
0.11.2-rc.0         First feature merged after hotfix, new base
0.11.2-rc.1         Second feature on new base
0.12.0              Sprint closed, target reached
                    No more merges accepted to stg-0.12.0
```

```
Branch: stg-0.11.1 (target: unscheduled hotfix)

Value               Meaning
─────────────────────────────────────────────────────────────
0.11.0              Base version, branch created from main tag 0.11.0
0.11.1-hotfix.0     First hotfix candidate
0.11.1-hotfix.1     Second iteration (if needed)
0.11.1              Hotfix closed, ready for release
                    Merges to main, cherry-picks into stg-0.12.0
```

Pre-release suffixes are entirely internal. They never appear on main. Production consumers only ever see clean SemVer version numbers (`0.11.0`, `0.11.1`, `0.12.0`, etc.).

### Ceiling Rule

The `stg_merge` bump step will not write a VERSION value that exceeds the sprint target. If the stg branch is `stg-0.12.0` and the computed next value would be `0.12.1-rc.0` (which exceeds `0.12.0`), the bump step logs `sprint target reached` and exits cleanly without committing. Subsequent merges to that branch continue to succeed but produce no further bumps — the sprint is at its target and ready to release.

### The File Store Mutex

The bump step acquires a mutex before reading and writing VERSION, to prevent two concurrent `stg_merge` runs from computing the same next value. The mutex uses the Harness Platform File Store:

1. **Acquire**: POST `version_lock` file to the File Store. The API returns HTTP 400 `DUPLICATE_FIELD` if the file already exists, atomically rejecting the second writer.
2. **Retry**: Failed acquisitions retry with exponential backoff (2s, 4s, 8s, 16s, 32s). If the lock is older than 10 minutes (stale — the holder pipeline died), it is force-deleted and acquisition is retried.
3. **Release**: DELETE the lock file on pipeline exit (normal or error), via a `trap EXIT` handler.

Lock payload is `{"exec_id": "...", "ts": <unix-seconds>}` — the exec ID identifies the holding pipeline in Harness UI; the timestamp drives stale detection.

CLI: `harness-cli ng-file-store create/delete-file/download-file`

### Automation

The initial VERSION value on a new stg branch is set by `main_release` → `close_sprint` when a release merges to main. The bump step in `stg_merge` handles all subsequent increments. No human ever writes to VERSION.

The bump logic (`repo/scripts/next-version.py`) determines the correct label from the branch name:

```
stg-X.Y.0 (patch is zero)     → sprint branch  → use rc.N
stg-X.Y.Z (patch is non-zero) → hotfix branch  → use hotfix.N
```

---

## The Full Flow

### Normal Sprint Cycle

```
1. Previous release ships
   main is tagged 0.11.0
   Automation creates stg-0.12.0 from main
   VERSION in stg-0.12.0 set to 0.11.0 (the base)

2. Developer picks up work
   git checkout -b dev/my-feature stg-0.12.0
   Makes changes
   Runs bump script → VERSION set to 0.11.1-rc.0
   Pushes dev/my-feature

3. Pipeline runs on dev/my-feature
   Builds 16 AMIs locally (QEMU/KVM on builder)
   Runs short tests (local simulation)
   Pass → artifacts tagged with content hash and version
   Fail → developer fixes and pushes again

4. Developer opens PR: dev/my-feature → stg-0.12.0
   Pipeline pre-check runs (seconds):
     Is VERSION bumped above current stg? ✓
     Is VERSION within sprint target? ✓
     Is branch current with stg HEAD? ✓
   If any check fails → PR blocked with clear message, no build runs

5. PR approved by reviewer
   Developer merges

6. stg-0.12.0 pipeline runs:
   Does NOT rebuild
   Grabs artifact from dev/my-feature build (by content hash)
   Converts QCOW2 → AMI if not already converted
   Spins up real cloud instances in parallel (~16 instances)
   Runs long integration tests in parallel
   ~45 minutes total
   Pass → artifact tagged stg-passing, VERSION 0.11.1-rc.0
   Fail → stg goes red, developer investigates

7. Repeat for each developer's feature
   Each merge increments VERSION: rc.1, rc.2, ... rc.N

8. Release owner decides sprint is done
   Bumps VERSION from 0.11.1-rc.N to 0.12.0
   Commits VERSION change only
   Pipeline sees VERSION-only change → no rebuild, no retest
   Existing rc.N artifact retagged as 0.12.0
   stg-0.12.0 is now closed — no more merges accepted

   The VERSION value is itself the closed door. Any dev branch
   still carrying a pre-release version will conflict immediately.
   No human has to police the closed sprint. No branch protection
   rule has to be configured. This eliminates the "finalized branch"
   problem from the previous system where a separate branch had to
   be created to signal release readiness, causing a double build.

9. Release owner opens PR: stg-0.12.0 → main
   Security gate pipeline runs (separate from build pipeline):
     CIS compliance validation
     Static vulnerability scan against existing AMIs (parallel)
     Dynamic vulnerability scan against spun-up instances (parallel)
     ~30-45 minutes
   Security team reviews findings
   Security team approves (or requests changes)
   Release owner approves

10. PR merges to main
    main tagged 0.12.0
    Deployment pipeline fires:
      Grabs artifacts tagged 0.12.0
      Deploys to production
      Copies AMIs to production account
      Shares across org
      Tags Git

11. Automation runs post-merge:
    Attempts to create stg-0.13.0 from main
    If stg-0.13.0 already exists (e.g., hotfix was in flight): skips with warning
    Sets VERSION in stg-0.13.0 to 0.12.0
    Next sprint begins
    Cleanup job runs against stg-0.12.0 artifacts
```

### Hotfix Interrupting a Sprint

```
Production running: 0.12.0
Sprint in progress: stg-0.13.0 at 0.12.1-rc.5

Problem: critical bug found in 0.12.0
         stg-0.13.0 has changes not ready to ship
         cannot release stg-0.13.0 to fix this

1. Automation creates stg-0.12.1 from main tag 0.12.0
   VERSION in stg-0.12.1 set to 0.12.0

2. Developer creates dev/hotfix-critical-bug from stg-0.12.1
   Makes fix
   Runs bump script → VERSION set to 0.12.1-hotfix.0
   Pushes
   Short tests run on dev branch

3. PR: dev/hotfix-critical-bug → stg-0.12.1
   Standard pre-checks
   Merges

4. stg-0.12.1 long tests run against real cloud instances
   Same process as normal sprint merge
   ~45 minutes
   Pass → artifact tagged stg-passing

5. VERSION bumped to 0.12.1 (hotfix release close)
   Pipeline retags → no rebuild

6. PR: stg-0.12.1 → main
   Full security gate runs
   Approvals received
   Merges → main tagged 0.12.1
   Hotfix deployed

7. Hotfix cherry-picked into stg-0.13.0
   VERSION in stg-0.13.0 becomes 0.12.1
   SemVer: 0.12.1 > 0.12.1-rc.5 — forces conflict
   All active dev branches must rebase
   Next developer bumps to 0.12.2-rc.0
   Sprint continues toward 0.13.0

8. Automation attempts to create stg-0.13.0
   Already exists → skips with warning
   stg-0.12.1 deleted
```

The hotfix does not interrupt the current sprint's progress. `stg-0.13.0` continues accumulating features while `stg-0.12.1` is prepared in parallel. The process is identical to a normal release — same pipeline, same gates, same flow. The cherry-pick ensures the fix is not accidentally dropped when `0.13.0` ships. The conflict trap forces active developers to rebase, so the hotfix cannot be silently ignored.

---

## Pipeline Behavior by Branch Type

Different branches trigger different pipelines. This is intentional and critical.

### dev/* Branch Pipeline

**Trigger:** Push to any branch matching `dev/*`

**What it does:**

- Runs VERSION pre-check (fast, seconds)
- Builds 16 AMIs using QCOW2 backing file chain on local builder
- Boots images in QEMU/KVM on builder hardware (no cloud cost)
- Runs short test suite (unit, component, smoke tests)
- Runs developer-level compliance checks to prepare for the security gate
- Tags passing artifacts with content hash

**What it does NOT do:**

- Spin up real cloud instances
- Run long integration tests
- Run formal security scans
- Interact with AWS beyond artifact registration

**Duration:** Minutes, not hours. Fast feedback for developer iteration.

**Cost:** Zero cloud spend. All work happens on local builder hardware.

**Failure response:** Developer fixes on their branch and pushes again. No upstream work is affected.

### stg-* Branch Pipeline

**Trigger:** Merge of a dev/* branch into stg-*

**What it does:**

- Retrieves existing artifact from dev branch build (by content hash)
- Converts QCOW2 to AMI format if not already converted
- Spins up real cloud instances in parallel (one per AMI type)
- Runs long integration test suite in parallel
- Terminates instances after tests complete
- Tags passing artifacts as stg-passing

**What it does NOT do:**

- Build any images
- Run short tests again
- Run security scans

**Duration:** ~45 minutes (dominated by long test suite, not spin-up)

**Cost:** Modest cloud spend. Instances live for ~45-60 minutes per merge. Only triggered on merges, not on every dev push.

**Failure response:**

- Flaky test: retry long tests against same artifact (no rebuild)
- Real defect: developer fixes on dev branch, rebuilds there, re-merges

**VERSION-only change behavior:** If only the VERSION file changed (e.g., the release close bump or hotfix cherry-pick):

- Pipeline detects VERSION-only change
- Skips all testing
- Retags existing stg-passing artifact with new version
- Completes in seconds

### stg-* → main PR Pipeline (Security Gate)

**Trigger:** Pull request opened from stg-* to main

This is the single security gate for the entire pipeline. All formal security validation happens here and nowhere else.

**What it does:**

- CIS compliance validation (formal, produces proof for the enterprise)
- Static vulnerability scan against existing registered AMIs (no instances needed)
- Dynamic vulnerability scan against freshly spun-up instances
- All scans run in parallel
- Aggregates findings into PR report
- Requires human security team approval
- Requires release owner approval

**What it does NOT do:**

- Build any images
- Run any functional tests
- Re-run integration tests

**Duration:** ~30-45 minutes for scans plus human review time

**Failure response:**

- CIS compliance failure: fix the hardening script, rebuild on a dev branch, re-merge to stg, re-run long tests, open a new PR. This is a build defect.
- Vulnerability finding with available patch: security team requests fix, developer updates the package on dev branch, re-merges through the pipeline.
- Vulnerability finding with no available patch: security team reviews, documents exception with rationale, PR proceeds.
- Security team judgment is the final gate, not the automation.

### main Branch

**Trigger:** Merge of stg-* into main

**What it does:**

- Tags the commit with the release version
- Triggers deployment pipeline
- Deployment pipeline grabs already-built, already-tested, already-scanned artifacts
- Deploys to production

**What it does NOT do:**

- Build anything
- Test anything
- Scan anything

**Duration:** Deployment time only. No build, no test overhead.

### ops/* Branch Pipeline

**Trigger:** Push to any branch matching `ops/*`

**What it does:**

- Runs operational automation defined in the branch (GC, future nightly jobs)
- Reports results independently — does not affect main's pipeline status
- Nightly ops branches are cleaned up by subsequent runs

**What it does NOT do:**

- Build any images
- Run any tests
- Touch versioning
- Deploy anything

**For pipeline maintenance (ops/* → main merges):**

- Code review required — human gate prevents image code from slipping through
- No pipeline triggers on merge to main — these are infrastructure-only changes
- Changes are picked up by the next stg branch created from main

---

## The Merge Conflict Trap

The VERSION file is the primary mechanism for preventing stale merges. It works at two levels.

### Level 1: Git Conflict (Automatic)

When two developers both bump VERSION to the same value, whoever merges second gets a standard Git conflict. No configuration required — this is how Git works.

```
stg at: 0.12.1-rc.3

dude-1 branch: bumped VERSION to 0.12.1-rc.4
dude-2 branch: also bumped VERSION to 0.12.1-rc.4

dude-1 merges first → stg now at 0.12.1-rc.4

dude-2 tries to merge:
  Git conflict on VERSION — both sides say rc.4
  PR blocked automatically
  dude-2 rebases, bumps to rc.5, pushes
  VERSION-only change → retag, seconds, no rebuild
```

This also handles the sprint close and hotfix scenarios:

```
Sprint close:
  stg VERSION bumped to 0.12.0
  Any dev branch still at rc.N → Git conflict
  Sprint is closed, enforced mechanically

Hotfix lands:
  Hotfix cherry-picked, stg VERSION becomes 0.12.1
  Any dev branch at 0.12.1-rc.N → Git conflict
  0.12.1 > 0.12.1-rc.anything (SemVer rule)
  Developers must rebase and bump to 0.12.2-rc.0
```

### Level 2: Pipeline Pre-Check (Catches What Git Misses)

Git only conflicts when two different values collide. If a developer forgets to bump entirely, their branch and stg both have the same value — Git sees no conflict. The pipeline pre-check catches this and several other cases.

The pre-check runs before any build work, completes in seconds, and validates:

- **VERSION was bumped.** If the developer's VERSION matches stg current, the check fails with a message showing the expected value.
- **VERSION is above stg current.** If the developer's VERSION is behind stg (e.g., they branched early and others merged ahead of them), the check fails and instructs them to rebase.
- **VERSION is below the sprint target.** If the developer's VERSION exceeds the target release, the check fails. You cannot overshoot the release you are working toward.
- **Pre-release label is correct.** Sprint branches (`stg-X.Y.0`) require `rc.N`. Hotfix branches (`stg-X.Y.Z` where Z > 0) require `hotfix.N`. Wrong label, check fails.

Every failure produces a clear, actionable error message showing what the developer has, what stg has, and what the expected value is. The bump script calculates this automatically — in practice, a developer who gets a pre-check failure just runs the bump script and pushes again.

### VERSION-Only Changes Never Trigger Builds

This rule is non-negotiable for developer adoption. When the only changed file is VERSION:

- Pipeline detects no code changes via content hash comparison
- Skips all build and test stages
- Retags the existing artifact with the new version
- Completes in seconds

A developer who had to rebase and bump their VERSION is not penalized with a full pipeline run just to update a single file. The existing artifact from their previous build is simply retagged.

Without this rule, developers will find workarounds to avoid the version bump requirement. With it, the cost of compliance is nearly zero.

---

## Security Gate

### Philosophy

The security gate lives at the stg→main PR. This is the single point where formal security validation occurs. It is structured as a PR review process — security concerns are raised, discussed, and resolved the same way code review concerns are. The PR links to the artifacts under review, scan results are attached, and the security team approves or requests changes just like any other reviewer.

### Two Concerns, Different Dispositions

**CIS Compliance — hard fail, non-negotiable.** The organization has agreed on a specific security posture — CIS benchmarks, hardening standards, configuration baselines. Either the image meets that posture or it does not. A CIS failure means the hardening script is wrong and must be fixed before release. There is no exception process for misconfiguration.

**Vulnerability Findings — soft fail, negotiated through the PR.** Vulnerabilities are an ever-changing landscape. Blocking a release for a CVE that nobody can fix leaves production more vulnerable, not less. Vulnerability findings are reviewed by the security team in the PR, and exceptions can be negotiated through the same review process as any code concern.

### Why Heavyweight Security Lives at the PR Gate

Dynamic vulnerability scanning and full CIS compliance validation require spinning up real instances and running extensive checks. This is too expensive to run on every dev push or every stg merge. The PR from stg to main happens once per release cycle, making it the appropriate place for these expensive scans.

Developer-level compliance checks run earlier in the pipeline as a development aid, but they are not the formal gate. The PR gate produces the official record.

### Deliverables

Each release passing through the security gate produces:

- Formal CIS compliance report
- Static and dynamic vulnerability scan results
- SBOM (Software Bill of Materials) — a complete package manifest for every image in the release
- Security team approval on record in the PR

The SBOM ensures that consumers of the image know exactly what packages are installed. It travels with the release as a permanent artifact.

---

## Artifact Lifecycle and Tagging

### The Problem This Solves

The pipeline builds 16 AMIs across 4 seed families. Multiple pipeline stages need to coordinate — dev builds, stg tests, deployment promotes — without rebuilding. Cleanup needs to know what is safe to delete. Rollback needs to know what constitutes a complete release. And if an image ever gets separated from its tags or registry, someone needs to be able to identify it.

### Three Tiers of Identity

Identity is stored at three levels. Each level serves a different operational need.

**Tier 1: AMI Tags (minimal, for pipeline coordination and cleanup)**

Three tags on every AMI for pipeline operations, plus a few for correlation without requiring SSH. Tags are only applied when the build succeeds — an image without tags is an incomplete build.

```
Tag              Example              Purpose
──────────────────────────────────────────────────────────
version          0.11.1-rc.3          Lookup key — stg finds dev artifacts by this
component        web-server           Which of the 16 AMIs this is
git-sha          a3f4c2d              Correlate back to the commit
build-date       2026-04-10           When this artifact was built
execution-id     exec-4522            Which pipeline run produced this
```

The version tag is rewritten as the artifact promotes. When the release close bumps VERSION to `0.12.0`, all 16 artifacts are retagged `version=0.12.0`. Deployment grabs everything matching that version. No hash lookups, no manifest queries — just a tag filter.

**Tier 2: In-Image Metadata (permanent, survives tag loss)**

A JSON file baked into every image at build time (e.g., `/etc/image-metadata.json`). Contains only the information specific to this image.

```json
{
  "component": "web-server",
  "version": "0.12.0",
  "seed": "seed-a",
  "git-sha": "a3f4c2d",
  "build-date": "2026-04-10",
  "execution-id": "exec-4522",
  "stg-branch": "stg-0.12.0"
}
```

If the AMI tags get stripped, if the cloud account is disconnected from the registry, if someone is troubleshooting a live instance at 3 AM — they can SSH in, read this file, and know exactly what they are looking at. This is the image's birth certificate.

The version field in the in-image metadata is set at build time and is NOT rewritten during promotion — it records the version the image was actually built as. The AMI tag is the current version; the in-image metadata is the original version.

**Tier 3: Release Manifest (aggregate, authoritative record)**

A manifest file is generated for each release and stored externally. It aggregates all 16 images into a single document. This is the same concept as Packer's manifest output.

```json
{
  "release": "0.12.0",
  "git-sha": "a3f4c2d",
  "build-date": "2026-04-10",
  "execution-id": "exec-4522",
  "sbom": "s3://pipeline-artifacts/sbom/0.12.0.json",
  "images": {
    "web-server":   { "seed": "seed-a", "ami-id": "ami-0001" },
    "app-server":   { "seed": "seed-a", "ami-id": "ami-0002" },
    "db-proxy":     { "seed": "seed-a", "ami-id": "ami-0003" },
    "bastion":      { "seed": "seed-a", "ami-id": "ami-0004" },
    "monitoring":   { "seed": "seed-b", "ami-id": "ami-0005" }
  }
}
```

The manifest is the complete truth about a release. It links to the SBOM, records every AMI ID, and provides the data needed for rollback and audit.

### Status Lifecycle

Every artifact carries a status tag that acts as a safety mechanism — an artifact cannot be promoted to a stage it is not ready for. Deployment will not grab an artifact that is not tagged appropriately.

```
Status Value        Meaning                             Cleanup Rule
──────────────────────────────────────────────────────────────────────
building            Pipeline is working on it            Don't touch
failed              Build or test failed                 Delete after 72 hours
tested              Passed its stage, eligible           Managed by release lifecycle
deployed            Live in production                   Don't touch
rollback            Previous production release          Keep for rollback window
```

Detailed image lifecycle management — sharing across accounts, customer delivery, image recall, cross-cloud distribution — is out of scope for this document and should be addressed in a separate operational guide.

### Rollback

Rollback is a pointer update. The deployment reads a manifest pointer to determine which AMI IDs to deploy. Rolling back means pointing at the previous release's manifest. No rebuild, no retest — the previous 16 AMIs are still registered. The deployment grabs them and promotes them back to production.

---

## Nightly Automation and Garbage Collection

### Why Cleanup Must Be Independent

The previous system had cleanup inside the build pipeline. When the pipeline failed, cleanup never ran. Over time, orphaned AMIs accumulated. Cleanup and build are orthogonal concerns that must run independently.

### How It Runs

A scheduled job triggers nightly from main. The job creates an `ops/gc-YYYY-MM-DD` branch from main, which triggers the operational pipeline. This ensures GC always runs the latest code from main. Results are reported independently — a GC failure does not affect main's pipeline status. Each run cleans up the previous night's ops/gc branch.

```
Nightly trigger (cron):
  Creates ops/gc-2026-04-12 from main
  Push triggers ops/* pipeline automatically
  GC runs, reports results
  Fire and forget — main doesn't know or care

Next night:
  Creates ops/gc-2026-04-13 from main
  GC runs, deletes ops/gc-2026-04-12
  Self-cleaning
```

### Retention Rules

**Never delete:**

- Any AMI tagged `status=deployed` — current production
- Any AMI tagged `status=rollback` — previous production, needed for rollback
- Any AMI tagged `status=building` — pipeline is actively working

**Delete:**

- Any AMI tagged `status=failed` older than 72 hours — troubleshooting window has passed
- Any AMI tagged `status=building` older than N hours — pipeline died, these are orphaned
- Any AMI tagged `status=tested` with a pre-release version whose stg branch no longer exists — release shipped, these are leftover candidates
- Any AMI with no recognized status tag older than N days — orphaned, flag for review or delete

### Properties

- Idempotent — safe to run multiple times with no side effects
- Dry-run capable — shows what would be deleted before deleting
- Logged — every deletion recorded with the reason

### Stretch Goal: Full Nightly Pipeline Exercise

Once garbage collection is running reliably, the nightly automation can be expanded to simulate a full developer cycle:

- GC runs first (Phase 1 — implement now)
- Automated build exercises the full dev→stg pipeline (Phase 2 — stretch goal)
- Full security suite runs since no one is waiting (Phase 2)
- Morning report delivered: build health, security posture, patches applied

The intent is to exercise the pipeline nightly so that failures are discovered in a low-stakes overnight context rather than during a high-stakes release. Over time, fixing nightly failures forces the pipeline to become genuinely reliable.

This is significant automation to build — it requires a bot that creates synthetic dev branches, triggers builds, opens PRs, and merges to stg. It should not be attempted until the core pipeline is stable and GC is running cleanly.

---

## ASCII Flow Diagrams

### Diagram 1: Branch Architecture

```
                         ┌─────────────────────────────────────────┐
                         │                  main                    │
                         │  (permanent, production record)          │
                         │                                          │
                         │  ...──● 0.11.0 ──● 0.12.0 ──● 0.13.0── │
                         └────────────────────────────────┬─────────┘
                                                          │
                                    ┌─────────────────────┘
                                    │ auto-created from main tag
                                    ▼
                    ┌───────────────────────────────────┐
                    │          stg-0.13.0               │
                    │  (ephemeral, one per sprint)      │
                    │                                   │
                    │  VERSION: 0.12.0  (base)          │
                    │       ↓ (dev/feat-1 merges)       │
                    │  VERSION: 0.12.1-rc.0             │
                    │       ↓ (dev/feat-2 merges)       │
                    │  VERSION: 0.12.1-rc.1             │
                    │       ↓ (release close)           │
                    │  VERSION: 0.13.0  ← CLOSED        │
                    └────────────┬──────────────────────┘
                                 │ PR + security gate
                                 ▼
                         ┌───────────────┐
                         │     main      │
                         │  ● 0.13.0     │
                         └───────────────┘

         ┌───────────────────────────────────────────────────┐
         │                 dev/* branches                    │
         │              (ephemeral, per feature)             │
         │                                                   │
         │  dev/feat-1  ──────────────────────────┐         │
         │   VERSION: 0.12.1-rc.0                 │ merge   │
         │   Build + short tests                  ▼         │
         │                                                   │
         │  dev/feat-2  ──────────────────────────┐         │
         │   VERSION: 0.12.1-rc.1                 │ merge   │
         │                                        ▼         │
         └───────────────────────────────────────────────────┘

         ┌───────────────────────────────────────────────────┐
         │                 ops/* branches                    │
         │           (operational automation)                │
         │                                                   │
         │  ops/gc-2026-04-12  ── GC run (nightly)          │
         │  ops/fix-deploy     ── pipeline maintenance      │
         │                        (merges to main directly) │
         └───────────────────────────────────────────────────┘
```

---

### Diagram 2: Pipeline Behavior by Stage

```
  dev/* PUSH              stg MERGE             stg→main PR           main MERGE
  ──────────              ─────────             ───────────           ──────────

  VERSION pre-check       Grab artifact         CIS compliance        Tag commit
  (seconds)               from dev by           validation
                          version tag                                 Deploy pipeline
  Build 16 AMIs                                 Static vuln scan      fires
  (QCOW2, local)         Convert QCOW2→AMI     (parallel)
                          if needed                                   Grab manifest
  Short tests                                   Dynamic vuln scan     AMI IDs
  (local QEMU/KVM)       Spin up 16 real        (parallel)
                          instances                                   Deploy to prod
  Developer-level                               Security team
  compliance checks       Long tests ~45 min    review (PR)           Share across org
                          (parallel)
  Tag artifact                                  Release owner         Tag git commit
  (tested)                Tag artifact           approve
                          (tested)
                                                Merge to main

  If VERSION-only:        If VERSION-only:
  skip all above          skip all above
  retag, seconds          retag, seconds
```

---

### Diagram 3: VERSION File Merge Conflict Trap

```
  stg-0.13.0 state:
  VERSION = 0.12.1-rc.3
       │
       ├─────────────────────────────────────────┐
       │                                         │
       ▼                                         ▼
  dev/feat-1                                dev/feat-2
  bumps to rc.4                             bumps to rc.4
  builds ✓                                  builds ✓
  tests pass ✓                              tests pass ✓
       │                                         │
       │ merges first                            │ tries to merge
       ▼                                         ▼
  stg VERSION = rc.4                    ┌────────────────────┐
                                        │  GIT CONFLICT      │
                                        │                    │
                                        │  stg says: rc.4   │
                                        │  you say:  rc.4   │
                                        │                    │
                                        │  Rebase and        │
                                        │  bump to rc.5      │
                                        └────────────────────┘
                                                 │
                                                 │ rebases, bumps to rc.5
                                                 │ VERSION-only change → retag
                                                 ▼
                                        stg VERSION = rc.5
                                        Merge accepted ✓
```

---

### Diagram 4: Release Close

```
  Sprint nearing end:
  stg-0.13.0
  VERSION = 0.12.1-rc.N
  All features merged, all tests green
       │
       │ Release owner decides: we are done
       ▼
  Bump VERSION: 0.12.1-rc.N → 0.13.0
  Commit: "close release 0.13.0"
       │
       ▼
  Pipeline detects: VERSION-only change
  Action: retag rc.N artifacts as 0.13.0
  Duration: seconds
       │
       │ Sprint is now CLOSED
       ▼
  Any dev branch tries to merge:
  ┌─────────────────────────────────┐
  │  GIT CONFLICT                   │
  │                                 │
  │  stg says:  0.13.0              │
  │  you say:   0.12.1-rc.something │
  │                                 │
  │  Sprint is closed.              │
  │  Wait for stg-0.14.0            │
  └─────────────────────────────────┘
       │
       │ Release owner opens PR: stg-0.13.0 → main
       ▼
  Security gate runs
  Human review + approvals
       │
       ▼
  Merge to main
  main tagged 0.13.0
  Deploy pipeline fires
  Automation creates stg-0.14.0
  VERSION in stg-0.14.0 = 0.13.0
  Next sprint begins
```

---

### Diagram 5: Hotfix Flow

```
  main tagged: 0.12.0 (production)
  stg-0.13.0: VERSION = 0.12.1-rc.5 (sprint in progress)
       │
       │ Critical bug found in production
       ▼
  ┌─────────────────────────────────────────────────┐
  │                                                 │
  │  stg-0.12.1  ←── created from main tag 0.12.0  │
  │  VERSION = 0.12.0                               │
  │                                                 │
  │  dev/hotfix-critical-bug                        │
  │    bumps to 0.12.1-hotfix.0                     │
  │    fixes bug                                    │
  │    builds + short tests ✓                       │
  │    merges to stg-0.12.1                         │
  │                                                 │
  │  stg-0.12.1 long tests run ✓                    │
  │                                                 │
  │  VERSION bumped to 0.12.1 (release close)       │
  │  artifact retagged, seconds                     │
  │                                                 │
  │  PR stg-0.12.1 → main                           │
  │  Security gate runs                             │
  │  Merge → main tagged 0.12.1                     │
  │  Hotfix deployed                                │
  │                                                 │
  └─────────────────────────────────────────────────┘
       │
       │ Cherry-pick into stg-0.13.0
       │ VERSION becomes 0.12.1
       │ 0.12.1 > 0.12.1-rc.5 — forces conflict
       │ Next developer bumps to 0.12.2-rc.0
       ▼
  stg-0.13.0 continues toward 0.13.0
  Fix included, nothing lost
```

---

### Diagram 6: Artifact Flow (Build Once, Promote Through Gates)

```
  dev/feat-1 build
  ┌─────────────────────────────────────────────────────────────────┐
  │  QEMU/KVM on local builder                                      │
  │  16 AMIs built                                                  │
  │  Short tests ✓                                                  │
  │  Artifact: ami-0001..ami-0016, tagged tested, 0.12.1-rc.0      │
  └────────────────────────────┬────────────────────────────────────┘
                               │ same artifact, never rebuilt
                               ▼
  stg-0.13.0 merge
  ┌─────────────────────────────────────────────────────────────────┐
  │  Convert QCOW2 → AMI (once)                                     │
  │  Spin up 16 real instances in parallel                          │
  │  Long integration tests ~45 min                                 │
  │  Artifact: same ami-0001..ami-0016, now tagged tested           │
  └────────────────────────────┬────────────────────────────────────┘
                               │ same artifact, never rebuilt
                               ▼
  Release close
  ┌─────────────────────────────────────────────────────────────────┐
  │  VERSION bump only → retag                                      │
  │  Artifact: same ami-0001..ami-0016, tagged 0.13.0               │
  └────────────────────────────┬────────────────────────────────────┘
                               │ same artifact, never rebuilt
                               ▼
  stg → main PR security gate
  ┌─────────────────────────────────────────────────────────────────┐
  │  CIS compliance validation                                      │
  │  Static + dynamic vulnerability scans                           │
  │  Human security review + approvals                              │
  │  Artifact: same ami-0001..ami-0016, tagged deployed             │
  └────────────────────────────┬────────────────────────────────────┘
                               │ same artifact, deployed
                               ▼
  Production
  ┌─────────────────────────────────────────────────────────────────┐
  │  ami-0001..ami-0016 running in production                       │
  │  Built ONCE on dev branch                                       │
  │  Never rebuilt through entire lifecycle                         │
  │  Tested progressively at each gate                              │
  │  Monitored continuously post-deployment                         │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Rules Reference

### Branch Rules

| Rule | Enforcement |
|---|---|
| main receives image code only from stg-* | Branch protection rule |
| main receives pipeline code from ops/* | Code review (human gate) |
| stg-* only receives merges from dev/* | Branch protection rule |
| dev/* can only merge to their parent stg-* | Branch protection rule |
| ops/* merges directly to main (no stg) | Code review (human gate) |
| No direct pushes to main | Branch protection rule |
| No direct pushes to stg-* (except automated VERSION bumps) | Branch protection rule |
| Pipeline must pass before merge to stg-* | Branch protection rule |

### VERSION File Rules

| Rule | Enforcement |
|---|---|
| Must be bumped before merging to stg-* | Pipeline pre-check |
| Must be above stg current value | Pipeline pre-check |
| Must be below sprint target version | Pipeline pre-check |
| Pre-release label must match branch type (rc for sprint, hotfix for hotfix) | Pipeline pre-check |
| Duplicate values cause merge conflict | Git automatic |
| VERSION-only change never triggers rebuild | Pipeline trigger logic |
| Sprint close: bump to release target (drop pre-release suffix) | Bump script |
| Post-sprint close: no more merges accepted | Git conflict automatic |

### Version Numbering Rules

| Rule | Meaning |
|---|---|
| Minor version increments are scheduled sprint releases | 0.12.0 → 0.13.0 → 0.14.0 |
| Patch versions are unscheduled hotfix releases only | 0.12.1, 0.12.2 |
| rc.N suffix for sprint branch work | 0.12.1-rc.0, rc.1, rc.2 |
| hotfix.N suffix for hotfix branch work | 0.12.1-hotfix.0, hotfix.1 |
| Solid version (no suffix) means release closed or production | 0.13.0 on main |
| Pre-release suffixes never appear on main | Internal only |

### Pipeline Rules

| Situation | Pipeline Behavior |
|---|---|
| dev/* push, code changed | Full build + short tests |
| dev/* push, VERSION only | Retag existing artifact, seconds |
| stg merge, code changed | Grab artifact, long tests only, no rebuild |
| stg merge, VERSION only | Retag existing artifact, seconds |
| stg→main PR | Security gate only: CIS + vuln scans + human review |
| main merge | Tag + deploy only, no build, no test |
| ops/* push | Operational automation (GC, etc.), no image builds |

---

## FAQ

**Q: What happens if a developer forgets to bump VERSION?**

The pipeline pre-check catches it within seconds and displays a clear message showing the expected version. No build runs. The developer runs the bump script, pushes, and the pipeline proceeds. If only the VERSION file changed, the build is skipped entirely and the existing artifact is retagged.

**Q: What if two developers both bump to the same rc version?**

Whoever merges second gets a Git conflict on the VERSION file. The developer rebases, runs the bump script to get the next available value, and pushes. Their pipeline reruns but the VERSION-only change logic means it completes in seconds.

**Q: Can someone merge after the sprint is closed?**

No. Once VERSION is bumped to the release target (e.g., `0.13.0`), any branch still carrying a pre-release version will conflict immediately. Git blocks it without any pipeline involvement.

**Q: What happens if a hotfix ships while my sprint is in progress?**

The hotfix merges to main independently, then gets cherry-picked into your active stg branch. The VERSION in stg advances to the hotfix's solid version (e.g., `0.12.1`), which is higher than your `0.12.1-rc.N`. You get a Git conflict, rebase, run the bump script (which gives you `0.12.2-rc.0`), and continue. Your work is not invalidated — just rebased onto the new base.

**Q: Why does the hotfix use a `hotfix.N` label instead of `rc.N`?**

Two reasons. First, SemVer sorts `hotfix` below `rc` alphabetically, so the version ordering is correct at every step. Second, it prevents artifact tag collisions — a sprint and a hotfix branch can both be working in the same patch version space, but `0.12.1-rc.0` and `0.12.1-hotfix.0` are different strings. No ambiguity in artifact lookups.

**Q: What happens if stg long tests fail?**

If the failure is a flaky test, retry against the same artifact — no rebuild. If there is a real defect, the developer fixes on their dev branch, rebuilds there, and re-merges to stg. Nothing upstream is invalidated.

**Q: What happens if the deploy fails?**

Rerun the deployment pipeline. It reads the release manifest, finds the same 16 AMI IDs, and deploys them again. Nothing is rebuilt, nothing is retested.

**Q: How do we roll back?**

Update the manifest pointer to the previous release. The deployment pipeline reads that manifest, grabs the previous AMI IDs, and deploys them. No rebuild. No pipeline run beyond the deployment step.

**Q: What if a security scan fails at the PR gate?**

For CIS compliance failures: fix the hardening script, rebuild on a dev branch, re-merge to stg, re-run long tests, open a new PR.

For vulnerability findings: the security team reviews the finding in the PR and either approves with a documented exception or requests a fix. This works like any code review — concerns are raised and resolved in the PR.

**Q: What does a developer actually have to do differently?**

Very little. The only new requirement is running the bump script before merging to stg. The script calculates the correct version automatically. Everything else either stays the same or becomes easier because failed downstream stages no longer invalidate their work.

**Q: How long does a full release cycle take?**

```
Assuming a clean run with no failures:

dev/* build and short tests:   15-30 minutes (per push)
stg long tests:                ~45 minutes (per merge to stg)
Security gate:                 30-45 min scans + human review time
Deployment:                    depends on infrastructure

Total calendar time:           ~2 hours from "ready to release"
                               to "in production"
                               not including human review/approval time
```

**Q: What are ops/* branches for?**

Pipeline maintenance and operational automation. Pipeline infrastructure changes that can't follow the image release process merge to main directly through ops/* with code review. Nightly automation (garbage collection, future nightly builds) runs by creating timestamped ops/* branches from main on a scheduled trigger.

**Q: Why not just use containers?**

Some workloads require VM-level isolation for compliance, regulatory, or technical reasons. This design provides reliable image management for VM-based workloads. If the organization moves to containers, the branching and versioning model still applies — only the build artifacts change.

---

_Document reflects intended target state, not current implementation._
