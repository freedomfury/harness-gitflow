from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeInfo")


@_attrs_define
class NodeInfo:
    """
    Attributes:
        identifier (str | Unset):
        name (str | Unset):
        local_fqn (str | Unset):
    """

    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    local_fqn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        local_fqn = self.local_fqn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if local_fqn is not UNSET:
            field_dict["localFqn"] = local_fqn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        local_fqn = d.pop("localFqn", UNSET)

        node_info = cls(
            identifier=identifier,
            name=name,
            local_fqn=local_fqn,
        )

        node_info.additional_properties = d
        return node_info

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
