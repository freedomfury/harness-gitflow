from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_execution import PipelineExecution


T = TypeVar("T", bound="DashboardPipelineExecution")


@_attrs_define
class DashboardPipelineExecution:
    """This is the view of the Pipeline Executions for given Time Interval presented in day wise format

    Attributes:
        pipeline_execution_info_list (list[PipelineExecution] | Unset):
    """

    pipeline_execution_info_list: list[PipelineExecution] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pipeline_execution_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pipeline_execution_info_list, Unset):
            pipeline_execution_info_list = []
            for pipeline_execution_info_list_item_data in self.pipeline_execution_info_list:
                pipeline_execution_info_list_item = pipeline_execution_info_list_item_data.to_dict()
                pipeline_execution_info_list.append(pipeline_execution_info_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_execution_info_list is not UNSET:
            field_dict["pipelineExecutionInfoList"] = pipeline_execution_info_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_execution import PipelineExecution

        d = dict(src_dict)
        _pipeline_execution_info_list = d.pop("pipelineExecutionInfoList", UNSET)
        pipeline_execution_info_list: list[PipelineExecution] | Unset = UNSET
        if _pipeline_execution_info_list is not UNSET:
            pipeline_execution_info_list = []
            for pipeline_execution_info_list_item_data in _pipeline_execution_info_list:
                pipeline_execution_info_list_item = PipelineExecution.from_dict(pipeline_execution_info_list_item_data)

                pipeline_execution_info_list.append(pipeline_execution_info_list_item)

        dashboard_pipeline_execution = cls(
            pipeline_execution_info_list=pipeline_execution_info_list,
        )

        dashboard_pipeline_execution.additional_properties = d
        return dashboard_pipeline_execution

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
