from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_label_color import EnumLabelColor
from ..models.enum_label_type import EnumLabelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DefineRepoLabelBody")


@_attrs_define
class DefineRepoLabelBody:
    """
    Attributes:
        color (EnumLabelColor | Unset):
        description (str | Unset):
        key (str | Unset):
        type_ (EnumLabelType | Unset):
    """

    color: EnumLabelColor | Unset = UNSET
    description: str | Unset = UNSET
    key: str | Unset = UNSET
    type_: EnumLabelType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        description = self.description

        key = self.key

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if key is not UNSET:
            field_dict["key"] = key
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: EnumLabelColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = EnumLabelColor(_color)

        description = d.pop("description", UNSET)

        key = d.pop("key", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EnumLabelType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnumLabelType(_type_)

        define_repo_label_body = cls(
            color=color,
            description=description,
            key=key,
            type_=type_,
        )

        define_repo_label_body.additional_properties = d
        return define_repo_label_body

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
