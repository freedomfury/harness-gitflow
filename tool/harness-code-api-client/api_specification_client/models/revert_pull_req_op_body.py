from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RevertPullReqOpBody")


@_attrs_define
class RevertPullReqOpBody:
    """
    Attributes:
        message (str | Unset):
        revert_branch (str | Unset):
        title (str | Unset):
    """

    message: str | Unset = UNSET
    revert_branch: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        revert_branch = self.revert_branch

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if revert_branch is not UNSET:
            field_dict["revert_branch"] = revert_branch
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        revert_branch = d.pop("revert_branch", UNSET)

        title = d.pop("title", UNSET)

        revert_pull_req_op_body = cls(
            message=message,
            revert_branch=revert_branch,
            title=title,
        )

        revert_pull_req_op_body.additional_properties = d
        return revert_pull_req_op_body

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
