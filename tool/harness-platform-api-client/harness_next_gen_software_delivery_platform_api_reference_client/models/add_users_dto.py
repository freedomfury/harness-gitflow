from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_binding import RoleBinding
    from ..models.user_setting_from_invite import UserSettingFromInvite


T = TypeVar("T", bound="AddUsersDTO")


@_attrs_define
class AddUsersDTO:
    """
    Attributes:
        emails (list[str]):
        role_bindings (list[RoleBinding] | Unset):
        user_groups (list[str] | Unset):
        user_settings (list[UserSettingFromInvite] | Unset):
    """

    emails: list[str]
    role_bindings: list[RoleBinding] | Unset = UNSET
    user_groups: list[str] | Unset = UNSET
    user_settings: list[UserSettingFromInvite] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emails = self.emails

        role_bindings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.role_bindings, Unset):
            role_bindings = []
            for role_bindings_item_data in self.role_bindings:
                role_bindings_item = role_bindings_item_data.to_dict()
                role_bindings.append(role_bindings_item)

        user_groups: list[str] | Unset = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = self.user_groups

        user_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_settings, Unset):
            user_settings = []
            for user_settings_item_data in self.user_settings:
                user_settings_item = user_settings_item_data.to_dict()
                user_settings.append(user_settings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
            }
        )
        if role_bindings is not UNSET:
            field_dict["roleBindings"] = role_bindings
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups
        if user_settings is not UNSET:
            field_dict["userSettings"] = user_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_binding import RoleBinding
        from ..models.user_setting_from_invite import UserSettingFromInvite

        d = dict(src_dict)
        emails = cast(list[str], d.pop("emails"))

        _role_bindings = d.pop("roleBindings", UNSET)
        role_bindings: list[RoleBinding] | Unset = UNSET
        if _role_bindings is not UNSET:
            role_bindings = []
            for role_bindings_item_data in _role_bindings:
                role_bindings_item = RoleBinding.from_dict(role_bindings_item_data)

                role_bindings.append(role_bindings_item)

        user_groups = cast(list[str], d.pop("userGroups", UNSET))

        _user_settings = d.pop("userSettings", UNSET)
        user_settings: list[UserSettingFromInvite] | Unset = UNSET
        if _user_settings is not UNSET:
            user_settings = []
            for user_settings_item_data in _user_settings:
                user_settings_item = UserSettingFromInvite.from_dict(user_settings_item_data)

                user_settings.append(user_settings_item)

        add_users_dto = cls(
            emails=emails,
            role_bindings=role_bindings,
            user_groups=user_groups,
            user_settings=user_settings,
        )

        add_users_dto.additional_properties = d
        return add_users_dto

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
