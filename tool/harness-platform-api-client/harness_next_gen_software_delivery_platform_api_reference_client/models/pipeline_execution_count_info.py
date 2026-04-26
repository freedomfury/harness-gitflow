from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.count_grouped_on_service import CountGroupedOnService


T = TypeVar("T", bound="PipelineExecutionCountInfo")


@_attrs_define
class PipelineExecutionCountInfo:
    """
    Attributes:
        execution_count_grouped_on_service_list (list[CountGroupedOnService] | Unset):
    """

    execution_count_grouped_on_service_list: list[CountGroupedOnService] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_count_grouped_on_service_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.execution_count_grouped_on_service_list, Unset):
            execution_count_grouped_on_service_list = []
            for execution_count_grouped_on_service_list_item_data in self.execution_count_grouped_on_service_list:
                execution_count_grouped_on_service_list_item = (
                    execution_count_grouped_on_service_list_item_data.to_dict()
                )
                execution_count_grouped_on_service_list.append(execution_count_grouped_on_service_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_count_grouped_on_service_list is not UNSET:
            field_dict["executionCountGroupedOnServiceList"] = execution_count_grouped_on_service_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.count_grouped_on_service import CountGroupedOnService

        d = dict(src_dict)
        _execution_count_grouped_on_service_list = d.pop("executionCountGroupedOnServiceList", UNSET)
        execution_count_grouped_on_service_list: list[CountGroupedOnService] | Unset = UNSET
        if _execution_count_grouped_on_service_list is not UNSET:
            execution_count_grouped_on_service_list = []
            for execution_count_grouped_on_service_list_item_data in _execution_count_grouped_on_service_list:
                execution_count_grouped_on_service_list_item = CountGroupedOnService.from_dict(
                    execution_count_grouped_on_service_list_item_data
                )

                execution_count_grouped_on_service_list.append(execution_count_grouped_on_service_list_item)

        pipeline_execution_count_info = cls(
            execution_count_grouped_on_service_list=execution_count_grouped_on_service_list,
        )

        pipeline_execution_count_info.additional_properties = d
        return pipeline_execution_count_info

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
