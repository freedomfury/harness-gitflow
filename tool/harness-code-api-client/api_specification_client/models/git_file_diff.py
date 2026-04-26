from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitFileDiff")


@_attrs_define
class GitFileDiff:
    """
    Attributes:
        additions (int | Unset):
        changes (int | Unset):
        deletions (int | Unset):
        is_binary (bool | Unset):
        is_submodule (bool | Unset):
        old_path (str | Unset):
        old_sha (str | Unset):
        patch (list[int] | Unset):
        path (str | Unset):
        sha (str | Unset):
        status (str | Unset):
    """

    additions: int | Unset = UNSET
    changes: int | Unset = UNSET
    deletions: int | Unset = UNSET
    is_binary: bool | Unset = UNSET
    is_submodule: bool | Unset = UNSET
    old_path: str | Unset = UNSET
    old_sha: str | Unset = UNSET
    patch: list[int] | Unset = UNSET
    path: str | Unset = UNSET
    sha: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additions = self.additions

        changes = self.changes

        deletions = self.deletions

        is_binary = self.is_binary

        is_submodule = self.is_submodule

        old_path = self.old_path

        old_sha = self.old_sha

        patch: list[int] | Unset = UNSET
        if not isinstance(self.patch, Unset):
            patch = self.patch

        path = self.path

        sha = self.sha

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additions is not UNSET:
            field_dict["additions"] = additions
        if changes is not UNSET:
            field_dict["changes"] = changes
        if deletions is not UNSET:
            field_dict["deletions"] = deletions
        if is_binary is not UNSET:
            field_dict["is_binary"] = is_binary
        if is_submodule is not UNSET:
            field_dict["is_submodule"] = is_submodule
        if old_path is not UNSET:
            field_dict["old_path"] = old_path
        if old_sha is not UNSET:
            field_dict["old_sha"] = old_sha
        if patch is not UNSET:
            field_dict["patch"] = patch
        if path is not UNSET:
            field_dict["path"] = path
        if sha is not UNSET:
            field_dict["sha"] = sha
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additions = d.pop("additions", UNSET)

        changes = d.pop("changes", UNSET)

        deletions = d.pop("deletions", UNSET)

        is_binary = d.pop("is_binary", UNSET)

        is_submodule = d.pop("is_submodule", UNSET)

        old_path = d.pop("old_path", UNSET)

        old_sha = d.pop("old_sha", UNSET)

        patch = cast(list[int], d.pop("patch", UNSET))

        path = d.pop("path", UNSET)

        sha = d.pop("sha", UNSET)

        status = d.pop("status", UNSET)

        git_file_diff = cls(
            additions=additions,
            changes=changes,
            deletions=deletions,
            is_binary=is_binary,
            is_submodule=is_submodule,
            old_path=old_path,
            old_sha=old_sha,
            patch=patch,
            path=path,
            sha=sha,
            status=status,
        )

        git_file_diff.additional_properties = d
        return git_file_diff

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
