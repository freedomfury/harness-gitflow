from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_settings_allowed_providers_item import (
    OAuthSettingsAllowedProvidersItem,
    check_o_auth_settings_allowed_providers_item,
)
from ..models.o_auth_settings_settings_type import OAuthSettingsSettingsType, check_o_auth_settings_settings_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthSettings")


@_attrs_define
class OAuthSettings:
    """This contains the information about OAuth settings defined in Harness.

    Attributes:
        filter_ (str | Unset): Filter out the available OAuth providers.
        allowed_providers (list[OAuthSettingsAllowedProvidersItem] | Unset): This is the list of OAuth Providers that
            are supported.
        settings_type (OAuthSettingsSettingsType | Unset):
    """

    filter_: str | Unset = UNSET
    allowed_providers: list[OAuthSettingsAllowedProvidersItem] | Unset = UNSET
    settings_type: OAuthSettingsSettingsType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        allowed_providers: list[str] | Unset = UNSET
        if not isinstance(self.allowed_providers, Unset):
            allowed_providers = []
            for allowed_providers_item_data in self.allowed_providers:
                allowed_providers_item: str = allowed_providers_item_data
                allowed_providers.append(allowed_providers_item)

        settings_type: str | Unset = UNSET
        if not isinstance(self.settings_type, Unset):
            settings_type = self.settings_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if allowed_providers is not UNSET:
            field_dict["allowedProviders"] = allowed_providers
        if settings_type is not UNSET:
            field_dict["settingsType"] = settings_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_ = d.pop("filter", UNSET)

        _allowed_providers = d.pop("allowedProviders", UNSET)
        allowed_providers: list[OAuthSettingsAllowedProvidersItem] | Unset = UNSET
        if _allowed_providers is not UNSET:
            allowed_providers = []
            for allowed_providers_item_data in _allowed_providers:
                allowed_providers_item = check_o_auth_settings_allowed_providers_item(allowed_providers_item_data)

                allowed_providers.append(allowed_providers_item)

        _settings_type = d.pop("settingsType", UNSET)
        settings_type: OAuthSettingsSettingsType | Unset
        if isinstance(_settings_type, Unset):
            settings_type = UNSET
        else:
            settings_type = check_o_auth_settings_settings_type(_settings_type)

        o_auth_settings = cls(
            filter_=filter_,
            allowed_providers=allowed_providers,
            settings_type=settings_type,
        )

        o_auth_settings.additional_properties = d
        return o_auth_settings

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
