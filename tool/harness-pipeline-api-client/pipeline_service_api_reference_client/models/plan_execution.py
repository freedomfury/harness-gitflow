from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.plan_execution_node_type import PlanExecutionNodeType, check_plan_execution_node_type
from ..models.plan_execution_priority_type import PlanExecutionPriorityType, check_plan_execution_priority_type
from ..models.plan_execution_status import PlanExecutionStatus, check_plan_execution_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ambiance import Ambiance
    from ..models.execution_metadata import ExecutionMetadata
    from ..models.failure_info import FailureInfo
    from ..models.governance_metadata import GovernanceMetadata
    from ..models.header_config import HeaderConfig
    from ..models.plan_execution_setup_abstractions import PlanExecutionSetupAbstractions
    from ..models.plan_execution_stage_expression_values_map import PlanExecutionStageExpressionValuesMap
    from ..models.post_execution_rollback_info import PostExecutionRollbackInfo
    from ..models.stages_execution_metadata import StagesExecutionMetadata
    from ..models.trigger_payload import TriggerPayload


T = TypeVar("T", bound="PlanExecution")


@_attrs_define
class PlanExecution:
    """
    Attributes:
        uuid (str | Unset):
        created_at (int | Unset):
        plan_id (str | Unset):
        setup_abstractions (PlanExecutionSetupAbstractions | Unset):
        valid_until (datetime.datetime | Unset):
        status (PlanExecutionStatus | Unset):
        start_ts (int | Unset):
        end_ts (int | Unset):
        metadata (ExecutionMetadata | Unset):
        governance_metadata (GovernanceMetadata | Unset):
        trigger_header (list[HeaderConfig] | Unset):
        trigger_json_payload (str | Unset):
        expression_functor_token (int | Unset):
        trigger_payload (TriggerPayload | Unset):
        stage_expression_values_map (PlanExecutionStageExpressionValuesMap | Unset):
        stages_execution_metadata (StagesExecutionMetadata | Unset):
        processed_yaml (str | Unset):
        post_execution_rollback_infos (list[PostExecutionRollbackInfo] | Unset):
        last_updated_at (int | Unset):
        version (int | Unset):
        next_iteration (int | Unset):
        ambiance (Ambiance | Unset):
        failure_info (FailureInfo | Unset):
        priority_type (PlanExecutionPriorityType | Unset):
        node_type (PlanExecutionNodeType | Unset):
        node_id (str | Unset):
    """

    uuid: str | Unset = UNSET
    created_at: int | Unset = UNSET
    plan_id: str | Unset = UNSET
    setup_abstractions: PlanExecutionSetupAbstractions | Unset = UNSET
    valid_until: datetime.datetime | Unset = UNSET
    status: PlanExecutionStatus | Unset = UNSET
    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    metadata: ExecutionMetadata | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    trigger_header: list[HeaderConfig] | Unset = UNSET
    trigger_json_payload: str | Unset = UNSET
    expression_functor_token: int | Unset = UNSET
    trigger_payload: TriggerPayload | Unset = UNSET
    stage_expression_values_map: PlanExecutionStageExpressionValuesMap | Unset = UNSET
    stages_execution_metadata: StagesExecutionMetadata | Unset = UNSET
    processed_yaml: str | Unset = UNSET
    post_execution_rollback_infos: list[PostExecutionRollbackInfo] | Unset = UNSET
    last_updated_at: int | Unset = UNSET
    version: int | Unset = UNSET
    next_iteration: int | Unset = UNSET
    ambiance: Ambiance | Unset = UNSET
    failure_info: FailureInfo | Unset = UNSET
    priority_type: PlanExecutionPriorityType | Unset = UNSET
    node_type: PlanExecutionNodeType | Unset = UNSET
    node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        created_at = self.created_at

        plan_id = self.plan_id

        setup_abstractions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.setup_abstractions, Unset):
            setup_abstractions = self.setup_abstractions.to_dict()

        valid_until: str | Unset = UNSET
        if not isinstance(self.valid_until, Unset):
            valid_until = self.valid_until.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        start_ts = self.start_ts

        end_ts = self.end_ts

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        trigger_header: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.trigger_header, Unset):
            trigger_header = []
            for trigger_header_item_data in self.trigger_header:
                trigger_header_item = trigger_header_item_data.to_dict()
                trigger_header.append(trigger_header_item)

        trigger_json_payload = self.trigger_json_payload

        expression_functor_token = self.expression_functor_token

        trigger_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_payload, Unset):
            trigger_payload = self.trigger_payload.to_dict()

        stage_expression_values_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stage_expression_values_map, Unset):
            stage_expression_values_map = self.stage_expression_values_map.to_dict()

        stages_execution_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stages_execution_metadata, Unset):
            stages_execution_metadata = self.stages_execution_metadata.to_dict()

        processed_yaml = self.processed_yaml

        post_execution_rollback_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.post_execution_rollback_infos, Unset):
            post_execution_rollback_infos = []
            for post_execution_rollback_infos_item_data in self.post_execution_rollback_infos:
                post_execution_rollback_infos_item = post_execution_rollback_infos_item_data.to_dict()
                post_execution_rollback_infos.append(post_execution_rollback_infos_item)

        last_updated_at = self.last_updated_at

        version = self.version

        next_iteration = self.next_iteration

        ambiance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ambiance, Unset):
            ambiance = self.ambiance.to_dict()

        failure_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure_info, Unset):
            failure_info = self.failure_info.to_dict()

        priority_type: str | Unset = UNSET
        if not isinstance(self.priority_type, Unset):
            priority_type = self.priority_type

        node_type: str | Unset = UNSET
        if not isinstance(self.node_type, Unset):
            node_type = self.node_type

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if plan_id is not UNSET:
            field_dict["planId"] = plan_id
        if setup_abstractions is not UNSET:
            field_dict["setupAbstractions"] = setup_abstractions
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if status is not UNSET:
            field_dict["status"] = status
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata
        if trigger_header is not UNSET:
            field_dict["triggerHeader"] = trigger_header
        if trigger_json_payload is not UNSET:
            field_dict["triggerJsonPayload"] = trigger_json_payload
        if expression_functor_token is not UNSET:
            field_dict["expressionFunctorToken"] = expression_functor_token
        if trigger_payload is not UNSET:
            field_dict["triggerPayload"] = trigger_payload
        if stage_expression_values_map is not UNSET:
            field_dict["stageExpressionValuesMap"] = stage_expression_values_map
        if stages_execution_metadata is not UNSET:
            field_dict["stagesExecutionMetadata"] = stages_execution_metadata
        if processed_yaml is not UNSET:
            field_dict["processedYaml"] = processed_yaml
        if post_execution_rollback_infos is not UNSET:
            field_dict["postExecutionRollbackInfos"] = post_execution_rollback_infos
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if version is not UNSET:
            field_dict["version"] = version
        if next_iteration is not UNSET:
            field_dict["nextIteration"] = next_iteration
        if ambiance is not UNSET:
            field_dict["ambiance"] = ambiance
        if failure_info is not UNSET:
            field_dict["failureInfo"] = failure_info
        if priority_type is not UNSET:
            field_dict["priorityType"] = priority_type
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ambiance import Ambiance
        from ..models.execution_metadata import ExecutionMetadata
        from ..models.failure_info import FailureInfo
        from ..models.governance_metadata import GovernanceMetadata
        from ..models.header_config import HeaderConfig
        from ..models.plan_execution_setup_abstractions import PlanExecutionSetupAbstractions
        from ..models.plan_execution_stage_expression_values_map import PlanExecutionStageExpressionValuesMap
        from ..models.post_execution_rollback_info import PostExecutionRollbackInfo
        from ..models.stages_execution_metadata import StagesExecutionMetadata
        from ..models.trigger_payload import TriggerPayload

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        created_at = d.pop("createdAt", UNSET)

        plan_id = d.pop("planId", UNSET)

        _setup_abstractions = d.pop("setupAbstractions", UNSET)
        setup_abstractions: PlanExecutionSetupAbstractions | Unset
        if isinstance(_setup_abstractions, Unset):
            setup_abstractions = UNSET
        else:
            setup_abstractions = PlanExecutionSetupAbstractions.from_dict(_setup_abstractions)

        _valid_until = d.pop("validUntil", UNSET)
        valid_until: datetime.datetime | Unset
        if isinstance(_valid_until, Unset):
            valid_until = UNSET
        else:
            valid_until = isoparse(_valid_until)

        _status = d.pop("status", UNSET)
        status: PlanExecutionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_plan_execution_status(_status)

        start_ts = d.pop("startTs", UNSET)

        end_ts = d.pop("endTs", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ExecutionMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ExecutionMetadata.from_dict(_metadata)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        _trigger_header = d.pop("triggerHeader", UNSET)
        trigger_header: list[HeaderConfig] | Unset = UNSET
        if _trigger_header is not UNSET:
            trigger_header = []
            for trigger_header_item_data in _trigger_header:
                trigger_header_item = HeaderConfig.from_dict(trigger_header_item_data)

                trigger_header.append(trigger_header_item)

        trigger_json_payload = d.pop("triggerJsonPayload", UNSET)

        expression_functor_token = d.pop("expressionFunctorToken", UNSET)

        _trigger_payload = d.pop("triggerPayload", UNSET)
        trigger_payload: TriggerPayload | Unset
        if isinstance(_trigger_payload, Unset):
            trigger_payload = UNSET
        else:
            trigger_payload = TriggerPayload.from_dict(_trigger_payload)

        _stage_expression_values_map = d.pop("stageExpressionValuesMap", UNSET)
        stage_expression_values_map: PlanExecutionStageExpressionValuesMap | Unset
        if isinstance(_stage_expression_values_map, Unset):
            stage_expression_values_map = UNSET
        else:
            stage_expression_values_map = PlanExecutionStageExpressionValuesMap.from_dict(_stage_expression_values_map)

        _stages_execution_metadata = d.pop("stagesExecutionMetadata", UNSET)
        stages_execution_metadata: StagesExecutionMetadata | Unset
        if isinstance(_stages_execution_metadata, Unset):
            stages_execution_metadata = UNSET
        else:
            stages_execution_metadata = StagesExecutionMetadata.from_dict(_stages_execution_metadata)

        processed_yaml = d.pop("processedYaml", UNSET)

        _post_execution_rollback_infos = d.pop("postExecutionRollbackInfos", UNSET)
        post_execution_rollback_infos: list[PostExecutionRollbackInfo] | Unset = UNSET
        if _post_execution_rollback_infos is not UNSET:
            post_execution_rollback_infos = []
            for post_execution_rollback_infos_item_data in _post_execution_rollback_infos:
                post_execution_rollback_infos_item = PostExecutionRollbackInfo.from_dict(
                    post_execution_rollback_infos_item_data
                )

                post_execution_rollback_infos.append(post_execution_rollback_infos_item)

        last_updated_at = d.pop("lastUpdatedAt", UNSET)

        version = d.pop("version", UNSET)

        next_iteration = d.pop("nextIteration", UNSET)

        _ambiance = d.pop("ambiance", UNSET)
        ambiance: Ambiance | Unset
        if isinstance(_ambiance, Unset):
            ambiance = UNSET
        else:
            ambiance = Ambiance.from_dict(_ambiance)

        _failure_info = d.pop("failureInfo", UNSET)
        failure_info: FailureInfo | Unset
        if isinstance(_failure_info, Unset):
            failure_info = UNSET
        else:
            failure_info = FailureInfo.from_dict(_failure_info)

        _priority_type = d.pop("priorityType", UNSET)
        priority_type: PlanExecutionPriorityType | Unset
        if isinstance(_priority_type, Unset):
            priority_type = UNSET
        else:
            priority_type = check_plan_execution_priority_type(_priority_type)

        _node_type = d.pop("nodeType", UNSET)
        node_type: PlanExecutionNodeType | Unset
        if isinstance(_node_type, Unset):
            node_type = UNSET
        else:
            node_type = check_plan_execution_node_type(_node_type)

        node_id = d.pop("nodeId", UNSET)

        plan_execution = cls(
            uuid=uuid,
            created_at=created_at,
            plan_id=plan_id,
            setup_abstractions=setup_abstractions,
            valid_until=valid_until,
            status=status,
            start_ts=start_ts,
            end_ts=end_ts,
            metadata=metadata,
            governance_metadata=governance_metadata,
            trigger_header=trigger_header,
            trigger_json_payload=trigger_json_payload,
            expression_functor_token=expression_functor_token,
            trigger_payload=trigger_payload,
            stage_expression_values_map=stage_expression_values_map,
            stages_execution_metadata=stages_execution_metadata,
            processed_yaml=processed_yaml,
            post_execution_rollback_infos=post_execution_rollback_infos,
            last_updated_at=last_updated_at,
            version=version,
            next_iteration=next_iteration,
            ambiance=ambiance,
            failure_info=failure_info,
            priority_type=priority_type,
            node_type=node_type,
            node_id=node_id,
        )

        plan_execution.additional_properties = d
        return plan_execution

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
