from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_merge_method import EnumMergeMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrAutoMergeEnableBody")


@_attrs_define
class PrAutoMergeEnableBody:
    """
    Attributes:
        delete_source_branch (bool | Unset):
        message (str | Unset):
        method (EnumMergeMethod | Unset):
        title (str | Unset):
    """

    delete_source_branch: bool | Unset = UNSET
    message: str | Unset = UNSET
    method: EnumMergeMethod | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_source_branch = self.delete_source_branch

        message = self.message

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_source_branch is not UNSET:
            field_dict["delete_source_branch"] = delete_source_branch
        if message is not UNSET:
            field_dict["message"] = message
        if method is not UNSET:
            field_dict["method"] = method
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_source_branch = d.pop("delete_source_branch", UNSET)

        message = d.pop("message", UNSET)

        _method = d.pop("method", UNSET)
        method: EnumMergeMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = EnumMergeMethod(_method)

        title = d.pop("title", UNSET)

        pr_auto_merge_enable_body = cls(
            delete_source_branch=delete_source_branch,
            message=message,
            method=method,
            title=title,
        )

        pr_auto_merge_enable_body.additional_properties = d
        return pr_auto_merge_enable_body

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
