variable "org_id" {
  description = "Harness org identifier"
  type        = string
  default     = "default"
}

variable "project_id" {
  description = "Harness project identifier"
  type        = string
  default     = "image_flow"
}

variable "code_api_key" {
  description = "API key with Harness Code permissions (for pipeline steps)"
  type        = string
  sensitive   = true
}

variable "minio_url" {
  description = "MinIO endpoint URL (e.g. http://localhost:9000)"
  type        = string
  sensitive   = true
}

variable "minio_user" {
  description = "MinIO access key"
  type        = string
  sensitive   = true
}

variable "minio_pass" {
  description = "MinIO secret key"
  type        = string
  sensitive   = true
}

