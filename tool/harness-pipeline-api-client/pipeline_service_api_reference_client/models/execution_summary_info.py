from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_summary_info_last_execution_status import (
    ExecutionSummaryInfoLastExecutionStatus,
    check_execution_summary_info_last_execution_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSummaryInfo")


@_attrs_define
class ExecutionSummaryInfo:
    """This is the view of the Execution Summary

    Attributes:
        num_of_errors (list[int] | Unset):
        deployments (list[int] | Unset):
        last_execution_ts (int | Unset):
        last_execution_status (ExecutionSummaryInfoLastExecutionStatus | Unset): Execution Status of the entity. Valid
            values (PascalCase): Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed,
            NotStarted, Expired, Aborted, Discontinuing, Queued, Paused, ResourceWaiting, InterventionWaiting,
            ApprovalWaiting, WaitStepRunning, QueuedLicenseLimitReached, QueuedExecutionConcurrencyReached, Success,
            Suspended, Skipped, Pausing, ApprovalRejected, InputWaiting, AbortedByFreeze, UploadWaiting,
            QueuedGlobalInfraCapacityReached.
        last_execution_id (str | Unset):
    """

    num_of_errors: list[int] | Unset = UNSET
    deployments: list[int] | Unset = UNSET
    last_execution_ts: int | Unset = UNSET
    last_execution_status: ExecutionSummaryInfoLastExecutionStatus | Unset = UNSET
    last_execution_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_of_errors: list[int] | Unset = UNSET
        if not isinstance(self.num_of_errors, Unset):
            num_of_errors = self.num_of_errors

        deployments: list[int] | Unset = UNSET
        if not isinstance(self.deployments, Unset):
            deployments = self.deployments

        last_execution_ts = self.last_execution_ts

        last_execution_status: str | Unset = UNSET
        if not isinstance(self.last_execution_status, Unset):
            last_execution_status = self.last_execution_status

        last_execution_id = self.last_execution_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_of_errors is not UNSET:
            field_dict["numOfErrors"] = num_of_errors
        if deployments is not UNSET:
            field_dict["deployments"] = deployments
        if last_execution_ts is not UNSET:
            field_dict["lastExecutionTs"] = last_execution_ts
        if last_execution_status is not UNSET:
            field_dict["lastExecutionStatus"] = last_execution_status
        if last_execution_id is not UNSET:
            field_dict["lastExecutionId"] = last_execution_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_of_errors = cast(list[int], d.pop("numOfErrors", UNSET))

        deployments = cast(list[int], d.pop("deployments", UNSET))

        last_execution_ts = d.pop("lastExecutionTs", UNSET)

        _last_execution_status = d.pop("lastExecutionStatus", UNSET)
        last_execution_status: ExecutionSummaryInfoLastExecutionStatus | Unset
        if isinstance(_last_execution_status, Unset):
            last_execution_status = UNSET
        else:
            last_execution_status = check_execution_summary_info_last_execution_status(_last_execution_status)

        last_execution_id = d.pop("lastExecutionId", UNSET)

        execution_summary_info = cls(
            num_of_errors=num_of_errors,
            deployments=deployments,
            last_execution_ts=last_execution_ts,
            last_execution_status=last_execution_status,
            last_execution_id=last_execution_id,
        )

        execution_summary_info.additional_properties = d
        return execution_summary_info

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
