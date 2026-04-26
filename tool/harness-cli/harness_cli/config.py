"""Credential resolution and client factory for Harness APIs."""

import os
import sys
from dataclasses import dataclass

from api_specification_client import AuthenticatedClient as CodeClient
from pipeline_service_api_reference_client import AuthenticatedClient as PipelineClient

try:
    from harness_next_gen_software_delivery_platform_api_reference_client import AuthenticatedClient as PlatformClient
except ImportError:
    PlatformClient = None


@dataclass
class HarnessConfig:
    account_id: str
    org_id: str
    project_id: str
    api_key: str
    harness_base: str = "https://app.harness.io/gateway"

    @classmethod
    def from_env(cls) -> "HarnessConfig":
        """Resolve credentials from environment variables.

        Pipeline env:  HARNESS_ACCOUNT_ID, HARNESS_ORG_ID, HARNESS_PROJECT_ID, HARNESS_PASSWORD_API
        Local dev env: POC_HARNESS_ACCOUNT_ID, POC_HARNESS_API_KEY (+ defaults)
        """
        # POC vars take priority (explicit override), then fall back to pipeline-injected vars
        account_id = os.environ.get("POC_HARNESS_ACCOUNT_ID") or os.environ.get("HARNESS_ACCOUNT_ID")
        api_key = os.environ.get("POC_HARNESS_API_KEY") or os.environ.get("HARNESS_PASSWORD_API")
        org_id = os.environ.get("HARNESS_ORG_ID", "default")
        project_id = os.environ.get("HARNESS_PROJECT_ID", "image_flow")

        if not account_id or not api_key:
            print(
                "Error: Missing credentials. Set either:\n"
                "  Pipeline: HARNESS_ACCOUNT_ID + HARNESS_PASSWORD_API\n"
                "  Local:    POC_HARNESS_ACCOUNT_ID + POC_HARNESS_API_KEY\n",
                file=sys.stderr,
            )
            sys.exit(1)

        return cls(
            account_id=account_id,
            org_id=org_id,
            project_id=project_id,
            api_key=api_key,
        )

    def get_client(self) -> CodeClient:
        """Create a Code API client (base: /gateway/code/api/v1)."""
        return CodeClient(
            base_url=f"{self.harness_base}/code/api/v1",
            token=self.api_key,
            prefix="",
            auth_header_name="x-api-key",
        )

    def get_pipeline_client(self) -> PipelineClient:
        """Create a Pipeline API client (base: /gateway/pipeline/api)."""
        return PipelineClient(
            base_url=f"{self.harness_base}/pipeline/api",
            token=self.api_key,
            prefix="",
            auth_header_name="x-api-key",
        )

    def get_platform_client(self):
        """Create a Platform API client (base: /gateway/ng/api)."""
        if PlatformClient is None:
            raise ImportError("Platform SDK not installed. Install harness-next-gen-software-delivery-platform-api-reference-client.")
        return PlatformClient(
            base_url=f"{self.harness_base}/ng/api",
            token=self.api_key,
            prefix="",
            auth_header_name="x-api-key",
        )
