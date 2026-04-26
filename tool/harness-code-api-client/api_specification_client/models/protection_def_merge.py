from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_merge_method import EnumMergeMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionDefMerge")


@_attrs_define
class ProtectionDefMerge:
    """
    Attributes:
        block (bool | Unset):
        delete_branch (bool | Unset):
        require_bypass_message (bool | Unset):
        strategies_allowed (list[EnumMergeMethod] | Unset):
    """

    block: bool | Unset = UNSET
    delete_branch: bool | Unset = UNSET
    require_bypass_message: bool | Unset = UNSET
    strategies_allowed: list[EnumMergeMethod] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block = self.block

        delete_branch = self.delete_branch

        require_bypass_message = self.require_bypass_message

        strategies_allowed: list[str] | Unset = UNSET
        if not isinstance(self.strategies_allowed, Unset):
            strategies_allowed = []
            for strategies_allowed_item_data in self.strategies_allowed:
                strategies_allowed_item = strategies_allowed_item_data.value
                strategies_allowed.append(strategies_allowed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block is not UNSET:
            field_dict["block"] = block
        if delete_branch is not UNSET:
            field_dict["delete_branch"] = delete_branch
        if require_bypass_message is not UNSET:
            field_dict["require_bypass_message"] = require_bypass_message
        if strategies_allowed is not UNSET:
            field_dict["strategies_allowed"] = strategies_allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block = d.pop("block", UNSET)

        delete_branch = d.pop("delete_branch", UNSET)

        require_bypass_message = d.pop("require_bypass_message", UNSET)

        _strategies_allowed = d.pop("strategies_allowed", UNSET)
        strategies_allowed: list[EnumMergeMethod] | Unset = UNSET
        if _strategies_allowed is not UNSET:
            strategies_allowed = []
            for strategies_allowed_item_data in _strategies_allowed:
                strategies_allowed_item = EnumMergeMethod(strategies_allowed_item_data)

                strategies_allowed.append(strategies_allowed_item)

        protection_def_merge = cls(
            block=block,
            delete_branch=delete_branch,
            require_bypass_message=require_bypass_message,
            strategies_allowed=strategies_allowed,
        )

        protection_def_merge.additional_properties = d
        return protection_def_merge

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
