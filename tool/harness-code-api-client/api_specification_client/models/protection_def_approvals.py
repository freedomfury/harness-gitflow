from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionDefApprovals")


@_attrs_define
class ProtectionDefApprovals:
    """
    Attributes:
        require_code_owners (bool | Unset):
        require_latest_commit (bool | Unset):
        require_minimum_count (int | Unset):
        require_minimum_default_reviewer_count (int | Unset):
        require_no_change_request (bool | Unset):
    """

    require_code_owners: bool | Unset = UNSET
    require_latest_commit: bool | Unset = UNSET
    require_minimum_count: int | Unset = UNSET
    require_minimum_default_reviewer_count: int | Unset = UNSET
    require_no_change_request: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        require_code_owners = self.require_code_owners

        require_latest_commit = self.require_latest_commit

        require_minimum_count = self.require_minimum_count

        require_minimum_default_reviewer_count = self.require_minimum_default_reviewer_count

        require_no_change_request = self.require_no_change_request

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if require_code_owners is not UNSET:
            field_dict["require_code_owners"] = require_code_owners
        if require_latest_commit is not UNSET:
            field_dict["require_latest_commit"] = require_latest_commit
        if require_minimum_count is not UNSET:
            field_dict["require_minimum_count"] = require_minimum_count
        if require_minimum_default_reviewer_count is not UNSET:
            field_dict["require_minimum_default_reviewer_count"] = require_minimum_default_reviewer_count
        if require_no_change_request is not UNSET:
            field_dict["require_no_change_request"] = require_no_change_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        require_code_owners = d.pop("require_code_owners", UNSET)

        require_latest_commit = d.pop("require_latest_commit", UNSET)

        require_minimum_count = d.pop("require_minimum_count", UNSET)

        require_minimum_default_reviewer_count = d.pop("require_minimum_default_reviewer_count", UNSET)

        require_no_change_request = d.pop("require_no_change_request", UNSET)

        protection_def_approvals = cls(
            require_code_owners=require_code_owners,
            require_latest_commit=require_latest_commit,
            require_minimum_count=require_minimum_count,
            require_minimum_default_reviewer_count=require_minimum_default_reviewer_count,
            require_no_change_request=require_no_change_request,
        )

        protection_def_approvals.additional_properties = d
        return protection_def_approvals

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
