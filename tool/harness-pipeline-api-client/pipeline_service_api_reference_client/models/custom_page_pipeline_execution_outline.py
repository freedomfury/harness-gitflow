from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_execution_outline import PipelineExecutionOutline


T = TypeVar("T", bound="CustomPagePipelineExecutionOutline")


@_attrs_define
class CustomPagePipelineExecutionOutline:
    """This is the custom page implementation

    Attributes:
        content (list[PipelineExecutionOutline] | Unset):
        current_size (int | Unset):
        last_seen_execution_id (str | Unset):
        last_seen_start_time (int | Unset):
        has_more (bool | Unset):
    """

    content: list[PipelineExecutionOutline] | Unset = UNSET
    current_size: int | Unset = UNSET
    last_seen_execution_id: str | Unset = UNSET
    last_seen_start_time: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        current_size = self.current_size

        last_seen_execution_id = self.last_seen_execution_id

        last_seen_start_time = self.last_seen_start_time

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if last_seen_execution_id is not UNSET:
            field_dict["lastSeenExecutionId"] = last_seen_execution_id
        if last_seen_start_time is not UNSET:
            field_dict["lastSeenStartTime"] = last_seen_start_time
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_execution_outline import PipelineExecutionOutline

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: list[PipelineExecutionOutline] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = PipelineExecutionOutline.from_dict(content_item_data)

                content.append(content_item)

        current_size = d.pop("currentSize", UNSET)

        last_seen_execution_id = d.pop("lastSeenExecutionId", UNSET)

        last_seen_start_time = d.pop("lastSeenStartTime", UNSET)

        has_more = d.pop("hasMore", UNSET)

        custom_page_pipeline_execution_outline = cls(
            content=content,
            current_size=current_size,
            last_seen_execution_id=last_seen_execution_id,
            last_seen_start_time=last_seen_start_time,
            has_more=has_more,
        )

        custom_page_pipeline_execution_outline.additional_properties = d
        return custom_page_pipeline_execution_outline

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
