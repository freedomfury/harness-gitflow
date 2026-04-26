from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_dto_host_attributes import HostDTOHostAttributes


T = TypeVar("T", bound="HostDTO")


@_attrs_define
class HostDTO:
    """This entity contains the Host details

    Attributes:
        hostname (str):
        host_attributes (HostDTOHostAttributes | Unset):
    """

    hostname: str
    host_attributes: HostDTOHostAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        host_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.host_attributes, Unset):
            host_attributes = self.host_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
            }
        )
        if host_attributes is not UNSET:
            field_dict["hostAttributes"] = host_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_dto_host_attributes import HostDTOHostAttributes

        d = dict(src_dict)
        hostname = d.pop("hostname")

        _host_attributes = d.pop("hostAttributes", UNSET)
        host_attributes: HostDTOHostAttributes | Unset
        if isinstance(_host_attributes, Unset):
            host_attributes = UNSET
        else:
            host_attributes = HostDTOHostAttributes.from_dict(_host_attributes)

        host_dto = cls(
            hostname=hostname,
            host_attributes=host_attributes,
        )

        host_dto.additional_properties = d
        return host_dto

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
