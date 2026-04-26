from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitFullSyncConfig")


@_attrs_define
class GitFullSyncConfig:
    """This has config details specific to Git Full Sync with Harness.

    Attributes:
        account_identifier (str | Unset): Account Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        base_branch (str | Unset): Name of the branch from which the new branch will be forked out.
        branch (str | Unset): Name of the branch. Entities were pushed to this branch, and a pull request was made from
            it.
        pr_title (str | Unset): Title of the pull request.
        create_pull_request (bool | Unset): Determines if pull request was created.
        repo_identifier (str | Unset): Git Sync Config Id. [Applicable for Old Git Sync only]
        is_new_branch (bool | Unset):
        target_branch (str | Unset): Name of the target branch of the pull request.
        root_folder (str | Unset): Path of the root folder inside which entities were pushed.
        new_branch (bool | Unset):
    """

    account_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    base_branch: str | Unset = UNSET
    branch: str | Unset = UNSET
    pr_title: str | Unset = UNSET
    create_pull_request: bool | Unset = UNSET
    repo_identifier: str | Unset = UNSET
    is_new_branch: bool | Unset = UNSET
    target_branch: str | Unset = UNSET
    root_folder: str | Unset = UNSET
    new_branch: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        base_branch = self.base_branch

        branch = self.branch

        pr_title = self.pr_title

        create_pull_request = self.create_pull_request

        repo_identifier = self.repo_identifier

        is_new_branch = self.is_new_branch

        target_branch = self.target_branch

        root_folder = self.root_folder

        new_branch = self.new_branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if base_branch is not UNSET:
            field_dict["baseBranch"] = base_branch
        if branch is not UNSET:
            field_dict["branch"] = branch
        if pr_title is not UNSET:
            field_dict["prTitle"] = pr_title
        if create_pull_request is not UNSET:
            field_dict["createPullRequest"] = create_pull_request
        if repo_identifier is not UNSET:
            field_dict["repoIdentifier"] = repo_identifier
        if is_new_branch is not UNSET:
            field_dict["isNewBranch"] = is_new_branch
        if target_branch is not UNSET:
            field_dict["targetBranch"] = target_branch
        if root_folder is not UNSET:
            field_dict["rootFolder"] = root_folder
        if new_branch is not UNSET:
            field_dict["newBranch"] = new_branch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        base_branch = d.pop("baseBranch", UNSET)

        branch = d.pop("branch", UNSET)

        pr_title = d.pop("prTitle", UNSET)

        create_pull_request = d.pop("createPullRequest", UNSET)

        repo_identifier = d.pop("repoIdentifier", UNSET)

        is_new_branch = d.pop("isNewBranch", UNSET)

        target_branch = d.pop("targetBranch", UNSET)

        root_folder = d.pop("rootFolder", UNSET)

        new_branch = d.pop("newBranch", UNSET)

        git_full_sync_config = cls(
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            base_branch=base_branch,
            branch=branch,
            pr_title=pr_title,
            create_pull_request=create_pull_request,
            repo_identifier=repo_identifier,
            is_new_branch=is_new_branch,
            target_branch=target_branch,
            root_folder=root_folder,
            new_branch=new_branch,
        )

        git_full_sync_config.additional_properties = d
        return git_full_sync_config

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
