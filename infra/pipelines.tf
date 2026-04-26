resource "harness_platform_pipeline" "dev_build" {
  identifier = "dev_build"
  name       = "dev build"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  yaml       = file("${path.module}/../pipelines/dev-build.yaml")
}

resource "harness_platform_triggers" "dev_build_push" {
  identifier = "dev_build_push"
  name       = "dev push"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  target_id  = harness_platform_pipeline.dev_build.identifier
  yaml = templatefile("${path.module}/triggers/dev-build-push.tpl.yml", {
    org_id     = var.org_id
    project_id = var.project_id
  })
}

resource "harness_platform_triggers" "dev_build_branch_create" {
  identifier = "dev_build_branch_create"
  name       = "dev branch create"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  target_id  = harness_platform_pipeline.dev_build.identifier
  yaml = templatefile("${path.module}/triggers/dev-build-branch-create.tpl.yml", {
    org_id     = var.org_id
    project_id = var.project_id
  })
}

resource "harness_platform_triggers" "dev_build_pr" {
  identifier = "dev_build_pr"
  name       = "dev PR"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  target_id  = harness_platform_pipeline.dev_build.identifier
  yaml = templatefile("${path.module}/triggers/dev-build-pr.tpl.yml", {
    org_id     = var.org_id
    project_id = var.project_id
  })
}

# ---------------------------------------------------------------------------
# stg merge pipeline — runs on push to stg-* (i.e., after dev/* PR merges)
# ---------------------------------------------------------------------------

resource "harness_platform_pipeline" "stg_merge" {
  identifier = "stg_merge"
  name       = "stg merge"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  yaml       = file("${path.module}/../pipelines/stg-merge.yaml")
}

resource "harness_platform_triggers" "stg_merge_push" {
  identifier = "stg_merge_push"
  name       = "stg push"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  target_id  = harness_platform_pipeline.stg_merge.identifier
  yaml = templatefile("${path.module}/triggers/stg-merge-push.tpl.yml", {
    org_id     = var.org_id
    project_id = var.project_id
  })
}

# ---------------------------------------------------------------------------
# main release pipeline — runs on push to main (i.e., after stg-* PR merges)
# ---------------------------------------------------------------------------

resource "harness_platform_pipeline" "main_release" {
  identifier = "main_release"
  name       = "main release"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  yaml       = file("${path.module}/../pipelines/main-release.yaml")
}

resource "harness_platform_triggers" "main_release_push" {
  identifier = "main_release_push"
  name       = "main push"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  target_id  = harness_platform_pipeline.main_release.identifier
  yaml = templatefile("${path.module}/triggers/main-release-push.tpl.yml", {
    org_id     = var.org_id
    project_id = var.project_id
  })
}

# ---------------------------------------------------------------------------
# ops build pipeline — runs on push to ops/* (infrastructure-only changes)
# ---------------------------------------------------------------------------

resource "harness_platform_pipeline" "ops_build" {
  identifier = "ops_build"
  name       = "ops build"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  yaml       = file("${path.module}/../pipelines/ops-build.yaml")
}

resource "harness_platform_triggers" "ops_build_push" {
  identifier = "ops_build_push"
  name       = "ops push"
  org_id     = var.org_id
  project_id = harness_platform_project.image_flow.identifier
  target_id  = harness_platform_pipeline.ops_build.identifier
  yaml = templatefile("${path.module}/triggers/ops-build-push.tpl.yml", {
    org_id     = var.org_id
    project_id = var.project_id
  })
}
