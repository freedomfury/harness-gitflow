from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.queued_pipeline_bulk_abort_result import QueuedPipelineBulkAbortResult


T = TypeVar("T", bound="QueuedPipelineBulkAbortResponse")


@_attrs_define
class QueuedPipelineBulkAbortResponse:
    """Response for bulk abort of queued pipeline executions

    Attributes:
        results (list[QueuedPipelineBulkAbortResult] | Unset): Per-execution abort results
        success_count (int | Unset): Number of successfully aborted executions
        failure_count (int | Unset): Number of failed abort attempts
    """

    results: list[QueuedPipelineBulkAbortResult] | Unset = UNSET
    success_count: int | Unset = UNSET
    failure_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        success_count = self.success_count

        failure_count = self.failure_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if success_count is not UNSET:
            field_dict["successCount"] = success_count
        if failure_count is not UNSET:
            field_dict["failureCount"] = failure_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.queued_pipeline_bulk_abort_result import QueuedPipelineBulkAbortResult

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[QueuedPipelineBulkAbortResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = QueuedPipelineBulkAbortResult.from_dict(results_item_data)

                results.append(results_item)

        success_count = d.pop("successCount", UNSET)

        failure_count = d.pop("failureCount", UNSET)

        queued_pipeline_bulk_abort_response = cls(
            results=results,
            success_count=success_count,
            failure_count=failure_count,
        )

        queued_pipeline_bulk_abort_response.additional_properties = d
        return queued_pipeline_bulk_abort_response

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
