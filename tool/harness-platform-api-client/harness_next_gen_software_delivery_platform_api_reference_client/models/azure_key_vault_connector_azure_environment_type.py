from typing import Literal, cast

AzureKeyVaultConnectorAzureEnvironmentType = Literal["AZURE", "AZURE_US_GOVERNMENT"]

AZURE_KEY_VAULT_CONNECTOR_AZURE_ENVIRONMENT_TYPE_VALUES: set[AzureKeyVaultConnectorAzureEnvironmentType] = {
    "AZURE",
    "AZURE_US_GOVERNMENT",
}


def check_azure_key_vault_connector_azure_environment_type(value: str) -> AzureKeyVaultConnectorAzureEnvironmentType:
    if value in AZURE_KEY_VAULT_CONNECTOR_AZURE_ENVIRONMENT_TYPE_VALUES:
        return cast(AzureKeyVaultConnectorAzureEnvironmentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AZURE_KEY_VAULT_CONNECTOR_AZURE_ENVIRONMENT_TYPE_VALUES!r}"
    )
