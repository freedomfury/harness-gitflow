from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_content_encoding_type import EnumContentEncodingType
from ..models.git_file_action import GitFileAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepoCommitFileAction")


@_attrs_define
class RepoCommitFileAction:
    """
    Attributes:
        action (GitFileAction | Unset):
        encoding (EnumContentEncodingType | Unset):
        path (str | Unset):
        payload (str | Unset):
        sha (str | Unset): Git object hash
    """

    action: GitFileAction | Unset = UNSET
    encoding: EnumContentEncodingType | Unset = UNSET
    path: str | Unset = UNSET
    payload: str | Unset = UNSET
    sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        encoding: str | Unset = UNSET
        if not isinstance(self.encoding, Unset):
            encoding = self.encoding.value

        path = self.path

        payload = self.payload

        sha = self.sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if path is not UNSET:
            field_dict["path"] = path
        if payload is not UNSET:
            field_dict["payload"] = payload
        if sha is not UNSET:
            field_dict["sha"] = sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: GitFileAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = GitFileAction(_action)

        _encoding = d.pop("encoding", UNSET)
        encoding: EnumContentEncodingType | Unset
        if isinstance(_encoding, Unset):
            encoding = UNSET
        else:
            encoding = EnumContentEncodingType(_encoding)

        path = d.pop("path", UNSET)

        payload = d.pop("payload", UNSET)

        sha = d.pop("sha", UNSET)

        repo_commit_file_action = cls(
            action=action,
            encoding=encoding,
            path=path,
            payload=payload,
            sha=sha,
        )

        repo_commit_file_action.additional_properties = d
        return repo_commit_file_action

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
