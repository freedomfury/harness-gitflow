from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesRepositoryPullReqSummary")


@_attrs_define
class TypesRepositoryPullReqSummary:
    """
    Attributes:
        closed_count (int | Unset):
        merged_count (int | Unset):
        open_count (int | Unset):
    """

    closed_count: int | Unset = UNSET
    merged_count: int | Unset = UNSET
    open_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        closed_count = self.closed_count

        merged_count = self.merged_count

        open_count = self.open_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closed_count is not UNSET:
            field_dict["closed_count"] = closed_count
        if merged_count is not UNSET:
            field_dict["merged_count"] = merged_count
        if open_count is not UNSET:
            field_dict["open_count"] = open_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        closed_count = d.pop("closed_count", UNSET)

        merged_count = d.pop("merged_count", UNSET)

        open_count = d.pop("open_count", UNSET)

        types_repository_pull_req_summary = cls(
            closed_count=closed_count,
            merged_count=merged_count,
            open_count=open_count,
        )

        types_repository_pull_req_summary.additional_properties = d
        return types_repository_pull_req_summary

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
