from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_trigger_info import ExecutionTriggerInfo


T = TypeVar("T", bound="RetryExecutionMetadata")


@_attrs_define
class RetryExecutionMetadata:
    """This gives the Parent and Root execution id of the Execution part of Retried Execution

    Attributes:
        start_ts (int | Unset):
        end_ts (int | Unset):
        run_sequence (int | Unset):
        executed_by (ExecutionTriggerInfo | Unset):
        parent_execution_id (str | Unset):
        root_execution_id (str | Unset):
    """

    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    run_sequence: int | Unset = UNSET
    executed_by: ExecutionTriggerInfo | Unset = UNSET
    parent_execution_id: str | Unset = UNSET
    root_execution_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_ts = self.start_ts

        end_ts = self.end_ts

        run_sequence = self.run_sequence

        executed_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executed_by, Unset):
            executed_by = self.executed_by.to_dict()

        parent_execution_id = self.parent_execution_id

        root_execution_id = self.root_execution_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence
        if executed_by is not UNSET:
            field_dict["executedBy"] = executed_by
        if parent_execution_id is not UNSET:
            field_dict["parentExecutionId"] = parent_execution_id
        if root_execution_id is not UNSET:
            field_dict["rootExecutionId"] = root_execution_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_trigger_info import ExecutionTriggerInfo

        d = dict(src_dict)
        start_ts = d.pop("startTs", UNSET)

        end_ts = d.pop("endTs", UNSET)

        run_sequence = d.pop("runSequence", UNSET)

        _executed_by = d.pop("executedBy", UNSET)
        executed_by: ExecutionTriggerInfo | Unset
        if isinstance(_executed_by, Unset):
            executed_by = UNSET
        else:
            executed_by = ExecutionTriggerInfo.from_dict(_executed_by)

        parent_execution_id = d.pop("parentExecutionId", UNSET)

        root_execution_id = d.pop("rootExecutionId", UNSET)

        retry_execution_metadata = cls(
            start_ts=start_ts,
            end_ts=end_ts,
            run_sequence=run_sequence,
            executed_by=executed_by,
            parent_execution_id=parent_execution_id,
            root_execution_id=root_execution_id,
        )

        retry_execution_metadata.additional_properties = d
        return retry_execution_metadata

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
