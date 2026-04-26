from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_node_manual_intervention_available_actions_item import (
    ExecutionNodeManualInterventionAvailableActionsItem,
    check_execution_node_manual_intervention_available_actions_item,
)
from ..models.execution_node_status import ExecutionNodeStatus, check_execution_node_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delegate_info import DelegateInfo
    from ..models.executable_response import ExecutableResponse
    from ..models.execution_node_outcomes import ExecutionNodeOutcomes
    from ..models.execution_node_step_details import ExecutionNodeStepDetails
    from ..models.failure_info_dto import FailureInfoDTO
    from ..models.interrupt_effect_dto import InterruptEffectDTO
    from ..models.node_run_info import NodeRunInfo
    from ..models.orchestration_map import OrchestrationMap
    from ..models.retry_node_metadata import RetryNodeMetadata
    from ..models.skip_info import SkipInfo
    from ..models.strategy_metadata import StrategyMetadata
    from ..models.unit_progress import UnitProgress


T = TypeVar("T", bound="ExecutionNode")


@_attrs_define
class ExecutionNode:
    """
    Attributes:
        uuid (str | Unset):
        setup_id (str | Unset):
        name (str | Unset):
        identifier (str | Unset):
        base_fqn (str | Unset):
        outcomes (ExecutionNodeOutcomes | Unset):
        step_parameters (OrchestrationMap | Unset):
        created_at (int | Unset):
        start_ts (int | Unset):
        end_ts (int | Unset):
        step_type (str | Unset):
        status (ExecutionNodeStatus | Unset): Execution Status of the entity. Valid values (PascalCase): Running,
            AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted,
            Discontinuing, Queued, Paused, ResourceWaiting, InterventionWaiting, ApprovalWaiting, WaitStepRunning,
            QueuedLicenseLimitReached, QueuedExecutionConcurrencyReached, Success, Suspended, Skipped, Pausing,
            ApprovalRejected, InputWaiting, AbortedByFreeze, UploadWaiting, QueuedGlobalInfraCapacityReached.
        failure_info (FailureInfoDTO | Unset):
        skip_info (SkipInfo | Unset):
        node_run_info (NodeRunInfo | Unset):
        retry_node_metadata (RetryNodeMetadata | Unset):
        executable_responses (list[ExecutableResponse] | Unset):
        unit_progresses (list[UnitProgress] | Unset):
        progress_data (OrchestrationMap | Unset):
        delegate_info_list (list[DelegateInfo] | Unset):
        interrupt_histories (list[InterruptEffectDTO] | Unset):
        step_details (ExecutionNodeStepDetails | Unset):
        strategy_metadata (StrategyMetadata | Unset):
        execution_input_configured (bool | Unset):
        log_base_key (str | Unset):
        manual_intervention_available_actions (list[ExecutionNodeManualInterventionAvailableActionsItem] | Unset):
        children_count (int | Unset):
    """

    uuid: str | Unset = UNSET
    setup_id: str | Unset = UNSET
    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    base_fqn: str | Unset = UNSET
    outcomes: ExecutionNodeOutcomes | Unset = UNSET
    step_parameters: OrchestrationMap | Unset = UNSET
    created_at: int | Unset = UNSET
    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    step_type: str | Unset = UNSET
    status: ExecutionNodeStatus | Unset = UNSET
    failure_info: FailureInfoDTO | Unset = UNSET
    skip_info: SkipInfo | Unset = UNSET
    node_run_info: NodeRunInfo | Unset = UNSET
    retry_node_metadata: RetryNodeMetadata | Unset = UNSET
    executable_responses: list[ExecutableResponse] | Unset = UNSET
    unit_progresses: list[UnitProgress] | Unset = UNSET
    progress_data: OrchestrationMap | Unset = UNSET
    delegate_info_list: list[DelegateInfo] | Unset = UNSET
    interrupt_histories: list[InterruptEffectDTO] | Unset = UNSET
    step_details: ExecutionNodeStepDetails | Unset = UNSET
    strategy_metadata: StrategyMetadata | Unset = UNSET
    execution_input_configured: bool | Unset = UNSET
    log_base_key: str | Unset = UNSET
    manual_intervention_available_actions: list[ExecutionNodeManualInterventionAvailableActionsItem] | Unset = UNSET
    children_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        setup_id = self.setup_id

        name = self.name

        identifier = self.identifier

        base_fqn = self.base_fqn

        outcomes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outcomes, Unset):
            outcomes = self.outcomes.to_dict()

        step_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.step_parameters, Unset):
            step_parameters = self.step_parameters.to_dict()

        created_at = self.created_at

        start_ts = self.start_ts

        end_ts = self.end_ts

        step_type = self.step_type

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        failure_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure_info, Unset):
            failure_info = self.failure_info.to_dict()

        skip_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip_info, Unset):
            skip_info = self.skip_info.to_dict()

        node_run_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_run_info, Unset):
            node_run_info = self.node_run_info.to_dict()

        retry_node_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_node_metadata, Unset):
            retry_node_metadata = self.retry_node_metadata.to_dict()

        executable_responses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.executable_responses, Unset):
            executable_responses = []
            for executable_responses_item_data in self.executable_responses:
                executable_responses_item = executable_responses_item_data.to_dict()
                executable_responses.append(executable_responses_item)

        unit_progresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unit_progresses, Unset):
            unit_progresses = []
            for unit_progresses_item_data in self.unit_progresses:
                unit_progresses_item = unit_progresses_item_data.to_dict()
                unit_progresses.append(unit_progresses_item)

        progress_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.progress_data, Unset):
            progress_data = self.progress_data.to_dict()

        delegate_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delegate_info_list, Unset):
            delegate_info_list = []
            for delegate_info_list_item_data in self.delegate_info_list:
                delegate_info_list_item = delegate_info_list_item_data.to_dict()
                delegate_info_list.append(delegate_info_list_item)

        interrupt_histories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interrupt_histories, Unset):
            interrupt_histories = []
            for interrupt_histories_item_data in self.interrupt_histories:
                interrupt_histories_item = interrupt_histories_item_data.to_dict()
                interrupt_histories.append(interrupt_histories_item)

        step_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.step_details, Unset):
            step_details = self.step_details.to_dict()

        strategy_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_metadata, Unset):
            strategy_metadata = self.strategy_metadata.to_dict()

        execution_input_configured = self.execution_input_configured

        log_base_key = self.log_base_key

        manual_intervention_available_actions: list[str] | Unset = UNSET
        if not isinstance(self.manual_intervention_available_actions, Unset):
            manual_intervention_available_actions = []
            for manual_intervention_available_actions_item_data in self.manual_intervention_available_actions:
                manual_intervention_available_actions_item: str = manual_intervention_available_actions_item_data
                manual_intervention_available_actions.append(manual_intervention_available_actions_item)

        children_count = self.children_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if setup_id is not UNSET:
            field_dict["setupId"] = setup_id
        if name is not UNSET:
            field_dict["name"] = name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if base_fqn is not UNSET:
            field_dict["baseFqn"] = base_fqn
        if outcomes is not UNSET:
            field_dict["outcomes"] = outcomes
        if step_parameters is not UNSET:
            field_dict["stepParameters"] = step_parameters
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if step_type is not UNSET:
            field_dict["stepType"] = step_type
        if status is not UNSET:
            field_dict["status"] = status
        if failure_info is not UNSET:
            field_dict["failureInfo"] = failure_info
        if skip_info is not UNSET:
            field_dict["skipInfo"] = skip_info
        if node_run_info is not UNSET:
            field_dict["nodeRunInfo"] = node_run_info
        if retry_node_metadata is not UNSET:
            field_dict["retryNodeMetadata"] = retry_node_metadata
        if executable_responses is not UNSET:
            field_dict["executableResponses"] = executable_responses
        if unit_progresses is not UNSET:
            field_dict["unitProgresses"] = unit_progresses
        if progress_data is not UNSET:
            field_dict["progressData"] = progress_data
        if delegate_info_list is not UNSET:
            field_dict["delegateInfoList"] = delegate_info_list
        if interrupt_histories is not UNSET:
            field_dict["interruptHistories"] = interrupt_histories
        if step_details is not UNSET:
            field_dict["stepDetails"] = step_details
        if strategy_metadata is not UNSET:
            field_dict["strategyMetadata"] = strategy_metadata
        if execution_input_configured is not UNSET:
            field_dict["executionInputConfigured"] = execution_input_configured
        if log_base_key is not UNSET:
            field_dict["logBaseKey"] = log_base_key
        if manual_intervention_available_actions is not UNSET:
            field_dict["manualInterventionAvailableActions"] = manual_intervention_available_actions
        if children_count is not UNSET:
            field_dict["childrenCount"] = children_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delegate_info import DelegateInfo
        from ..models.executable_response import ExecutableResponse
        from ..models.execution_node_outcomes import ExecutionNodeOutcomes
        from ..models.execution_node_step_details import ExecutionNodeStepDetails
        from ..models.failure_info_dto import FailureInfoDTO
        from ..models.interrupt_effect_dto import InterruptEffectDTO
        from ..models.node_run_info import NodeRunInfo
        from ..models.orchestration_map import OrchestrationMap
        from ..models.retry_node_metadata import RetryNodeMetadata
        from ..models.skip_info import SkipInfo
        from ..models.strategy_metadata import StrategyMetadata
        from ..models.unit_progress import UnitProgress

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        setup_id = d.pop("setupId", UNSET)

        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        base_fqn = d.pop("baseFqn", UNSET)

        _outcomes = d.pop("outcomes", UNSET)
        outcomes: ExecutionNodeOutcomes | Unset
        if isinstance(_outcomes, Unset):
            outcomes = UNSET
        else:
            outcomes = ExecutionNodeOutcomes.from_dict(_outcomes)

        _step_parameters = d.pop("stepParameters", UNSET)
        step_parameters: OrchestrationMap | Unset
        if isinstance(_step_parameters, Unset):
            step_parameters = UNSET
        else:
            step_parameters = OrchestrationMap.from_dict(_step_parameters)

        created_at = d.pop("createdAt", UNSET)

        start_ts = d.pop("startTs", UNSET)

        end_ts = d.pop("endTs", UNSET)

        step_type = d.pop("stepType", UNSET)

        _status = d.pop("status", UNSET)
        status: ExecutionNodeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_execution_node_status(_status)

        _failure_info = d.pop("failureInfo", UNSET)
        failure_info: FailureInfoDTO | Unset
        if isinstance(_failure_info, Unset):
            failure_info = UNSET
        else:
            failure_info = FailureInfoDTO.from_dict(_failure_info)

        _skip_info = d.pop("skipInfo", UNSET)
        skip_info: SkipInfo | Unset
        if isinstance(_skip_info, Unset):
            skip_info = UNSET
        else:
            skip_info = SkipInfo.from_dict(_skip_info)

        _node_run_info = d.pop("nodeRunInfo", UNSET)
        node_run_info: NodeRunInfo | Unset
        if isinstance(_node_run_info, Unset):
            node_run_info = UNSET
        else:
            node_run_info = NodeRunInfo.from_dict(_node_run_info)

        _retry_node_metadata = d.pop("retryNodeMetadata", UNSET)
        retry_node_metadata: RetryNodeMetadata | Unset
        if isinstance(_retry_node_metadata, Unset):
            retry_node_metadata = UNSET
        else:
            retry_node_metadata = RetryNodeMetadata.from_dict(_retry_node_metadata)

        _executable_responses = d.pop("executableResponses", UNSET)
        executable_responses: list[ExecutableResponse] | Unset = UNSET
        if _executable_responses is not UNSET:
            executable_responses = []
            for executable_responses_item_data in _executable_responses:
                executable_responses_item = ExecutableResponse.from_dict(executable_responses_item_data)

                executable_responses.append(executable_responses_item)

        _unit_progresses = d.pop("unitProgresses", UNSET)
        unit_progresses: list[UnitProgress] | Unset = UNSET
        if _unit_progresses is not UNSET:
            unit_progresses = []
            for unit_progresses_item_data in _unit_progresses:
                unit_progresses_item = UnitProgress.from_dict(unit_progresses_item_data)

                unit_progresses.append(unit_progresses_item)

        _progress_data = d.pop("progressData", UNSET)
        progress_data: OrchestrationMap | Unset
        if isinstance(_progress_data, Unset):
            progress_data = UNSET
        else:
            progress_data = OrchestrationMap.from_dict(_progress_data)

        _delegate_info_list = d.pop("delegateInfoList", UNSET)
        delegate_info_list: list[DelegateInfo] | Unset = UNSET
        if _delegate_info_list is not UNSET:
            delegate_info_list = []
            for delegate_info_list_item_data in _delegate_info_list:
                delegate_info_list_item = DelegateInfo.from_dict(delegate_info_list_item_data)

                delegate_info_list.append(delegate_info_list_item)

        _interrupt_histories = d.pop("interruptHistories", UNSET)
        interrupt_histories: list[InterruptEffectDTO] | Unset = UNSET
        if _interrupt_histories is not UNSET:
            interrupt_histories = []
            for interrupt_histories_item_data in _interrupt_histories:
                interrupt_histories_item = InterruptEffectDTO.from_dict(interrupt_histories_item_data)

                interrupt_histories.append(interrupt_histories_item)

        _step_details = d.pop("stepDetails", UNSET)
        step_details: ExecutionNodeStepDetails | Unset
        if isinstance(_step_details, Unset):
            step_details = UNSET
        else:
            step_details = ExecutionNodeStepDetails.from_dict(_step_details)

        _strategy_metadata = d.pop("strategyMetadata", UNSET)
        strategy_metadata: StrategyMetadata | Unset
        if isinstance(_strategy_metadata, Unset):
            strategy_metadata = UNSET
        else:
            strategy_metadata = StrategyMetadata.from_dict(_strategy_metadata)

        execution_input_configured = d.pop("executionInputConfigured", UNSET)

        log_base_key = d.pop("logBaseKey", UNSET)

        _manual_intervention_available_actions = d.pop("manualInterventionAvailableActions", UNSET)
        manual_intervention_available_actions: list[ExecutionNodeManualInterventionAvailableActionsItem] | Unset = UNSET
        if _manual_intervention_available_actions is not UNSET:
            manual_intervention_available_actions = []
            for manual_intervention_available_actions_item_data in _manual_intervention_available_actions:
                manual_intervention_available_actions_item = (
                    check_execution_node_manual_intervention_available_actions_item(
                        manual_intervention_available_actions_item_data
                    )
                )

                manual_intervention_available_actions.append(manual_intervention_available_actions_item)

        children_count = d.pop("childrenCount", UNSET)

        execution_node = cls(
            uuid=uuid,
            setup_id=setup_id,
            name=name,
            identifier=identifier,
            base_fqn=base_fqn,
            outcomes=outcomes,
            step_parameters=step_parameters,
            created_at=created_at,
            start_ts=start_ts,
            end_ts=end_ts,
            step_type=step_type,
            status=status,
            failure_info=failure_info,
            skip_info=skip_info,
            node_run_info=node_run_info,
            retry_node_metadata=retry_node_metadata,
            executable_responses=executable_responses,
            unit_progresses=unit_progresses,
            progress_data=progress_data,
            delegate_info_list=delegate_info_list,
            interrupt_histories=interrupt_histories,
            step_details=step_details,
            strategy_metadata=strategy_metadata,
            execution_input_configured=execution_input_configured,
            log_base_key=log_base_key,
            manual_intervention_available_actions=manual_intervention_available_actions,
            children_count=children_count,
        )

        execution_node.additional_properties = d
        return execution_node

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
