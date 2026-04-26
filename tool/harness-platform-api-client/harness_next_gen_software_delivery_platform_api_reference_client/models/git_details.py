from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitDetails")


@_attrs_define
class GitDetails:
    """
    Attributes:
        branch (str | Unset):
        repo_url (str | Unset):
        file_path (str | Unset):
    """

    branch: str | Unset = UNSET
    repo_url: str | Unset = UNSET
    file_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        repo_url = self.repo_url

        file_path = self.file_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["branch"] = branch
        if repo_url is not UNSET:
            field_dict["repoUrl"] = repo_url
        if file_path is not UNSET:
            field_dict["filePath"] = file_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = d.pop("branch", UNSET)

        repo_url = d.pop("repoUrl", UNSET)

        file_path = d.pop("filePath", UNSET)

        git_details = cls(
            branch=branch,
            repo_url=repo_url,
            file_path=file_path,
        )

        git_details.additional_properties = d
        return git_details

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
