from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_key_vault_connector_azure_environment_type import (
    AzureKeyVaultConnectorAzureEnvironmentType,
    check_azure_key_vault_connector_azure_environment_type,
)
from ..models.azure_key_vault_connector_azure_managed_identity_type import (
    AzureKeyVaultConnectorAzureManagedIdentityType,
    check_azure_key_vault_connector_azure_managed_identity_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureKeyVaultConnector")


@_attrs_define
class AzureKeyVaultConnector:
    """Returns configuration details for the Azure Key Vault Secret Manager.

    Attributes:
        connector_type (str):
        vault_name (str): The Azure Vault name
        subscription (str): Azure Subscription ID.
        client_id (str | Unset): Application ID of the Azure App.
        secret_key (str | Unset): This is the Harness text secret with the Azure authentication key as its value.
        tenant_id (str | Unset): The Azure Active Directory (AAD) directory ID where you created your application.
        vault_configured_manually (bool | Unset):
        azure_environment_type (AzureKeyVaultConnectorAzureEnvironmentType | Unset): This specifies the Azure
            Environment type, which is AZURE by default.
        delegate_selectors (list[str] | Unset): List of Delegate Selectors that belong to the same Delegate and are used
            to connect to the Secret Manager.
        use_managed_identity (bool | Unset): Boolean value to indicate if managed identity is used
        azure_managed_identity_type (AzureKeyVaultConnectorAzureManagedIdentityType | Unset): Managed Identity Type
        managed_client_id (str | Unset): Client Id of the ManagedIdentity resource
        ignore_test_connection (bool | Unset):
        enable_purge (bool | Unset): Boolean value to indicate if purge is enabled
        default (bool | Unset):
    """

    connector_type: str
    vault_name: str
    subscription: str
    client_id: str | Unset = UNSET
    secret_key: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    vault_configured_manually: bool | Unset = UNSET
    azure_environment_type: AzureKeyVaultConnectorAzureEnvironmentType | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    use_managed_identity: bool | Unset = UNSET
    azure_managed_identity_type: AzureKeyVaultConnectorAzureManagedIdentityType | Unset = UNSET
    managed_client_id: str | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    enable_purge: bool | Unset = UNSET
    default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        vault_name = self.vault_name

        subscription = self.subscription

        client_id = self.client_id

        secret_key = self.secret_key

        tenant_id = self.tenant_id

        vault_configured_manually = self.vault_configured_manually

        azure_environment_type: str | Unset = UNSET
        if not isinstance(self.azure_environment_type, Unset):
            azure_environment_type = self.azure_environment_type

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        use_managed_identity = self.use_managed_identity

        azure_managed_identity_type: str | Unset = UNSET
        if not isinstance(self.azure_managed_identity_type, Unset):
            azure_managed_identity_type = self.azure_managed_identity_type

        managed_client_id = self.managed_client_id

        ignore_test_connection = self.ignore_test_connection

        enable_purge = self.enable_purge

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "vaultName": vault_name,
                "subscription": subscription,
            }
        )
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if vault_configured_manually is not UNSET:
            field_dict["vaultConfiguredManually"] = vault_configured_manually
        if azure_environment_type is not UNSET:
            field_dict["azureEnvironmentType"] = azure_environment_type
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if use_managed_identity is not UNSET:
            field_dict["useManagedIdentity"] = use_managed_identity
        if azure_managed_identity_type is not UNSET:
            field_dict["azureManagedIdentityType"] = azure_managed_identity_type
        if managed_client_id is not UNSET:
            field_dict["managedClientId"] = managed_client_id
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if enable_purge is not UNSET:
            field_dict["enablePurge"] = enable_purge
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        vault_name = d.pop("vaultName")

        subscription = d.pop("subscription")

        client_id = d.pop("clientId", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        vault_configured_manually = d.pop("vaultConfiguredManually", UNSET)

        _azure_environment_type = d.pop("azureEnvironmentType", UNSET)
        azure_environment_type: AzureKeyVaultConnectorAzureEnvironmentType | Unset
        if isinstance(_azure_environment_type, Unset):
            azure_environment_type = UNSET
        else:
            azure_environment_type = check_azure_key_vault_connector_azure_environment_type(_azure_environment_type)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        use_managed_identity = d.pop("useManagedIdentity", UNSET)

        _azure_managed_identity_type = d.pop("azureManagedIdentityType", UNSET)
        azure_managed_identity_type: AzureKeyVaultConnectorAzureManagedIdentityType | Unset
        if isinstance(_azure_managed_identity_type, Unset):
            azure_managed_identity_type = UNSET
        else:
            azure_managed_identity_type = check_azure_key_vault_connector_azure_managed_identity_type(
                _azure_managed_identity_type
            )

        managed_client_id = d.pop("managedClientId", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        enable_purge = d.pop("enablePurge", UNSET)

        default = d.pop("default", UNSET)

        azure_key_vault_connector = cls(
            connector_type=connector_type,
            vault_name=vault_name,
            subscription=subscription,
            client_id=client_id,
            secret_key=secret_key,
            tenant_id=tenant_id,
            vault_configured_manually=vault_configured_manually,
            azure_environment_type=azure_environment_type,
            delegate_selectors=delegate_selectors,
            use_managed_identity=use_managed_identity,
            azure_managed_identity_type=azure_managed_identity_type,
            managed_client_id=managed_client_id,
            ignore_test_connection=ignore_test_connection,
            enable_purge=enable_purge,
            default=default,
        )

        azure_key_vault_connector.additional_properties = d
        return azure_key_vault_connector

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
