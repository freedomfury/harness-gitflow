from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_settings_settings_type import LDAPSettingsSettingsType, check_ldap_settings_settings_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_connection_settings import LdapConnectionSettings
    from ..models.ldap_group_settings import LdapGroupSettings
    from ..models.ldap_user_settings import LdapUserSettings


T = TypeVar("T", bound="LDAPSettings")


@_attrs_define
class LDAPSettings:
    """This has the details of LDAP Settings supported in NG.

    Attributes:
        connection_settings (LdapConnectionSettings): This is the LDAP connection setting.
        identifier (str): This is the LDAP setting identifier.
        display_name (str): This is the LDAP setting display name.
        user_settings_list (list[LdapUserSettings] | Unset): This is the user settings list in LDAP setting.
        group_settings_list (list[LdapGroupSettings] | Unset): This is the group settings list in LDAP setting.
        cron_expression (str | Unset): This is the cron expression in LDAP Settings.
        next_iterations (list[int] | Unset): This is the list of iterations for next LDAP sync job.
        disabled (bool | Unset): This tells if LDAP Settings is disabled or not, LDAP sync won't happen in disabled
            state.
        settings_type (LDAPSettingsSettingsType | Unset):
    """

    connection_settings: LdapConnectionSettings
    identifier: str
    display_name: str
    user_settings_list: list[LdapUserSettings] | Unset = UNSET
    group_settings_list: list[LdapGroupSettings] | Unset = UNSET
    cron_expression: str | Unset = UNSET
    next_iterations: list[int] | Unset = UNSET
    disabled: bool | Unset = UNSET
    settings_type: LDAPSettingsSettingsType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_settings = self.connection_settings.to_dict()

        identifier = self.identifier

        display_name = self.display_name

        user_settings_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_settings_list, Unset):
            user_settings_list = []
            for user_settings_list_item_data in self.user_settings_list:
                user_settings_list_item = user_settings_list_item_data.to_dict()
                user_settings_list.append(user_settings_list_item)

        group_settings_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_settings_list, Unset):
            group_settings_list = []
            for group_settings_list_item_data in self.group_settings_list:
                group_settings_list_item = group_settings_list_item_data.to_dict()
                group_settings_list.append(group_settings_list_item)

        cron_expression = self.cron_expression

        next_iterations: list[int] | Unset = UNSET
        if not isinstance(self.next_iterations, Unset):
            next_iterations = self.next_iterations

        disabled = self.disabled

        settings_type: str | Unset = UNSET
        if not isinstance(self.settings_type, Unset):
            settings_type = self.settings_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionSettings": connection_settings,
                "identifier": identifier,
                "displayName": display_name,
            }
        )
        if user_settings_list is not UNSET:
            field_dict["userSettingsList"] = user_settings_list
        if group_settings_list is not UNSET:
            field_dict["groupSettingsList"] = group_settings_list
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if next_iterations is not UNSET:
            field_dict["nextIterations"] = next_iterations
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if settings_type is not UNSET:
            field_dict["settingsType"] = settings_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_connection_settings import LdapConnectionSettings
        from ..models.ldap_group_settings import LdapGroupSettings
        from ..models.ldap_user_settings import LdapUserSettings

        d = dict(src_dict)
        connection_settings = LdapConnectionSettings.from_dict(d.pop("connectionSettings"))

        identifier = d.pop("identifier")

        display_name = d.pop("displayName")

        _user_settings_list = d.pop("userSettingsList", UNSET)
        user_settings_list: list[LdapUserSettings] | Unset = UNSET
        if _user_settings_list is not UNSET:
            user_settings_list = []
            for user_settings_list_item_data in _user_settings_list:
                user_settings_list_item = LdapUserSettings.from_dict(user_settings_list_item_data)

                user_settings_list.append(user_settings_list_item)

        _group_settings_list = d.pop("groupSettingsList", UNSET)
        group_settings_list: list[LdapGroupSettings] | Unset = UNSET
        if _group_settings_list is not UNSET:
            group_settings_list = []
            for group_settings_list_item_data in _group_settings_list:
                group_settings_list_item = LdapGroupSettings.from_dict(group_settings_list_item_data)

                group_settings_list.append(group_settings_list_item)

        cron_expression = d.pop("cronExpression", UNSET)

        next_iterations = cast(list[int], d.pop("nextIterations", UNSET))

        disabled = d.pop("disabled", UNSET)

        _settings_type = d.pop("settingsType", UNSET)
        settings_type: LDAPSettingsSettingsType | Unset
        if isinstance(_settings_type, Unset):
            settings_type = UNSET
        else:
            settings_type = check_ldap_settings_settings_type(_settings_type)

        ldap_settings = cls(
            connection_settings=connection_settings,
            identifier=identifier,
            display_name=display_name,
            user_settings_list=user_settings_list,
            group_settings_list=group_settings_list,
            cron_expression=cron_expression,
            next_iterations=next_iterations,
            disabled=disabled,
            settings_type=settings_type,
        )

        ldap_settings.additional_properties = d
        return ldap_settings

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
