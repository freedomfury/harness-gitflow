from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitSyncFolderConfig")


@_attrs_define
class GitSyncFolderConfig:
    """This contains details of Root Folder

    Attributes:
        root_folder (str): Root Folder Name
        is_default (bool | Unset): This checks if the folder is the default folder
    """

    root_folder: str
    is_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        root_folder = self.root_folder

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rootFolder": root_folder,
            }
        )
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        root_folder = d.pop("rootFolder")

        is_default = d.pop("isDefault", UNSET)

        git_sync_folder_config = cls(
            root_folder=root_folder,
            is_default=is_default,
        )

        git_sync_folder_config.additional_properties = d
        return git_sync_folder_config

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
