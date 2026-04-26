from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.graph_layout_node_status import GraphLayoutNodeStatus, check_graph_layout_node_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edge_layout_list import EdgeLayoutList
    from ..models.execution_error_info import ExecutionErrorInfo
    from ..models.failure_info_dto import FailureInfoDTO
    from ..models.graph_layout_node_module_info import GraphLayoutNodeModuleInfo
    from ..models.graph_layout_node_step_details import GraphLayoutNodeStepDetails
    from ..models.node_run_info import NodeRunInfo
    from ..models.skip_info import SkipInfo
    from ..models.strategy_metadata import StrategyMetadata


T = TypeVar("T", bound="GraphLayoutNode")


@_attrs_define
class GraphLayoutNode:
    """This is the view of the Graph for execution of the Pipeline.

    Attributes:
        node_type (str | Unset):
        node_group (str | Unset):
        node_identifier (str | Unset):
        name (str | Unset):
        node_uuid (str | Unset):
        status (GraphLayoutNodeStatus | Unset): Execution Status of the entity. Valid values (PascalCase): Running,
            AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted,
            Discontinuing, Queued, Paused, ResourceWaiting, InterventionWaiting, ApprovalWaiting, WaitStepRunning,
            QueuedLicenseLimitReached, QueuedExecutionConcurrencyReached, Success, Suspended, Skipped, Pausing,
            ApprovalRejected, InputWaiting, AbortedByFreeze, UploadWaiting, QueuedGlobalInfraCapacityReached.
        module (str | Unset):
        module_info (GraphLayoutNodeModuleInfo | Unset):
        created_at (int | Unset):
        start_ts (int | Unset):
        end_ts (int | Unset):
        edge_layout_list (EdgeLayoutList | Unset): This contains info about the Layout of the Graph
        skip_info (SkipInfo | Unset):
        node_run_info (NodeRunInfo | Unset):
        barrier_found (bool | Unset):
        failure_info (ExecutionErrorInfo | Unset):
        failure_info_dto (FailureInfoDTO | Unset):
        step_details (GraphLayoutNodeStepDetails | Unset):
        hidden (bool | Unset):
        node_execution_id (str | Unset):
        strategy_metadata (StrategyMetadata | Unset):
        execution_input_configured (bool | Unset):
        is_rollback_stage_node (bool | Unset):
        is_manual_execution (bool | Unset):
        children_count (int | Unset):
    """

    node_type: str | Unset = UNSET
    node_group: str | Unset = UNSET
    node_identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    node_uuid: str | Unset = UNSET
    status: GraphLayoutNodeStatus | Unset = UNSET
    module: str | Unset = UNSET
    module_info: GraphLayoutNodeModuleInfo | Unset = UNSET
    created_at: int | Unset = UNSET
    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    edge_layout_list: EdgeLayoutList | Unset = UNSET
    skip_info: SkipInfo | Unset = UNSET
    node_run_info: NodeRunInfo | Unset = UNSET
    barrier_found: bool | Unset = UNSET
    failure_info: ExecutionErrorInfo | Unset = UNSET
    failure_info_dto: FailureInfoDTO | Unset = UNSET
    step_details: GraphLayoutNodeStepDetails | Unset = UNSET
    hidden: bool | Unset = UNSET
    node_execution_id: str | Unset = UNSET
    strategy_metadata: StrategyMetadata | Unset = UNSET
    execution_input_configured: bool | Unset = UNSET
    is_rollback_stage_node: bool | Unset = UNSET
    is_manual_execution: bool | Unset = UNSET
    children_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_type = self.node_type

        node_group = self.node_group

        node_identifier = self.node_identifier

        name = self.name

        node_uuid = self.node_uuid

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        module = self.module

        module_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module_info, Unset):
            module_info = self.module_info.to_dict()

        created_at = self.created_at

        start_ts = self.start_ts

        end_ts = self.end_ts

        edge_layout_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.edge_layout_list, Unset):
            edge_layout_list = self.edge_layout_list.to_dict()

        skip_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip_info, Unset):
            skip_info = self.skip_info.to_dict()

        node_run_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_run_info, Unset):
            node_run_info = self.node_run_info.to_dict()

        barrier_found = self.barrier_found

        failure_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure_info, Unset):
            failure_info = self.failure_info.to_dict()

        failure_info_dto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure_info_dto, Unset):
            failure_info_dto = self.failure_info_dto.to_dict()

        step_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.step_details, Unset):
            step_details = self.step_details.to_dict()

        hidden = self.hidden

        node_execution_id = self.node_execution_id

        strategy_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_metadata, Unset):
            strategy_metadata = self.strategy_metadata.to_dict()

        execution_input_configured = self.execution_input_configured

        is_rollback_stage_node = self.is_rollback_stage_node

        is_manual_execution = self.is_manual_execution

        children_count = self.children_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if node_group is not UNSET:
            field_dict["nodeGroup"] = node_group
        if node_identifier is not UNSET:
            field_dict["nodeIdentifier"] = node_identifier
        if name is not UNSET:
            field_dict["name"] = name
        if node_uuid is not UNSET:
            field_dict["nodeUuid"] = node_uuid
        if status is not UNSET:
            field_dict["status"] = status
        if module is not UNSET:
            field_dict["module"] = module
        if module_info is not UNSET:
            field_dict["moduleInfo"] = module_info
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if edge_layout_list is not UNSET:
            field_dict["edgeLayoutList"] = edge_layout_list
        if skip_info is not UNSET:
            field_dict["skipInfo"] = skip_info
        if node_run_info is not UNSET:
            field_dict["nodeRunInfo"] = node_run_info
        if barrier_found is not UNSET:
            field_dict["barrierFound"] = barrier_found
        if failure_info is not UNSET:
            field_dict["failureInfo"] = failure_info
        if failure_info_dto is not UNSET:
            field_dict["failureInfoDTO"] = failure_info_dto
        if step_details is not UNSET:
            field_dict["stepDetails"] = step_details
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if node_execution_id is not UNSET:
            field_dict["nodeExecutionId"] = node_execution_id
        if strategy_metadata is not UNSET:
            field_dict["strategyMetadata"] = strategy_metadata
        if execution_input_configured is not UNSET:
            field_dict["executionInputConfigured"] = execution_input_configured
        if is_rollback_stage_node is not UNSET:
            field_dict["isRollbackStageNode"] = is_rollback_stage_node
        if is_manual_execution is not UNSET:
            field_dict["isManualExecution"] = is_manual_execution
        if children_count is not UNSET:
            field_dict["childrenCount"] = children_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edge_layout_list import EdgeLayoutList
        from ..models.execution_error_info import ExecutionErrorInfo
        from ..models.failure_info_dto import FailureInfoDTO
        from ..models.graph_layout_node_module_info import GraphLayoutNodeModuleInfo
        from ..models.graph_layout_node_step_details import GraphLayoutNodeStepDetails
        from ..models.node_run_info import NodeRunInfo
        from ..models.skip_info import SkipInfo
        from ..models.strategy_metadata import StrategyMetadata

        d = dict(src_dict)
        node_type = d.pop("nodeType", UNSET)

        node_group = d.pop("nodeGroup", UNSET)

        node_identifier = d.pop("nodeIdentifier", UNSET)

        name = d.pop("name", UNSET)

        node_uuid = d.pop("nodeUuid", UNSET)

        _status = d.pop("status", UNSET)
        status: GraphLayoutNodeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_graph_layout_node_status(_status)

        module = d.pop("module", UNSET)

        _module_info = d.pop("moduleInfo", UNSET)
        module_info: GraphLayoutNodeModuleInfo | Unset
        if isinstance(_module_info, Unset):
            module_info = UNSET
        else:
            module_info = GraphLayoutNodeModuleInfo.from_dict(_module_info)

        created_at = d.pop("createdAt", UNSET)

        start_ts = d.pop("startTs", UNSET)

        end_ts = d.pop("endTs", UNSET)

        _edge_layout_list = d.pop("edgeLayoutList", UNSET)
        edge_layout_list: EdgeLayoutList | Unset
        if isinstance(_edge_layout_list, Unset):
            edge_layout_list = UNSET
        else:
            edge_layout_list = EdgeLayoutList.from_dict(_edge_layout_list)

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

        barrier_found = d.pop("barrierFound", UNSET)

        _failure_info = d.pop("failureInfo", UNSET)
        failure_info: ExecutionErrorInfo | Unset
        if isinstance(_failure_info, Unset):
            failure_info = UNSET
        else:
            failure_info = ExecutionErrorInfo.from_dict(_failure_info)

        _failure_info_dto = d.pop("failureInfoDTO", UNSET)
        failure_info_dto: FailureInfoDTO | Unset
        if isinstance(_failure_info_dto, Unset):
            failure_info_dto = UNSET
        else:
            failure_info_dto = FailureInfoDTO.from_dict(_failure_info_dto)

        _step_details = d.pop("stepDetails", UNSET)
        step_details: GraphLayoutNodeStepDetails | Unset
        if isinstance(_step_details, Unset):
            step_details = UNSET
        else:
            step_details = GraphLayoutNodeStepDetails.from_dict(_step_details)

        hidden = d.pop("hidden", UNSET)

        node_execution_id = d.pop("nodeExecutionId", UNSET)

        _strategy_metadata = d.pop("strategyMetadata", UNSET)
        strategy_metadata: StrategyMetadata | Unset
        if isinstance(_strategy_metadata, Unset):
            strategy_metadata = UNSET
        else:
            strategy_metadata = StrategyMetadata.from_dict(_strategy_metadata)

        execution_input_configured = d.pop("executionInputConfigured", UNSET)

        is_rollback_stage_node = d.pop("isRollbackStageNode", UNSET)

        is_manual_execution = d.pop("isManualExecution", UNSET)

        children_count = d.pop("childrenCount", UNSET)

        graph_layout_node = cls(
            node_type=node_type,
            node_group=node_group,
            node_identifier=node_identifier,
            name=name,
            node_uuid=node_uuid,
            status=status,
            module=module,
            module_info=module_info,
            created_at=created_at,
            start_ts=start_ts,
            end_ts=end_ts,
            edge_layout_list=edge_layout_list,
            skip_info=skip_info,
            node_run_info=node_run_info,
            barrier_found=barrier_found,
            failure_info=failure_info,
            failure_info_dto=failure_info_dto,
            step_details=step_details,
            hidden=hidden,
            node_execution_id=node_execution_id,
            strategy_metadata=strategy_metadata,
            execution_input_configured=execution_input_configured,
            is_rollback_stage_node=is_rollback_stage_node,
            is_manual_execution=is_manual_execution,
            children_count=children_count,
        )

        graph_layout_node.additional_properties = d
        return graph_layout_node

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
