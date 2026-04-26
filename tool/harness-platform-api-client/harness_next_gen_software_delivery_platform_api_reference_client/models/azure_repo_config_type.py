from typing import Literal, cast

AzureRepoConfigType = Literal["Project", "Repo"]

AZURE_REPO_CONFIG_TYPE_VALUES: set[AzureRepoConfigType] = {
    "Project",
    "Repo",
}


def check_azure_repo_config_type(value: str) -> AzureRepoConfigType:
    if value in AZURE_REPO_CONFIG_TYPE_VALUES:
        return cast(AzureRepoConfigType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AZURE_REPO_CONFIG_TYPE_VALUES!r}")
