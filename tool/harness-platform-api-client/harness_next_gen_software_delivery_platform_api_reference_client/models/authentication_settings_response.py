from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.authentication_settings_response_authentication_mechanism import (
    AuthenticationSettingsResponseAuthenticationMechanism,
    check_authentication_settings_response_authentication_mechanism,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ng_auth_settings import NGAuthSettings


T = TypeVar("T", bound="AuthenticationSettingsResponse")


@_attrs_define
class AuthenticationSettingsResponse:
    """This contains information on the Authentication Settings defined in Harness.

    Attributes:
        ng_auth_settings (list[NGAuthSettings] | Unset): List of Auth Settings configured for an Account.
        whitelisted_domains (list[str] | Unset): List of the whitelisted domains.
        authentication_mechanism (AuthenticationSettingsResponseAuthenticationMechanism | Unset): Indicates if the
            Authentication Mechanism is SSO or NON-SSO.
        two_factor_enabled (bool | Unset): If Two Factor Authentication is enabled, this value is true. Otherwise, it is
            false.
        session_timeout_in_minutes (int | Unset): Any user of this account will be logged out if there is no activity
            for this number of minutes
        public_access_enabled (bool | Unset): If public access is enabled, this value is true. Otherwise, it is false.
        oauth_enabled (bool | Unset): If OAUTH is enabled
        absolute_session_timeout_in_minutes (int | Unset): Any user of this account will be logged out after this number
            of minutes
    """

    ng_auth_settings: list[NGAuthSettings] | Unset = UNSET
    whitelisted_domains: list[str] | Unset = UNSET
    authentication_mechanism: AuthenticationSettingsResponseAuthenticationMechanism | Unset = UNSET
    two_factor_enabled: bool | Unset = UNSET
    session_timeout_in_minutes: int | Unset = UNSET
    public_access_enabled: bool | Unset = UNSET
    oauth_enabled: bool | Unset = UNSET
    absolute_session_timeout_in_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ng_auth_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ng_auth_settings, Unset):
            ng_auth_settings = []
            for ng_auth_settings_item_data in self.ng_auth_settings:
                ng_auth_settings_item = ng_auth_settings_item_data.to_dict()
                ng_auth_settings.append(ng_auth_settings_item)

        whitelisted_domains: list[str] | Unset = UNSET
        if not isinstance(self.whitelisted_domains, Unset):
            whitelisted_domains = self.whitelisted_domains

        authentication_mechanism: str | Unset = UNSET
        if not isinstance(self.authentication_mechanism, Unset):
            authentication_mechanism = self.authentication_mechanism

        two_factor_enabled = self.two_factor_enabled

        session_timeout_in_minutes = self.session_timeout_in_minutes

        public_access_enabled = self.public_access_enabled

        oauth_enabled = self.oauth_enabled

        absolute_session_timeout_in_minutes = self.absolute_session_timeout_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ng_auth_settings is not UNSET:
            field_dict["ngAuthSettings"] = ng_auth_settings
        if whitelisted_domains is not UNSET:
            field_dict["whitelistedDomains"] = whitelisted_domains
        if authentication_mechanism is not UNSET:
            field_dict["authenticationMechanism"] = authentication_mechanism
        if two_factor_enabled is not UNSET:
            field_dict["twoFactorEnabled"] = two_factor_enabled
        if session_timeout_in_minutes is not UNSET:
            field_dict["sessionTimeoutInMinutes"] = session_timeout_in_minutes
        if public_access_enabled is not UNSET:
            field_dict["publicAccessEnabled"] = public_access_enabled
        if oauth_enabled is not UNSET:
            field_dict["oauthEnabled"] = oauth_enabled
        if absolute_session_timeout_in_minutes is not UNSET:
            field_dict["absoluteSessionTimeoutInMinutes"] = absolute_session_timeout_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ng_auth_settings import NGAuthSettings

        d = dict(src_dict)
        _ng_auth_settings = d.pop("ngAuthSettings", UNSET)
        ng_auth_settings: list[NGAuthSettings] | Unset = UNSET
        if _ng_auth_settings is not UNSET:
            ng_auth_settings = []
            for ng_auth_settings_item_data in _ng_auth_settings:
                ng_auth_settings_item = NGAuthSettings.from_dict(ng_auth_settings_item_data)

                ng_auth_settings.append(ng_auth_settings_item)

        whitelisted_domains = cast(list[str], d.pop("whitelistedDomains", UNSET))

        _authentication_mechanism = d.pop("authenticationMechanism", UNSET)
        authentication_mechanism: AuthenticationSettingsResponseAuthenticationMechanism | Unset
        if isinstance(_authentication_mechanism, Unset):
            authentication_mechanism = UNSET
        else:
            authentication_mechanism = check_authentication_settings_response_authentication_mechanism(
                _authentication_mechanism
            )

        two_factor_enabled = d.pop("twoFactorEnabled", UNSET)

        session_timeout_in_minutes = d.pop("sessionTimeoutInMinutes", UNSET)

        public_access_enabled = d.pop("publicAccessEnabled", UNSET)

        oauth_enabled = d.pop("oauthEnabled", UNSET)

        absolute_session_timeout_in_minutes = d.pop("absoluteSessionTimeoutInMinutes", UNSET)

        authentication_settings_response = cls(
            ng_auth_settings=ng_auth_settings,
            whitelisted_domains=whitelisted_domains,
            authentication_mechanism=authentication_mechanism,
            two_factor_enabled=two_factor_enabled,
            session_timeout_in_minutes=session_timeout_in_minutes,
            public_access_enabled=public_access_enabled,
            oauth_enabled=oauth_enabled,
            absolute_session_timeout_in_minutes=absolute_session_timeout_in_minutes,
        )

        authentication_settings_response.additional_properties = d
        return authentication_settings_response

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
