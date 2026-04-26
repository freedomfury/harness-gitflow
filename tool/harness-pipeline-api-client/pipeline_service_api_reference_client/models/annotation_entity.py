from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnotationEntity")


@_attrs_define
class AnnotationEntity:
    """AnnotationEntity

    Attributes:
        context_id (str | Unset): Unique context identifier for the annotation
        mode (str | Unset): Operation mode: replace, append, or delete
        style (str | Unset): Visual style of the annotation
        priority (int | Unset): Priority level of the annotation
        summary (str | Unset): Summary content of the annotation
        timestamp (int | Unset): Timestamp when the annotation was created
        step_id (str | Unset): Step identifier associated with the annotation
    """

    context_id: str | Unset = UNSET
    mode: str | Unset = UNSET
    style: str | Unset = UNSET
    priority: int | Unset = UNSET
    summary: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    step_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        mode = self.mode

        style = self.style

        priority = self.priority

        summary = self.summary

        timestamp = self.timestamp

        step_id = self.step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_id is not UNSET:
            field_dict["contextId"] = context_id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if style is not UNSET:
            field_dict["style"] = style
        if priority is not UNSET:
            field_dict["priority"] = priority
        if summary is not UNSET:
            field_dict["summary"] = summary
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if step_id is not UNSET:
            field_dict["stepId"] = step_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_id = d.pop("contextId", UNSET)

        mode = d.pop("mode", UNSET)

        style = d.pop("style", UNSET)

        priority = d.pop("priority", UNSET)

        summary = d.pop("summary", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        step_id = d.pop("stepId", UNSET)

        annotation_entity = cls(
            context_id=context_id,
            mode=mode,
            style=style,
            priority=priority,
            summary=summary,
            timestamp=timestamp,
            step_id=step_id,
        )

        annotation_entity.additional_properties = d
        return annotation_entity

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
