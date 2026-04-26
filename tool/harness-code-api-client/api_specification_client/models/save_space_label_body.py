from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_save_label_input import TypesSaveLabelInput
    from ..models.types_save_label_value_input import TypesSaveLabelValueInput


T = TypeVar("T", bound="SaveSpaceLabelBody")


@_attrs_define
class SaveSpaceLabelBody:
    """
    Attributes:
        label (TypesSaveLabelInput | Unset):
        values (list[TypesSaveLabelValueInput] | Unset):
    """

    label: TypesSaveLabelInput | Unset = UNSET
    values: list[TypesSaveLabelValueInput] | Unset = UNSET
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
        from ..models.types_save_label_input import TypesSaveLabelInput
        from ..models.types_save_label_value_input import TypesSaveLabelValueInput

        d = dict(src_dict)
        _label = d.pop("label", UNSET)
        label: TypesSaveLabelInput | Unset
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = TypesSaveLabelInput.from_dict(_label)

        _values = d.pop("values", UNSET)
        values: list[TypesSaveLabelValueInput] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = TypesSaveLabelValueInput.from_dict(values_item_data)

                values.append(values_item)

        save_space_label_body = cls(
            label=label,
            values=values,
        )

        save_space_label_body.additional_properties = d
        return save_space_label_body

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
