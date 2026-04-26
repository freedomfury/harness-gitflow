from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_execution_outline_status import (
    PipelineExecutionOutlineStatus,
    check_pipeline_execution_outline_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_execution_outline_dependency_graph import PipelineExecutionOutlineDependencyGraph
    from ..models.pipeline_execution_outline_stages_map import PipelineExecutionOutlineStagesMap


T = TypeVar("T", bound="PipelineExecutionOutline")


@_attrs_define
class PipelineExecutionOutline:
    """This is the view of the Pipeline Execution Outline

    Attributes:
        account_identifier (str):
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str | Unset):
        plan_execution_id (str | Unset):
        name (str | Unset):
        starting_node_id (str | Unset):
        starting_node_ids (list[str] | Unset):
        is_dag_enabled (bool | Unset):
        dependency_graph (PipelineExecutionOutlineDependencyGraph | Unset):
        status (PipelineExecutionOutlineStatus | Unset): Execution Status of the entity. Valid values (PascalCase):
            Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted,
            Discontinuing, Queued, Paused, ResourceWaiting, InterventionWaiting, ApprovalWaiting, WaitStepRunning,
            QueuedLicenseLimitReached, QueuedExecutionConcurrencyReached, Success, Suspended, Skipped, Pausing,
            ApprovalRejected, InputWaiting, AbortedByFreeze, UploadWaiting, QueuedGlobalInfraCapacityReached.
        failure_info (str | Unset):
        stages_map (PipelineExecutionOutlineStagesMap | Unset):
        modules (list[str] | Unset):
        start_ts (int | Unset):
        end_ts (int | Unset):
        created_at (int | Unset):
        last_updated_at (int | Unset):
        runtime_input_yaml (str | Unset):
        run_sequence (int | Unset):
    """

    account_identifier: str
    org_identifier: str
    project_identifier: str
    pipeline_identifier: str | Unset = UNSET
    plan_execution_id: str | Unset = UNSET
    name: str | Unset = UNSET
    starting_node_id: str | Unset = UNSET
    starting_node_ids: list[str] | Unset = UNSET
    is_dag_enabled: bool | Unset = UNSET
    dependency_graph: PipelineExecutionOutlineDependencyGraph | Unset = UNSET
    status: PipelineExecutionOutlineStatus | Unset = UNSET
    failure_info: str | Unset = UNSET
    stages_map: PipelineExecutionOutlineStagesMap | Unset = UNSET
    modules: list[str] | Unset = UNSET
    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    created_at: int | Unset = UNSET
    last_updated_at: int | Unset = UNSET
    runtime_input_yaml: str | Unset = UNSET
    run_sequence: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        pipeline_identifier = self.pipeline_identifier

        plan_execution_id = self.plan_execution_id

        name = self.name

        starting_node_id = self.starting_node_id

        starting_node_ids: list[str] | Unset = UNSET
        if not isinstance(self.starting_node_ids, Unset):
            starting_node_ids = self.starting_node_ids

        is_dag_enabled = self.is_dag_enabled

        dependency_graph: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dependency_graph, Unset):
            dependency_graph = self.dependency_graph.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        failure_info = self.failure_info

        stages_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stages_map, Unset):
            stages_map = self.stages_map.to_dict()

        modules: list[str] | Unset = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules

        start_ts = self.start_ts

        end_ts = self.end_ts

        created_at = self.created_at

        last_updated_at = self.last_updated_at

        runtime_input_yaml = self.runtime_input_yaml

        run_sequence = self.run_sequence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountIdentifier": account_identifier,
                "orgIdentifier": org_identifier,
                "projectIdentifier": project_identifier,
            }
        )
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if plan_execution_id is not UNSET:
            field_dict["planExecutionId"] = plan_execution_id
        if name is not UNSET:
            field_dict["name"] = name
        if starting_node_id is not UNSET:
            field_dict["startingNodeId"] = starting_node_id
        if starting_node_ids is not UNSET:
            field_dict["startingNodeIds"] = starting_node_ids
        if is_dag_enabled is not UNSET:
            field_dict["isDagEnabled"] = is_dag_enabled
        if dependency_graph is not UNSET:
            field_dict["dependencyGraph"] = dependency_graph
        if status is not UNSET:
            field_dict["status"] = status
        if failure_info is not UNSET:
            field_dict["failureInfo"] = failure_info
        if stages_map is not UNSET:
            field_dict["stagesMap"] = stages_map
        if modules is not UNSET:
            field_dict["modules"] = modules
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if runtime_input_yaml is not UNSET:
            field_dict["runtimeInputYaml"] = runtime_input_yaml
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_execution_outline_dependency_graph import PipelineExecutionOutlineDependencyGraph
        from ..models.pipeline_execution_outline_stages_map import PipelineExecutionOutlineStagesMap

        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier")

        org_identifier = d.pop("orgIdentifier")

        project_identifier = d.pop("projectIdentifier")

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        plan_execution_id = d.pop("planExecutionId", UNSET)

        name = d.pop("name", UNSET)

        starting_node_id = d.pop("startingNodeId", UNSET)

        starting_node_ids = cast(list[str], d.pop("startingNodeIds", UNSET))

        is_dag_enabled = d.pop("isDagEnabled", UNSET)

        _dependency_graph = d.pop("dependencyGraph", UNSET)
        dependency_graph: PipelineExecutionOutlineDependencyGraph | Unset
        if isinstance(_dependency_graph, Unset):
            dependency_graph = UNSET
        else:
            dependency_graph = PipelineExecutionOutlineDependencyGraph.from_dict(_dependency_graph)

        _status = d.pop("status", UNSET)
        status: PipelineExecutionOutlineStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_pipeline_execution_outline_status(_status)

        failure_info = d.pop("failureInfo", UNSET)

        _stages_map = d.pop("stagesMap", UNSET)
        stages_map: PipelineExecutionOutlineStagesMap | Unset
        if isinstance(_stages_map, Unset):
            stages_map = UNSET
        else:
            stages_map = PipelineExecutionOutlineStagesMap.from_dict(_stages_map)

        modules = cast(list[str], d.pop("modules", UNSET))

        start_ts = d.pop("startTs", UNSET)

        end_ts = d.pop("endTs", UNSET)

        created_at = d.pop("createdAt", UNSET)

        last_updated_at = d.pop("lastUpdatedAt", UNSET)

        runtime_input_yaml = d.pop("runtimeInputYaml", UNSET)

        run_sequence = d.pop("runSequence", UNSET)

        pipeline_execution_outline = cls(
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            plan_execution_id=plan_execution_id,
            name=name,
            starting_node_id=starting_node_id,
            starting_node_ids=starting_node_ids,
            is_dag_enabled=is_dag_enabled,
            dependency_graph=dependency_graph,
            status=status,
            failure_info=failure_info,
            stages_map=stages_map,
            modules=modules,
            start_ts=start_ts,
            end_ts=end_ts,
            created_at=created_at,
            last_updated_at=last_updated_at,
            runtime_input_yaml=runtime_input_yaml,
            run_sequence=run_sequence,
        )

        pipeline_execution_outline.additional_properties = d
        return pipeline_execution_outline

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
