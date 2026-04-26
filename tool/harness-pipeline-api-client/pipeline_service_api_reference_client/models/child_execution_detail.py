from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_graph import ExecutionGraph
    from ..models.pipeline_execution_summary import PipelineExecutionSummary


T = TypeVar("T", bound="ChildExecutionDetail")


@_attrs_define
class ChildExecutionDetail:
    """This contains the Pipeline Execution details of Child Pipeline

    Attributes:
        pipeline_execution_summary (PipelineExecutionSummary | Unset): This is the view of the Pipeline Execution
            Summary
        execution_graph (ExecutionGraph | Unset):
    """

    pipeline_execution_summary: PipelineExecutionSummary | Unset = UNSET
    execution_graph: ExecutionGraph | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pipeline_execution_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline_execution_summary, Unset):
            pipeline_execution_summary = self.pipeline_execution_summary.to_dict()

        execution_graph: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_graph, Unset):
            execution_graph = self.execution_graph.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_execution_summary is not UNSET:
            field_dict["pipelineExecutionSummary"] = pipeline_execution_summary
        if execution_graph is not UNSET:
            field_dict["executionGraph"] = execution_graph

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_graph import ExecutionGraph
        from ..models.pipeline_execution_summary import PipelineExecutionSummary

        d = dict(src_dict)
        _pipeline_execution_summary = d.pop("pipelineExecutionSummary", UNSET)
        pipeline_execution_summary: PipelineExecutionSummary | Unset
        if isinstance(_pipeline_execution_summary, Unset):
            pipeline_execution_summary = UNSET
        else:
            pipeline_execution_summary = PipelineExecutionSummary.from_dict(_pipeline_execution_summary)

        _execution_graph = d.pop("executionGraph", UNSET)
        execution_graph: ExecutionGraph | Unset
        if isinstance(_execution_graph, Unset):
            execution_graph = UNSET
        else:
            execution_graph = ExecutionGraph.from_dict(_execution_graph)

        child_execution_detail = cls(
            pipeline_execution_summary=pipeline_execution_summary,
            execution_graph=execution_graph,
        )

        child_execution_detail.additional_properties = d
        return child_execution_detail

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
