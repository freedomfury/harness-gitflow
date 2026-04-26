from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueuedPipelineBulkAbortResult")


@_attrs_define
class QueuedPipelineBulkAbortResult:
    """Result of aborting a single queued pipeline execution

    Attributes:
        plan_execution_id (str | Unset): Plan execution ID
        success (bool | Unset): Whether the abort was successful
        error_message (str | Unset): Error message if the abort failed
    """

    plan_execution_id: str | Unset = UNSET
    success: bool | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_execution_id = self.plan_execution_id

        success = self.success

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_execution_id is not UNSET:
            field_dict["planExecutionId"] = plan_execution_id
        if success is not UNSET:
            field_dict["success"] = success
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan_execution_id = d.pop("planExecutionId", UNSET)

        success = d.pop("success", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        queued_pipeline_bulk_abort_result = cls(
            plan_execution_id=plan_execution_id,
            success=success,
            error_message=error_message,
        )

        queued_pipeline_bulk_abort_result.additional_properties = d
        return queued_pipeline_bulk_abort_result

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
