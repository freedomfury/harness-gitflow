from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesCommitFileStats")


@_attrs_define
class TypesCommitFileStats:
    """
    Attributes:
        changes (int | Unset):
        deletions (int | Unset):
        insertions (int | Unset):
        old_path (str | Unset):
        path (str | Unset):
        status (str | Unset):
    """

    changes: int | Unset = UNSET
    deletions: int | Unset = UNSET
    insertions: int | Unset = UNSET
    old_path: str | Unset = UNSET
    path: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes = self.changes

        deletions = self.deletions

        insertions = self.insertions

        old_path = self.old_path

        path = self.path

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changes is not UNSET:
            field_dict["changes"] = changes
        if deletions is not UNSET:
            field_dict["deletions"] = deletions
        if insertions is not UNSET:
            field_dict["insertions"] = insertions
        if old_path is not UNSET:
            field_dict["old_path"] = old_path
        if path is not UNSET:
            field_dict["path"] = path
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        changes = d.pop("changes", UNSET)

        deletions = d.pop("deletions", UNSET)

        insertions = d.pop("insertions", UNSET)

        old_path = d.pop("old_path", UNSET)

        path = d.pop("path", UNSET)

        status = d.pop("status", UNSET)

        types_commit_file_stats = cls(
            changes=changes,
            deletions=deletions,
            insertions=insertions,
            old_path=old_path,
            path=path,
            status=status,
        )

        types_commit_file_stats.additional_properties = d
        return types_commit_file_stats

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
