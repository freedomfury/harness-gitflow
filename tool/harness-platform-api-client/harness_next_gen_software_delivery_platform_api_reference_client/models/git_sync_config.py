from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_sync_config_git_connector_type import (
    GitSyncConfigGitConnectorType,
    check_git_sync_config_git_connector_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_sync_folder_config import GitSyncFolderConfig


T = TypeVar("T", bound="GitSyncConfig")


@_attrs_define
class GitSyncConfig:
    """This contains details of Git Sync Config

    Attributes:
        identifier (str): Git Sync Config Id. [Applicable for Old Git Sync only]
        name (str): Name of the repository. Any leading/trailing spaces will be removed.
        git_connector_ref (str): Id of the Connector referenced in Git
        repo (str): URL of the repository. Any leading/trailing spaces will be removed.
        branch (str): Name of the branch. Any leading/trailing spaces will be removed.
        git_connector_type (GitSyncConfigGitConnectorType): Connector Type
        project_identifier (str | Unset): Project Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        git_sync_folder_config_dt_os (list[GitSyncFolderConfig] | Unset): List of all Root Folder Details
    """

    identifier: str
    name: str
    git_connector_ref: str
    repo: str
    branch: str
    git_connector_type: GitSyncConfigGitConnectorType
    project_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    git_sync_folder_config_dt_os: list[GitSyncFolderConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        git_connector_ref = self.git_connector_ref

        repo = self.repo

        branch = self.branch

        git_connector_type: str = self.git_connector_type

        project_identifier = self.project_identifier

        org_identifier = self.org_identifier

        git_sync_folder_config_dt_os: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.git_sync_folder_config_dt_os, Unset):
            git_sync_folder_config_dt_os = []
            for git_sync_folder_config_dt_os_item_data in self.git_sync_folder_config_dt_os:
                git_sync_folder_config_dt_os_item = git_sync_folder_config_dt_os_item_data.to_dict()
                git_sync_folder_config_dt_os.append(git_sync_folder_config_dt_os_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
                "gitConnectorRef": git_connector_ref,
                "repo": repo,
                "branch": branch,
                "gitConnectorType": git_connector_type,
            }
        )
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if git_sync_folder_config_dt_os is not UNSET:
            field_dict["gitSyncFolderConfigDTOs"] = git_sync_folder_config_dt_os

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_sync_folder_config import GitSyncFolderConfig

        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        git_connector_ref = d.pop("gitConnectorRef")

        repo = d.pop("repo")

        branch = d.pop("branch")

        git_connector_type = check_git_sync_config_git_connector_type(d.pop("gitConnectorType"))

        project_identifier = d.pop("projectIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        _git_sync_folder_config_dt_os = d.pop("gitSyncFolderConfigDTOs", UNSET)
        git_sync_folder_config_dt_os: list[GitSyncFolderConfig] | Unset = UNSET
        if _git_sync_folder_config_dt_os is not UNSET:
            git_sync_folder_config_dt_os = []
            for git_sync_folder_config_dt_os_item_data in _git_sync_folder_config_dt_os:
                git_sync_folder_config_dt_os_item = GitSyncFolderConfig.from_dict(
                    git_sync_folder_config_dt_os_item_data
                )

                git_sync_folder_config_dt_os.append(git_sync_folder_config_dt_os_item)

        git_sync_config = cls(
            identifier=identifier,
            name=name,
            git_connector_ref=git_connector_ref,
            repo=repo,
            branch=branch,
            git_connector_type=git_connector_type,
            project_identifier=project_identifier,
            org_identifier=org_identifier,
            git_sync_folder_config_dt_os=git_sync_folder_config_dt_os,
        )

        git_sync_config.additional_properties = d
        return git_sync_config

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
