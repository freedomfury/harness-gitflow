from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitBlamePartPrevious")


@_attrs_define
class GitBlamePartPrevious:
    """
    Attributes:
        commit_sha (str | Unset): Git object hash
        file_name (str | Unset):
    """

    commit_sha: str | Unset = UNSET
    file_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_sha = self.commit_sha

        file_name = self.file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_sha is not UNSET:
            field_dict["commit_sha"] = commit_sha
        if file_name is not UNSET:
            field_dict["file_name"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commit_sha = d.pop("commit_sha", UNSET)

        file_name = d.pop("file_name", UNSET)

        git_blame_part_previous = cls(
            commit_sha=commit_sha,
            file_name=file_name,
        )

        git_blame_part_previous.additional_properties = d
        return git_blame_part_previous

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
