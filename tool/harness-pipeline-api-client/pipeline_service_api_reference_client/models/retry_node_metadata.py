from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_trigger_info import ExecutionTriggerInfo


T = TypeVar("T", bound="RetryNodeMetadata")


@_attrs_define
class RetryNodeMetadata:
    """
    Attributes:
        start_ts (int | Unset):
        end_ts (int | Unset):
        run_sequence (int | Unset):
        original_plan_execution_id (str | Unset):
        executed_by (ExecutionTriggerInfo | Unset):
    """

    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    run_sequence: int | Unset = UNSET
    original_plan_execution_id: str | Unset = UNSET
    executed_by: ExecutionTriggerInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_ts = self.start_ts

        end_ts = self.end_ts

        run_sequence = self.run_sequence

        original_plan_execution_id = self.original_plan_execution_id

        executed_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executed_by, Unset):
            executed_by = self.executed_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence
        if original_plan_execution_id is not UNSET:
            field_dict["originalPlanExecutionId"] = original_plan_execution_id
        if executed_by is not UNSET:
            field_dict["executedBy"] = executed_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_trigger_info import ExecutionTriggerInfo

        d = dict(src_dict)
        start_ts = d.pop("startTs", UNSET)

        end_ts = d.pop("endTs", UNSET)

        run_sequence = d.pop("runSequence", UNSET)

        original_plan_execution_id = d.pop("originalPlanExecutionId", UNSET)

        _executed_by = d.pop("executedBy", UNSET)
        executed_by: ExecutionTriggerInfo | Unset
        if isinstance(_executed_by, Unset):
            executed_by = UNSET
        else:
            executed_by = ExecutionTriggerInfo.from_dict(_executed_by)

        retry_node_metadata = cls(
            start_ts=start_ts,
            end_ts=end_ts,
            run_sequence=run_sequence,
            original_plan_execution_id=original_plan_execution_id,
            executed_by=executed_by,
        )

        retry_node_metadata.additional_properties = d
        return retry_node_metadata

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
