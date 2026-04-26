from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_info import ExecutionInfo
    from ..models.retry_stages_metadata import RetryStagesMetadata


T = TypeVar("T", bound="RetryHistoryResponse")


@_attrs_define
class RetryHistoryResponse:
    """This is the view of the history of Retry Failed Pipelines.

    Attributes:
        error_message (str | Unset):
        latest_execution_id (str | Unset):
        execution_infos (list[ExecutionInfo] | Unset):
        retry_stages_metadata (RetryStagesMetadata | Unset): This has lists of retried and skipped stage identifiers
    """

    error_message: str | Unset = UNSET
    latest_execution_id: str | Unset = UNSET
    execution_infos: list[ExecutionInfo] | Unset = UNSET
    retry_stages_metadata: RetryStagesMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        latest_execution_id = self.latest_execution_id

        execution_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.execution_infos, Unset):
            execution_infos = []
            for execution_infos_item_data in self.execution_infos:
                execution_infos_item = execution_infos_item_data.to_dict()
                execution_infos.append(execution_infos_item)

        retry_stages_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_stages_metadata, Unset):
            retry_stages_metadata = self.retry_stages_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if latest_execution_id is not UNSET:
            field_dict["latestExecutionId"] = latest_execution_id
        if execution_infos is not UNSET:
            field_dict["executionInfos"] = execution_infos
        if retry_stages_metadata is not UNSET:
            field_dict["retryStagesMetadata"] = retry_stages_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_info import ExecutionInfo
        from ..models.retry_stages_metadata import RetryStagesMetadata

        d = dict(src_dict)
        error_message = d.pop("errorMessage", UNSET)

        latest_execution_id = d.pop("latestExecutionId", UNSET)

        _execution_infos = d.pop("executionInfos", UNSET)
        execution_infos: list[ExecutionInfo] | Unset = UNSET
        if _execution_infos is not UNSET:
            execution_infos = []
            for execution_infos_item_data in _execution_infos:
                execution_infos_item = ExecutionInfo.from_dict(execution_infos_item_data)

                execution_infos.append(execution_infos_item)

        _retry_stages_metadata = d.pop("retryStagesMetadata", UNSET)
        retry_stages_metadata: RetryStagesMetadata | Unset
        if isinstance(_retry_stages_metadata, Unset):
            retry_stages_metadata = UNSET
        else:
            retry_stages_metadata = RetryStagesMetadata.from_dict(_retry_stages_metadata)

        retry_history_response = cls(
            error_message=error_message,
            latest_execution_id=latest_execution_id,
            execution_infos=execution_infos,
            retry_stages_metadata=retry_stages_metadata,
        )

        retry_history_response.additional_properties = d
        return retry_history_response

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
