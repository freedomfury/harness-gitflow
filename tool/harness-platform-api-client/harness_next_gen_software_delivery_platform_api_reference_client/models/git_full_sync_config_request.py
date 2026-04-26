from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitFullSyncConfigRequest")


@_attrs_define
class GitFullSyncConfigRequest:
    """Details required to trigger Git Full Sync.

    Attributes:
        branch (str): Name of the branch to which the entities will be pushed and from which pull request will be
            created.
        repo_identifier (str): Git Sync Config Id. [Applicable for Old Git Sync only]
        root_folder (str): Path of the root folder inside which the entities will be pushed.
        is_new_branch (bool | Unset):
        base_branch (str | Unset): Name of the branch from which new branch will be forked out.
        create_pull_request (bool | Unset): If true a pull request will be created from branch to target branch.Default:
            false.
        target_branch (str | Unset): Name of the branch to which pull request will be merged.
        pr_title (str | Unset): Title of the pull request.
        new_branch (bool | Unset):
    """

    branch: str
    repo_identifier: str
    root_folder: str
    is_new_branch: bool | Unset = UNSET
    base_branch: str | Unset = UNSET
    create_pull_request: bool | Unset = UNSET
    target_branch: str | Unset = UNSET
    pr_title: str | Unset = UNSET
    new_branch: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        repo_identifier = self.repo_identifier

        root_folder = self.root_folder

        is_new_branch = self.is_new_branch

        base_branch = self.base_branch

        create_pull_request = self.create_pull_request

        target_branch = self.target_branch

        pr_title = self.pr_title

        new_branch = self.new_branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branch": branch,
                "repoIdentifier": repo_identifier,
                "rootFolder": root_folder,
            }
        )
        if is_new_branch is not UNSET:
            field_dict["isNewBranch"] = is_new_branch
        if base_branch is not UNSET:
            field_dict["baseBranch"] = base_branch
        if create_pull_request is not UNSET:
            field_dict["createPullRequest"] = create_pull_request
        if target_branch is not UNSET:
            field_dict["targetBranch"] = target_branch
        if pr_title is not UNSET:
            field_dict["prTitle"] = pr_title
        if new_branch is not UNSET:
            field_dict["newBranch"] = new_branch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = d.pop("branch")

        repo_identifier = d.pop("repoIdentifier")

        root_folder = d.pop("rootFolder")

        is_new_branch = d.pop("isNewBranch", UNSET)

        base_branch = d.pop("baseBranch", UNSET)

        create_pull_request = d.pop("createPullRequest", UNSET)

        target_branch = d.pop("targetBranch", UNSET)

        pr_title = d.pop("prTitle", UNSET)

        new_branch = d.pop("newBranch", UNSET)

        git_full_sync_config_request = cls(
            branch=branch,
            repo_identifier=repo_identifier,
            root_folder=root_folder,
            is_new_branch=is_new_branch,
            base_branch=base_branch,
            create_pull_request=create_pull_request,
            target_branch=target_branch,
            pr_title=pr_title,
            new_branch=new_branch,
        )

        git_full_sync_config_request.additional_properties = d
        return git_full_sync_config_request

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
