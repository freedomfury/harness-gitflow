resource "harness_platform_repo" "image_flow" {
  identifier     = "image-build"
  org_id         = var.org_id
  project_id     = harness_platform_project.image_flow.identifier
  default_branch = "main"
  description    = "Multi-branch release workflow for golden image builds"
}

resource "harness_platform_repo_rule_branch" "main_protection" {
  identifier      = "protect_main"
  repo_identifier = harness_platform_repo.image_flow.identifier
  org_id          = var.org_id
  project_id      = harness_platform_project.image_flow.identifier
  state           = "active"

  pattern {
    default_branch = true
  }

  bypass {
    repo_owners = true
  }

  policies {
    require_pull_request           = true
    require_minimum_approval_count = 1
    block_branch_deletion          = true
    require_latest_commit_approval = false
    require_resolve_all_comments   = false
    require_no_change_request      = false
    require_status_checks          = ["stg_merge-promote"]
  }
}
