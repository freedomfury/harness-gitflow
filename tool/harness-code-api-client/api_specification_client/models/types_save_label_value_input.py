from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_label_color import EnumLabelColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesSaveLabelValueInput")


@_attrs_define
class TypesSaveLabelValueInput:
    """
    Attributes:
        color (EnumLabelColor | Unset):
        id (int | Unset):
        value (str | Unset):
    """

    color: EnumLabelColor | Unset = UNSET
    id: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        id = self.id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

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

        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        types_save_label_value_input = cls(
            color=color,
            id=id,
            value=value,
        )

        types_save_label_value_input.additional_properties = d
        return types_save_label_value_input

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
