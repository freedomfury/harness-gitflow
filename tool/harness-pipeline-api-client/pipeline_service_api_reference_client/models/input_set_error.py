from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InputSetError")


@_attrs_define
class InputSetError:
    """This contains the error details for a field while saving an Input Set

    Attributes:
        field_name (str | Unset): Name of the field that has the error
        message (str | Unset): Error message for this field
        identifier_of_error_source (str | Unset): Identifier of the Input Set from which this field is from
    """

    field_name: str | Unset = UNSET
    message: str | Unset = UNSET
    identifier_of_error_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        message = self.message

        identifier_of_error_source = self.identifier_of_error_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if message is not UNSET:
            field_dict["message"] = message
        if identifier_of_error_source is not UNSET:
            field_dict["identifierOfErrorSource"] = identifier_of_error_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("fieldName", UNSET)

        message = d.pop("message", UNSET)

        identifier_of_error_source = d.pop("identifierOfErrorSource", UNSET)

        input_set_error = cls(
            field_name=field_name,
            message=message,
            identifier_of_error_source=identifier_of_error_source,
        )

        input_set_error.additional_properties = d
        return input_set_error

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
