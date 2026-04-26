from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepoMergeCheck")


@_attrs_define
class RepoMergeCheck:
    """
    Attributes:
        conflict_files (list[str] | Unset):
        mergeable (bool | Unset):
    """

    conflict_files: list[str] | Unset = UNSET
    mergeable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conflict_files: list[str] | Unset = UNSET
        if not isinstance(self.conflict_files, Unset):
            conflict_files = self.conflict_files

        mergeable = self.mergeable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conflict_files is not UNSET:
            field_dict["conflict_files"] = conflict_files
        if mergeable is not UNSET:
            field_dict["mergeable"] = mergeable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conflict_files = cast(list[str], d.pop("conflict_files", UNSET))

        mergeable = d.pop("mergeable", UNSET)

        repo_merge_check = cls(
            conflict_files=conflict_files,
            mergeable=mergeable,
        )

        repo_merge_check.additional_properties = d
        return repo_merge_check

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
