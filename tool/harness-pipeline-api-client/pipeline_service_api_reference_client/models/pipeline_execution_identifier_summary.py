from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_execution_identifier_summary_status import (
    PipelineExecutionIdentifierSummaryStatus,
    check_pipeline_execution_identifier_summary_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineExecutionIdentifierSummary")


@_attrs_define
class PipelineExecutionIdentifierSummary:
    """This is the view of the Pipeline Execution Identifier Summary

    Attributes:
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str | Unset):
        plan_execution_id (str | Unset):
        status (PipelineExecutionIdentifierSummaryStatus | Unset): Execution Status of the entity. Valid values
            (PascalCase): Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted,
            Expired, Aborted, Discontinuing, Queued, Paused, ResourceWaiting, InterventionWaiting, ApprovalWaiting,
            WaitStepRunning, QueuedLicenseLimitReached, QueuedExecutionConcurrencyReached, Success, Suspended, Skipped,
            Pausing, ApprovalRejected, InputWaiting, AbortedByFreeze, UploadWaiting, QueuedGlobalInfraCapacityReached.
        run_sequence (int | Unset):
    """

    org_identifier: str
    project_identifier: str
    pipeline_identifier: str | Unset = UNSET
    plan_execution_id: str | Unset = UNSET
    status: PipelineExecutionIdentifierSummaryStatus | Unset = UNSET
    run_sequence: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        pipeline_identifier = self.pipeline_identifier

        plan_execution_id = self.plan_execution_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        run_sequence = self.run_sequence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgIdentifier": org_identifier,
                "projectIdentifier": project_identifier,
            }
        )
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if plan_execution_id is not UNSET:
            field_dict["planExecutionId"] = plan_execution_id
        if status is not UNSET:
            field_dict["status"] = status
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        org_identifier = d.pop("orgIdentifier")

        project_identifier = d.pop("projectIdentifier")

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        plan_execution_id = d.pop("planExecutionId", UNSET)

        _status = d.pop("status", UNSET)
        status: PipelineExecutionIdentifierSummaryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_pipeline_execution_identifier_summary_status(_status)

        run_sequence = d.pop("runSequence", UNSET)

        pipeline_execution_identifier_summary = cls(
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            plan_execution_id=plan_execution_id,
            status=status,
            run_sequence=run_sequence,
        )

        pipeline_execution_identifier_summary.additional_properties = d
        return pipeline_execution_identifier_summary

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
