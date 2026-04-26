from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connector_validation_result_status import (
    ConnectorValidationResultStatus,
    check_connector_validation_result_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail import ErrorDetail


T = TypeVar("T", bound="ConnectorValidationResult")


@_attrs_define
class ConnectorValidationResult:
    """This has validation details for the Connector defined in Harness.

    Attributes:
        status (ConnectorValidationResultStatus | Unset): Connectivity status of a Connector.
        errors (list[ErrorDetail] | Unset): List of errors and their details.
        error_summary (str | Unset): Summary of errors.
        tested_at (int | Unset): Time at which Test Connection was completed
        delegate_id (str | Unset): ID of Delegate on which Test Connection is executed.
        task_id (str | Unset): ID of Delegate Task.
    """

    status: ConnectorValidationResultStatus | Unset = UNSET
    errors: list[ErrorDetail] | Unset = UNSET
    error_summary: str | Unset = UNSET
    tested_at: int | Unset = UNSET
    delegate_id: str | Unset = UNSET
    task_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        error_summary = self.error_summary

        tested_at = self.tested_at

        delegate_id = self.delegate_id

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if errors is not UNSET:
            field_dict["errors"] = errors
        if error_summary is not UNSET:
            field_dict["errorSummary"] = error_summary
        if tested_at is not UNSET:
            field_dict["testedAt"] = tested_at
        if delegate_id is not UNSET:
            field_dict["delegateId"] = delegate_id
        if task_id is not UNSET:
            field_dict["taskId"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_detail import ErrorDetail

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ConnectorValidationResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_connector_validation_result_status(_status)

        _errors = d.pop("errors", UNSET)
        errors: list[ErrorDetail] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ErrorDetail.from_dict(errors_item_data)

                errors.append(errors_item)

        error_summary = d.pop("errorSummary", UNSET)

        tested_at = d.pop("testedAt", UNSET)

        delegate_id = d.pop("delegateId", UNSET)

        task_id = d.pop("taskId", UNSET)

        connector_validation_result = cls(
            status=status,
            errors=errors,
            error_summary=error_summary,
            tested_at=tested_at,
            delegate_id=delegate_id,
            task_id=task_id,
        )

        connector_validation_result.additional_properties = d
        return connector_validation_result

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
