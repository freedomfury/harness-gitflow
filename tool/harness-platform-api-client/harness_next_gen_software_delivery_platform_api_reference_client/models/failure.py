from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.failure_code import FailureCode, check_failure_code
from ..models.failure_status import FailureStatus, check_failure_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_error import ValidationError


T = TypeVar("T", bound="Failure")


@_attrs_define
class Failure:
    """This is Failure entity as defied in Harness

    Attributes:
        status (FailureStatus | Unset):
        code (FailureCode | Unset):
        message (str | Unset):
        correlation_id (str | Unset):
        errors (list[ValidationError] | Unset):
    """

    status: FailureStatus | Unset = UNSET
    code: FailureCode | Unset = UNSET
    message: str | Unset = UNSET
    correlation_id: str | Unset = UNSET
    errors: list[ValidationError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        message = self.message

        correlation_id = self.correlation_id

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_error import ValidationError

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: FailureStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_failure_status(_status)

        _code = d.pop("code", UNSET)
        code: FailureCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = check_failure_code(_code)

        message = d.pop("message", UNSET)

        correlation_id = d.pop("correlationId", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[ValidationError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ValidationError.from_dict(errors_item_data)

                errors.append(errors_item)

        failure = cls(
            status=status,
            code=code,
            message=message,
            correlation_id=correlation_id,
            errors=errors,
        )

        failure.additional_properties = d
        return failure

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
