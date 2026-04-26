from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeErrorInfo")


@_attrs_define
class NodeErrorInfo:
    """
    Attributes:
        identifier (str | Unset):
        type_ (str | Unset):
        name (str | Unset):
        fqn (str | Unset):
    """

    identifier: str | Unset = UNSET
    type_: str | Unset = UNSET
    name: str | Unset = UNSET
    fqn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        type_ = self.type_

        name = self.name

        fqn = self.fqn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if fqn is not UNSET:
            field_dict["fqn"] = fqn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        fqn = d.pop("fqn", UNSET)

        node_error_info = cls(
            identifier=identifier,
            type_=type_,
            name=name,
            fqn=fqn,
        )

        node_error_info.additional_properties = d
        return node_error_info

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
