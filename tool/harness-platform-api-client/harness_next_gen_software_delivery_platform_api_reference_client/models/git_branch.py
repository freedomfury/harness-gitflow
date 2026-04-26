from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_branch_branch_sync_status import GitBranchBranchSyncStatus, check_git_branch_branch_sync_status

T = TypeVar("T", bound="GitBranch")


@_attrs_define
class GitBranch:
    """This contains details of the Git branch

    Attributes:
        branch_name (str): Name of the branch.
        branch_sync_status (GitBranchBranchSyncStatus): Sync Status of the Branch
    """

    branch_name: str
    branch_sync_status: GitBranchBranchSyncStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch_name = self.branch_name

        branch_sync_status: str = self.branch_sync_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branchName": branch_name,
                "branchSyncStatus": branch_sync_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch_name = d.pop("branchName")

        branch_sync_status = check_git_branch_branch_sync_status(d.pop("branchSyncStatus"))

        git_branch = cls(
            branch_name=branch_name,
            branch_sync_status=branch_sync_status,
        )

        git_branch.additional_properties = d
        return git_branch

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
