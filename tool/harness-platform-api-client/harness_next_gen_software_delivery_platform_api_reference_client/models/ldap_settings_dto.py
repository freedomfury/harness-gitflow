from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_connection_settings_dto import LdapConnectionSettingsDTO
    from ..models.ldap_group_settings_dto import LdapGroupSettingsDTO
    from ..models.ldap_user_settings_dto import LdapUserSettingsDTO


T = TypeVar("T", bound="LdapSettingsDTO")


@_attrs_define
class LdapSettingsDTO:
    """Ldap Settings DTO

    Attributes:
        account_identifier (str):
        identifier (str):
        name (str):
        url (str | Unset):
        disabled (bool | Unset):
        cron_expression (str | Unset):
        ldap_connection_settings (LdapConnectionSettingsDTO | Unset): Ldap Connection Settings DTO
        ldap_user_settings (list[LdapUserSettingsDTO] | Unset):
        ldap_group_settings (list[LdapGroupSettingsDTO] | Unset):
        sso_type (str | Unset):
    """

    account_identifier: str
    identifier: str
    name: str
    url: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    cron_expression: str | Unset = UNSET
    ldap_connection_settings: LdapConnectionSettingsDTO | Unset = UNSET
    ldap_user_settings: list[LdapUserSettingsDTO] | Unset = UNSET
    ldap_group_settings: list[LdapGroupSettingsDTO] | Unset = UNSET
    sso_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        identifier = self.identifier

        name = self.name

        url = self.url

        disabled = self.disabled

        cron_expression = self.cron_expression

        ldap_connection_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap_connection_settings, Unset):
            ldap_connection_settings = self.ldap_connection_settings.to_dict()

        ldap_user_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ldap_user_settings, Unset):
            ldap_user_settings = []
            for ldap_user_settings_item_data in self.ldap_user_settings:
                ldap_user_settings_item = ldap_user_settings_item_data.to_dict()
                ldap_user_settings.append(ldap_user_settings_item)

        ldap_group_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ldap_group_settings, Unset):
            ldap_group_settings = []
            for ldap_group_settings_item_data in self.ldap_group_settings:
                ldap_group_settings_item = ldap_group_settings_item_data.to_dict()
                ldap_group_settings.append(ldap_group_settings_item)

        sso_type = self.sso_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_identifier": account_identifier,
                "identifier": identifier,
                "name": name,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if cron_expression is not UNSET:
            field_dict["cron_expression"] = cron_expression
        if ldap_connection_settings is not UNSET:
            field_dict["ldap_connection_settings"] = ldap_connection_settings
        if ldap_user_settings is not UNSET:
            field_dict["ldap_user_settings"] = ldap_user_settings
        if ldap_group_settings is not UNSET:
            field_dict["ldap_group_settings"] = ldap_group_settings
        if sso_type is not UNSET:
            field_dict["sso_type"] = sso_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_connection_settings_dto import LdapConnectionSettingsDTO
        from ..models.ldap_group_settings_dto import LdapGroupSettingsDTO
        from ..models.ldap_user_settings_dto import LdapUserSettingsDTO

        d = dict(src_dict)
        account_identifier = d.pop("account_identifier")

        identifier = d.pop("identifier")

        name = d.pop("name")

        url = d.pop("url", UNSET)

        disabled = d.pop("disabled", UNSET)

        cron_expression = d.pop("cron_expression", UNSET)

        _ldap_connection_settings = d.pop("ldap_connection_settings", UNSET)
        ldap_connection_settings: LdapConnectionSettingsDTO | Unset
        if isinstance(_ldap_connection_settings, Unset):
            ldap_connection_settings = UNSET
        else:
            ldap_connection_settings = LdapConnectionSettingsDTO.from_dict(_ldap_connection_settings)

        _ldap_user_settings = d.pop("ldap_user_settings", UNSET)
        ldap_user_settings: list[LdapUserSettingsDTO] | Unset = UNSET
        if _ldap_user_settings is not UNSET:
            ldap_user_settings = []
            for ldap_user_settings_item_data in _ldap_user_settings:
                ldap_user_settings_item = LdapUserSettingsDTO.from_dict(ldap_user_settings_item_data)

                ldap_user_settings.append(ldap_user_settings_item)

        _ldap_group_settings = d.pop("ldap_group_settings", UNSET)
        ldap_group_settings: list[LdapGroupSettingsDTO] | Unset = UNSET
        if _ldap_group_settings is not UNSET:
            ldap_group_settings = []
            for ldap_group_settings_item_data in _ldap_group_settings:
                ldap_group_settings_item = LdapGroupSettingsDTO.from_dict(ldap_group_settings_item_data)

                ldap_group_settings.append(ldap_group_settings_item)

        sso_type = d.pop("sso_type", UNSET)

        ldap_settings_dto = cls(
            account_identifier=account_identifier,
            identifier=identifier,
            name=name,
            url=url,
            disabled=disabled,
            cron_expression=cron_expression,
            ldap_connection_settings=ldap_connection_settings,
            ldap_user_settings=ldap_user_settings,
            ldap_group_settings=ldap_group_settings,
            sso_type=sso_type,
        )

        ldap_settings_dto.additional_properties = d
        return ldap_settings_dto

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
