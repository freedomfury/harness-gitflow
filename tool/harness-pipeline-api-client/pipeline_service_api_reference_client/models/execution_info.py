from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_info_status import ExecutionInfoStatus, check_execution_info_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionInfo")


@_attrs_define
class ExecutionInfo:
    """This is the view for a particular Execution in Retry History

    Attributes:
        uuid (str | Unset):
        start_ts (int | Unset):
        end_ts (int | Unset):
        status (ExecutionInfoStatus | Unset): Execution Status of the entity. Valid values (PascalCase): Running,
            AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted,
            Discontinuing, Queued, Paused, ResourceWaiting, InterventionWaiting, ApprovalWaiting, WaitStepRunning,
            QueuedLicenseLimitReached, QueuedExecutionConcurrencyReached, Success, Suspended, Skipped, Pausing,
            ApprovalRejected, InputWaiting, AbortedByFreeze, UploadWaiting, QueuedGlobalInfraCapacityReached.
        run_sequence (int | Unset):
    """

    uuid: str | Unset = UNSET
    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    status: ExecutionInfoStatus | Unset = UNSET
    run_sequence: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        start_ts = self.start_ts

        end_ts = self.end_ts

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        run_sequence = self.run_sequence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if status is not UNSET:
            field_dict["status"] = status
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        start_ts = d.pop("startTs", UNSET)

        end_ts = d.pop("endTs", UNSET)

        _status = d.pop("status", UNSET)
        status: ExecutionInfoStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_execution_info_status(_status)

        run_sequence = d.pop("runSequence", UNSET)

        execution_info = cls(
            uuid=uuid,
            start_ts=start_ts,
            end_ts=end_ts,
            status=status,
            run_sequence=run_sequence,
        )

        execution_info.additional_properties = d
        return execution_info

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
