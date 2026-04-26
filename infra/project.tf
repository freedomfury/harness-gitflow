resource "harness_platform_project" "image_flow" {
  identifier  = var.project_id
  name        = "Image Flow"
  org_id      = var.org_id
  description = "Multi-branch release workflow for golden image builds"
}
