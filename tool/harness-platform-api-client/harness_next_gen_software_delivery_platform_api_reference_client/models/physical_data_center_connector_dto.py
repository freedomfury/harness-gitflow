from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_dto import HostDTO


T = TypeVar("T", bound="PhysicalDataCenterConnectorDTO")


@_attrs_define
class PhysicalDataCenterConnectorDTO:
    """This contains Physical Data Center connector details

    Attributes:
        connector_type (str):
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
        hosts (list[HostDTO] | Unset):
    """

    connector_type: str
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    hosts: list[HostDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        hosts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = []
            for hosts_item_data in self.hosts:
                hosts_item = hosts_item_data.to_dict()
                hosts.append(hosts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
            }
        )
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if hosts is not UNSET:
            field_dict["hosts"] = hosts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_dto import HostDTO

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        _hosts = d.pop("hosts", UNSET)
        hosts: list[HostDTO] | Unset = UNSET
        if _hosts is not UNSET:
            hosts = []
            for hosts_item_data in _hosts:
                hosts_item = HostDTO.from_dict(hosts_item_data)

                hosts.append(hosts_item)

        physical_data_center_connector_dto = cls(
            connector_type=connector_type,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
            hosts=hosts,
        )

        physical_data_center_connector_dto.additional_properties = d
        return physical_data_center_connector_dto

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
