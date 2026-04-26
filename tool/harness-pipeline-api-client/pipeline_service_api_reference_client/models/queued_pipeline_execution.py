from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.queued_pipeline_execution_priority_type import (
    QueuedPipelineExecutionPriorityType,
    check_queued_pipeline_execution_priority_type,
)
from ..models.queued_pipeline_execution_status import (
    QueuedPipelineExecutionStatus,
    check_queued_pipeline_execution_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_trigger_info import ExecutionTriggerInfo
    from ..models.ng_label import NGLabel
    from ..models.ng_tag import NGTag


T = TypeVar("T", bound="QueuedPipelineExecution")


@_attrs_define
class QueuedPipelineExecution:
    """Represents a single queued pipeline execution with its global queue position

    Attributes:
        queue_position (int | Unset): Global position in the account queue (1-based), stable across filters
        plan_execution_id (str | Unset): Execution ID
        pipeline_identifier (str | Unset): Pipeline identifier
        pipeline_name (str | Unset): Pipeline display name
        org_identifier (str | Unset): Organization identifier
        project_identifier (str | Unset): Project identifier
        status (QueuedPipelineExecutionStatus | Unset): Execution Status of the entity. Valid values (PascalCase):
            Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted,
            Discontinuing, Queued, Paused, ResourceWaiting, InterventionWaiting, ApprovalWaiting, WaitStepRunning,
            QueuedLicenseLimitReached, QueuedExecutionConcurrencyReached, Success, Suspended, Skipped, Pausing,
            ApprovalRejected, InputWaiting, AbortedByFreeze, UploadWaiting, QueuedGlobalInfraCapacityReached.
        priority_type (QueuedPipelineExecutionPriorityType | Unset): Execution priority
        start_ts (int | Unset): When the execution was queued
        created_at (int | Unset): Creation timestamp
        execution_trigger_info (ExecutionTriggerInfo | Unset):
        run_sequence (int | Unset): Pipeline run number
        tags (list[NGTag] | Unset): Pipeline tags
        labels (list[NGLabel] | Unset): Pipeline labels
    """

    queue_position: int | Unset = UNSET
    plan_execution_id: str | Unset = UNSET
    pipeline_identifier: str | Unset = UNSET
    pipeline_name: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    status: QueuedPipelineExecutionStatus | Unset = UNSET
    priority_type: QueuedPipelineExecutionPriorityType | Unset = UNSET
    start_ts: int | Unset = UNSET
    created_at: int | Unset = UNSET
    execution_trigger_info: ExecutionTriggerInfo | Unset = UNSET
    run_sequence: int | Unset = UNSET
    tags: list[NGTag] | Unset = UNSET
    labels: list[NGLabel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue_position = self.queue_position

        plan_execution_id = self.plan_execution_id

        pipeline_identifier = self.pipeline_identifier

        pipeline_name = self.pipeline_name

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        priority_type: str | Unset = UNSET
        if not isinstance(self.priority_type, Unset):
            priority_type = self.priority_type

        start_ts = self.start_ts

        created_at = self.created_at

        execution_trigger_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_trigger_info, Unset):
            execution_trigger_info = self.execution_trigger_info.to_dict()

        run_sequence = self.run_sequence

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if queue_position is not UNSET:
            field_dict["queuePosition"] = queue_position
        if plan_execution_id is not UNSET:
            field_dict["planExecutionId"] = plan_execution_id
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if pipeline_name is not UNSET:
            field_dict["pipelineName"] = pipeline_name
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if status is not UNSET:
            field_dict["status"] = status
        if priority_type is not UNSET:
            field_dict["priorityType"] = priority_type
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if execution_trigger_info is not UNSET:
            field_dict["executionTriggerInfo"] = execution_trigger_info
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence
        if tags is not UNSET:
            field_dict["tags"] = tags
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_trigger_info import ExecutionTriggerInfo
        from ..models.ng_label import NGLabel
        from ..models.ng_tag import NGTag

        d = dict(src_dict)
        queue_position = d.pop("queuePosition", UNSET)

        plan_execution_id = d.pop("planExecutionId", UNSET)

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        pipeline_name = d.pop("pipelineName", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _status = d.pop("status", UNSET)
        status: QueuedPipelineExecutionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_queued_pipeline_execution_status(_status)

        _priority_type = d.pop("priorityType", UNSET)
        priority_type: QueuedPipelineExecutionPriorityType | Unset
        if isinstance(_priority_type, Unset):
            priority_type = UNSET
        else:
            priority_type = check_queued_pipeline_execution_priority_type(_priority_type)

        start_ts = d.pop("startTs", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _execution_trigger_info = d.pop("executionTriggerInfo", UNSET)
        execution_trigger_info: ExecutionTriggerInfo | Unset
        if isinstance(_execution_trigger_info, Unset):
            execution_trigger_info = UNSET
        else:
            execution_trigger_info = ExecutionTriggerInfo.from_dict(_execution_trigger_info)

        run_sequence = d.pop("runSequence", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[NGTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = NGTag.from_dict(tags_item_data)

                tags.append(tags_item)

        _labels = d.pop("labels", UNSET)
        labels: list[NGLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = NGLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        queued_pipeline_execution = cls(
            queue_position=queue_position,
            plan_execution_id=plan_execution_id,
            pipeline_identifier=pipeline_identifier,
            pipeline_name=pipeline_name,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            status=status,
            priority_type=priority_type,
            start_ts=start_ts,
            created_at=created_at,
            execution_trigger_info=execution_trigger_info,
            run_sequence=run_sequence,
            tags=tags,
            labels=labels,
        )

        queued_pipeline_execution.additional_properties = d
        return queued_pipeline_execution

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
