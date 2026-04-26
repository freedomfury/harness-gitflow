from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForkSyncBranchBody")


@_attrs_define
class ForkSyncBranchBody:
    """
    Attributes:
        branch (str | Unset):
        branch_commit_sha (str | Unset): Git object hash
        branch_upstream (str | Unset):
    """

    branch: str | Unset = UNSET
    branch_commit_sha: str | Unset = UNSET
    branch_upstream: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        branch_commit_sha = self.branch_commit_sha

        branch_upstream = self.branch_upstream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["branch"] = branch
        if branch_commit_sha is not UNSET:
            field_dict["branch_commit_sha"] = branch_commit_sha
        if branch_upstream is not UNSET:
            field_dict["branch_upstream"] = branch_upstream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = d.pop("branch", UNSET)

        branch_commit_sha = d.pop("branch_commit_sha", UNSET)

        branch_upstream = d.pop("branch_upstream", UNSET)

        fork_sync_branch_body = cls(
            branch=branch,
            branch_commit_sha=branch_commit_sha,
            branch_upstream=branch_upstream,
        )

        fork_sync_branch_body.additional_properties = d
        return fork_sync_branch_body

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
