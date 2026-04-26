from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesCodeCommentFields")


@_attrs_define
class TypesCodeCommentFields:
    """
    Attributes:
        line_new (int | Unset):
        line_old (int | Unset):
        merge_base_sha (str | Unset):
        outdated (bool | Unset):
        path (str | Unset):
        source_sha (str | Unset):
        span_new (int | Unset):
        span_old (int | Unset):
    """

    line_new: int | Unset = UNSET
    line_old: int | Unset = UNSET
    merge_base_sha: str | Unset = UNSET
    outdated: bool | Unset = UNSET
    path: str | Unset = UNSET
    source_sha: str | Unset = UNSET
    span_new: int | Unset = UNSET
    span_old: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_new = self.line_new

        line_old = self.line_old

        merge_base_sha = self.merge_base_sha

        outdated = self.outdated

        path = self.path

        source_sha = self.source_sha

        span_new = self.span_new

        span_old = self.span_old

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_new is not UNSET:
            field_dict["line_new"] = line_new
        if line_old is not UNSET:
            field_dict["line_old"] = line_old
        if merge_base_sha is not UNSET:
            field_dict["merge_base_sha"] = merge_base_sha
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if path is not UNSET:
            field_dict["path"] = path
        if source_sha is not UNSET:
            field_dict["source_sha"] = source_sha
        if span_new is not UNSET:
            field_dict["span_new"] = span_new
        if span_old is not UNSET:
            field_dict["span_old"] = span_old

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_new = d.pop("line_new", UNSET)

        line_old = d.pop("line_old", UNSET)

        merge_base_sha = d.pop("merge_base_sha", UNSET)

        outdated = d.pop("outdated", UNSET)

        path = d.pop("path", UNSET)

        source_sha = d.pop("source_sha", UNSET)

        span_new = d.pop("span_new", UNSET)

        span_old = d.pop("span_old", UNSET)

        types_code_comment_fields = cls(
            line_new=line_new,
            line_old=line_old,
            merge_base_sha=merge_base_sha,
            outdated=outdated,
            path=path,
            source_sha=source_sha,
            span_new=span_new,
            span_old=span_old,
        )

        types_code_comment_fields.additional_properties = d
        return types_code_comment_fields

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
