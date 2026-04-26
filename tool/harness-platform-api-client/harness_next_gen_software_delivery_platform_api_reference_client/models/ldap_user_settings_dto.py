from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapUserSettingsDTO")


@_attrs_define
class LdapUserSettingsDTO:
    """Ldap User Settings DTO

    Attributes:
        base_d_n (str | Unset):
        search_filter (str | Unset):
        uid_attr (str | Unset):
        sam_account_name_attr (str | Unset):
        email_attr (str | Unset):
        display_name_attr (str | Unset):
        group_membership_attr (str | Unset):
    """

    base_d_n: str | Unset = UNSET
    search_filter: str | Unset = UNSET
    uid_attr: str | Unset = UNSET
    sam_account_name_attr: str | Unset = UNSET
    email_attr: str | Unset = UNSET
    display_name_attr: str | Unset = UNSET
    group_membership_attr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_d_n = self.base_d_n

        search_filter = self.search_filter

        uid_attr = self.uid_attr

        sam_account_name_attr = self.sam_account_name_attr

        email_attr = self.email_attr

        display_name_attr = self.display_name_attr

        group_membership_attr = self.group_membership_attr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_d_n is not UNSET:
            field_dict["base_d_n"] = base_d_n
        if search_filter is not UNSET:
            field_dict["search_filter"] = search_filter
        if uid_attr is not UNSET:
            field_dict["uid_attr"] = uid_attr
        if sam_account_name_attr is not UNSET:
            field_dict["sam_account_name_attr"] = sam_account_name_attr
        if email_attr is not UNSET:
            field_dict["email_attr"] = email_attr
        if display_name_attr is not UNSET:
            field_dict["display_name_attr"] = display_name_attr
        if group_membership_attr is not UNSET:
            field_dict["group_membership_attr"] = group_membership_attr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_d_n = d.pop("base_d_n", UNSET)

        search_filter = d.pop("search_filter", UNSET)

        uid_attr = d.pop("uid_attr", UNSET)

        sam_account_name_attr = d.pop("sam_account_name_attr", UNSET)

        email_attr = d.pop("email_attr", UNSET)

        display_name_attr = d.pop("display_name_attr", UNSET)

        group_membership_attr = d.pop("group_membership_attr", UNSET)

        ldap_user_settings_dto = cls(
            base_d_n=base_d_n,
            search_filter=search_filter,
            uid_attr=uid_attr,
            sam_account_name_attr=sam_account_name_attr,
            email_attr=email_attr,
            display_name_attr=display_name_attr,
            group_membership_attr=group_membership_attr,
        )

        ldap_user_settings_dto.additional_properties = d
        return ldap_user_settings_dto

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
