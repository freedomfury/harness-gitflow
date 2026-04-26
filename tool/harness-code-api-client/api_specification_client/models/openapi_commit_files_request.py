from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_identity_type_0 import GitIdentityType0
    from ..models.repo_commit_file_action import RepoCommitFileAction


T = TypeVar("T", bound="OpenapiCommitFilesRequest")


@_attrs_define
class OpenapiCommitFilesRequest:
    """
    Attributes:
        actions (list[RepoCommitFileAction] | None | Unset):
        author (GitIdentityType0 | None | Unset):
        branch (str | Unset):
        bypass_rules (bool | Unset):
        dry_run_rules (bool | Unset):
        message (str | Unset):
        new_branch (str | Unset):
        title (str | Unset):
    """

    actions: list[RepoCommitFileAction] | None | Unset = UNSET
    author: GitIdentityType0 | None | Unset = UNSET
    branch: str | Unset = UNSET
    bypass_rules: bool | Unset = UNSET
    dry_run_rules: bool | Unset = UNSET
    message: str | Unset = UNSET
    new_branch: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.git_identity_type_0 import GitIdentityType0

        actions: list[dict[str, Any]] | None | Unset
        if isinstance(self.actions, Unset):
            actions = UNSET
        elif isinstance(self.actions, list):
            actions = []
            for actions_type_0_item_data in self.actions:
                actions_type_0_item = actions_type_0_item_data.to_dict()
                actions.append(actions_type_0_item)

        else:
            actions = self.actions

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, GitIdentityType0):
            author = self.author.to_dict()
        else:
            author = self.author

        branch = self.branch

        bypass_rules = self.bypass_rules

        dry_run_rules = self.dry_run_rules

        message = self.message

        new_branch = self.new_branch

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if author is not UNSET:
            field_dict["author"] = author
        if branch is not UNSET:
            field_dict["branch"] = branch
        if bypass_rules is not UNSET:
            field_dict["bypass_rules"] = bypass_rules
        if dry_run_rules is not UNSET:
            field_dict["dry_run_rules"] = dry_run_rules
        if message is not UNSET:
            field_dict["message"] = message
        if new_branch is not UNSET:
            field_dict["new_branch"] = new_branch
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_identity_type_0 import GitIdentityType0
        from ..models.repo_commit_file_action import RepoCommitFileAction

        d = dict(src_dict)

        def _parse_actions(data: object) -> list[RepoCommitFileAction] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                actions_type_0 = []
                _actions_type_0 = data
                for actions_type_0_item_data in _actions_type_0:
                    actions_type_0_item = RepoCommitFileAction.from_dict(actions_type_0_item_data)

                    actions_type_0.append(actions_type_0_item)

                return actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RepoCommitFileAction] | None | Unset, data)

        actions = _parse_actions(d.pop("actions", UNSET))

        def _parse_author(data: object) -> GitIdentityType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_git_identity_type_0 = GitIdentityType0.from_dict(data)

                return componentsschemas_git_identity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GitIdentityType0 | None | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        branch = d.pop("branch", UNSET)

        bypass_rules = d.pop("bypass_rules", UNSET)

        dry_run_rules = d.pop("dry_run_rules", UNSET)

        message = d.pop("message", UNSET)

        new_branch = d.pop("new_branch", UNSET)

        title = d.pop("title", UNSET)

        openapi_commit_files_request = cls(
            actions=actions,
            author=author,
            branch=branch,
            bypass_rules=bypass_rules,
            dry_run_rules=dry_run_rules,
            message=message,
            new_branch=new_branch,
            title=title,
        )

        openapi_commit_files_request.additional_properties = d
        return openapi_commit_files_request

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
