from typing import Literal, cast

AzureArtifactsHttpCredentialsType = Literal["PersonalAccessToken"]

AZURE_ARTIFACTS_HTTP_CREDENTIALS_TYPE_VALUES: set[AzureArtifactsHttpCredentialsType] = {
    "PersonalAccessToken",
}


def check_azure_artifacts_http_credentials_type(value: str) -> AzureArtifactsHttpCredentialsType:
    if value in AZURE_ARTIFACTS_HTTP_CREDENTIALS_TYPE_VALUES:
        return cast(AzureArtifactsHttpCredentialsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AZURE_ARTIFACTS_HTTP_CREDENTIALS_TYPE_VALUES!r}")
