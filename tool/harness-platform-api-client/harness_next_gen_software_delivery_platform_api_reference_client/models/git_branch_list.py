from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_branch import GitBranch
    from ..models.page_response_git_branch import PageResponseGitBranch


T = TypeVar("T", bound="GitBranchList")


@_attrs_define
class GitBranchList:
    """This contains details of the default and other branch

    Attributes:
        default_branch (GitBranch | Unset): This contains details of the Git branch
        branches (PageResponseGitBranch | Unset): This contains details of all the branches of given repo
    """

    default_branch: GitBranch | Unset = UNSET
    branches: PageResponseGitBranch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_branch, Unset):
            default_branch = self.default_branch.to_dict()

        branches: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branches, Unset):
            branches = self.branches.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_branch is not UNSET:
            field_dict["defaultBranch"] = default_branch
        if branches is not UNSET:
            field_dict["branches"] = branches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_branch import GitBranch
        from ..models.page_response_git_branch import PageResponseGitBranch

        d = dict(src_dict)
        _default_branch = d.pop("defaultBranch", UNSET)
        default_branch: GitBranch | Unset
        if isinstance(_default_branch, Unset):
            default_branch = UNSET
        else:
            default_branch = GitBranch.from_dict(_default_branch)

        _branches = d.pop("branches", UNSET)
        branches: PageResponseGitBranch | Unset
        if isinstance(_branches, Unset):
            branches = UNSET
        else:
            branches = PageResponseGitBranch.from_dict(_branches)

        git_branch_list = cls(
            default_branch=default_branch,
            branches=branches,
        )

        git_branch_list.additional_properties = d
        return git_branch_list

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
