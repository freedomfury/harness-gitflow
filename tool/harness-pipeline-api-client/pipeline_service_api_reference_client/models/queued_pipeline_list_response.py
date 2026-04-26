from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_queued_pipeline_execution import PageQueuedPipelineExecution


T = TypeVar("T", bound="QueuedPipelineListResponse")


@_attrs_define
class QueuedPipelineListResponse:
    """Paginated list of queued pipeline executions with queue metadata

    Attributes:
        queued_executions (PageQueuedPipelineExecution | Unset): Paginated list of queued pipeline executions
        total_queued_in_account (int | Unset): Total queued executions in the account regardless of filters
        max_concurrency (int | Unset): Account's maximum concurrent execution limit
        current_running (int | Unset): Currently running execution count
    """

    queued_executions: PageQueuedPipelineExecution | Unset = UNSET
    total_queued_in_account: int | Unset = UNSET
    max_concurrency: int | Unset = UNSET
    current_running: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queued_executions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queued_executions, Unset):
            queued_executions = self.queued_executions.to_dict()

        total_queued_in_account = self.total_queued_in_account

        max_concurrency = self.max_concurrency

        current_running = self.current_running

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if queued_executions is not UNSET:
            field_dict["queuedExecutions"] = queued_executions
        if total_queued_in_account is not UNSET:
            field_dict["totalQueuedInAccount"] = total_queued_in_account
        if max_concurrency is not UNSET:
            field_dict["maxConcurrency"] = max_concurrency
        if current_running is not UNSET:
            field_dict["currentRunning"] = current_running

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_queued_pipeline_execution import PageQueuedPipelineExecution

        d = dict(src_dict)
        _queued_executions = d.pop("queuedExecutions", UNSET)
        queued_executions: PageQueuedPipelineExecution | Unset
        if isinstance(_queued_executions, Unset):
            queued_executions = UNSET
        else:
            queued_executions = PageQueuedPipelineExecution.from_dict(_queued_executions)

        total_queued_in_account = d.pop("totalQueuedInAccount", UNSET)

        max_concurrency = d.pop("maxConcurrency", UNSET)

        current_running = d.pop("currentRunning", UNSET)

        queued_pipeline_list_response = cls(
            queued_executions=queued_executions,
            total_queued_in_account=total_queued_in_account,
            max_concurrency=max_concurrency,
            current_running=current_running,
        )

        queued_pipeline_list_response.additional_properties = d
        return queued_pipeline_list_response

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
