from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_graph_node_status import WorkflowGraphNodeStatus, check_workflow_graph_node_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_graph_node_inputs import WorkflowGraphNodeInputs
    from ..models.workflow_graph_node_outputs import WorkflowGraphNodeOutputs


T = TypeVar("T", bound="WorkflowGraphNode")


@_attrs_define
class WorkflowGraphNode:
    """
    Attributes:
        uuid (str | Unset):
        name (str | Unset):
        identifier (str | Unset):
        status (WorkflowGraphNodeStatus | Unset):
        inputs (WorkflowGraphNodeInputs | Unset):
        outputs (WorkflowGraphNodeOutputs | Unset):
    """

    uuid: str | Unset = UNSET
    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    status: WorkflowGraphNodeStatus | Unset = UNSET
    inputs: WorkflowGraphNodeInputs | Unset = UNSET
    outputs: WorkflowGraphNodeOutputs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

        identifier = self.identifier

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if status is not UNSET:
            field_dict["status"] = status
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if outputs is not UNSET:
            field_dict["outputs"] = outputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_graph_node_inputs import WorkflowGraphNodeInputs
        from ..models.workflow_graph_node_outputs import WorkflowGraphNodeOutputs

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        _status = d.pop("status", UNSET)
        status: WorkflowGraphNodeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_workflow_graph_node_status(_status)

        _inputs = d.pop("inputs", UNSET)
        inputs: WorkflowGraphNodeInputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = WorkflowGraphNodeInputs.from_dict(_inputs)

        _outputs = d.pop("outputs", UNSET)
        outputs: WorkflowGraphNodeOutputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = WorkflowGraphNodeOutputs.from_dict(_outputs)

        workflow_graph_node = cls(
            uuid=uuid,
            name=name,
            identifier=identifier,
            status=status,
            inputs=inputs,
            outputs=outputs,
        )

        workflow_graph_node.additional_properties = d
        return workflow_graph_node

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
