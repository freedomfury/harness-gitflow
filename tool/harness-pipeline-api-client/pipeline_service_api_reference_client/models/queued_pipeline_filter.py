from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.queued_pipeline_filter_priority_types_item import (
    QueuedPipelineFilterPriorityTypesItem,
    check_queued_pipeline_filter_priority_types_item,
)
from ..models.queued_pipeline_filter_statuses_item import (
    QueuedPipelineFilterStatusesItem,
    check_queued_pipeline_filter_statuses_item,
)
from ..models.queued_pipeline_filter_trigger_types_item import (
    QueuedPipelineFilterTriggerTypesItem,
    check_queued_pipeline_filter_trigger_types_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ng_tag import NGTag
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="QueuedPipelineFilter")


@_attrs_define
class QueuedPipelineFilter:
    """Filter criteria for listing queued pipeline executions

    Attributes:
        org_identifiers (list[str] | Unset): Filter by organization identifiers
        project_identifiers (list[str] | Unset): Filter by project identifiers
        pipeline_identifiers (list[str] | Unset): Filter by pipeline identifiers
        statuses (list[QueuedPipelineFilterStatusesItem] | Unset): Sub-filter within queued statuses
        priority_types (list[QueuedPipelineFilterPriorityTypesItem] | Unset): Filter by priority types (HIGH, LOW,
            NORMAL)
        trigger_types (list[QueuedPipelineFilterTriggerTypesItem] | Unset): Filter by trigger types
        pipeline_tags (list[NGTag] | Unset): Filter by pipeline tags
        queued_time_range (TimeRange | Unset): Filter by queued time window
    """

    org_identifiers: list[str] | Unset = UNSET
    project_identifiers: list[str] | Unset = UNSET
    pipeline_identifiers: list[str] | Unset = UNSET
    statuses: list[QueuedPipelineFilterStatusesItem] | Unset = UNSET
    priority_types: list[QueuedPipelineFilterPriorityTypesItem] | Unset = UNSET
    trigger_types: list[QueuedPipelineFilterTriggerTypesItem] | Unset = UNSET
    pipeline_tags: list[NGTag] | Unset = UNSET
    queued_time_range: TimeRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.org_identifiers, Unset):
            org_identifiers = self.org_identifiers

        project_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.project_identifiers, Unset):
            project_identifiers = self.project_identifiers

        pipeline_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.pipeline_identifiers, Unset):
            pipeline_identifiers = self.pipeline_identifiers

        statuses: list[str] | Unset = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item: str = statuses_item_data
                statuses.append(statuses_item)

        priority_types: list[str] | Unset = UNSET
        if not isinstance(self.priority_types, Unset):
            priority_types = []
            for priority_types_item_data in self.priority_types:
                priority_types_item: str = priority_types_item_data
                priority_types.append(priority_types_item)

        trigger_types: list[str] | Unset = UNSET
        if not isinstance(self.trigger_types, Unset):
            trigger_types = []
            for trigger_types_item_data in self.trigger_types:
                trigger_types_item: str = trigger_types_item_data
                trigger_types.append(trigger_types_item)

        pipeline_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pipeline_tags, Unset):
            pipeline_tags = []
            for pipeline_tags_item_data in self.pipeline_tags:
                pipeline_tags_item = pipeline_tags_item_data.to_dict()
                pipeline_tags.append(pipeline_tags_item)

        queued_time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queued_time_range, Unset):
            queued_time_range = self.queued_time_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_identifiers is not UNSET:
            field_dict["orgIdentifiers"] = org_identifiers
        if project_identifiers is not UNSET:
            field_dict["projectIdentifiers"] = project_identifiers
        if pipeline_identifiers is not UNSET:
            field_dict["pipelineIdentifiers"] = pipeline_identifiers
        if statuses is not UNSET:
            field_dict["statuses"] = statuses
        if priority_types is not UNSET:
            field_dict["priorityTypes"] = priority_types
        if trigger_types is not UNSET:
            field_dict["triggerTypes"] = trigger_types
        if pipeline_tags is not UNSET:
            field_dict["pipelineTags"] = pipeline_tags
        if queued_time_range is not UNSET:
            field_dict["queuedTimeRange"] = queued_time_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ng_tag import NGTag
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        org_identifiers = cast(list[str], d.pop("orgIdentifiers", UNSET))

        project_identifiers = cast(list[str], d.pop("projectIdentifiers", UNSET))

        pipeline_identifiers = cast(list[str], d.pop("pipelineIdentifiers", UNSET))

        _statuses = d.pop("statuses", UNSET)
        statuses: list[QueuedPipelineFilterStatusesItem] | Unset = UNSET
        if _statuses is not UNSET:
            statuses = []
            for statuses_item_data in _statuses:
                statuses_item = check_queued_pipeline_filter_statuses_item(statuses_item_data)

                statuses.append(statuses_item)

        _priority_types = d.pop("priorityTypes", UNSET)
        priority_types: list[QueuedPipelineFilterPriorityTypesItem] | Unset = UNSET
        if _priority_types is not UNSET:
            priority_types = []
            for priority_types_item_data in _priority_types:
                priority_types_item = check_queued_pipeline_filter_priority_types_item(priority_types_item_data)

                priority_types.append(priority_types_item)

        _trigger_types = d.pop("triggerTypes", UNSET)
        trigger_types: list[QueuedPipelineFilterTriggerTypesItem] | Unset = UNSET
        if _trigger_types is not UNSET:
            trigger_types = []
            for trigger_types_item_data in _trigger_types:
                trigger_types_item = check_queued_pipeline_filter_trigger_types_item(trigger_types_item_data)

                trigger_types.append(trigger_types_item)

        _pipeline_tags = d.pop("pipelineTags", UNSET)
        pipeline_tags: list[NGTag] | Unset = UNSET
        if _pipeline_tags is not UNSET:
            pipeline_tags = []
            for pipeline_tags_item_data in _pipeline_tags:
                pipeline_tags_item = NGTag.from_dict(pipeline_tags_item_data)

                pipeline_tags.append(pipeline_tags_item)

        _queued_time_range = d.pop("queuedTimeRange", UNSET)
        queued_time_range: TimeRange | Unset
        if isinstance(_queued_time_range, Unset):
            queued_time_range = UNSET
        else:
            queued_time_range = TimeRange.from_dict(_queued_time_range)

        queued_pipeline_filter = cls(
            org_identifiers=org_identifiers,
            project_identifiers=project_identifiers,
            pipeline_identifiers=pipeline_identifiers,
            statuses=statuses,
            priority_types=priority_types,
            trigger_types=trigger_types,
            pipeline_tags=pipeline_tags,
            queued_time_range=queued_time_range,
        )

        queued_pipeline_filter.additional_properties = d
        return queued_pipeline_filter

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
