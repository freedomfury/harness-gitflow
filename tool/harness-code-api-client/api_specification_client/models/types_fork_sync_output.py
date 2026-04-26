from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesForkSyncOutput")


@_attrs_define
class TypesForkSyncOutput:
    """
    Attributes:
        already_ancestor (bool | Unset):
        new_commit_sha (str | Unset): Git object hash
    """

    already_ancestor: bool | Unset = UNSET
    new_commit_sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        already_ancestor = self.already_ancestor

        new_commit_sha = self.new_commit_sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if already_ancestor is not UNSET:
            field_dict["already_ancestor"] = already_ancestor
        if new_commit_sha is not UNSET:
            field_dict["new_commit_sha"] = new_commit_sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        already_ancestor = d.pop("already_ancestor", UNSET)

        new_commit_sha = d.pop("new_commit_sha", UNSET)

        types_fork_sync_output = cls(
            already_ancestor=already_ancestor,
            new_commit_sha=new_commit_sha,
        )

        types_fork_sync_output.additional_properties = d
        return types_fork_sync_output

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
