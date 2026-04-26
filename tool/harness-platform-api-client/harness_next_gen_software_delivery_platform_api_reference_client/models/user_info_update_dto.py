from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserInfoUpdateDTO")


@_attrs_define
class UserInfoUpdateDTO:
    """
    Attributes:
        name (str | Unset):
        email (str | Unset):
        given_name (str | Unset):
        family_name (str | Unset):
    """

    name: str | Unset = UNSET
    email: str | Unset = UNSET
    given_name: str | Unset = UNSET
    family_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        given_name = self.given_name

        family_name = self.family_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if family_name is not UNSET:
            field_dict["familyName"] = family_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        given_name = d.pop("givenName", UNSET)

        family_name = d.pop("familyName", UNSET)

        user_info_update_dto = cls(
            name=name,
            email=email,
            given_name=given_name,
            family_name=family_name,
        )

        user_info_update_dto.additional_properties = d
        return user_info_update_dto

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
