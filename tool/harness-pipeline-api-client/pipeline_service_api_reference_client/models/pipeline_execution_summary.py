from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_execution_summary_execution_mode import (
    PipelineExecutionSummaryExecutionMode,
    check_pipeline_execution_summary_execution_mode,
)
from ..models.pipeline_execution_summary_queued_type import (
    PipelineExecutionSummaryQueuedType,
    check_pipeline_execution_summary_queued_type,
)
from ..models.pipeline_execution_summary_status import (
    PipelineExecutionSummaryStatus,
    check_pipeline_execution_summary_status,
)
from ..models.pipeline_execution_summary_store_type import (
    PipelineExecutionSummaryStoreType,
    check_pipeline_execution_summary_store_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aborted_by import AbortedBy
    from ..models.entity_git_details import EntityGitDetails
    from ..models.execution_error_info import ExecutionErrorInfo
    from ..models.execution_trigger_info import ExecutionTriggerInfo
    from ..models.failure_info_dto import FailureInfoDTO
    from ..models.governance_metadata import GovernanceMetadata
    from ..models.ng_label import NGLabel
    from ..models.ng_tag import NGTag
    from ..models.pipeline_execution_summary_dependency_graph import PipelineExecutionSummaryDependencyGraph
    from ..models.pipeline_execution_summary_layout_node_map import PipelineExecutionSummaryLayoutNodeMap
    from ..models.pipeline_execution_summary_module_info import PipelineExecutionSummaryModuleInfo
    from ..models.pipeline_execution_summary_stages_executed_names import PipelineExecutionSummaryStagesExecutedNames
    from ..models.pipeline_stage_info import PipelineStageInfo
    from ..models.retry_execution_metadata import RetryExecutionMetadata
    from ..models.template_reference_summary import TemplateReferenceSummary


T = TypeVar("T", bound="PipelineExecutionSummary")


@_attrs_define
class PipelineExecutionSummary:
    """This is the view of the Pipeline Execution Summary

    Attributes:
        org_identifier (str):
        project_identifier (str):
        pipeline_identifier (str | Unset):
        plan_execution_id (str | Unset):
        name (str | Unset):
        yaml_version (str | Unset):
        status (PipelineExecutionSummaryStatus | Unset): Execution Status of the entity. Valid values (PascalCase):
            Running, AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted,
            Discontinuing, Queued, Paused, ResourceWaiting, InterventionWaiting, ApprovalWaiting, WaitStepRunning,
            QueuedLicenseLimitReached, QueuedExecutionConcurrencyReached, Success, Suspended, Skipped, Pausing,
            ApprovalRejected, InputWaiting, AbortedByFreeze, UploadWaiting, QueuedGlobalInfraCapacityReached.
        tags (list[NGTag] | Unset):
        labels (list[NGLabel] | Unset):
        execution_trigger_info (ExecutionTriggerInfo | Unset):
        execution_error_info (ExecutionErrorInfo | Unset):
        governance_metadata (GovernanceMetadata | Unset):
        failure_info (FailureInfoDTO | Unset):
        retry_execution_metadata (RetryExecutionMetadata | Unset): This gives the Parent and Root execution id of the
            Execution part of Retried Execution
        module_info (PipelineExecutionSummaryModuleInfo | Unset):
        layout_node_map (PipelineExecutionSummaryLayoutNodeMap | Unset):
        modules (list[str] | Unset):
        starting_node_id (str | Unset):
        starting_node_ids (list[str] | Unset):
        is_dag_enabled (bool | Unset):
        dependency_graph (PipelineExecutionSummaryDependencyGraph | Unset):
        start_ts (int | Unset):
        end_ts (int | Unset):
        created_at (int | Unset):
        can_retry (bool | Unset):
        can_re_execute (bool | Unset):
        show_retry_history (bool | Unset):
        is_retried_execution (bool | Unset):
        run_sequence (int | Unset):
        successful_stages_count (int | Unset):
        running_stages_count (int | Unset):
        failed_stages_count (int | Unset):
        total_stages_count (int | Unset):
        git_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        store_type (PipelineExecutionSummaryStoreType | Unset):
        connector_ref (str | Unset):
        execution_input_configured (bool | Unset):
        is_stages_execution (bool | Unset):
        parent_stage_info (PipelineStageInfo | Unset):
        stages_executed (list[str] | Unset):
        stages_executed_names (PipelineExecutionSummaryStagesExecutedNames | Unset):
        allow_stage_executions (bool | Unset):
        aborted_by (AbortedBy | Unset): This contains info of the user who aborted the pipeline
        execution_mode (PipelineExecutionSummaryExecutionMode | Unset):
        notes_exist_for_plan_execution_id (bool | Unset):
        should_use_simplified_key (bool | Unset):
        is_dynamic_execution (bool | Unset):
        is_original_yaml_used_on_rerun (bool | Unset):
        input_set_identifiers (list[str] | Unset):
        queued_type (PipelineExecutionSummaryQueuedType | Unset):
        queued_reason (str | Unset):
        template_reference_summary (TemplateReferenceSummary | Unset):
        notes (str | Unset):
        retried_execution (bool | Unset):
        stages_execution (bool | Unset):
        dynamic_execution (bool | Unset):
        original_yaml_used_on_rerun (bool | Unset):
    """

    org_identifier: str
    project_identifier: str
    pipeline_identifier: str | Unset = UNSET
    plan_execution_id: str | Unset = UNSET
    name: str | Unset = UNSET
    yaml_version: str | Unset = UNSET
    status: PipelineExecutionSummaryStatus | Unset = UNSET
    tags: list[NGTag] | Unset = UNSET
    labels: list[NGLabel] | Unset = UNSET
    execution_trigger_info: ExecutionTriggerInfo | Unset = UNSET
    execution_error_info: ExecutionErrorInfo | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    failure_info: FailureInfoDTO | Unset = UNSET
    retry_execution_metadata: RetryExecutionMetadata | Unset = UNSET
    module_info: PipelineExecutionSummaryModuleInfo | Unset = UNSET
    layout_node_map: PipelineExecutionSummaryLayoutNodeMap | Unset = UNSET
    modules: list[str] | Unset = UNSET
    starting_node_id: str | Unset = UNSET
    starting_node_ids: list[str] | Unset = UNSET
    is_dag_enabled: bool | Unset = UNSET
    dependency_graph: PipelineExecutionSummaryDependencyGraph | Unset = UNSET
    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    created_at: int | Unset = UNSET
    can_retry: bool | Unset = UNSET
    can_re_execute: bool | Unset = UNSET
    show_retry_history: bool | Unset = UNSET
    is_retried_execution: bool | Unset = UNSET
    run_sequence: int | Unset = UNSET
    successful_stages_count: int | Unset = UNSET
    running_stages_count: int | Unset = UNSET
    failed_stages_count: int | Unset = UNSET
    total_stages_count: int | Unset = UNSET
    git_details: EntityGitDetails | Unset = UNSET
    store_type: PipelineExecutionSummaryStoreType | Unset = UNSET
    connector_ref: str | Unset = UNSET
    execution_input_configured: bool | Unset = UNSET
    is_stages_execution: bool | Unset = UNSET
    parent_stage_info: PipelineStageInfo | Unset = UNSET
    stages_executed: list[str] | Unset = UNSET
    stages_executed_names: PipelineExecutionSummaryStagesExecutedNames | Unset = UNSET
    allow_stage_executions: bool | Unset = UNSET
    aborted_by: AbortedBy | Unset = UNSET
    execution_mode: PipelineExecutionSummaryExecutionMode | Unset = UNSET
    notes_exist_for_plan_execution_id: bool | Unset = UNSET
    should_use_simplified_key: bool | Unset = UNSET
    is_dynamic_execution: bool | Unset = UNSET
    is_original_yaml_used_on_rerun: bool | Unset = UNSET
    input_set_identifiers: list[str] | Unset = UNSET
    queued_type: PipelineExecutionSummaryQueuedType | Unset = UNSET
    queued_reason: str | Unset = UNSET
    template_reference_summary: TemplateReferenceSummary | Unset = UNSET
    notes: str | Unset = UNSET
    retried_execution: bool | Unset = UNSET
    stages_execution: bool | Unset = UNSET
    dynamic_execution: bool | Unset = UNSET
    original_yaml_used_on_rerun: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        pipeline_identifier = self.pipeline_identifier

        plan_execution_id = self.plan_execution_id

        name = self.name

        yaml_version = self.yaml_version

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

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

        execution_trigger_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_trigger_info, Unset):
            execution_trigger_info = self.execution_trigger_info.to_dict()

        execution_error_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_error_info, Unset):
            execution_error_info = self.execution_error_info.to_dict()

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        failure_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure_info, Unset):
            failure_info = self.failure_info.to_dict()

        retry_execution_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_execution_metadata, Unset):
            retry_execution_metadata = self.retry_execution_metadata.to_dict()

        module_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module_info, Unset):
            module_info = self.module_info.to_dict()

        layout_node_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.layout_node_map, Unset):
            layout_node_map = self.layout_node_map.to_dict()

        modules: list[str] | Unset = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules

        starting_node_id = self.starting_node_id

        starting_node_ids: list[str] | Unset = UNSET
        if not isinstance(self.starting_node_ids, Unset):
            starting_node_ids = self.starting_node_ids

        is_dag_enabled = self.is_dag_enabled

        dependency_graph: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dependency_graph, Unset):
            dependency_graph = self.dependency_graph.to_dict()

        start_ts = self.start_ts

        end_ts = self.end_ts

        created_at = self.created_at

        can_retry = self.can_retry

        can_re_execute = self.can_re_execute

        show_retry_history = self.show_retry_history

        is_retried_execution = self.is_retried_execution

        run_sequence = self.run_sequence

        successful_stages_count = self.successful_stages_count

        running_stages_count = self.running_stages_count

        failed_stages_count = self.failed_stages_count

        total_stages_count = self.total_stages_count

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

        store_type: str | Unset = UNSET
        if not isinstance(self.store_type, Unset):
            store_type = self.store_type

        connector_ref = self.connector_ref

        execution_input_configured = self.execution_input_configured

        is_stages_execution = self.is_stages_execution

        parent_stage_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_stage_info, Unset):
            parent_stage_info = self.parent_stage_info.to_dict()

        stages_executed: list[str] | Unset = UNSET
        if not isinstance(self.stages_executed, Unset):
            stages_executed = self.stages_executed

        stages_executed_names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stages_executed_names, Unset):
            stages_executed_names = self.stages_executed_names.to_dict()

        allow_stage_executions = self.allow_stage_executions

        aborted_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aborted_by, Unset):
            aborted_by = self.aborted_by.to_dict()

        execution_mode: str | Unset = UNSET
        if not isinstance(self.execution_mode, Unset):
            execution_mode = self.execution_mode

        notes_exist_for_plan_execution_id = self.notes_exist_for_plan_execution_id

        should_use_simplified_key = self.should_use_simplified_key

        is_dynamic_execution = self.is_dynamic_execution

        is_original_yaml_used_on_rerun = self.is_original_yaml_used_on_rerun

        input_set_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.input_set_identifiers, Unset):
            input_set_identifiers = self.input_set_identifiers

        queued_type: str | Unset = UNSET
        if not isinstance(self.queued_type, Unset):
            queued_type = self.queued_type

        queued_reason = self.queued_reason

        template_reference_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_reference_summary, Unset):
            template_reference_summary = self.template_reference_summary.to_dict()

        notes = self.notes

        retried_execution = self.retried_execution

        stages_execution = self.stages_execution

        dynamic_execution = self.dynamic_execution

        original_yaml_used_on_rerun = self.original_yaml_used_on_rerun

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
        if name is not UNSET:
            field_dict["name"] = name
        if yaml_version is not UNSET:
            field_dict["yamlVersion"] = yaml_version
        if status is not UNSET:
            field_dict["status"] = status
        if tags is not UNSET:
            field_dict["tags"] = tags
        if labels is not UNSET:
            field_dict["labels"] = labels
        if execution_trigger_info is not UNSET:
            field_dict["executionTriggerInfo"] = execution_trigger_info
        if execution_error_info is not UNSET:
            field_dict["executionErrorInfo"] = execution_error_info
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata
        if failure_info is not UNSET:
            field_dict["failureInfo"] = failure_info
        if retry_execution_metadata is not UNSET:
            field_dict["retryExecutionMetadata"] = retry_execution_metadata
        if module_info is not UNSET:
            field_dict["moduleInfo"] = module_info
        if layout_node_map is not UNSET:
            field_dict["layoutNodeMap"] = layout_node_map
        if modules is not UNSET:
            field_dict["modules"] = modules
        if starting_node_id is not UNSET:
            field_dict["startingNodeId"] = starting_node_id
        if starting_node_ids is not UNSET:
            field_dict["startingNodeIds"] = starting_node_ids
        if is_dag_enabled is not UNSET:
            field_dict["isDagEnabled"] = is_dag_enabled
        if dependency_graph is not UNSET:
            field_dict["dependencyGraph"] = dependency_graph
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if can_retry is not UNSET:
            field_dict["canRetry"] = can_retry
        if can_re_execute is not UNSET:
            field_dict["canReExecute"] = can_re_execute
        if show_retry_history is not UNSET:
            field_dict["showRetryHistory"] = show_retry_history
        if is_retried_execution is not UNSET:
            field_dict["isRetriedExecution"] = is_retried_execution
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence
        if successful_stages_count is not UNSET:
            field_dict["successfulStagesCount"] = successful_stages_count
        if running_stages_count is not UNSET:
            field_dict["runningStagesCount"] = running_stages_count
        if failed_stages_count is not UNSET:
            field_dict["failedStagesCount"] = failed_stages_count
        if total_stages_count is not UNSET:
            field_dict["totalStagesCount"] = total_stages_count
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if connector_ref is not UNSET:
            field_dict["connectorRef"] = connector_ref
        if execution_input_configured is not UNSET:
            field_dict["executionInputConfigured"] = execution_input_configured
        if is_stages_execution is not UNSET:
            field_dict["isStagesExecution"] = is_stages_execution
        if parent_stage_info is not UNSET:
            field_dict["parentStageInfo"] = parent_stage_info
        if stages_executed is not UNSET:
            field_dict["stagesExecuted"] = stages_executed
        if stages_executed_names is not UNSET:
            field_dict["stagesExecutedNames"] = stages_executed_names
        if allow_stage_executions is not UNSET:
            field_dict["allowStageExecutions"] = allow_stage_executions
        if aborted_by is not UNSET:
            field_dict["abortedBy"] = aborted_by
        if execution_mode is not UNSET:
            field_dict["executionMode"] = execution_mode
        if notes_exist_for_plan_execution_id is not UNSET:
            field_dict["notesExistForPlanExecutionId"] = notes_exist_for_plan_execution_id
        if should_use_simplified_key is not UNSET:
            field_dict["shouldUseSimplifiedKey"] = should_use_simplified_key
        if is_dynamic_execution is not UNSET:
            field_dict["isDynamicExecution"] = is_dynamic_execution
        if is_original_yaml_used_on_rerun is not UNSET:
            field_dict["isOriginalYamlUsedOnRerun"] = is_original_yaml_used_on_rerun
        if input_set_identifiers is not UNSET:
            field_dict["inputSetIdentifiers"] = input_set_identifiers
        if queued_type is not UNSET:
            field_dict["queuedType"] = queued_type
        if queued_reason is not UNSET:
            field_dict["queuedReason"] = queued_reason
        if template_reference_summary is not UNSET:
            field_dict["templateReferenceSummary"] = template_reference_summary
        if notes is not UNSET:
            field_dict["notes"] = notes
        if retried_execution is not UNSET:
            field_dict["retriedExecution"] = retried_execution
        if stages_execution is not UNSET:
            field_dict["stagesExecution"] = stages_execution
        if dynamic_execution is not UNSET:
            field_dict["dynamicExecution"] = dynamic_execution
        if original_yaml_used_on_rerun is not UNSET:
            field_dict["originalYamlUsedOnRerun"] = original_yaml_used_on_rerun

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aborted_by import AbortedBy
        from ..models.entity_git_details import EntityGitDetails
        from ..models.execution_error_info import ExecutionErrorInfo
        from ..models.execution_trigger_info import ExecutionTriggerInfo
        from ..models.failure_info_dto import FailureInfoDTO
        from ..models.governance_metadata import GovernanceMetadata
        from ..models.ng_label import NGLabel
        from ..models.ng_tag import NGTag
        from ..models.pipeline_execution_summary_dependency_graph import PipelineExecutionSummaryDependencyGraph
        from ..models.pipeline_execution_summary_layout_node_map import PipelineExecutionSummaryLayoutNodeMap
        from ..models.pipeline_execution_summary_module_info import PipelineExecutionSummaryModuleInfo
        from ..models.pipeline_execution_summary_stages_executed_names import (
            PipelineExecutionSummaryStagesExecutedNames,
        )
        from ..models.pipeline_stage_info import PipelineStageInfo
        from ..models.retry_execution_metadata import RetryExecutionMetadata
        from ..models.template_reference_summary import TemplateReferenceSummary

        d = dict(src_dict)
        org_identifier = d.pop("orgIdentifier")

        project_identifier = d.pop("projectIdentifier")

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        plan_execution_id = d.pop("planExecutionId", UNSET)

        name = d.pop("name", UNSET)

        yaml_version = d.pop("yamlVersion", UNSET)

        _status = d.pop("status", UNSET)
        status: PipelineExecutionSummaryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_pipeline_execution_summary_status(_status)

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

        _execution_trigger_info = d.pop("executionTriggerInfo", UNSET)
        execution_trigger_info: ExecutionTriggerInfo | Unset
        if isinstance(_execution_trigger_info, Unset):
            execution_trigger_info = UNSET
        else:
            execution_trigger_info = ExecutionTriggerInfo.from_dict(_execution_trigger_info)

        _execution_error_info = d.pop("executionErrorInfo", UNSET)
        execution_error_info: ExecutionErrorInfo | Unset
        if isinstance(_execution_error_info, Unset):
            execution_error_info = UNSET
        else:
            execution_error_info = ExecutionErrorInfo.from_dict(_execution_error_info)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        _failure_info = d.pop("failureInfo", UNSET)
        failure_info: FailureInfoDTO | Unset
        if isinstance(_failure_info, Unset):
            failure_info = UNSET
        else:
            failure_info = FailureInfoDTO.from_dict(_failure_info)

        _retry_execution_metadata = d.pop("retryExecutionMetadata", UNSET)
        retry_execution_metadata: RetryExecutionMetadata | Unset
        if isinstance(_retry_execution_metadata, Unset):
            retry_execution_metadata = UNSET
        else:
            retry_execution_metadata = RetryExecutionMetadata.from_dict(_retry_execution_metadata)

        _module_info = d.pop("moduleInfo", UNSET)
        module_info: PipelineExecutionSummaryModuleInfo | Unset
        if isinstance(_module_info, Unset):
            module_info = UNSET
        else:
            module_info = PipelineExecutionSummaryModuleInfo.from_dict(_module_info)

        _layout_node_map = d.pop("layoutNodeMap", UNSET)
        layout_node_map: PipelineExecutionSummaryLayoutNodeMap | Unset
        if isinstance(_layout_node_map, Unset):
            layout_node_map = UNSET
        else:
            layout_node_map = PipelineExecutionSummaryLayoutNodeMap.from_dict(_layout_node_map)

        modules = cast(list[str], d.pop("modules", UNSET))

        starting_node_id = d.pop("startingNodeId", UNSET)

        starting_node_ids = cast(list[str], d.pop("startingNodeIds", UNSET))

        is_dag_enabled = d.pop("isDagEnabled", UNSET)

        _dependency_graph = d.pop("dependencyGraph", UNSET)
        dependency_graph: PipelineExecutionSummaryDependencyGraph | Unset
        if isinstance(_dependency_graph, Unset):
            dependency_graph = UNSET
        else:
            dependency_graph = PipelineExecutionSummaryDependencyGraph.from_dict(_dependency_graph)

        start_ts = d.pop("startTs", UNSET)

        end_ts = d.pop("endTs", UNSET)

        created_at = d.pop("createdAt", UNSET)

        can_retry = d.pop("canRetry", UNSET)

        can_re_execute = d.pop("canReExecute", UNSET)

        show_retry_history = d.pop("showRetryHistory", UNSET)

        is_retried_execution = d.pop("isRetriedExecution", UNSET)

        run_sequence = d.pop("runSequence", UNSET)

        successful_stages_count = d.pop("successfulStagesCount", UNSET)

        running_stages_count = d.pop("runningStagesCount", UNSET)

        failed_stages_count = d.pop("failedStagesCount", UNSET)

        total_stages_count = d.pop("totalStagesCount", UNSET)

        _git_details = d.pop("gitDetails", UNSET)
        git_details: EntityGitDetails | Unset
        if isinstance(_git_details, Unset):
            git_details = UNSET
        else:
            git_details = EntityGitDetails.from_dict(_git_details)

        _store_type = d.pop("storeType", UNSET)
        store_type: PipelineExecutionSummaryStoreType | Unset
        if isinstance(_store_type, Unset):
            store_type = UNSET
        else:
            store_type = check_pipeline_execution_summary_store_type(_store_type)

        connector_ref = d.pop("connectorRef", UNSET)

        execution_input_configured = d.pop("executionInputConfigured", UNSET)

        is_stages_execution = d.pop("isStagesExecution", UNSET)

        _parent_stage_info = d.pop("parentStageInfo", UNSET)
        parent_stage_info: PipelineStageInfo | Unset
        if isinstance(_parent_stage_info, Unset):
            parent_stage_info = UNSET
        else:
            parent_stage_info = PipelineStageInfo.from_dict(_parent_stage_info)

        stages_executed = cast(list[str], d.pop("stagesExecuted", UNSET))

        _stages_executed_names = d.pop("stagesExecutedNames", UNSET)
        stages_executed_names: PipelineExecutionSummaryStagesExecutedNames | Unset
        if isinstance(_stages_executed_names, Unset):
            stages_executed_names = UNSET
        else:
            stages_executed_names = PipelineExecutionSummaryStagesExecutedNames.from_dict(_stages_executed_names)

        allow_stage_executions = d.pop("allowStageExecutions", UNSET)

        _aborted_by = d.pop("abortedBy", UNSET)
        aborted_by: AbortedBy | Unset
        if isinstance(_aborted_by, Unset):
            aborted_by = UNSET
        else:
            aborted_by = AbortedBy.from_dict(_aborted_by)

        _execution_mode = d.pop("executionMode", UNSET)
        execution_mode: PipelineExecutionSummaryExecutionMode | Unset
        if isinstance(_execution_mode, Unset):
            execution_mode = UNSET
        else:
            execution_mode = check_pipeline_execution_summary_execution_mode(_execution_mode)

        notes_exist_for_plan_execution_id = d.pop("notesExistForPlanExecutionId", UNSET)

        should_use_simplified_key = d.pop("shouldUseSimplifiedKey", UNSET)

        is_dynamic_execution = d.pop("isDynamicExecution", UNSET)

        is_original_yaml_used_on_rerun = d.pop("isOriginalYamlUsedOnRerun", UNSET)

        input_set_identifiers = cast(list[str], d.pop("inputSetIdentifiers", UNSET))

        _queued_type = d.pop("queuedType", UNSET)
        queued_type: PipelineExecutionSummaryQueuedType | Unset
        if isinstance(_queued_type, Unset):
            queued_type = UNSET
        else:
            queued_type = check_pipeline_execution_summary_queued_type(_queued_type)

        queued_reason = d.pop("queuedReason", UNSET)

        _template_reference_summary = d.pop("templateReferenceSummary", UNSET)
        template_reference_summary: TemplateReferenceSummary | Unset
        if isinstance(_template_reference_summary, Unset):
            template_reference_summary = UNSET
        else:
            template_reference_summary = TemplateReferenceSummary.from_dict(_template_reference_summary)

        notes = d.pop("notes", UNSET)

        retried_execution = d.pop("retriedExecution", UNSET)

        stages_execution = d.pop("stagesExecution", UNSET)

        dynamic_execution = d.pop("dynamicExecution", UNSET)

        original_yaml_used_on_rerun = d.pop("originalYamlUsedOnRerun", UNSET)

        pipeline_execution_summary = cls(
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            plan_execution_id=plan_execution_id,
            name=name,
            yaml_version=yaml_version,
            status=status,
            tags=tags,
            labels=labels,
            execution_trigger_info=execution_trigger_info,
            execution_error_info=execution_error_info,
            governance_metadata=governance_metadata,
            failure_info=failure_info,
            retry_execution_metadata=retry_execution_metadata,
            module_info=module_info,
            layout_node_map=layout_node_map,
            modules=modules,
            starting_node_id=starting_node_id,
            starting_node_ids=starting_node_ids,
            is_dag_enabled=is_dag_enabled,
            dependency_graph=dependency_graph,
            start_ts=start_ts,
            end_ts=end_ts,
            created_at=created_at,
            can_retry=can_retry,
            can_re_execute=can_re_execute,
            show_retry_history=show_retry_history,
            is_retried_execution=is_retried_execution,
            run_sequence=run_sequence,
            successful_stages_count=successful_stages_count,
            running_stages_count=running_stages_count,
            failed_stages_count=failed_stages_count,
            total_stages_count=total_stages_count,
            git_details=git_details,
            store_type=store_type,
            connector_ref=connector_ref,
            execution_input_configured=execution_input_configured,
            is_stages_execution=is_stages_execution,
            parent_stage_info=parent_stage_info,
            stages_executed=stages_executed,
            stages_executed_names=stages_executed_names,
            allow_stage_executions=allow_stage_executions,
            aborted_by=aborted_by,
            execution_mode=execution_mode,
            notes_exist_for_plan_execution_id=notes_exist_for_plan_execution_id,
            should_use_simplified_key=should_use_simplified_key,
            is_dynamic_execution=is_dynamic_execution,
            is_original_yaml_used_on_rerun=is_original_yaml_used_on_rerun,
            input_set_identifiers=input_set_identifiers,
            queued_type=queued_type,
            queued_reason=queued_reason,
            template_reference_summary=template_reference_summary,
            notes=notes,
            retried_execution=retried_execution,
            stages_execution=stages_execution,
            dynamic_execution=dynamic_execution,
            original_yaml_used_on_rerun=original_yaml_used_on_rerun,
        )

        pipeline_execution_summary.additional_properties = d
        return pipeline_execution_summary

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
