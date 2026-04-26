from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nexus_authentication import NexusAuthentication


T = TypeVar("T", bound="NexusConnector")


@_attrs_define
class NexusConnector:
    """Nexus Connector details.

    Attributes:
        connector_type (str):
        nexus_server_url (str):
        version (str):
        auth (NexusAuthentication | Unset): This entity contains the details for Nexus Authentication
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    nexus_server_url: str
    version: str
    auth: NexusAuthentication | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        nexus_server_url = self.nexus_server_url

        version = self.version

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "nexusServerUrl": nexus_server_url,
                "version": version,
            }
        )
        if auth is not UNSET:
            field_dict["auth"] = auth
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nexus_authentication import NexusAuthentication

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        nexus_server_url = d.pop("nexusServerUrl")

        version = d.pop("version")

        _auth = d.pop("auth", UNSET)
        auth: NexusAuthentication | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = NexusAuthentication.from_dict(_auth)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        nexus_connector = cls(
            connector_type=connector_type,
            nexus_server_url=nexus_server_url,
            version=version,
            auth=auth,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
        )

        nexus_connector.additional_properties = d
        return nexus_connector

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
