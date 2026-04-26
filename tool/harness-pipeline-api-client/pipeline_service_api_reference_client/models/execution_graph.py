from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_graph_representation_strategy import (
    ExecutionGraphRepresentationStrategy,
    check_execution_graph_representation_strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_graph_execution_metadata import ExecutionGraphExecutionMetadata
    from ..models.execution_graph_node_adjacency_list_map import ExecutionGraphNodeAdjacencyListMap
    from ..models.execution_graph_node_map import ExecutionGraphNodeMap


T = TypeVar("T", bound="ExecutionGraph")


@_attrs_define
class ExecutionGraph:
    """
    Attributes:
        root_node_id (str | Unset):
        node_map (ExecutionGraphNodeMap | Unset):
        node_adjacency_list_map (ExecutionGraphNodeAdjacencyListMap | Unset):
        execution_metadata (ExecutionGraphExecutionMetadata | Unset):
        representation_strategy (ExecutionGraphRepresentationStrategy | Unset):
    """

    root_node_id: str | Unset = UNSET
    node_map: ExecutionGraphNodeMap | Unset = UNSET
    node_adjacency_list_map: ExecutionGraphNodeAdjacencyListMap | Unset = UNSET
    execution_metadata: ExecutionGraphExecutionMetadata | Unset = UNSET
    representation_strategy: ExecutionGraphRepresentationStrategy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        root_node_id = self.root_node_id

        node_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_map, Unset):
            node_map = self.node_map.to_dict()

        node_adjacency_list_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_adjacency_list_map, Unset):
            node_adjacency_list_map = self.node_adjacency_list_map.to_dict()

        execution_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_metadata, Unset):
            execution_metadata = self.execution_metadata.to_dict()

        representation_strategy: str | Unset = UNSET
        if not isinstance(self.representation_strategy, Unset):
            representation_strategy = self.representation_strategy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if root_node_id is not UNSET:
            field_dict["rootNodeId"] = root_node_id
        if node_map is not UNSET:
            field_dict["nodeMap"] = node_map
        if node_adjacency_list_map is not UNSET:
            field_dict["nodeAdjacencyListMap"] = node_adjacency_list_map
        if execution_metadata is not UNSET:
            field_dict["executionMetadata"] = execution_metadata
        if representation_strategy is not UNSET:
            field_dict["representationStrategy"] = representation_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_graph_execution_metadata import ExecutionGraphExecutionMetadata
        from ..models.execution_graph_node_adjacency_list_map import ExecutionGraphNodeAdjacencyListMap
        from ..models.execution_graph_node_map import ExecutionGraphNodeMap

        d = dict(src_dict)
        root_node_id = d.pop("rootNodeId", UNSET)

        _node_map = d.pop("nodeMap", UNSET)
        node_map: ExecutionGraphNodeMap | Unset
        if isinstance(_node_map, Unset):
            node_map = UNSET
        else:
            node_map = ExecutionGraphNodeMap.from_dict(_node_map)

        _node_adjacency_list_map = d.pop("nodeAdjacencyListMap", UNSET)
        node_adjacency_list_map: ExecutionGraphNodeAdjacencyListMap | Unset
        if isinstance(_node_adjacency_list_map, Unset):
            node_adjacency_list_map = UNSET
        else:
            node_adjacency_list_map = ExecutionGraphNodeAdjacencyListMap.from_dict(_node_adjacency_list_map)

        _execution_metadata = d.pop("executionMetadata", UNSET)
        execution_metadata: ExecutionGraphExecutionMetadata | Unset
        if isinstance(_execution_metadata, Unset):
            execution_metadata = UNSET
        else:
            execution_metadata = ExecutionGraphExecutionMetadata.from_dict(_execution_metadata)

        _representation_strategy = d.pop("representationStrategy", UNSET)
        representation_strategy: ExecutionGraphRepresentationStrategy | Unset
        if isinstance(_representation_strategy, Unset):
            representation_strategy = UNSET
        else:
            representation_strategy = check_execution_graph_representation_strategy(_representation_strategy)

        execution_graph = cls(
            root_node_id=root_node_id,
            node_map=node_map,
            node_adjacency_list_map=node_adjacency_list_map,
            execution_metadata=execution_metadata,
            representation_strategy=representation_strategy,
        )

        execution_graph.additional_properties = d
        return execution_graph

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
