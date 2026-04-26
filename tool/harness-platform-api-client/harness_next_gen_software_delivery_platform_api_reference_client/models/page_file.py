from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File
    from ..models.pageable import Pageable
    from ..models.sort import Sort


T = TypeVar("T", bound="PageFile")


@_attrs_define
class PageFile:
    """
    Attributes:
        total_elements (int | Unset):
        total_pages (int | Unset):
        pageable (Pageable | Unset):
        last (bool | Unset):
        size (int | Unset):
        content (list[File] | Unset):
        number (int | Unset):
        sort (Sort | Unset):
        first (bool | Unset):
        number_of_elements (int | Unset):
        empty (bool | Unset):
    """

    total_elements: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    pageable: Pageable | Unset = UNSET
    last: bool | Unset = UNSET
    size: int | Unset = UNSET
    content: list[File] | Unset = UNSET
    number: int | Unset = UNSET
    sort: Sort | Unset = UNSET
    first: bool | Unset = UNSET
    number_of_elements: int | Unset = UNSET
    empty: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_elements = self.total_elements

        total_pages = self.total_pages

        pageable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pageable, Unset):
            pageable = self.pageable.to_dict()

        last = self.last

        size = self.size

        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        number = self.number

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        first = self.first

        number_of_elements = self.number_of_elements

        empty = self.empty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if pageable is not UNSET:
            field_dict["pageable"] = pageable
        if last is not UNSET:
            field_dict["last"] = last
        if size is not UNSET:
            field_dict["size"] = size
        if content is not UNSET:
            field_dict["content"] = content
        if number is not UNSET:
            field_dict["number"] = number
        if sort is not UNSET:
            field_dict["sort"] = sort
        if first is not UNSET:
            field_dict["first"] = first
        if number_of_elements is not UNSET:
            field_dict["numberOfElements"] = number_of_elements
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File
        from ..models.pageable import Pageable
        from ..models.sort import Sort

        d = dict(src_dict)
        total_elements = d.pop("totalElements", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        _pageable = d.pop("pageable", UNSET)
        pageable: Pageable | Unset
        if isinstance(_pageable, Unset):
            pageable = UNSET
        else:
            pageable = Pageable.from_dict(_pageable)

        last = d.pop("last", UNSET)

        size = d.pop("size", UNSET)

        _content = d.pop("content", UNSET)
        content: list[File] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = File.from_dict(content_item_data)

                content.append(content_item)

        number = d.pop("number", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: Sort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = Sort.from_dict(_sort)

        first = d.pop("first", UNSET)

        number_of_elements = d.pop("numberOfElements", UNSET)

        empty = d.pop("empty", UNSET)

        page_file = cls(
            total_elements=total_elements,
            total_pages=total_pages,
            pageable=pageable,
            last=last,
            size=size,
            content=content,
            number=number,
            sort=sort,
            first=first,
            number_of_elements=number_of_elements,
            empty=empty,
        )

        page_file.additional_properties = d
        return page_file

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
