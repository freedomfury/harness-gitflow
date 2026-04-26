from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LdapUserSettings")


@_attrs_define
class LdapUserSettings:
    """This is the user settings list in LDAP setting.

    Attributes:
        base_dn (str):
        search_filter (str):
        uid_attr (str):
        sam_account_name_attr (str):
        email_attr (str):
        display_name_attr (str):
        group_membership_attr (str):
    """

    base_dn: str
    search_filter: str
    uid_attr: str
    sam_account_name_attr: str
    email_attr: str
    display_name_attr: str
    group_membership_attr: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_dn = self.base_dn

        search_filter = self.search_filter

        uid_attr = self.uid_attr

        sam_account_name_attr = self.sam_account_name_attr

        email_attr = self.email_attr

        display_name_attr = self.display_name_attr

        group_membership_attr = self.group_membership_attr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseDN": base_dn,
                "searchFilter": search_filter,
                "uidAttr": uid_attr,
                "samAccountNameAttr": sam_account_name_attr,
                "emailAttr": email_attr,
                "displayNameAttr": display_name_attr,
                "groupMembershipAttr": group_membership_attr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_dn = d.pop("baseDN")

        search_filter = d.pop("searchFilter")

        uid_attr = d.pop("uidAttr")

        sam_account_name_attr = d.pop("samAccountNameAttr")

        email_attr = d.pop("emailAttr")

        display_name_attr = d.pop("displayNameAttr")

        group_membership_attr = d.pop("groupMembershipAttr")

        ldap_user_settings = cls(
            base_dn=base_dn,
            search_filter=search_filter,
            uid_attr=uid_attr,
            sam_account_name_attr=sam_account_name_attr,
            email_attr=email_attr,
            display_name_attr=display_name_attr,
            group_membership_attr=group_membership_attr,
        )

        ldap_user_settings.additional_properties = d
        return ldap_user_settings

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
