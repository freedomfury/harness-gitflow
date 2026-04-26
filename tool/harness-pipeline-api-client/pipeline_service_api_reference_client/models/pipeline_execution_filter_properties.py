from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_execution_filter_properties_execution_mode_filter import (
    PipelineExecutionFilterPropertiesExecutionModeFilter,
    check_pipeline_execution_filter_properties_execution_mode_filter,
)
from ..models.pipeline_execution_filter_properties_filter_type import (
    PipelineExecutionFilterPropertiesFilterType,
    check_pipeline_execution_filter_properties_filter_type,
)
from ..models.pipeline_execution_filter_properties_status_item import (
    PipelineExecutionFilterPropertiesStatusItem,
    check_pipeline_execution_filter_properties_status_item,
)
from ..models.pipeline_execution_filter_properties_trigger_types_item import (
    PipelineExecutionFilterPropertiesTriggerTypesItem,
    check_pipeline_execution_filter_properties_trigger_types_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.module_properties_dto import ModulePropertiesDTO
    from ..models.ng_label import NGLabel
    from ..models.ng_tag import NGTag
    from ..models.pipeline_execution_filter_properties_tags import PipelineExecutionFilterPropertiesTags
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="PipelineExecutionFilterProperties")


@_attrs_define
class PipelineExecutionFilterProperties:
    """Filter properties for listing pipeline executions. The `filterType` field (inherited) is required and must be set to
    `PipelineExecution`.

        Attributes:
            filter_type (PipelineExecutionFilterPropertiesFilterType): This specifies the corresponding Entity of the
                filter.
            tags (PipelineExecutionFilterPropertiesTags | Unset): Filter tags as a key-value pair.
            pipeline_tags (list[NGTag] | Unset): Filter executions by pipeline-level tags (key-value pairs).
            pipeline_labels (list[NGLabel] | Unset): Filter executions by pipeline-level labels (key-value pairs).
            status (list[PipelineExecutionFilterPropertiesStatusItem] | Unset): Filter executions by execution status.
                Accepts a list of status values such as: Running, Success, Failed, Aborted, Expired, etc. Uses PascalCase format
                (e.g. 'Success', not 'SUCCESS').
            pipeline_name (str | Unset): Filter executions by pipeline name (partial match supported).
            time_range (TimeRange | Unset): Filter by queued time window
            module_properties (ModulePropertiesDTO | Unset): Module-specific filter properties (e.g. CD service/environment
                filters, CI build event filters).
            trigger_types (list[PipelineExecutionFilterPropertiesTriggerTypesItem] | Unset): Filter executions by trigger
                type. Examples: MANUAL, WEBHOOK, SCHEDULER_CRON, etc.
            trigger_identifiers (list[str] | Unset): Filter executions by trigger identifiers.
            execution_mode_filter (PipelineExecutionFilterPropertiesExecutionModeFilter | Unset): Filter by execution mode
                (e.g. default executions only, rollback executions only, or all).
            pipeline_identifiers (list[str] | Unset): Filter executions by a list of pipeline identifiers.
            my_deployments (bool | Unset): If true, returns only executions triggered by the current authenticated user.
            branch_name (str | Unset): Filter executions by the codebase/repository branch used during execution. This is
                different from the `branch` query parameter, which refers to the Git branch where the pipeline YAML definition
                is stored (for Git Experience / remote pipelines).
            repo (str | Unset): Filter executions by the repository name associated with the execution.
            input_set_identifiers (list[str] | Unset): Filter executions by input set identifiers used during execution.
            plan_execution_ids (list[str] | Unset): Filter by specific plan execution IDs.
            execution_notes (list[str] | Unset): Filter executions by execution notes content.
    """

    filter_type: PipelineExecutionFilterPropertiesFilterType
    tags: PipelineExecutionFilterPropertiesTags | Unset = UNSET
    pipeline_tags: list[NGTag] | Unset = UNSET
    pipeline_labels: list[NGLabel] | Unset = UNSET
    status: list[PipelineExecutionFilterPropertiesStatusItem] | Unset = UNSET
    pipeline_name: str | Unset = UNSET
    time_range: TimeRange | Unset = UNSET
    module_properties: ModulePropertiesDTO | Unset = UNSET
    trigger_types: list[PipelineExecutionFilterPropertiesTriggerTypesItem] | Unset = UNSET
    trigger_identifiers: list[str] | Unset = UNSET
    execution_mode_filter: PipelineExecutionFilterPropertiesExecutionModeFilter | Unset = UNSET
    pipeline_identifiers: list[str] | Unset = UNSET
    my_deployments: bool | Unset = UNSET
    branch_name: str | Unset = UNSET
    repo: str | Unset = UNSET
    input_set_identifiers: list[str] | Unset = UNSET
    plan_execution_ids: list[str] | Unset = UNSET
    execution_notes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type: str = self.filter_type

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        pipeline_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pipeline_tags, Unset):
            pipeline_tags = []
            for pipeline_tags_item_data in self.pipeline_tags:
                pipeline_tags_item = pipeline_tags_item_data.to_dict()
                pipeline_tags.append(pipeline_tags_item)

        pipeline_labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pipeline_labels, Unset):
            pipeline_labels = []
            for pipeline_labels_item_data in self.pipeline_labels:
                pipeline_labels_item = pipeline_labels_item_data.to_dict()
                pipeline_labels.append(pipeline_labels_item)

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item: str = status_item_data
                status.append(status_item)

        pipeline_name = self.pipeline_name

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        module_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module_properties, Unset):
            module_properties = self.module_properties.to_dict()

        trigger_types: list[str] | Unset = UNSET
        if not isinstance(self.trigger_types, Unset):
            trigger_types = []
            for trigger_types_item_data in self.trigger_types:
                trigger_types_item: str = trigger_types_item_data
                trigger_types.append(trigger_types_item)

        trigger_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.trigger_identifiers, Unset):
            trigger_identifiers = self.trigger_identifiers

        execution_mode_filter: str | Unset = UNSET
        if not isinstance(self.execution_mode_filter, Unset):
            execution_mode_filter = self.execution_mode_filter

        pipeline_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.pipeline_identifiers, Unset):
            pipeline_identifiers = self.pipeline_identifiers

        my_deployments = self.my_deployments

        branch_name = self.branch_name

        repo = self.repo

        input_set_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.input_set_identifiers, Unset):
            input_set_identifiers = self.input_set_identifiers

        plan_execution_ids: list[str] | Unset = UNSET
        if not isinstance(self.plan_execution_ids, Unset):
            plan_execution_ids = self.plan_execution_ids

        execution_notes: list[str] | Unset = UNSET
        if not isinstance(self.execution_notes, Unset):
            execution_notes = self.execution_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filterType": filter_type,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if pipeline_tags is not UNSET:
            field_dict["pipelineTags"] = pipeline_tags
        if pipeline_labels is not UNSET:
            field_dict["pipelineLabels"] = pipeline_labels
        if status is not UNSET:
            field_dict["status"] = status
        if pipeline_name is not UNSET:
            field_dict["pipelineName"] = pipeline_name
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range
        if module_properties is not UNSET:
            field_dict["moduleProperties"] = module_properties
        if trigger_types is not UNSET:
            field_dict["triggerTypes"] = trigger_types
        if trigger_identifiers is not UNSET:
            field_dict["triggerIdentifiers"] = trigger_identifiers
        if execution_mode_filter is not UNSET:
            field_dict["executionModeFilter"] = execution_mode_filter
        if pipeline_identifiers is not UNSET:
            field_dict["pipelineIdentifiers"] = pipeline_identifiers
        if my_deployments is not UNSET:
            field_dict["myDeployments"] = my_deployments
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if repo is not UNSET:
            field_dict["repo"] = repo
        if input_set_identifiers is not UNSET:
            field_dict["inputSetIdentifiers"] = input_set_identifiers
        if plan_execution_ids is not UNSET:
            field_dict["planExecutionIds"] = plan_execution_ids
        if execution_notes is not UNSET:
            field_dict["executionNotes"] = execution_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.module_properties_dto import ModulePropertiesDTO
        from ..models.ng_label import NGLabel
        from ..models.ng_tag import NGTag
        from ..models.pipeline_execution_filter_properties_tags import PipelineExecutionFilterPropertiesTags
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        filter_type = check_pipeline_execution_filter_properties_filter_type(d.pop("filterType"))

        _tags = d.pop("tags", UNSET)
        tags: PipelineExecutionFilterPropertiesTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = PipelineExecutionFilterPropertiesTags.from_dict(_tags)

        _pipeline_tags = d.pop("pipelineTags", UNSET)
        pipeline_tags: list[NGTag] | Unset = UNSET
        if _pipeline_tags is not UNSET:
            pipeline_tags = []
            for pipeline_tags_item_data in _pipeline_tags:
                pipeline_tags_item = NGTag.from_dict(pipeline_tags_item_data)

                pipeline_tags.append(pipeline_tags_item)

        _pipeline_labels = d.pop("pipelineLabels", UNSET)
        pipeline_labels: list[NGLabel] | Unset = UNSET
        if _pipeline_labels is not UNSET:
            pipeline_labels = []
            for pipeline_labels_item_data in _pipeline_labels:
                pipeline_labels_item = NGLabel.from_dict(pipeline_labels_item_data)

                pipeline_labels.append(pipeline_labels_item)

        _status = d.pop("status", UNSET)
        status: list[PipelineExecutionFilterPropertiesStatusItem] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = check_pipeline_execution_filter_properties_status_item(status_item_data)

                status.append(status_item)

        pipeline_name = d.pop("pipelineName", UNSET)

        _time_range = d.pop("timeRange", UNSET)
        time_range: TimeRange | Unset
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = TimeRange.from_dict(_time_range)

        _module_properties = d.pop("moduleProperties", UNSET)
        module_properties: ModulePropertiesDTO | Unset
        if isinstance(_module_properties, Unset):
            module_properties = UNSET
        else:
            module_properties = ModulePropertiesDTO.from_dict(_module_properties)

        _trigger_types = d.pop("triggerTypes", UNSET)
        trigger_types: list[PipelineExecutionFilterPropertiesTriggerTypesItem] | Unset = UNSET
        if _trigger_types is not UNSET:
            trigger_types = []
            for trigger_types_item_data in _trigger_types:
                trigger_types_item = check_pipeline_execution_filter_properties_trigger_types_item(
                    trigger_types_item_data
                )

                trigger_types.append(trigger_types_item)

        trigger_identifiers = cast(list[str], d.pop("triggerIdentifiers", UNSET))

        _execution_mode_filter = d.pop("executionModeFilter", UNSET)
        execution_mode_filter: PipelineExecutionFilterPropertiesExecutionModeFilter | Unset
        if isinstance(_execution_mode_filter, Unset):
            execution_mode_filter = UNSET
        else:
            execution_mode_filter = check_pipeline_execution_filter_properties_execution_mode_filter(
                _execution_mode_filter
            )

        pipeline_identifiers = cast(list[str], d.pop("pipelineIdentifiers", UNSET))

        my_deployments = d.pop("myDeployments", UNSET)

        branch_name = d.pop("branchName", UNSET)

        repo = d.pop("repo", UNSET)

        input_set_identifiers = cast(list[str], d.pop("inputSetIdentifiers", UNSET))

        plan_execution_ids = cast(list[str], d.pop("planExecutionIds", UNSET))

        execution_notes = cast(list[str], d.pop("executionNotes", UNSET))

        pipeline_execution_filter_properties = cls(
            filter_type=filter_type,
            tags=tags,
            pipeline_tags=pipeline_tags,
            pipeline_labels=pipeline_labels,
            status=status,
            pipeline_name=pipeline_name,
            time_range=time_range,
            module_properties=module_properties,
            trigger_types=trigger_types,
            trigger_identifiers=trigger_identifiers,
            execution_mode_filter=execution_mode_filter,
            pipeline_identifiers=pipeline_identifiers,
            my_deployments=my_deployments,
            branch_name=branch_name,
            repo=repo,
            input_set_identifiers=input_set_identifiers,
            plan_execution_ids=plan_execution_ids,
            execution_notes=execution_notes,
        )

        pipeline_execution_filter_properties.additional_properties = d
        return pipeline_execution_filter_properties

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
