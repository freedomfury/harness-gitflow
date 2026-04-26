from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesChangeStats")


@_attrs_define
class TypesChangeStats:
    """
    Attributes:
        changes (int | Unset):
        deletions (int | Unset):
        insertions (int | Unset):
    """

    changes: int | Unset = UNSET
    deletions: int | Unset = UNSET
    insertions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes = self.changes

        deletions = self.deletions

        insertions = self.insertions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changes is not UNSET:
            field_dict["changes"] = changes
        if deletions is not UNSET:
            field_dict["deletions"] = deletions
        if insertions is not UNSET:
            field_dict["insertions"] = insertions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        changes = d.pop("changes", UNSET)

        deletions = d.pop("deletions", UNSET)

        insertions = d.pop("insertions", UNSET)

        types_change_stats = cls(
            changes=changes,
            deletions=deletions,
            insertions=insertions,
        )

        types_change_stats.additional_properties = d
        return types_change_stats

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
