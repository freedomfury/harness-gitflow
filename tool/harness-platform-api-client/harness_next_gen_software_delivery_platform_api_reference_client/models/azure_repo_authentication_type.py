from typing import Literal, cast

AzureRepoAuthenticationType = Literal["Http", "Ssh"]

AZURE_REPO_AUTHENTICATION_TYPE_VALUES: set[AzureRepoAuthenticationType] = {
    "Http",
    "Ssh",
}


def check_azure_repo_authentication_type(value: str) -> AzureRepoAuthenticationType:
    if value in AZURE_REPO_AUTHENTICATION_TYPE_VALUES:
        return cast(AzureRepoAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AZURE_REPO_AUTHENTICATION_TYPE_VALUES!r}")
