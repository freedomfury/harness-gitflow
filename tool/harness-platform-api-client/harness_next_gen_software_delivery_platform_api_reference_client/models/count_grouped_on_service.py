from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.count_grouped_on_artifact import CountGroupedOnArtifact
    from ..models.count_grouped_on_status import CountGroupedOnStatus


T = TypeVar("T", bound="CountGroupedOnService")


@_attrs_define
class CountGroupedOnService:
    """
    Attributes:
        service_reference (str | Unset):
        service_name (str | Unset):
        count (int | Unset):
        execution_count_grouped_on_status_list (list[CountGroupedOnStatus] | Unset):
        execution_count_grouped_on_artifact_list (list[CountGroupedOnArtifact] | Unset):
    """

    service_reference: str | Unset = UNSET
    service_name: str | Unset = UNSET
    count: int | Unset = UNSET
    execution_count_grouped_on_status_list: list[CountGroupedOnStatus] | Unset = UNSET
    execution_count_grouped_on_artifact_list: list[CountGroupedOnArtifact] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_reference = self.service_reference

        service_name = self.service_name

        count = self.count

        execution_count_grouped_on_status_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.execution_count_grouped_on_status_list, Unset):
            execution_count_grouped_on_status_list = []
            for execution_count_grouped_on_status_list_item_data in self.execution_count_grouped_on_status_list:
                execution_count_grouped_on_status_list_item = execution_count_grouped_on_status_list_item_data.to_dict()
                execution_count_grouped_on_status_list.append(execution_count_grouped_on_status_list_item)

        execution_count_grouped_on_artifact_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.execution_count_grouped_on_artifact_list, Unset):
            execution_count_grouped_on_artifact_list = []
            for execution_count_grouped_on_artifact_list_item_data in self.execution_count_grouped_on_artifact_list:
                execution_count_grouped_on_artifact_list_item = (
                    execution_count_grouped_on_artifact_list_item_data.to_dict()
                )
                execution_count_grouped_on_artifact_list.append(execution_count_grouped_on_artifact_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_reference is not UNSET:
            field_dict["serviceReference"] = service_reference
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if count is not UNSET:
            field_dict["count"] = count
        if execution_count_grouped_on_status_list is not UNSET:
            field_dict["executionCountGroupedOnStatusList"] = execution_count_grouped_on_status_list
        if execution_count_grouped_on_artifact_list is not UNSET:
            field_dict["executionCountGroupedOnArtifactList"] = execution_count_grouped_on_artifact_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.count_grouped_on_artifact import CountGroupedOnArtifact
        from ..models.count_grouped_on_status import CountGroupedOnStatus

        d = dict(src_dict)
        service_reference = d.pop("serviceReference", UNSET)

        service_name = d.pop("serviceName", UNSET)

        count = d.pop("count", UNSET)

        _execution_count_grouped_on_status_list = d.pop("executionCountGroupedOnStatusList", UNSET)
        execution_count_grouped_on_status_list: list[CountGroupedOnStatus] | Unset = UNSET
        if _execution_count_grouped_on_status_list is not UNSET:
            execution_count_grouped_on_status_list = []
            for execution_count_grouped_on_status_list_item_data in _execution_count_grouped_on_status_list:
                execution_count_grouped_on_status_list_item = CountGroupedOnStatus.from_dict(
                    execution_count_grouped_on_status_list_item_data
                )

                execution_count_grouped_on_status_list.append(execution_count_grouped_on_status_list_item)

        _execution_count_grouped_on_artifact_list = d.pop("executionCountGroupedOnArtifactList", UNSET)
        execution_count_grouped_on_artifact_list: list[CountGroupedOnArtifact] | Unset = UNSET
        if _execution_count_grouped_on_artifact_list is not UNSET:
            execution_count_grouped_on_artifact_list = []
            for execution_count_grouped_on_artifact_list_item_data in _execution_count_grouped_on_artifact_list:
                execution_count_grouped_on_artifact_list_item = CountGroupedOnArtifact.from_dict(
                    execution_count_grouped_on_artifact_list_item_data
                )

                execution_count_grouped_on_artifact_list.append(execution_count_grouped_on_artifact_list_item)

        count_grouped_on_service = cls(
            service_reference=service_reference,
            service_name=service_name,
            count=count,
            execution_count_grouped_on_status_list=execution_count_grouped_on_status_list,
            execution_count_grouped_on_artifact_list=execution_count_grouped_on_artifact_list,
        )

        count_grouped_on_service.additional_properties = d
        return count_grouped_on_service

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
