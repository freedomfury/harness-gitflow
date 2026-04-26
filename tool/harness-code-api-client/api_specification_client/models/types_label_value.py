from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_label_color import EnumLabelColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesLabelValue")


@_attrs_define
class TypesLabelValue:
    """
    Attributes:
        color (EnumLabelColor | Unset):
        created (int | Unset):
        created_by (int | Unset):
        id (int | Unset):
        label_id (int | Unset):
        updated (int | Unset):
        updated_by (int | Unset):
        value (str | Unset):
    """

    color: EnumLabelColor | Unset = UNSET
    created: int | Unset = UNSET
    created_by: int | Unset = UNSET
    id: int | Unset = UNSET
    label_id: int | Unset = UNSET
    updated: int | Unset = UNSET
    updated_by: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        created = self.created

        created_by = self.created_by

        id = self.id

        label_id = self.label_id

        updated = self.updated

        updated_by = self.updated_by

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if id is not UNSET:
            field_dict["id"] = id
        if label_id is not UNSET:
            field_dict["label_id"] = label_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
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

        created = d.pop("created", UNSET)

        created_by = d.pop("created_by", UNSET)

        id = d.pop("id", UNSET)

        label_id = d.pop("label_id", UNSET)

        updated = d.pop("updated", UNSET)

        updated_by = d.pop("updated_by", UNSET)

        value = d.pop("value", UNSET)

        types_label_value = cls(
            color=color,
            created=created,
            created_by=created_by,
            id=id,
            label_id=label_id,
            updated=updated,
            updated_by=updated_by,
            value=value,
        )

        types_label_value.additional_properties = d
        return types_label_value

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
