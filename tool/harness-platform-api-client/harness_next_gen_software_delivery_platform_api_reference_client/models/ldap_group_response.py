from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_user_response import LdapUserResponse


T = TypeVar("T", bound="LdapGroupResponse")


@_attrs_define
class LdapGroupResponse:
    """
    Attributes:
        dn (str):
        name (str):
        description (str | Unset):
        total_members (int | Unset):
        selectable (bool | Unset):
        message (str | Unset):
        users (list[LdapUserResponse] | Unset):
    """

    dn: str
    name: str
    description: str | Unset = UNSET
    total_members: int | Unset = UNSET
    selectable: bool | Unset = UNSET
    message: str | Unset = UNSET
    users: list[LdapUserResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dn = self.dn

        name = self.name

        description = self.description

        total_members = self.total_members

        selectable = self.selectable

        message = self.message

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dn": dn,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if total_members is not UNSET:
            field_dict["totalMembers"] = total_members
        if selectable is not UNSET:
            field_dict["selectable"] = selectable
        if message is not UNSET:
            field_dict["message"] = message
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_user_response import LdapUserResponse

        d = dict(src_dict)
        dn = d.pop("dn")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        total_members = d.pop("totalMembers", UNSET)

        selectable = d.pop("selectable", UNSET)

        message = d.pop("message", UNSET)

        _users = d.pop("users", UNSET)
        users: list[LdapUserResponse] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = LdapUserResponse.from_dict(users_item_data)

                users.append(users_item)

        ldap_group_response = cls(
            dn=dn,
            name=name,
            description=description,
            total_members=total_members,
            selectable=selectable,
            message=message,
            users=users,
        )

        ldap_group_response.additional_properties = d
        return ldap_group_response

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
