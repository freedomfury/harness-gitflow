from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesDiffStats")


@_attrs_define
class TypesDiffStats:
    """
    Attributes:
        additions (int | None | Unset):
        commits (int | None | Unset):
        deletions (int | None | Unset):
        files_changed (int | None | Unset):
    """

    additions: int | None | Unset = UNSET
    commits: int | None | Unset = UNSET
    deletions: int | None | Unset = UNSET
    files_changed: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additions: int | None | Unset
        if isinstance(self.additions, Unset):
            additions = UNSET
        else:
            additions = self.additions

        commits: int | None | Unset
        if isinstance(self.commits, Unset):
            commits = UNSET
        else:
            commits = self.commits

        deletions: int | None | Unset
        if isinstance(self.deletions, Unset):
            deletions = UNSET
        else:
            deletions = self.deletions

        files_changed: int | None | Unset
        if isinstance(self.files_changed, Unset):
            files_changed = UNSET
        else:
            files_changed = self.files_changed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additions is not UNSET:
            field_dict["additions"] = additions
        if commits is not UNSET:
            field_dict["commits"] = commits
        if deletions is not UNSET:
            field_dict["deletions"] = deletions
        if files_changed is not UNSET:
            field_dict["files_changed"] = files_changed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_additions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        additions = _parse_additions(d.pop("additions", UNSET))

        def _parse_commits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        commits = _parse_commits(d.pop("commits", UNSET))

        def _parse_deletions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deletions = _parse_deletions(d.pop("deletions", UNSET))

        def _parse_files_changed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        files_changed = _parse_files_changed(d.pop("files_changed", UNSET))

        types_diff_stats = cls(
            additions=additions,
            commits=commits,
            deletions=deletions,
            files_changed=files_changed,
        )

        types_diff_stats.additional_properties = d
        return types_diff_stats

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
