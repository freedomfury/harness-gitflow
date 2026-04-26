from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_enabled_connectivity_mode import GitEnabledConnectivityMode, check_git_enabled_connectivity_mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitEnabled")


@_attrs_define
class GitEnabled:
    """This contains details of connectivity mode and whether Git Sync is enabled

    Attributes:
        is_git_sync_enabled (bool | Unset):
        connectivity_mode (GitEnabledConnectivityMode | Unset): This is the Git Sync connectivity mode
        is_git_simplification_enabled (bool | Unset):
        is_git_sync_enabled_only_for_ff (bool | Unset):
        git_sync_enabled (bool | Unset):
        git_simplification_enabled (bool | Unset):
        git_sync_enabled_only_for_ff (bool | Unset):
    """

    is_git_sync_enabled: bool | Unset = UNSET
    connectivity_mode: GitEnabledConnectivityMode | Unset = UNSET
    is_git_simplification_enabled: bool | Unset = UNSET
    is_git_sync_enabled_only_for_ff: bool | Unset = UNSET
    git_sync_enabled: bool | Unset = UNSET
    git_simplification_enabled: bool | Unset = UNSET
    git_sync_enabled_only_for_ff: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_git_sync_enabled = self.is_git_sync_enabled

        connectivity_mode: str | Unset = UNSET
        if not isinstance(self.connectivity_mode, Unset):
            connectivity_mode = self.connectivity_mode

        is_git_simplification_enabled = self.is_git_simplification_enabled

        is_git_sync_enabled_only_for_ff = self.is_git_sync_enabled_only_for_ff

        git_sync_enabled = self.git_sync_enabled

        git_simplification_enabled = self.git_simplification_enabled

        git_sync_enabled_only_for_ff = self.git_sync_enabled_only_for_ff

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_git_sync_enabled is not UNSET:
            field_dict["isGitSyncEnabled"] = is_git_sync_enabled
        if connectivity_mode is not UNSET:
            field_dict["connectivityMode"] = connectivity_mode
        if is_git_simplification_enabled is not UNSET:
            field_dict["isGitSimplificationEnabled"] = is_git_simplification_enabled
        if is_git_sync_enabled_only_for_ff is not UNSET:
            field_dict["isGitSyncEnabledOnlyForFF"] = is_git_sync_enabled_only_for_ff
        if git_sync_enabled is not UNSET:
            field_dict["gitSyncEnabled"] = git_sync_enabled
        if git_simplification_enabled is not UNSET:
            field_dict["gitSimplificationEnabled"] = git_simplification_enabled
        if git_sync_enabled_only_for_ff is not UNSET:
            field_dict["gitSyncEnabledOnlyForFF"] = git_sync_enabled_only_for_ff

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_git_sync_enabled = d.pop("isGitSyncEnabled", UNSET)

        _connectivity_mode = d.pop("connectivityMode", UNSET)
        connectivity_mode: GitEnabledConnectivityMode | Unset
        if isinstance(_connectivity_mode, Unset):
            connectivity_mode = UNSET
        else:
            connectivity_mode = check_git_enabled_connectivity_mode(_connectivity_mode)

        is_git_simplification_enabled = d.pop("isGitSimplificationEnabled", UNSET)

        is_git_sync_enabled_only_for_ff = d.pop("isGitSyncEnabledOnlyForFF", UNSET)

        git_sync_enabled = d.pop("gitSyncEnabled", UNSET)

        git_simplification_enabled = d.pop("gitSimplificationEnabled", UNSET)

        git_sync_enabled_only_for_ff = d.pop("gitSyncEnabledOnlyForFF", UNSET)

        git_enabled = cls(
            is_git_sync_enabled=is_git_sync_enabled,
            connectivity_mode=connectivity_mode,
            is_git_simplification_enabled=is_git_simplification_enabled,
            is_git_sync_enabled_only_for_ff=is_git_sync_enabled_only_for_ff,
            git_sync_enabled=git_sync_enabled,
            git_simplification_enabled=git_simplification_enabled,
            git_sync_enabled_only_for_ff=git_sync_enabled_only_for_ff,
        )

        git_enabled.additional_properties = d
        return git_enabled

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
