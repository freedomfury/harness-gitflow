from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_sync_error_change_type import GitSyncErrorChangeType, check_git_sync_error_change_type
from ..models.git_sync_error_entity_type import GitSyncErrorEntityType, check_git_sync_error_entity_type
from ..models.git_sync_error_error_type import GitSyncErrorErrorType, check_git_sync_error_error_type
from ..models.git_sync_error_status import GitSyncErrorStatus, check_git_sync_error_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_sync_error_details import GitSyncErrorDetails
    from ..models.scope import Scope


T = TypeVar("T", bound="GitSyncError")


@_attrs_define
class GitSyncError:
    """This contains Git Sync Error Details

    Attributes:
        account_identifier (str | Unset): Account Identifier for the Entity.
        repo_url (str | Unset): URL of the repository.
        repo_id (str | Unset): Git Sync Config Id. [Applicable for Old Git Sync only]
        branch_name (str | Unset): Name of the branch.
        scopes (list[Scope] | Unset): List of scope of the Git Sync Error
        change_type (GitSyncErrorChangeType | Unset): Type of operation done in file
        complete_file_path (str | Unset): Complete File Path of the Entity
        entity_type (GitSyncErrorEntityType | Unset): Entity Type.
        failure_reason (str | Unset): Error Message
        status (GitSyncErrorStatus | Unset): Status of Git Sync Error
        error_type (GitSyncErrorErrorType | Unset): Type of Git Sync Error
        additional_error_details (GitSyncErrorDetails | Unset): This contains Git Sync error details specific to Error
            Type
        created_at (int | Unset): Time at which the Git Sync error was logged
    """

    account_identifier: str | Unset = UNSET
    repo_url: str | Unset = UNSET
    repo_id: str | Unset = UNSET
    branch_name: str | Unset = UNSET
    scopes: list[Scope] | Unset = UNSET
    change_type: GitSyncErrorChangeType | Unset = UNSET
    complete_file_path: str | Unset = UNSET
    entity_type: GitSyncErrorEntityType | Unset = UNSET
    failure_reason: str | Unset = UNSET
    status: GitSyncErrorStatus | Unset = UNSET
    error_type: GitSyncErrorErrorType | Unset = UNSET
    additional_error_details: GitSyncErrorDetails | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        repo_url = self.repo_url

        repo_id = self.repo_id

        branch_name = self.branch_name

        scopes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()
                scopes.append(scopes_item)

        change_type: str | Unset = UNSET
        if not isinstance(self.change_type, Unset):
            change_type = self.change_type

        complete_file_path = self.complete_file_path

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type

        failure_reason = self.failure_reason

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        error_type: str | Unset = UNSET
        if not isinstance(self.error_type, Unset):
            error_type = self.error_type

        additional_error_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_error_details, Unset):
            additional_error_details = self.additional_error_details.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if repo_url is not UNSET:
            field_dict["repoUrl"] = repo_url
        if repo_id is not UNSET:
            field_dict["repoId"] = repo_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if change_type is not UNSET:
            field_dict["changeType"] = change_type
        if complete_file_path is not UNSET:
            field_dict["completeFilePath"] = complete_file_path
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if status is not UNSET:
            field_dict["status"] = status
        if error_type is not UNSET:
            field_dict["errorType"] = error_type
        if additional_error_details is not UNSET:
            field_dict["additionalErrorDetails"] = additional_error_details
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_sync_error_details import GitSyncErrorDetails
        from ..models.scope import Scope

        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier", UNSET)

        repo_url = d.pop("repoUrl", UNSET)

        repo_id = d.pop("repoId", UNSET)

        branch_name = d.pop("branchName", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[Scope] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = Scope.from_dict(scopes_item_data)

                scopes.append(scopes_item)

        _change_type = d.pop("changeType", UNSET)
        change_type: GitSyncErrorChangeType | Unset
        if isinstance(_change_type, Unset):
            change_type = UNSET
        else:
            change_type = check_git_sync_error_change_type(_change_type)

        complete_file_path = d.pop("completeFilePath", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: GitSyncErrorEntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = check_git_sync_error_entity_type(_entity_type)

        failure_reason = d.pop("failureReason", UNSET)

        _status = d.pop("status", UNSET)
        status: GitSyncErrorStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_git_sync_error_status(_status)

        _error_type = d.pop("errorType", UNSET)
        error_type: GitSyncErrorErrorType | Unset
        if isinstance(_error_type, Unset):
            error_type = UNSET
        else:
            error_type = check_git_sync_error_error_type(_error_type)

        _additional_error_details = d.pop("additionalErrorDetails", UNSET)
        additional_error_details: GitSyncErrorDetails | Unset
        if isinstance(_additional_error_details, Unset):
            additional_error_details = UNSET
        else:
            additional_error_details = GitSyncErrorDetails.from_dict(_additional_error_details)

        created_at = d.pop("createdAt", UNSET)

        git_sync_error = cls(
            account_identifier=account_identifier,
            repo_url=repo_url,
            repo_id=repo_id,
            branch_name=branch_name,
            scopes=scopes,
            change_type=change_type,
            complete_file_path=complete_file_path,
            entity_type=entity_type,
            failure_reason=failure_reason,
            status=status,
            error_type=error_type,
            additional_error_details=additional_error_details,
            created_at=created_at,
        )

        git_sync_error.additional_properties = d
        return git_sync_error

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
