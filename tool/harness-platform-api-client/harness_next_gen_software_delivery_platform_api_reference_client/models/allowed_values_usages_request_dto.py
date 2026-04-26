from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AllowedValuesUsagesRequestDTO")


@_attrs_define
class AllowedValuesUsagesRequestDTO:
    """This is the request details for finding the Allowed values usages in the entities.

    Attributes:
        max_pages (int | Unset):
        page_size (int | Unset):
    """

    max_pages: int | Unset = UNSET
    page_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_pages = self.max_pages

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_pages is not UNSET:
            field_dict["maxPages"] = max_pages
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_pages = d.pop("maxPages", UNSET)

        page_size = d.pop("pageSize", UNSET)

        allowed_values_usages_request_dto = cls(
            max_pages=max_pages,
            page_size=page_size,
        )

        allowed_values_usages_request_dto.additional_properties = d
        return allowed_values_usages_request_dto

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
