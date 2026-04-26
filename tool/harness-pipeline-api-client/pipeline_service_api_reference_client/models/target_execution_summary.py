from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetExecutionSummary")


@_attrs_define
class TargetExecutionSummary:
    """
    Attributes:
        trigger_id (str | Unset):
        target_id (str | Unset):
        runtime_input (str | Unset):
        plan_execution_id (str | Unset):
        run_sequence (int | Unset):
        execution_status (str | Unset):
        start_ts (int | Unset):
    """

    trigger_id: str | Unset = UNSET
    target_id: str | Unset = UNSET
    runtime_input: str | Unset = UNSET
    plan_execution_id: str | Unset = UNSET
    run_sequence: int | Unset = UNSET
    execution_status: str | Unset = UNSET
    start_ts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_id = self.trigger_id

        target_id = self.target_id

        runtime_input = self.runtime_input

        plan_execution_id = self.plan_execution_id

        run_sequence = self.run_sequence

        execution_status = self.execution_status

        start_ts = self.start_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trigger_id is not UNSET:
            field_dict["triggerId"] = trigger_id
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if runtime_input is not UNSET:
            field_dict["runtimeInput"] = runtime_input
        if plan_execution_id is not UNSET:
            field_dict["planExecutionId"] = plan_execution_id
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence
        if execution_status is not UNSET:
            field_dict["executionStatus"] = execution_status
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger_id = d.pop("triggerId", UNSET)

        target_id = d.pop("targetId", UNSET)

        runtime_input = d.pop("runtimeInput", UNSET)

        plan_execution_id = d.pop("planExecutionId", UNSET)

        run_sequence = d.pop("runSequence", UNSET)

        execution_status = d.pop("executionStatus", UNSET)

        start_ts = d.pop("startTs", UNSET)

        target_execution_summary = cls(
            trigger_id=trigger_id,
            target_id=target_id,
            runtime_input=runtime_input,
            plan_execution_id=plan_execution_id,
            run_sequence=run_sequence,
            execution_status=execution_status,
            start_ts=start_ts,
        )

        target_execution_summary.additional_properties = d
        return target_execution_summary

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
