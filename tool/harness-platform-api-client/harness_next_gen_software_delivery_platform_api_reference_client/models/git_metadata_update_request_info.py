from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitMetadataUpdateRequestInfo")


@_attrs_define
class GitMetadataUpdateRequestInfo:
    """This lists down GIT metadata params that can be updated for given entity

    Attributes:
        connector_ref (str | Unset):
        repo_name (str | Unset):
        file_path (str | Unset):
    """

    connector_ref: str | Unset = UNSET
    repo_name: str | Unset = UNSET
    file_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_ref = self.connector_ref

        repo_name = self.repo_name

        file_path = self.file_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connector_ref is not UNSET:
            field_dict["connectorRef"] = connector_ref
        if repo_name is not UNSET:
            field_dict["repoName"] = repo_name
        if file_path is not UNSET:
            field_dict["filePath"] = file_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_ref = d.pop("connectorRef", UNSET)

        repo_name = d.pop("repoName", UNSET)

        file_path = d.pop("filePath", UNSET)

        git_metadata_update_request_info = cls(
            connector_ref=connector_ref,
            repo_name=repo_name,
            file_path=file_path,
        )

        git_metadata_update_request_info.additional_properties = d
        return git_metadata_update_request_info

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
