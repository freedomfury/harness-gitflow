from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesRenameDetails")


@_attrs_define
class TypesRenameDetails:
    """
    Attributes:
        commit_sha_after (str | Unset):
        commit_sha_before (str | Unset):
        new_path (str | Unset):
        old_path (str | Unset):
    """

    commit_sha_after: str | Unset = UNSET
    commit_sha_before: str | Unset = UNSET
    new_path: str | Unset = UNSET
    old_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_sha_after = self.commit_sha_after

        commit_sha_before = self.commit_sha_before

        new_path = self.new_path

        old_path = self.old_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_sha_after is not UNSET:
            field_dict["commit_sha_after"] = commit_sha_after
        if commit_sha_before is not UNSET:
            field_dict["commit_sha_before"] = commit_sha_before
        if new_path is not UNSET:
            field_dict["new_path"] = new_path
        if old_path is not UNSET:
            field_dict["old_path"] = old_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commit_sha_after = d.pop("commit_sha_after", UNSET)

        commit_sha_before = d.pop("commit_sha_before", UNSET)

        new_path = d.pop("new_path", UNSET)

        old_path = d.pop("old_path", UNSET)

        types_rename_details = cls(
            commit_sha_after=commit_sha_after,
            commit_sha_before=commit_sha_before,
            new_path=new_path,
            old_path=old_path,
        )

        types_rename_details.additional_properties = d
        return types_rename_details

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
