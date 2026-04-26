from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sso_config_authentication_mechanism import (
    SSOConfigAuthenticationMechanism,
    check_sso_config_authentication_mechanism,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sso_settings_dto import SSOSettingsDTO


T = TypeVar("T", bound="SSOConfig")


@_attrs_define
class SSOConfig:
    """
    Attributes:
        account_id (str | Unset):
        sso_settings (list[SSOSettingsDTO] | Unset):
        authentication_mechanism (SSOConfigAuthenticationMechanism | Unset):
    """

    account_id: str | Unset = UNSET
    sso_settings: list[SSOSettingsDTO] | Unset = UNSET
    authentication_mechanism: SSOConfigAuthenticationMechanism | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        sso_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sso_settings, Unset):
            sso_settings = []
            for sso_settings_item_data in self.sso_settings:
                sso_settings_item = sso_settings_item_data.to_dict()
                sso_settings.append(sso_settings_item)

        authentication_mechanism: str | Unset = UNSET
        if not isinstance(self.authentication_mechanism, Unset):
            authentication_mechanism = self.authentication_mechanism

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if sso_settings is not UNSET:
            field_dict["ssoSettings"] = sso_settings
        if authentication_mechanism is not UNSET:
            field_dict["authenticationMechanism"] = authentication_mechanism

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sso_settings_dto import SSOSettingsDTO

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        _sso_settings = d.pop("ssoSettings", UNSET)
        sso_settings: list[SSOSettingsDTO] | Unset = UNSET
        if _sso_settings is not UNSET:
            sso_settings = []
            for sso_settings_item_data in _sso_settings:
                sso_settings_item = SSOSettingsDTO.from_dict(sso_settings_item_data)

                sso_settings.append(sso_settings_item)

        _authentication_mechanism = d.pop("authenticationMechanism", UNSET)
        authentication_mechanism: SSOConfigAuthenticationMechanism | Unset
        if isinstance(_authentication_mechanism, Unset):
            authentication_mechanism = UNSET
        else:
            authentication_mechanism = check_sso_config_authentication_mechanism(_authentication_mechanism)

        sso_config = cls(
            account_id=account_id,
            sso_settings=sso_settings,
            authentication_mechanism=authentication_mechanism,
        )

        sso_config.additional_properties = d
        return sso_config

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
