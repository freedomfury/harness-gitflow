from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueuedPipelineBulkAbortRequest")


@_attrs_define
class QueuedPipelineBulkAbortRequest:
    """Request to bulk abort queued pipeline executions

    Attributes:
        plan_execution_ids (list[str]): List of plan execution IDs to abort
    """

    plan_execution_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_execution_ids = self.plan_execution_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "planExecutionIds": plan_execution_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan_execution_ids = cast(list[str], d.pop("planExecutionIds"))

        queued_pipeline_bulk_abort_request = cls(
            plan_execution_ids=plan_execution_ids,
        )

        queued_pipeline_bulk_abort_request.additional_properties = d
        return queued_pipeline_bulk_abort_request

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
