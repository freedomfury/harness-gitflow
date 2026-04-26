from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.input_set_validator_validator_type import (
    InputSetValidatorValidatorType,
    check_input_set_validator_validator_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InputSetValidator")


@_attrs_define
class InputSetValidator:
    """
    Attributes:
        validator_type (InputSetValidatorValidatorType | Unset):
        parameters (str | Unset):
    """

    validator_type: InputSetValidatorValidatorType | Unset = UNSET
    parameters: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        validator_type: str | Unset = UNSET
        if not isinstance(self.validator_type, Unset):
            validator_type = self.validator_type

        parameters = self.parameters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if validator_type is not UNSET:
            field_dict["validatorType"] = validator_type
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _validator_type = d.pop("validatorType", UNSET)
        validator_type: InputSetValidatorValidatorType | Unset
        if isinstance(_validator_type, Unset):
            validator_type = UNSET
        else:
            validator_type = check_input_set_validator_validator_type(_validator_type)

        parameters = d.pop("parameters", UNSET)

        input_set_validator = cls(
            validator_type=validator_type,
            parameters=parameters,
        )

        input_set_validator.additional_properties = d
        return input_set_validator

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
