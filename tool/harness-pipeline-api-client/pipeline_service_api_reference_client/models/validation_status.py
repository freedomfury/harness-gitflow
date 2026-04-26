from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_status_status_result import ValidationStatusStatusResult, check_validation_status_status_result
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationStatus")


@_attrs_define
class ValidationStatus:
    """
    Attributes:
        status_result (ValidationStatusStatusResult | Unset):
        detailed_message (str | Unset):
    """

    status_result: ValidationStatusStatusResult | Unset = UNSET
    detailed_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_result: str | Unset = UNSET
        if not isinstance(self.status_result, Unset):
            status_result = self.status_result

        detailed_message = self.detailed_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_result is not UNSET:
            field_dict["statusResult"] = status_result
        if detailed_message is not UNSET:
            field_dict["detailedMessage"] = detailed_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status_result = d.pop("statusResult", UNSET)
        status_result: ValidationStatusStatusResult | Unset
        if isinstance(_status_result, Unset):
            status_result = UNSET
        else:
            status_result = check_validation_status_status_result(_status_result)

        detailed_message = d.pop("detailedMessage", UNSET)

        validation_status = cls(
            status_result=status_result,
            detailed_message=detailed_message,
        )

        validation_status.additional_properties = d
        return validation_status

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
