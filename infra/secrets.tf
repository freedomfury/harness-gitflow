resource "harness_platform_secret_text" "code_api_key" {
  identifier  = "code_api_key"
  name        = "Code API Key"
  org_id      = var.org_id
  project_id  = harness_platform_project.image_flow.identifier
  description = "API key with Harness Code permissions for pipeline steps"

  secret_manager_identifier = "harnessSecretManager"
  value_type                = "Inline"
  value                     = var.code_api_key
}

resource "harness_platform_secret_text" "minio_url" {
  identifier  = "minio_url"
  name        = "MinIO URL"
  org_id      = var.org_id
  project_id  = harness_platform_project.image_flow.identifier
  description = "MinIO endpoint URL"

  secret_manager_identifier = "harnessSecretManager"
  value_type                = "Inline"
  value                     = var.minio_url
}

resource "harness_platform_secret_text" "minio_user" {
  identifier  = "minio_user"
  name        = "MinIO User"
  org_id      = var.org_id
  project_id  = harness_platform_project.image_flow.identifier
  description = "MinIO access key"

  secret_manager_identifier = "harnessSecretManager"
  value_type                = "Inline"
  value                     = var.minio_user
}

resource "harness_platform_secret_text" "minio_pass" {
  identifier  = "minio_pass"
  name        = "MinIO Password"
  org_id      = var.org_id
  project_id  = harness_platform_project.image_flow.identifier
  description = "MinIO secret key"

  secret_manager_identifier = "harnessSecretManager"
  value_type                = "Inline"
  value                     = var.minio_pass
}
