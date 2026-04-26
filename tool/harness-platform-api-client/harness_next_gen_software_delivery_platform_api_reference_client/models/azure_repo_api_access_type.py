from typing import Literal, cast

AzureRepoApiAccessType = Literal["Token"]

AZURE_REPO_API_ACCESS_TYPE_VALUES: set[AzureRepoApiAccessType] = {
    "Token",
}


def check_azure_repo_api_access_type(value: str) -> AzureRepoApiAccessType:
    if value in AZURE_REPO_API_ACCESS_TYPE_VALUES:
        return cast(AzureRepoApiAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AZURE_REPO_API_ACCESS_TYPE_VALUES!r}")
