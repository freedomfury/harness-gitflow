from typing import Literal, cast

AzureCredentialType = Literal["InheritFromDelegate", "ManualConfig", "OidcAuthentication"]

AZURE_CREDENTIAL_TYPE_VALUES: set[AzureCredentialType] = {
    "InheritFromDelegate",
    "ManualConfig",
    "OidcAuthentication",
}


def check_azure_credential_type(value: str) -> AzureCredentialType:
    if value in AZURE_CREDENTIAL_TYPE_VALUES:
        return cast(AzureCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AZURE_CREDENTIAL_TYPE_VALUES!r}")
