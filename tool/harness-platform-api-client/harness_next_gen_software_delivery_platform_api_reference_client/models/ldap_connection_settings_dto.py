from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapConnectionSettingsDTO")


@_attrs_define
class LdapConnectionSettingsDTO:
    """Ldap Connection Settings DTO

    Attributes:
        host (str | Unset):
        port (int | Unset):
        ssl_enabled (bool | Unset):
        referrals_enabled (bool | Unset):
        secret_ref_path (str | Unset):
        max_referral_hops (int | Unset):
        connection_timeout (int | Unset):
        response_timeout (int | Unset):
        use_recursive_group_membership_search (bool | Unset):
        bind_d_n (str | Unset):
        delegate_selectors (list[str] | Unset):
    """

    host: str | Unset = UNSET
    port: int | Unset = UNSET
    ssl_enabled: bool | Unset = UNSET
    referrals_enabled: bool | Unset = UNSET
    secret_ref_path: str | Unset = UNSET
    max_referral_hops: int | Unset = UNSET
    connection_timeout: int | Unset = UNSET
    response_timeout: int | Unset = UNSET
    use_recursive_group_membership_search: bool | Unset = UNSET
    bind_d_n: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        ssl_enabled = self.ssl_enabled

        referrals_enabled = self.referrals_enabled

        secret_ref_path = self.secret_ref_path

        max_referral_hops = self.max_referral_hops

        connection_timeout = self.connection_timeout

        response_timeout = self.response_timeout

        use_recursive_group_membership_search = self.use_recursive_group_membership_search

        bind_d_n = self.bind_d_n

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if ssl_enabled is not UNSET:
            field_dict["ssl_enabled"] = ssl_enabled
        if referrals_enabled is not UNSET:
            field_dict["referrals_enabled"] = referrals_enabled
        if secret_ref_path is not UNSET:
            field_dict["secret_ref_path"] = secret_ref_path
        if max_referral_hops is not UNSET:
            field_dict["max_referral_hops"] = max_referral_hops
        if connection_timeout is not UNSET:
            field_dict["connection_timeout"] = connection_timeout
        if response_timeout is not UNSET:
            field_dict["response_timeout"] = response_timeout
        if use_recursive_group_membership_search is not UNSET:
            field_dict["use_recursive_group_membership_search"] = use_recursive_group_membership_search
        if bind_d_n is not UNSET:
            field_dict["bind_d_n"] = bind_d_n
        if delegate_selectors is not UNSET:
            field_dict["delegate_selectors"] = delegate_selectors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        ssl_enabled = d.pop("ssl_enabled", UNSET)

        referrals_enabled = d.pop("referrals_enabled", UNSET)

        secret_ref_path = d.pop("secret_ref_path", UNSET)

        max_referral_hops = d.pop("max_referral_hops", UNSET)

        connection_timeout = d.pop("connection_timeout", UNSET)

        response_timeout = d.pop("response_timeout", UNSET)

        use_recursive_group_membership_search = d.pop("use_recursive_group_membership_search", UNSET)

        bind_d_n = d.pop("bind_d_n", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegate_selectors", UNSET))

        ldap_connection_settings_dto = cls(
            host=host,
            port=port,
            ssl_enabled=ssl_enabled,
            referrals_enabled=referrals_enabled,
            secret_ref_path=secret_ref_path,
            max_referral_hops=max_referral_hops,
            connection_timeout=connection_timeout,
            response_timeout=response_timeout,
            use_recursive_group_membership_search=use_recursive_group_membership_search,
            bind_d_n=bind_d_n,
            delegate_selectors=delegate_selectors,
        )

        ldap_connection_settings_dto.additional_properties = d
        return ldap_connection_settings_dto

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
