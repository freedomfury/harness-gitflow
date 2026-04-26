from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_label import TypesLabel
    from ..models.types_label_value import TypesLabelValue


T = TypeVar("T", bound="TypesLabelWithValues")


@_attrs_define
class TypesLabelWithValues:
    """
    Attributes:
        label (TypesLabel | Unset):
        values (list[TypesLabelValue] | Unset):
    """

    label: TypesLabel | Unset = UNSET
    values: list[TypesLabelValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_label import TypesLabel
        from ..models.types_label_value import TypesLabelValue

        d = dict(src_dict)
        _label = d.pop("label", UNSET)
        label: TypesLabel | Unset
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = TypesLabel.from_dict(_label)

        _values = d.pop("values", UNSET)
        values: list[TypesLabelValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = TypesLabelValue.from_dict(values_item_data)

                values.append(values_item)

        types_label_with_values = cls(
            label=label,
            values=values,
        )

        types_label_with_values.additional_properties = d
        return types_label_with_values

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
