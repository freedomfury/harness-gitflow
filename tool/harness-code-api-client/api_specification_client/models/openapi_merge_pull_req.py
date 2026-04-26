from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_merge_method import EnumMergeMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenapiMergePullReq")


@_attrs_define
class OpenapiMergePullReq:
    """
    Attributes:
        bypass_message (str | Unset):
        bypass_rules (bool | Unset):
        delete_source_branch (bool | Unset):
        dry_run (bool | Unset):
        dry_run_rules (bool | Unset):
        message (str | Unset):
        method (EnumMergeMethod | Unset):
        source_sha (str | Unset):
        title (str | Unset):
    """

    bypass_message: str | Unset = UNSET
    bypass_rules: bool | Unset = UNSET
    delete_source_branch: bool | Unset = UNSET
    dry_run: bool | Unset = UNSET
    dry_run_rules: bool | Unset = UNSET
    message: str | Unset = UNSET
    method: EnumMergeMethod | Unset = UNSET
    source_sha: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypass_message = self.bypass_message

        bypass_rules = self.bypass_rules

        delete_source_branch = self.delete_source_branch

        dry_run = self.dry_run

        dry_run_rules = self.dry_run_rules

        message = self.message

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        source_sha = self.source_sha

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypass_message is not UNSET:
            field_dict["bypass_message"] = bypass_message
        if bypass_rules is not UNSET:
            field_dict["bypass_rules"] = bypass_rules
        if delete_source_branch is not UNSET:
            field_dict["delete_source_branch"] = delete_source_branch
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if dry_run_rules is not UNSET:
            field_dict["dry_run_rules"] = dry_run_rules
        if message is not UNSET:
            field_dict["message"] = message
        if method is not UNSET:
            field_dict["method"] = method
        if source_sha is not UNSET:
            field_dict["source_sha"] = source_sha
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bypass_message = d.pop("bypass_message", UNSET)

        bypass_rules = d.pop("bypass_rules", UNSET)

        delete_source_branch = d.pop("delete_source_branch", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        dry_run_rules = d.pop("dry_run_rules", UNSET)

        message = d.pop("message", UNSET)

        _method = d.pop("method", UNSET)
        method: EnumMergeMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = EnumMergeMethod(_method)

        source_sha = d.pop("source_sha", UNSET)

        title = d.pop("title", UNSET)

        openapi_merge_pull_req = cls(
            bypass_message=bypass_message,
            bypass_rules=bypass_rules,
            delete_source_branch=delete_source_branch,
            dry_run=dry_run,
            dry_run_rules=dry_run_rules,
            message=message,
            method=method,
            source_sha=source_sha,
            title=title,
        )

        openapi_merge_pull_req.additional_properties = d
        return openapi_merge_pull_req

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
