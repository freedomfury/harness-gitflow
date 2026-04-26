from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_resource_type import EnumResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesFavoriteResource")


@_attrs_define
class TypesFavoriteResource:
    """
    Attributes:
        resource_id (int | Unset):
        resource_type (EnumResourceType | Unset):
    """

    resource_id: int | Unset = UNSET
    resource_type: EnumResourceType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        resource_type: str | Unset = UNSET
        if not isinstance(self.resource_type, Unset):
            resource_type = self.resource_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = d.pop("resource_id", UNSET)

        _resource_type = d.pop("resource_type", UNSET)
        resource_type: EnumResourceType | Unset
        if isinstance(_resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = EnumResourceType(_resource_type)

        types_favorite_resource = cls(
            resource_id=resource_id,
            resource_type=resource_type,
        )

        types_favorite_resource.additional_properties = d
        return types_favorite_resource

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
