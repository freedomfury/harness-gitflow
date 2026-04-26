from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.two_factor_auth_settings_info_mechanism import (
    TwoFactorAuthSettingsInfoMechanism,
    check_two_factor_auth_settings_info_mechanism,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TwoFactorAuthSettingsInfo")


@_attrs_define
class TwoFactorAuthSettingsInfo:
    """
    Attributes:
        user_id (str | Unset):
        email (str | Unset):
        two_factor_authentication_enabled (bool | Unset):
        mechanism (TwoFactorAuthSettingsInfoMechanism | Unset):
        totp_secret_key (str | Unset):
        totpqrurl (str | Unset):
    """

    user_id: str | Unset = UNSET
    email: str | Unset = UNSET
    two_factor_authentication_enabled: bool | Unset = UNSET
    mechanism: TwoFactorAuthSettingsInfoMechanism | Unset = UNSET
    totp_secret_key: str | Unset = UNSET
    totpqrurl: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        email = self.email

        two_factor_authentication_enabled = self.two_factor_authentication_enabled

        mechanism: str | Unset = UNSET
        if not isinstance(self.mechanism, Unset):
            mechanism = self.mechanism

        totp_secret_key = self.totp_secret_key

        totpqrurl = self.totpqrurl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if email is not UNSET:
            field_dict["email"] = email
        if two_factor_authentication_enabled is not UNSET:
            field_dict["twoFactorAuthenticationEnabled"] = two_factor_authentication_enabled
        if mechanism is not UNSET:
            field_dict["mechanism"] = mechanism
        if totp_secret_key is not UNSET:
            field_dict["totpSecretKey"] = totp_secret_key
        if totpqrurl is not UNSET:
            field_dict["totpqrurl"] = totpqrurl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        email = d.pop("email", UNSET)

        two_factor_authentication_enabled = d.pop("twoFactorAuthenticationEnabled", UNSET)

        _mechanism = d.pop("mechanism", UNSET)
        mechanism: TwoFactorAuthSettingsInfoMechanism | Unset
        if isinstance(_mechanism, Unset):
            mechanism = UNSET
        else:
            mechanism = check_two_factor_auth_settings_info_mechanism(_mechanism)

        totp_secret_key = d.pop("totpSecretKey", UNSET)

        totpqrurl = d.pop("totpqrurl", UNSET)

        two_factor_auth_settings_info = cls(
            user_id=user_id,
            email=email,
            two_factor_authentication_enabled=two_factor_authentication_enabled,
            mechanism=mechanism,
            totp_secret_key=totp_secret_key,
            totpqrurl=totpqrurl,
        )

        two_factor_auth_settings_info.additional_properties = d
        return two_factor_auth_settings_info

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
