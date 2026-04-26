from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitSyncErrorCount")


@_attrs_define
class GitSyncErrorCount:
    """This is the total number of Git sync and connectivity errors

    Attributes:
        git_to_harness_error_count (int | Unset): This is the number of Git to Harness errors
        connectivity_error_count (int | Unset): This is the number of connectivity errors
    """

    git_to_harness_error_count: int | Unset = UNSET
    connectivity_error_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git_to_harness_error_count = self.git_to_harness_error_count

        connectivity_error_count = self.connectivity_error_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git_to_harness_error_count is not UNSET:
            field_dict["gitToHarnessErrorCount"] = git_to_harness_error_count
        if connectivity_error_count is not UNSET:
            field_dict["connectivityErrorCount"] = connectivity_error_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        git_to_harness_error_count = d.pop("gitToHarnessErrorCount", UNSET)

        connectivity_error_count = d.pop("connectivityErrorCount", UNSET)

        git_sync_error_count = cls(
            git_to_harness_error_count=git_to_harness_error_count,
            connectivity_error_count=connectivity_error_count,
        )

        git_sync_error_count.additional_properties = d
        return git_sync_error_count

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
