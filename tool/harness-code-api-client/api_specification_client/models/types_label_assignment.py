from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_label_color import EnumLabelColor
from ..models.enum_label_type import EnumLabelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_label_value_info import TypesLabelValueInfo


T = TypeVar("T", bound="TypesLabelAssignment")


@_attrs_define
class TypesLabelAssignment:
    """
    Attributes:
        assigned (bool | None | Unset):
        assigned_value (TypesLabelValueInfo | Unset):
        color (EnumLabelColor | Unset):
        id (int | Unset):
        key (str | Unset):
        scope (int | Unset):
        type_ (EnumLabelType | Unset):
        values (list[TypesLabelValueInfo] | Unset):
    """

    assigned: bool | None | Unset = UNSET
    assigned_value: TypesLabelValueInfo | Unset = UNSET
    color: EnumLabelColor | Unset = UNSET
    id: int | Unset = UNSET
    key: str | Unset = UNSET
    scope: int | Unset = UNSET
    type_: EnumLabelType | Unset = UNSET
    values: list[TypesLabelValueInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned: bool | None | Unset
        if isinstance(self.assigned, Unset):
            assigned = UNSET
        else:
            assigned = self.assigned

        assigned_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assigned_value, Unset):
            assigned_value = self.assigned_value.to_dict()

        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        id = self.id

        key = self.key

        scope = self.scope

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if assigned_value is not UNSET:
            field_dict["assigned_value"] = assigned_value
        if color is not UNSET:
            field_dict["color"] = color
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if scope is not UNSET:
            field_dict["scope"] = scope
        if type_ is not UNSET:
            field_dict["type"] = type_
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_label_value_info import TypesLabelValueInfo

        d = dict(src_dict)

        def _parse_assigned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        assigned = _parse_assigned(d.pop("assigned", UNSET))

        _assigned_value = d.pop("assigned_value", UNSET)
        assigned_value: TypesLabelValueInfo | Unset
        if isinstance(_assigned_value, Unset):
            assigned_value = UNSET
        else:
            assigned_value = TypesLabelValueInfo.from_dict(_assigned_value)

        _color = d.pop("color", UNSET)
        color: EnumLabelColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = EnumLabelColor(_color)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        scope = d.pop("scope", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EnumLabelType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnumLabelType(_type_)

        _values = d.pop("values", UNSET)
        values: list[TypesLabelValueInfo] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = TypesLabelValueInfo.from_dict(values_item_data)

                values.append(values_item)

        types_label_assignment = cls(
            assigned=assigned,
            assigned_value=assigned_value,
            color=color,
            id=id,
            key=key,
            scope=scope,
            type_=type_,
            values=values,
        )

        types_label_assignment.additional_properties = d
        return types_label_assignment

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
