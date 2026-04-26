from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.variable_config_dto_value_type import VariableConfigDTOValueType, check_variable_config_dto_value_type

T = TypeVar("T", bound="StringVariableConfigDTO")


@_attrs_define
class StringVariableConfigDTO:
    """
    Attributes:
        value_type (VariableConfigDTOValueType): Type of Value of the Variable.
        type_ (str):
        fixed_value (str): Fixed Value of the Variable.
    """

    value_type: VariableConfigDTOValueType
    type_: str
    fixed_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_type: str = self.value_type

        type_ = self.type_

        fixed_value = self.fixed_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valueType": value_type,
                "type": type_,
                "fixedValue": fixed_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value_type = check_variable_config_dto_value_type(d.pop("valueType"))

        type_ = d.pop("type")

        fixed_value = d.pop("fixedValue")

        string_variable_config_dto = cls(
            value_type=value_type,
            type_=type_,
            fixed_value=fixed_value,
        )

        string_variable_config_dto.additional_properties = d
        return string_variable_config_dto

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
