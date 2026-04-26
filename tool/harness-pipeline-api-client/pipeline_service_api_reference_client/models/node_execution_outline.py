from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_execution_outline_status import NodeExecutionOutlineStatus, check_node_execution_outline_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edge_layout_list import EdgeLayoutList


T = TypeVar("T", bound="NodeExecutionOutline")


@_attrs_define
class NodeExecutionOutline:
    """This is the view of the Node Execution Outline

    Attributes:
        node_type (str | Unset):
        node_group (str | Unset):
        node_identifier (str | Unset):
        name (str | Unset):
        node_uuid (str | Unset):
        status (NodeExecutionOutlineStatus | Unset): Execution Status of the entity. Valid values (PascalCase): Running,
            AsyncWaiting, TaskWaiting, TimedWaiting, Failed, Errored, IgnoreFailed, NotStarted, Expired, Aborted,
            Discontinuing, Queued, Paused, ResourceWaiting, InterventionWaiting, ApprovalWaiting, WaitStepRunning,
            QueuedLicenseLimitReached, QueuedExecutionConcurrencyReached, Success, Suspended, Skipped, Pausing,
            ApprovalRejected, InputWaiting, AbortedByFreeze, UploadWaiting, QueuedGlobalInfraCapacityReached.
        start_ts (int | Unset):
        end_ts (int | Unset):
        failure_info (str | Unset):
        node_execution_id (str | Unset):
        edge_layout_list (EdgeLayoutList | Unset): This contains info about the Layout of the Graph
    """

    node_type: str | Unset = UNSET
    node_group: str | Unset = UNSET
    node_identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    node_uuid: str | Unset = UNSET
    status: NodeExecutionOutlineStatus | Unset = UNSET
    start_ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    failure_info: str | Unset = UNSET
    node_execution_id: str | Unset = UNSET
    edge_layout_list: EdgeLayoutList | Unset = UNSET
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

        start_ts = self.start_ts

        end_ts = self.end_ts

        failure_info = self.failure_info

        node_execution_id = self.node_execution_id

        edge_layout_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.edge_layout_list, Unset):
            edge_layout_list = self.edge_layout_list.to_dict()

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
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if failure_info is not UNSET:
            field_dict["failureInfo"] = failure_info
        if node_execution_id is not UNSET:
            field_dict["nodeExecutionId"] = node_execution_id
        if edge_layout_list is not UNSET:
            field_dict["edgeLayoutList"] = edge_layout_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edge_layout_list import EdgeLayoutList

        d = dict(src_dict)
        node_type = d.pop("nodeType", UNSET)

        node_group = d.pop("nodeGroup", UNSET)

        node_identifier = d.pop("nodeIdentifier", UNSET)

        name = d.pop("name", UNSET)

        node_uuid = d.pop("nodeUuid", UNSET)

        _status = d.pop("status", UNSET)
        status: NodeExecutionOutlineStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_node_execution_outline_status(_status)

        start_ts = d.pop("startTs", UNSET)

        end_ts = d.pop("endTs", UNSET)

        failure_info = d.pop("failureInfo", UNSET)

        node_execution_id = d.pop("nodeExecutionId", UNSET)

        _edge_layout_list = d.pop("edgeLayoutList", UNSET)
        edge_layout_list: EdgeLayoutList | Unset
        if isinstance(_edge_layout_list, Unset):
            edge_layout_list = UNSET
        else:
            edge_layout_list = EdgeLayoutList.from_dict(_edge_layout_list)

        node_execution_outline = cls(
            node_type=node_type,
            node_group=node_group,
            node_identifier=node_identifier,
            name=name,
            node_uuid=node_uuid,
            status=status,
            start_ts=start_ts,
            end_ts=end_ts,
            failure_info=failure_info,
            node_execution_id=node_execution_id,
            edge_layout_list=edge_layout_list,
        )

        node_execution_outline.additional_properties = d
        return node_execution_outline

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
