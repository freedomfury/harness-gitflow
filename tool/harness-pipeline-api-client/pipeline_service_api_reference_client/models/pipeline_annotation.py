from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_annotation_style import PipelineAnnotationStyle, check_pipeline_annotation_style

T = TypeVar("T", bound="PipelineAnnotation")


@_attrs_define
class PipelineAnnotation:
    """
    Attributes:
        context_id (str):
        timestamp (int):
        style (PipelineAnnotationStyle):
        summary (str):
        priority (int):
    """

    context_id: str
    timestamp: int
    style: PipelineAnnotationStyle
    summary: str
    priority: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        timestamp = self.timestamp

        style: str = self.style

        summary = self.summary

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contextId": context_id,
                "timestamp": timestamp,
                "style": style,
                "summary": summary,
                "priority": priority,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_id = d.pop("contextId")

        timestamp = d.pop("timestamp")

        style = check_pipeline_annotation_style(d.pop("style"))

        summary = d.pop("summary")

        priority = d.pop("priority")

        pipeline_annotation = cls(
            context_id=context_id,
            timestamp=timestamp,
            style=style,
            summary=summary,
            priority=priority,
        )

        pipeline_annotation.additional_properties = d
        return pipeline_annotation

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
