from typing import Literal, cast

AzureKeyVaultConnectorAzureManagedIdentityType = Literal["SystemAssignedManagedIdentity", "UserAssignedManagedIdentity"]

AZURE_KEY_VAULT_CONNECTOR_AZURE_MANAGED_IDENTITY_TYPE_VALUES: set[AzureKeyVaultConnectorAzureManagedIdentityType] = {
    "SystemAssignedManagedIdentity",
    "UserAssignedManagedIdentity",
}


def check_azure_key_vault_connector_azure_managed_identity_type(
    value: str,
) -> AzureKeyVaultConnectorAzureManagedIdentityType:
    if value in AZURE_KEY_VAULT_CONNECTOR_AZURE_MANAGED_IDENTITY_TYPE_VALUES:
        return cast(AzureKeyVaultConnectorAzureManagedIdentityType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AZURE_KEY_VAULT_CONNECTOR_AZURE_MANAGED_IDENTITY_TYPE_VALUES!r}"
    )
