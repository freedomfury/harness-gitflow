from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAddToUserGroupDTO")


@_attrs_define
class UserAddToUserGroupDTO:
    """
    Attributes:
        user_group_ids_to_add (list[str] | Unset):
    """

    user_group_ids_to_add: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_group_ids_to_add: list[str] | Unset = UNSET
        if not isinstance(self.user_group_ids_to_add, Unset):
            user_group_ids_to_add = self.user_group_ids_to_add

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_group_ids_to_add is not UNSET:
            field_dict["userGroupIdsToAdd"] = user_group_ids_to_add

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_group_ids_to_add = cast(list[str], d.pop("userGroupIdsToAdd", UNSET))

        user_add_to_user_group_dto = cls(
            user_group_ids_to_add=user_group_ids_to_add,
        )

        user_add_to_user_group_dto.additional_properties = d
        return user_add_to_user_group_dto

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
