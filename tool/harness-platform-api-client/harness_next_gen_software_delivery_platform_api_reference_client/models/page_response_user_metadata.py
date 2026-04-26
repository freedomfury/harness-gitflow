from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="PageResponseUserMetadata")


@_attrs_define
class PageResponseUserMetadata:
    """
    Attributes:
        total_pages (int | Unset):
        total_items (int | Unset):
        page_item_count (int | Unset):
        page_size (int | Unset):
        content (list[UserMetadata] | Unset):
        page_index (int | Unset):
        empty (bool | Unset):
        page_token (str | Unset):
    """

    total_pages: int | Unset = UNSET
    total_items: int | Unset = UNSET
    page_item_count: int | Unset = UNSET
    page_size: int | Unset = UNSET
    content: list[UserMetadata] | Unset = UNSET
    page_index: int | Unset = UNSET
    empty: bool | Unset = UNSET
    page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_pages = self.total_pages

        total_items = self.total_items

        page_item_count = self.page_item_count

        page_size = self.page_size

        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        page_index = self.page_index

        empty = self.empty

        page_token = self.page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items
        if page_item_count is not UNSET:
            field_dict["pageItemCount"] = page_item_count
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if content is not UNSET:
            field_dict["content"] = content
        if page_index is not UNSET:
            field_dict["pageIndex"] = page_index
        if empty is not UNSET:
            field_dict["empty"] = empty
        if page_token is not UNSET:
            field_dict["pageToken"] = page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        total_pages = d.pop("totalPages", UNSET)

        total_items = d.pop("totalItems", UNSET)

        page_item_count = d.pop("pageItemCount", UNSET)

        page_size = d.pop("pageSize", UNSET)

        _content = d.pop("content", UNSET)
        content: list[UserMetadata] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = UserMetadata.from_dict(content_item_data)

                content.append(content_item)

        page_index = d.pop("pageIndex", UNSET)

        empty = d.pop("empty", UNSET)

        page_token = d.pop("pageToken", UNSET)

        page_response_user_metadata = cls(
            total_pages=total_pages,
            total_items=total_items,
            page_item_count=page_item_count,
            page_size=page_size,
            content=content,
            page_index=page_index,
            empty=empty,
            page_token=page_token,
        )

        page_response_user_metadata.additional_properties = d
        return page_response_user_metadata

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
