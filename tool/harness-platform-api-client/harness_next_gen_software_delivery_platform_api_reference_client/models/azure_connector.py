from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_connector_azure_environment_type import (
    AzureConnectorAzureEnvironmentType,
    check_azure_connector_azure_environment_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_credential import AzureCredential


T = TypeVar("T", bound="AzureConnector")


@_attrs_define
class AzureConnector:
    """This contains details of the Azure connector

    Attributes:
        connector_type (str):
        credential (AzureCredential): This contains Azure connector credentials
        azure_environment_type (AzureConnectorAzureEnvironmentType): This specifies the Azure Environment type, which is
            AZURE by default.
        delegate_selectors (list[str] | Unset):
        execute_on_delegate (bool | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    credential: AzureCredential
    azure_environment_type: AzureConnectorAzureEnvironmentType
    delegate_selectors: list[str] | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        credential = self.credential.to_dict()

        azure_environment_type: str = self.azure_environment_type

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        execute_on_delegate = self.execute_on_delegate

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "credential": credential,
                "azureEnvironmentType": azure_environment_type,
            }
        )
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_credential import AzureCredential

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        credential = AzureCredential.from_dict(d.pop("credential"))

        azure_environment_type = check_azure_connector_azure_environment_type(d.pop("azureEnvironmentType"))

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        azure_connector = cls(
            connector_type=connector_type,
            credential=credential,
            azure_environment_type=azure_environment_type,
            delegate_selectors=delegate_selectors,
            execute_on_delegate=execute_on_delegate,
            ignore_test_connection=ignore_test_connection,
        )

        azure_connector.additional_properties = d
        return azure_connector

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
