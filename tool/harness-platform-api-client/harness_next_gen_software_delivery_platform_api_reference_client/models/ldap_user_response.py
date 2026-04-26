from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapUserResponse")


@_attrs_define
class LdapUserResponse:
    """
    Attributes:
        dn (str):
        email (str):
        name (str):
        user_id (str | Unset):
    """

    dn: str
    email: str
    name: str
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dn = self.dn

        email = self.email

        name = self.name

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dn": dn,
                "email": email,
                "name": name,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dn = d.pop("dn")

        email = d.pop("email")

        name = d.pop("name")

        user_id = d.pop("userId", UNSET)

        ldap_user_response = cls(
            dn=dn,
            email=email,
            name=name,
            user_id=user_id,
        )

        ldap_user_response.additional_properties = d
        return ldap_user_response

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
