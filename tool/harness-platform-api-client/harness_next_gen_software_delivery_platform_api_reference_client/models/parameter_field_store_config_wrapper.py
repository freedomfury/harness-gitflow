from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_set_validator import InputSetValidator
    from ..models.store_config_wrapper import StoreConfigWrapper


T = TypeVar("T", bound="ParameterFieldStoreConfigWrapper")


@_attrs_define
class ParameterFieldStoreConfigWrapper:
    """
    Attributes:
        expression_value (str | Unset):
        expression (bool | Unset):
        value (StoreConfigWrapper | Unset):
        default_value (StoreConfigWrapper | Unset):
        type_string (bool | Unset):
        input_set_validator (InputSetValidator | Unset):
        json_response_field (bool | Unset):
        response_field (str | Unset):
        execution_input (bool | Unset):
    """

    expression_value: str | Unset = UNSET
    expression: bool | Unset = UNSET
    value: StoreConfigWrapper | Unset = UNSET
    default_value: StoreConfigWrapper | Unset = UNSET
    type_string: bool | Unset = UNSET
    input_set_validator: InputSetValidator | Unset = UNSET
    json_response_field: bool | Unset = UNSET
    response_field: str | Unset = UNSET
    execution_input: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expression_value = self.expression_value

        expression = self.expression

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        default_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        type_string = self.type_string

        input_set_validator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_set_validator, Unset):
            input_set_validator = self.input_set_validator.to_dict()

        json_response_field = self.json_response_field

        response_field = self.response_field

        execution_input = self.execution_input

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expression_value is not UNSET:
            field_dict["expressionValue"] = expression_value
        if expression is not UNSET:
            field_dict["expression"] = expression
        if value is not UNSET:
            field_dict["value"] = value
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if type_string is not UNSET:
            field_dict["typeString"] = type_string
        if input_set_validator is not UNSET:
            field_dict["inputSetValidator"] = input_set_validator
        if json_response_field is not UNSET:
            field_dict["jsonResponseField"] = json_response_field
        if response_field is not UNSET:
            field_dict["responseField"] = response_field
        if execution_input is not UNSET:
            field_dict["executionInput"] = execution_input

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_set_validator import InputSetValidator
        from ..models.store_config_wrapper import StoreConfigWrapper

        d = dict(src_dict)
        expression_value = d.pop("expressionValue", UNSET)

        expression = d.pop("expression", UNSET)

        _value = d.pop("value", UNSET)
        value: StoreConfigWrapper | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = StoreConfigWrapper.from_dict(_value)

        _default_value = d.pop("defaultValue", UNSET)
        default_value: StoreConfigWrapper | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = StoreConfigWrapper.from_dict(_default_value)

        type_string = d.pop("typeString", UNSET)

        _input_set_validator = d.pop("inputSetValidator", UNSET)
        input_set_validator: InputSetValidator | Unset
        if isinstance(_input_set_validator, Unset):
            input_set_validator = UNSET
        else:
            input_set_validator = InputSetValidator.from_dict(_input_set_validator)

        json_response_field = d.pop("jsonResponseField", UNSET)

        response_field = d.pop("responseField", UNSET)

        execution_input = d.pop("executionInput", UNSET)

        parameter_field_store_config_wrapper = cls(
            expression_value=expression_value,
            expression=expression,
            value=value,
            default_value=default_value,
            type_string=type_string,
            input_set_validator=input_set_validator,
            json_response_field=json_response_field,
            response_field=response_field,
            execution_input=execution_input,
        )

        parameter_field_store_config_wrapper.additional_properties = d
        return parameter_field_store_config_wrapper

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
