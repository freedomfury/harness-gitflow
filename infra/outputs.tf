output "project_id" {
  description = "Harness project identifier"
  value       = harness_platform_project.image_flow.identifier
}

output "repo_id" {
  description = "Harness repo identifier"
  value       = harness_platform_repo.image_flow.identifier
}

output "repo_git_url" {
  description = "Git clone URL for the image_flow repo"
  value       = harness_platform_repo.image_flow.git_url
}
