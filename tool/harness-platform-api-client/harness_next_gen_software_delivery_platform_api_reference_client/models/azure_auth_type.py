from typing import Literal, cast

AzureAuthType = Literal["Certificate", "Secret"]

AZURE_AUTH_TYPE_VALUES: set[AzureAuthType] = {
    "Certificate",
    "Secret",
}


def check_azure_auth_type(value: str) -> AzureAuthType:
    if value in AZURE_AUTH_TYPE_VALUES:
        return cast(AzureAuthType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AZURE_AUTH_TYPE_VALUES!r}")
