from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.referenced_by_dto_type import ReferencedByDTOType, check_referenced_by_dto_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferencedByDTO")


@_attrs_define
class ReferencedByDTO:
    """File referenced by other entity

    Attributes:
        type_ (ReferencedByDTOType | Unset):
        name (str | Unset):
    """

    type_: ReferencedByDTOType | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ReferencedByDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_referenced_by_dto_type(_type_)

        name = d.pop("name", UNSET)

        referenced_by_dto = cls(
            type_=type_,
            name=name,
        )

        referenced_by_dto.additional_properties = d
        return referenced_by_dto

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
