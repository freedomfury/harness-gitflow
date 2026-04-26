from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_connection_settings_setting_type import (
    LdapConnectionSettingsSettingType,
    check_ldap_connection_settings_setting_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapConnectionSettings")


@_attrs_define
class LdapConnectionSettings:
    """This is the LDAP connection setting.

    Attributes:
        host (str):
        port (int | Unset):
        ssl_enabled (bool | Unset):
        referrals_enabled (bool | Unset):
        max_referral_hops (int | Unset):
        bind_dn (str | Unset):
        bind_password (str | Unset):
        encrypted_bind_password (str | Unset):
        password_type (str | Unset):
        bind_secret (list[str] | Unset):
        encrypted_bind_secret (str | Unset):
        connect_timeout (int | Unset):
        response_timeout (int | Unset):
        use_recursive_group_membership_search (bool | Unset):
        delegate_selectors (list[str] | Unset):
        password_ref (str | Unset):
        account_id (str | Unset):
        setting_type (LdapConnectionSettingsSettingType | Unset):
    """

    host: str
    port: int | Unset = UNSET
    ssl_enabled: bool | Unset = UNSET
    referrals_enabled: bool | Unset = UNSET
    max_referral_hops: int | Unset = UNSET
    bind_dn: str | Unset = UNSET
    bind_password: str | Unset = UNSET
    encrypted_bind_password: str | Unset = UNSET
    password_type: str | Unset = UNSET
    bind_secret: list[str] | Unset = UNSET
    encrypted_bind_secret: str | Unset = UNSET
    connect_timeout: int | Unset = UNSET
    response_timeout: int | Unset = UNSET
    use_recursive_group_membership_search: bool | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    password_ref: str | Unset = UNSET
    account_id: str | Unset = UNSET
    setting_type: LdapConnectionSettingsSettingType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        ssl_enabled = self.ssl_enabled

        referrals_enabled = self.referrals_enabled

        max_referral_hops = self.max_referral_hops

        bind_dn = self.bind_dn

        bind_password = self.bind_password

        encrypted_bind_password = self.encrypted_bind_password

        password_type = self.password_type

        bind_secret: list[str] | Unset = UNSET
        if not isinstance(self.bind_secret, Unset):
            bind_secret = self.bind_secret

        encrypted_bind_secret = self.encrypted_bind_secret

        connect_timeout = self.connect_timeout

        response_timeout = self.response_timeout

        use_recursive_group_membership_search = self.use_recursive_group_membership_search

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        password_ref = self.password_ref

        account_id = self.account_id

        setting_type: str | Unset = UNSET
        if not isinstance(self.setting_type, Unset):
            setting_type = self.setting_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if ssl_enabled is not UNSET:
            field_dict["sslEnabled"] = ssl_enabled
        if referrals_enabled is not UNSET:
            field_dict["referralsEnabled"] = referrals_enabled
        if max_referral_hops is not UNSET:
            field_dict["maxReferralHops"] = max_referral_hops
        if bind_dn is not UNSET:
            field_dict["bindDN"] = bind_dn
        if bind_password is not UNSET:
            field_dict["bindPassword"] = bind_password
        if encrypted_bind_password is not UNSET:
            field_dict["encryptedBindPassword"] = encrypted_bind_password
        if password_type is not UNSET:
            field_dict["passwordType"] = password_type
        if bind_secret is not UNSET:
            field_dict["bindSecret"] = bind_secret
        if encrypted_bind_secret is not UNSET:
            field_dict["encryptedBindSecret"] = encrypted_bind_secret
        if connect_timeout is not UNSET:
            field_dict["connectTimeout"] = connect_timeout
        if response_timeout is not UNSET:
            field_dict["responseTimeout"] = response_timeout
        if use_recursive_group_membership_search is not UNSET:
            field_dict["useRecursiveGroupMembershipSearch"] = use_recursive_group_membership_search
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if password_ref is not UNSET:
            field_dict["passwordRef"] = password_ref
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if setting_type is not UNSET:
            field_dict["settingType"] = setting_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        port = d.pop("port", UNSET)

        ssl_enabled = d.pop("sslEnabled", UNSET)

        referrals_enabled = d.pop("referralsEnabled", UNSET)

        max_referral_hops = d.pop("maxReferralHops", UNSET)

        bind_dn = d.pop("bindDN", UNSET)

        bind_password = d.pop("bindPassword", UNSET)

        encrypted_bind_password = d.pop("encryptedBindPassword", UNSET)

        password_type = d.pop("passwordType", UNSET)

        bind_secret = cast(list[str], d.pop("bindSecret", UNSET))

        encrypted_bind_secret = d.pop("encryptedBindSecret", UNSET)

        connect_timeout = d.pop("connectTimeout", UNSET)

        response_timeout = d.pop("responseTimeout", UNSET)

        use_recursive_group_membership_search = d.pop("useRecursiveGroupMembershipSearch", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        password_ref = d.pop("passwordRef", UNSET)

        account_id = d.pop("accountId", UNSET)

        _setting_type = d.pop("settingType", UNSET)
        setting_type: LdapConnectionSettingsSettingType | Unset
        if isinstance(_setting_type, Unset):
            setting_type = UNSET
        else:
            setting_type = check_ldap_connection_settings_setting_type(_setting_type)

        ldap_connection_settings = cls(
            host=host,
            port=port,
            ssl_enabled=ssl_enabled,
            referrals_enabled=referrals_enabled,
            max_referral_hops=max_referral_hops,
            bind_dn=bind_dn,
            bind_password=bind_password,
            encrypted_bind_password=encrypted_bind_password,
            password_type=password_type,
            bind_secret=bind_secret,
            encrypted_bind_secret=encrypted_bind_secret,
            connect_timeout=connect_timeout,
            response_timeout=response_timeout,
            use_recursive_group_membership_search=use_recursive_group_membership_search,
            delegate_selectors=delegate_selectors,
            password_ref=password_ref,
            account_id=account_id,
            setting_type=setting_type,
        )

        ldap_connection_settings.additional_properties = d
        return ldap_connection_settings

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
