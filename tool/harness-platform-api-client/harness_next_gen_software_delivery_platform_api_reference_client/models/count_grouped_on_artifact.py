from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.count_grouped_on_status import CountGroupedOnStatus


T = TypeVar("T", bound="CountGroupedOnArtifact")


@_attrs_define
class CountGroupedOnArtifact:
    """
    Attributes:
        artifact_path (str | Unset):
        artifact_version (str | Unset):
        artifact (str | Unset):
        count (int | Unset):
        execution_count_grouped_on_status_list (list[CountGroupedOnStatus] | Unset):
    """

    artifact_path: str | Unset = UNSET
    artifact_version: str | Unset = UNSET
    artifact: str | Unset = UNSET
    count: int | Unset = UNSET
    execution_count_grouped_on_status_list: list[CountGroupedOnStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifact_path = self.artifact_path

        artifact_version = self.artifact_version

        artifact = self.artifact

        count = self.count

        execution_count_grouped_on_status_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.execution_count_grouped_on_status_list, Unset):
            execution_count_grouped_on_status_list = []
            for execution_count_grouped_on_status_list_item_data in self.execution_count_grouped_on_status_list:
                execution_count_grouped_on_status_list_item = execution_count_grouped_on_status_list_item_data.to_dict()
                execution_count_grouped_on_status_list.append(execution_count_grouped_on_status_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifact_path is not UNSET:
            field_dict["artifactPath"] = artifact_path
        if artifact_version is not UNSET:
            field_dict["artifactVersion"] = artifact_version
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if count is not UNSET:
            field_dict["count"] = count
        if execution_count_grouped_on_status_list is not UNSET:
            field_dict["executionCountGroupedOnStatusList"] = execution_count_grouped_on_status_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.count_grouped_on_status import CountGroupedOnStatus

        d = dict(src_dict)
        artifact_path = d.pop("artifactPath", UNSET)

        artifact_version = d.pop("artifactVersion", UNSET)

        artifact = d.pop("artifact", UNSET)

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

        count_grouped_on_artifact = cls(
            artifact_path=artifact_path,
            artifact_version=artifact_version,
            artifact=artifact,
            count=count,
            execution_count_grouped_on_status_list=execution_count_grouped_on_status_list,
        )

        count_grouped_on_artifact.additional_properties = d
        return count_grouped_on_artifact

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
