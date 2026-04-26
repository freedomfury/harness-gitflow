from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LdapGroupSettings")


@_attrs_define
class LdapGroupSettings:
    """This is the group settings list in LDAP setting.

    Attributes:
        base_dn (str):
        search_filter (str):
        name_attr (str):
        description_attr (str):
        user_membership_attr (str):
        referenced_user_attr (str):
    """

    base_dn: str
    search_filter: str
    name_attr: str
    description_attr: str
    user_membership_attr: str
    referenced_user_attr: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_dn = self.base_dn

        search_filter = self.search_filter

        name_attr = self.name_attr

        description_attr = self.description_attr

        user_membership_attr = self.user_membership_attr

        referenced_user_attr = self.referenced_user_attr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseDN": base_dn,
                "searchFilter": search_filter,
                "nameAttr": name_attr,
                "descriptionAttr": description_attr,
                "userMembershipAttr": user_membership_attr,
                "referencedUserAttr": referenced_user_attr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_dn = d.pop("baseDN")

        search_filter = d.pop("searchFilter")

        name_attr = d.pop("nameAttr")

        description_attr = d.pop("descriptionAttr")

        user_membership_attr = d.pop("userMembershipAttr")

        referenced_user_attr = d.pop("referencedUserAttr")

        ldap_group_settings = cls(
            base_dn=base_dn,
            search_filter=search_filter,
            name_attr=name_attr,
            description_attr=description_attr,
            user_membership_attr=user_membership_attr,
            referenced_user_attr=referenced_user_attr,
        )

        ldap_group_settings.additional_properties = d
        return ldap_group_settings

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
