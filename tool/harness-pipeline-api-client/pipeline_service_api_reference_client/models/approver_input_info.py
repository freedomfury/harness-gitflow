from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApproverInputInfo")


@_attrs_define
class ApproverInputInfo:
    """This contains details of Approver Inputs

    Attributes:
        name (str):
        default_value (str | Unset):
        regex (str | Unset):
        allowed_values (list[str] | Unset):
        select_one_from (list[str] | Unset):
        required (bool | Unset):
        description (str | Unset):
    """

    name: str
    default_value: str | Unset = UNSET
    regex: str | Unset = UNSET
    allowed_values: list[str] | Unset = UNSET
    select_one_from: list[str] | Unset = UNSET
    required: bool | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        default_value = self.default_value

        regex = self.regex

        allowed_values: list[str] | Unset = UNSET
        if not isinstance(self.allowed_values, Unset):
            allowed_values = self.allowed_values

        select_one_from: list[str] | Unset = UNSET
        if not isinstance(self.select_one_from, Unset):
            select_one_from = self.select_one_from

        required = self.required

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if regex is not UNSET:
            field_dict["regex"] = regex
        if allowed_values is not UNSET:
            field_dict["allowedValues"] = allowed_values
        if select_one_from is not UNSET:
            field_dict["selectOneFrom"] = select_one_from
        if required is not UNSET:
            field_dict["required"] = required
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        default_value = d.pop("defaultValue", UNSET)

        regex = d.pop("regex", UNSET)

        allowed_values = cast(list[str], d.pop("allowedValues", UNSET))

        select_one_from = cast(list[str], d.pop("selectOneFrom", UNSET))

        required = d.pop("required", UNSET)

        description = d.pop("description", UNSET)

        approver_input_info = cls(
            name=name,
            default_value=default_value,
            regex=regex,
            allowed_values=allowed_values,
            select_one_from=select_one_from,
            required=required,
            description=description,
        )

        approver_input_info.additional_properties = d
        return approver_input_info

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
