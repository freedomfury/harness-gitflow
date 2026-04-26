from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_full_sync_entity_info_entity_type import (
    GitFullSyncEntityInfoEntityType,
    check_git_full_sync_entity_info_entity_type,
)
from ..models.git_full_sync_entity_info_sync_status import (
    GitFullSyncEntityInfoSyncStatus,
    check_git_full_sync_entity_info_sync_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitFullSyncEntityInfo")


@_attrs_define
class GitFullSyncEntityInfo:
    """This contains the details of a Git Full Sync Entity with its Sync status

    Attributes:
        account_identifier (str | Unset): Account Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        file_path (str | Unset): File Path of the Entity.
        entity_type (GitFullSyncEntityInfoEntityType | Unset): Entity Type.
        sync_status (GitFullSyncEntityInfoSyncStatus | Unset): Sync Status of the Entity that may be QUEUED, SUCCESS or
            FAILED.
        name (str | Unset): Name of the Entity.
        identifier (str | Unset): Identifier of the Entity.
        branch (str | Unset): Name of the branch.
        repo_name (str | Unset): Name of the repository.
        repo_url (str | Unset): URL of the repository.
        root_folder (str | Unset): Path to the root folder of the Entity. [Applicable for Old Git Sync only]
        retry_count (int | Unset): This is the number of full sync retry attempts.
        error_message (str | Unset): Contains the error details while syncing the entity to Git.
    """

    account_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    file_path: str | Unset = UNSET
    entity_type: GitFullSyncEntityInfoEntityType | Unset = UNSET
    sync_status: GitFullSyncEntityInfoSyncStatus | Unset = UNSET
    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    branch: str | Unset = UNSET
    repo_name: str | Unset = UNSET
    repo_url: str | Unset = UNSET
    root_folder: str | Unset = UNSET
    retry_count: int | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        file_path = self.file_path

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type

        sync_status: str | Unset = UNSET
        if not isinstance(self.sync_status, Unset):
            sync_status = self.sync_status

        name = self.name

        identifier = self.identifier

        branch = self.branch

        repo_name = self.repo_name

        repo_url = self.repo_url

        root_folder = self.root_folder

        retry_count = self.retry_count

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if file_path is not UNSET:
            field_dict["filePath"] = file_path
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if sync_status is not UNSET:
            field_dict["syncStatus"] = sync_status
        if name is not UNSET:
            field_dict["name"] = name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if branch is not UNSET:
            field_dict["branch"] = branch
        if repo_name is not UNSET:
            field_dict["repoName"] = repo_name
        if repo_url is not UNSET:
            field_dict["repoUrl"] = repo_url
        if root_folder is not UNSET:
            field_dict["rootFolder"] = root_folder
        if retry_count is not UNSET:
            field_dict["retryCount"] = retry_count
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        file_path = d.pop("filePath", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: GitFullSyncEntityInfoEntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = check_git_full_sync_entity_info_entity_type(_entity_type)

        _sync_status = d.pop("syncStatus", UNSET)
        sync_status: GitFullSyncEntityInfoSyncStatus | Unset
        if isinstance(_sync_status, Unset):
            sync_status = UNSET
        else:
            sync_status = check_git_full_sync_entity_info_sync_status(_sync_status)

        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        branch = d.pop("branch", UNSET)

        repo_name = d.pop("repoName", UNSET)

        repo_url = d.pop("repoUrl", UNSET)

        root_folder = d.pop("rootFolder", UNSET)

        retry_count = d.pop("retryCount", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        git_full_sync_entity_info = cls(
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            file_path=file_path,
            entity_type=entity_type,
            sync_status=sync_status,
            name=name,
            identifier=identifier,
            branch=branch,
            repo_name=repo_name,
            repo_url=repo_url,
            root_folder=root_folder,
            retry_count=retry_count,
            error_message=error_message,
        )

        git_full_sync_entity_info.additional_properties = d
        return git_full_sync_entity_info

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
