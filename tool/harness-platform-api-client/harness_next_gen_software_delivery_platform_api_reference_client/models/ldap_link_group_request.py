from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LdapLinkGroupRequest")


@_attrs_define
class LdapLinkGroupRequest:
    """
    Attributes:
        ldap_group_dn (str):
        ldap_group_name (str):
    """

    ldap_group_dn: str
    ldap_group_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ldap_group_dn = self.ldap_group_dn

        ldap_group_name = self.ldap_group_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ldapGroupDN": ldap_group_dn,
                "ldapGroupName": ldap_group_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ldap_group_dn = d.pop("ldapGroupDN")

        ldap_group_name = d.pop("ldapGroupName")

        ldap_link_group_request = cls(
            ldap_group_dn=ldap_group_dn,
            ldap_group_name=ldap_group_name,
        )

        ldap_link_group_request.additional_properties = d
        return ldap_link_group_request

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
