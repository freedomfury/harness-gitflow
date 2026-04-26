from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenapiCommentCreatePullReqRequest")


@_attrs_define
class OpenapiCommentCreatePullReqRequest:
    """
    Attributes:
        line_end (int | Unset):
        line_end_new (bool | Unset):
        line_start (int | Unset):
        line_start_new (bool | Unset):
        parent_id (int | Unset):
        path (str | Unset):
        source_commit_sha (str | Unset):
        target_commit_sha (str | Unset):
        text (str | Unset):
    """

    line_end: int | Unset = UNSET
    line_end_new: bool | Unset = UNSET
    line_start: int | Unset = UNSET
    line_start_new: bool | Unset = UNSET
    parent_id: int | Unset = UNSET
    path: str | Unset = UNSET
    source_commit_sha: str | Unset = UNSET
    target_commit_sha: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_end = self.line_end

        line_end_new = self.line_end_new

        line_start = self.line_start

        line_start_new = self.line_start_new

        parent_id = self.parent_id

        path = self.path

        source_commit_sha = self.source_commit_sha

        target_commit_sha = self.target_commit_sha

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_end is not UNSET:
            field_dict["line_end"] = line_end
        if line_end_new is not UNSET:
            field_dict["line_end_new"] = line_end_new
        if line_start is not UNSET:
            field_dict["line_start"] = line_start
        if line_start_new is not UNSET:
            field_dict["line_start_new"] = line_start_new
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if path is not UNSET:
            field_dict["path"] = path
        if source_commit_sha is not UNSET:
            field_dict["source_commit_sha"] = source_commit_sha
        if target_commit_sha is not UNSET:
            field_dict["target_commit_sha"] = target_commit_sha
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_end = d.pop("line_end", UNSET)

        line_end_new = d.pop("line_end_new", UNSET)

        line_start = d.pop("line_start", UNSET)

        line_start_new = d.pop("line_start_new", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        path = d.pop("path", UNSET)

        source_commit_sha = d.pop("source_commit_sha", UNSET)

        target_commit_sha = d.pop("target_commit_sha", UNSET)

        text = d.pop("text", UNSET)

        openapi_comment_create_pull_req_request = cls(
            line_end=line_end,
            line_end_new=line_end_new,
            line_start=line_start,
            line_start_new=line_start_new,
            parent_id=parent_id,
            path=path,
            source_commit_sha=source_commit_sha,
            target_commit_sha=target_commit_sha,
            text=text,
        )

        openapi_comment_create_pull_req_request.additional_properties = d
        return openapi_comment_create_pull_req_request

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
