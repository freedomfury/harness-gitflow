from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionDefBypass")


@_attrs_define
class ProtectionDefBypass:
    """
    Attributes:
        repo_owners (bool | Unset):
        user_group_ids (list[int] | Unset):
        user_ids (list[int] | Unset):
    """

    repo_owners: bool | Unset = UNSET
    user_group_ids: list[int] | Unset = UNSET
    user_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_owners = self.repo_owners

        user_group_ids: list[int] | Unset = UNSET
        if not isinstance(self.user_group_ids, Unset):
            user_group_ids = self.user_group_ids

        user_ids: list[int] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repo_owners is not UNSET:
            field_dict["repo_owners"] = repo_owners
        if user_group_ids is not UNSET:
            field_dict["user_group_ids"] = user_group_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_owners = d.pop("repo_owners", UNSET)

        user_group_ids = cast(list[int], d.pop("user_group_ids", UNSET))

        user_ids = cast(list[int], d.pop("user_ids", UNSET))

        protection_def_bypass = cls(
            repo_owners=repo_owners,
            user_group_ids=user_group_ids,
            user_ids=user_ids,
        )

        protection_def_bypass.additional_properties = d
        return protection_def_bypass

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
