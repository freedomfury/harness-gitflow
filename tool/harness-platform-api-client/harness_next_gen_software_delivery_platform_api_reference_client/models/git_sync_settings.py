from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitSyncSettings")


@_attrs_define
class GitSyncSettings:
    """This contains details of Git Sync Settings

    Attributes:
        project_identifier (str): Project Identifier for the Entity.
        org_identifier (str): Organization Identifier for the Entity.
        execute_on_delegate (bool): Specifies Connectivity Mode for Git Sync. If True, executes through Delegate, else
            executes through Platform. The default value is True
        is_git_simplification_enabled (bool | Unset):
        is_enabled_only_for_ff (bool | Unset):
        git_simplification_enabled (bool | Unset):
        enabled_only_for_ff (bool | Unset):
    """

    project_identifier: str
    org_identifier: str
    execute_on_delegate: bool
    is_git_simplification_enabled: bool | Unset = UNSET
    is_enabled_only_for_ff: bool | Unset = UNSET
    git_simplification_enabled: bool | Unset = UNSET
    enabled_only_for_ff: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_identifier = self.project_identifier

        org_identifier = self.org_identifier

        execute_on_delegate = self.execute_on_delegate

        is_git_simplification_enabled = self.is_git_simplification_enabled

        is_enabled_only_for_ff = self.is_enabled_only_for_ff

        git_simplification_enabled = self.git_simplification_enabled

        enabled_only_for_ff = self.enabled_only_for_ff

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectIdentifier": project_identifier,
                "orgIdentifier": org_identifier,
                "executeOnDelegate": execute_on_delegate,
            }
        )
        if is_git_simplification_enabled is not UNSET:
            field_dict["isGitSimplificationEnabled"] = is_git_simplification_enabled
        if is_enabled_only_for_ff is not UNSET:
            field_dict["isEnabledOnlyForFF"] = is_enabled_only_for_ff
        if git_simplification_enabled is not UNSET:
            field_dict["gitSimplificationEnabled"] = git_simplification_enabled
        if enabled_only_for_ff is not UNSET:
            field_dict["enabledOnlyForFF"] = enabled_only_for_ff

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_identifier = d.pop("projectIdentifier")

        org_identifier = d.pop("orgIdentifier")

        execute_on_delegate = d.pop("executeOnDelegate")

        is_git_simplification_enabled = d.pop("isGitSimplificationEnabled", UNSET)

        is_enabled_only_for_ff = d.pop("isEnabledOnlyForFF", UNSET)

        git_simplification_enabled = d.pop("gitSimplificationEnabled", UNSET)

        enabled_only_for_ff = d.pop("enabledOnlyForFF", UNSET)

        git_sync_settings = cls(
            project_identifier=project_identifier,
            org_identifier=org_identifier,
            execute_on_delegate=execute_on_delegate,
            is_git_simplification_enabled=is_git_simplification_enabled,
            is_enabled_only_for_ff=is_enabled_only_for_ff,
            git_simplification_enabled=git_simplification_enabled,
            enabled_only_for_ff=enabled_only_for_ff,
        )

        git_sync_settings.additional_properties = d
        return git_sync_settings

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
