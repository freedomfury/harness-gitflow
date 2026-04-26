from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SettingsGeneralSettings")


@_attrs_define
class SettingsGeneralSettings:
    """
    Attributes:
        auto_merge_enabled (bool | None | Unset):
        file_size_limit (int | None | Unset): file size limit in bytes
        git_lfs_enabled (bool | None | Unset):
    """

    auto_merge_enabled: bool | None | Unset = UNSET
    file_size_limit: int | None | Unset = UNSET
    git_lfs_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_merge_enabled: bool | None | Unset
        if isinstance(self.auto_merge_enabled, Unset):
            auto_merge_enabled = UNSET
        else:
            auto_merge_enabled = self.auto_merge_enabled

        file_size_limit: int | None | Unset
        if isinstance(self.file_size_limit, Unset):
            file_size_limit = UNSET
        else:
            file_size_limit = self.file_size_limit

        git_lfs_enabled: bool | None | Unset
        if isinstance(self.git_lfs_enabled, Unset):
            git_lfs_enabled = UNSET
        else:
            git_lfs_enabled = self.git_lfs_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_merge_enabled is not UNSET:
            field_dict["auto_merge_enabled"] = auto_merge_enabled
        if file_size_limit is not UNSET:
            field_dict["file_size_limit"] = file_size_limit
        if git_lfs_enabled is not UNSET:
            field_dict["git_lfs_enabled"] = git_lfs_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_auto_merge_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_merge_enabled = _parse_auto_merge_enabled(d.pop("auto_merge_enabled", UNSET))

        def _parse_file_size_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size_limit = _parse_file_size_limit(d.pop("file_size_limit", UNSET))

        def _parse_git_lfs_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        git_lfs_enabled = _parse_git_lfs_enabled(d.pop("git_lfs_enabled", UNSET))

        settings_general_settings = cls(
            auto_merge_enabled=auto_merge_enabled,
            file_size_limit=file_size_limit,
            git_lfs_enabled=git_lfs_enabled,
        )

        settings_general_settings.additional_properties = d
        return settings_general_settings

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
