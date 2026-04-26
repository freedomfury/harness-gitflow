from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapGroupSettingsDTO")


@_attrs_define
class LdapGroupSettingsDTO:
    """Ldap Group Settings DTO

    Attributes:
        base_d_n (str | Unset):
        search_filter (str | Unset):
        name_attr (str | Unset):
        description_attr (str | Unset):
        user_membership_attr (str | Unset):
        referenced_user_attr (str | Unset):
    """

    base_d_n: str | Unset = UNSET
    search_filter: str | Unset = UNSET
    name_attr: str | Unset = UNSET
    description_attr: str | Unset = UNSET
    user_membership_attr: str | Unset = UNSET
    referenced_user_attr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_d_n = self.base_d_n

        search_filter = self.search_filter

        name_attr = self.name_attr

        description_attr = self.description_attr

        user_membership_attr = self.user_membership_attr

        referenced_user_attr = self.referenced_user_attr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_d_n is not UNSET:
            field_dict["base_d_n"] = base_d_n
        if search_filter is not UNSET:
            field_dict["search_filter"] = search_filter
        if name_attr is not UNSET:
            field_dict["name_attr"] = name_attr
        if description_attr is not UNSET:
            field_dict["description_attr"] = description_attr
        if user_membership_attr is not UNSET:
            field_dict["user_membership_attr"] = user_membership_attr
        if referenced_user_attr is not UNSET:
            field_dict["referenced_user_attr"] = referenced_user_attr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_d_n = d.pop("base_d_n", UNSET)

        search_filter = d.pop("search_filter", UNSET)

        name_attr = d.pop("name_attr", UNSET)

        description_attr = d.pop("description_attr", UNSET)

        user_membership_attr = d.pop("user_membership_attr", UNSET)

        referenced_user_attr = d.pop("referenced_user_attr", UNSET)

        ldap_group_settings_dto = cls(
            base_d_n=base_d_n,
            search_filter=search_filter,
            name_attr=name_attr,
            description_attr=description_attr,
            user_membership_attr=user_membership_attr,
            referenced_user_attr=referenced_user_attr,
        )

        ldap_group_settings_dto.additional_properties = d
        return ldap_group_settings_dto

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
