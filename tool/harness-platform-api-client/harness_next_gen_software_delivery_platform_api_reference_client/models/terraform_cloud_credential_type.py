from typing import Literal, cast

TerraformCloudCredentialType = Literal["ApiToken"]

TERRAFORM_CLOUD_CREDENTIAL_TYPE_VALUES: set[TerraformCloudCredentialType] = {
    "ApiToken",
}


def check_terraform_cloud_credential_type(value: str) -> TerraformCloudCredentialType:
    if value in TERRAFORM_CLOUD_CREDENTIAL_TYPE_VALUES:
        return cast(TerraformCloudCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TERRAFORM_CLOUD_CREDENTIAL_TYPE_VALUES!r}")
