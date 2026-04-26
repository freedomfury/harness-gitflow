from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_label_color import EnumLabelColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesLabelPullReqAssignmentInfo")


@_attrs_define
class TypesLabelPullReqAssignmentInfo:
    """
    Attributes:
        color (EnumLabelColor | Unset):
        id (int | Unset):
        key (str | Unset):
        scope (int | Unset):
        value (None | str | Unset):
        value_color (EnumLabelColor | Unset):
        value_count (int | Unset):
        value_id (int | None | Unset):
    """

    color: EnumLabelColor | Unset = UNSET
    id: int | Unset = UNSET
    key: str | Unset = UNSET
    scope: int | Unset = UNSET
    value: None | str | Unset = UNSET
    value_color: EnumLabelColor | Unset = UNSET
    value_count: int | Unset = UNSET
    value_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        id = self.id

        key = self.key

        scope = self.scope

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        value_color: str | Unset = UNSET
        if not isinstance(self.value_color, Unset):
            value_color = self.value_color.value

        value_count = self.value_count

        value_id: int | None | Unset
        if isinstance(self.value_id, Unset):
            value_id = UNSET
        else:
            value_id = self.value_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if scope is not UNSET:
            field_dict["scope"] = scope
        if value is not UNSET:
            field_dict["value"] = value
        if value_color is not UNSET:
            field_dict["value_color"] = value_color
        if value_count is not UNSET:
            field_dict["value_count"] = value_count
        if value_id is not UNSET:
            field_dict["value_id"] = value_id

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

        key = d.pop("key", UNSET)

        scope = d.pop("scope", UNSET)

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        _value_color = d.pop("value_color", UNSET)
        value_color: EnumLabelColor | Unset
        if isinstance(_value_color, Unset):
            value_color = UNSET
        else:
            value_color = EnumLabelColor(_value_color)

        value_count = d.pop("value_count", UNSET)

        def _parse_value_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        value_id = _parse_value_id(d.pop("value_id", UNSET))

        types_label_pull_req_assignment_info = cls(
            color=color,
            id=id,
            key=key,
            scope=scope,
            value=value,
            value_color=value_color,
            value_count=value_count,
            value_id=value_id,
        )

        types_label_pull_req_assignment_info.additional_properties = d
        return types_label_pull_req_assignment_info

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
