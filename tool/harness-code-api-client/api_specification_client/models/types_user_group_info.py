from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesUserGroupInfo")


@_attrs_define
class TypesUserGroupInfo:
    """
    Attributes:
        description (str | Unset):
        id (int | Unset):
        identifier (str | Unset):
        name (str | Unset):
        scope (int | Unset):
    """

    description: str | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    scope: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        identifier = self.identifier

        name = self.name

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        scope = d.pop("scope", UNSET)

        types_user_group_info = cls(
            description=description,
            id=id,
            identifier=identifier,
            name=name,
            scope=scope,
        )

        types_user_group_info.additional_properties = d
        return types_user_group_info

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
