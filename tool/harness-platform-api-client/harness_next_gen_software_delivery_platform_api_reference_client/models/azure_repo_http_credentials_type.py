from typing import Literal, cast

AzureRepoHttpCredentialsType = Literal["UsernameToken"]

AZURE_REPO_HTTP_CREDENTIALS_TYPE_VALUES: set[AzureRepoHttpCredentialsType] = {
    "UsernameToken",
}


def check_azure_repo_http_credentials_type(value: str) -> AzureRepoHttpCredentialsType:
    if value in AZURE_REPO_HTTP_CREDENTIALS_TYPE_VALUES:
        return cast(AzureRepoHttpCredentialsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AZURE_REPO_HTTP_CREDENTIALS_TYPE_VALUES!r}")
