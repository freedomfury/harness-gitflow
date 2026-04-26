.ONESHELL:
SHELL := /bin/bash

TF_DIR := infra
EXPORTS := exports

# Common Terraform variable flags
TF_VARS := \
	-var='code_api_key=$$POC_HARNESS_API_KEY' \
	-var='minio_url=$$MINIO_URL' \
	-var='minio_user=$$MINIO_USER' \
	-var='minio_pass=$$MINIO_PASS'

# ---------------------------------------------------------------------------
# Core targets
# ---------------------------------------------------------------------------

.PHONY: init plan apply destroy fmt

init:
	source $(EXPORTS)
	export HARNESS_ACCOUNT_ID="$$POC_HARNESS_ACCOUNT_ID"
	export HARNESS_PLATFORM_API_KEY="$$POC_HARNESS_API_KEY"
	cd $(TF_DIR) && terraform init

plan:
	source $(EXPORTS)
	export HARNESS_ACCOUNT_ID="$$POC_HARNESS_ACCOUNT_ID"
	export HARNESS_PLATFORM_API_KEY="$$POC_HARNESS_API_KEY"
	cd $(TF_DIR) && terraform plan $(TF_VARS)

apply:
	source $(EXPORTS)
	export HARNESS_ACCOUNT_ID="$$POC_HARNESS_ACCOUNT_ID"
	export HARNESS_PLATFORM_API_KEY="$$POC_HARNESS_API_KEY"
	cd $(TF_DIR) && terraform apply $(TF_VARS)

destroy:
	source $(EXPORTS)
	export HARNESS_ACCOUNT_ID="$$POC_HARNESS_ACCOUNT_ID"
	export HARNESS_PLATFORM_API_KEY="$$POC_HARNESS_API_KEY"
	cd $(TF_DIR) && terraform destroy $(TF_VARS)

fmt:
	cd $(TF_DIR) && terraform fmt

# ---------------------------------------------------------------------------
# Per-pipeline replace targets
# Always pair pipeline + all associated triggers in the same -replace invocation.
# Replacing a pipeline without its triggers silently disconnects webhooks.
# ---------------------------------------------------------------------------

.PHONY: replace-dev-build replace-stg-merge replace-main-release replace-ops-build

replace-dev-build:
	source $(EXPORTS)
	export HARNESS_ACCOUNT_ID="$$POC_HARNESS_ACCOUNT_ID"
	export HARNESS_PLATFORM_API_KEY="$$POC_HARNESS_API_KEY"
	cd $(TF_DIR) && terraform apply $(TF_VARS) \
		-replace=harness_platform_pipeline.dev_build \
		-replace=harness_platform_triggers.dev_build_push \
		-replace=harness_platform_triggers.dev_build_branch_create \
		-replace=harness_platform_triggers.dev_build_pr

replace-stg-merge:
	source $(EXPORTS)
	export HARNESS_ACCOUNT_ID="$$POC_HARNESS_ACCOUNT_ID"
	export HARNESS_PLATFORM_API_KEY="$$POC_HARNESS_API_KEY"
	cd $(TF_DIR) && terraform apply $(TF_VARS) \
		-replace=harness_platform_pipeline.stg_merge \
		-replace=harness_platform_triggers.stg_merge_push

replace-main-release:
	source $(EXPORTS)
	export HARNESS_ACCOUNT_ID="$$POC_HARNESS_ACCOUNT_ID"
	export HARNESS_PLATFORM_API_KEY="$$POC_HARNESS_API_KEY"
	cd $(TF_DIR) && terraform apply $(TF_VARS) \
		-replace=harness_platform_pipeline.main_release \
		-replace=harness_platform_triggers.main_release_push

replace-ops-build:
	source $(EXPORTS)
	export HARNESS_ACCOUNT_ID="$$POC_HARNESS_ACCOUNT_ID"
	export HARNESS_PLATFORM_API_KEY="$$POC_HARNESS_API_KEY"
	cd $(TF_DIR) && terraform apply $(TF_VARS) \
		-replace=harness_platform_pipeline.ops_build \
		-replace=harness_platform_triggers.ops_build_push
