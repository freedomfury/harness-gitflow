from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_execution_outline_filter_dto_status_item import (
    PipelineExecutionOutlineFilterDTOStatusItem,
    check_pipeline_execution_outline_filter_dto_status_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="PipelineExecutionOutlineFilterDTO")


@_attrs_define
class PipelineExecutionOutlineFilterDTO:
    """
    Attributes:
        status (list[PipelineExecutionOutlineFilterDTOStatusItem] | Unset):
        time_range (TimeRange | Unset): Filter by queued time window
        pipeline_identifier (str | Unset):
        plan_execution_ids (list[str] | Unset):
    """

    status: list[PipelineExecutionOutlineFilterDTOStatusItem] | Unset = UNSET
    time_range: TimeRange | Unset = UNSET
    pipeline_identifier: str | Unset = UNSET
    plan_execution_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item: str = status_item_data
                status.append(status_item)

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        pipeline_identifier = self.pipeline_identifier

        plan_execution_ids: list[str] | Unset = UNSET
        if not isinstance(self.plan_execution_ids, Unset):
            plan_execution_ids = self.plan_execution_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if plan_execution_ids is not UNSET:
            field_dict["planExecutionIds"] = plan_execution_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: list[PipelineExecutionOutlineFilterDTOStatusItem] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = check_pipeline_execution_outline_filter_dto_status_item(status_item_data)

                status.append(status_item)

        _time_range = d.pop("timeRange", UNSET)
        time_range: TimeRange | Unset
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = TimeRange.from_dict(_time_range)

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        plan_execution_ids = cast(list[str], d.pop("planExecutionIds", UNSET))

        pipeline_execution_outline_filter_dto = cls(
            status=status,
            time_range=time_range,
            pipeline_identifier=pipeline_identifier,
            plan_execution_ids=plan_execution_ids,
        )

        pipeline_execution_outline_filter_dto.additional_properties = d
        return pipeline_execution_outline_filter_dto

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
