from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_sync_error import GitSyncError


T = TypeVar("T", bound="GitSyncErrorAggregateByCommit")


@_attrs_define
class GitSyncErrorAggregateByCommit:
    """This contains a list of Git Sync Error details for a given Commit Id

    Attributes:
        git_commit_id (str | Unset): Commit Id
        failed_count (int | Unset): The number of active errors in a commit
        repo_id (str | Unset): Git Sync Config Id. [Applicable for Old Git Sync only]
        branch_name (str | Unset): Name of the branch.
        commit_message (str | Unset): Commit Message to use for the merge commit.
        created_at (int | Unset): This is the time at which the Git Sync error was logged
        errors_for_summary_view (list[GitSyncError] | Unset): This has the list of Git Sync errors corresponding to a
            specific Commit Id
    """

    git_commit_id: str | Unset = UNSET
    failed_count: int | Unset = UNSET
    repo_id: str | Unset = UNSET
    branch_name: str | Unset = UNSET
    commit_message: str | Unset = UNSET
    created_at: int | Unset = UNSET
    errors_for_summary_view: list[GitSyncError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git_commit_id = self.git_commit_id

        failed_count = self.failed_count

        repo_id = self.repo_id

        branch_name = self.branch_name

        commit_message = self.commit_message

        created_at = self.created_at

        errors_for_summary_view: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors_for_summary_view, Unset):
            errors_for_summary_view = []
            for errors_for_summary_view_item_data in self.errors_for_summary_view:
                errors_for_summary_view_item = errors_for_summary_view_item_data.to_dict()
                errors_for_summary_view.append(errors_for_summary_view_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git_commit_id is not UNSET:
            field_dict["gitCommitId"] = git_commit_id
        if failed_count is not UNSET:
            field_dict["failedCount"] = failed_count
        if repo_id is not UNSET:
            field_dict["repoId"] = repo_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if errors_for_summary_view is not UNSET:
            field_dict["errorsForSummaryView"] = errors_for_summary_view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_sync_error import GitSyncError

        d = dict(src_dict)
        git_commit_id = d.pop("gitCommitId", UNSET)

        failed_count = d.pop("failedCount", UNSET)

        repo_id = d.pop("repoId", UNSET)

        branch_name = d.pop("branchName", UNSET)

        commit_message = d.pop("commitMessage", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _errors_for_summary_view = d.pop("errorsForSummaryView", UNSET)
        errors_for_summary_view: list[GitSyncError] | Unset = UNSET
        if _errors_for_summary_view is not UNSET:
            errors_for_summary_view = []
            for errors_for_summary_view_item_data in _errors_for_summary_view:
                errors_for_summary_view_item = GitSyncError.from_dict(errors_for_summary_view_item_data)

                errors_for_summary_view.append(errors_for_summary_view_item)

        git_sync_error_aggregate_by_commit = cls(
            git_commit_id=git_commit_id,
            failed_count=failed_count,
            repo_id=repo_id,
            branch_name=branch_name,
            commit_message=commit_message,
            created_at=created_at,
            errors_for_summary_view=errors_for_summary_view,
        )

        git_sync_error_aggregate_by_commit.additional_properties = d
        return git_sync_error_aggregate_by_commit

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
