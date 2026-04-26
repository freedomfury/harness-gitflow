from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sso_request_oauth_provider_type import SSORequestOauthProviderType, check_sso_request_oauth_provider_type
from ..models.sso_request_oauth_provider_types_item import (
    SSORequestOauthProviderTypesItem,
    check_sso_request_oauth_provider_types_item,
)
from ..models.sso_request_saml_provider_type import SSORequestSamlProviderType, check_sso_request_saml_provider_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SSORequest")


@_attrs_define
class SSORequest:
    """
    Attributes:
        oauth_provider_type (SSORequestOauthProviderType | Unset):
        idp_redirect_url (str | Unset):
        oauth_provider_types (list[SSORequestOauthProviderTypesItem] | Unset):
        sso_id (str | Unset):
        friendly_saml_name (str | Unset):
        saml_provider_type (SSORequestSamlProviderType | Unset):
    """

    oauth_provider_type: SSORequestOauthProviderType | Unset = UNSET
    idp_redirect_url: str | Unset = UNSET
    oauth_provider_types: list[SSORequestOauthProviderTypesItem] | Unset = UNSET
    sso_id: str | Unset = UNSET
    friendly_saml_name: str | Unset = UNSET
    saml_provider_type: SSORequestSamlProviderType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oauth_provider_type: str | Unset = UNSET
        if not isinstance(self.oauth_provider_type, Unset):
            oauth_provider_type = self.oauth_provider_type

        idp_redirect_url = self.idp_redirect_url

        oauth_provider_types: list[str] | Unset = UNSET
        if not isinstance(self.oauth_provider_types, Unset):
            oauth_provider_types = []
            for oauth_provider_types_item_data in self.oauth_provider_types:
                oauth_provider_types_item: str = oauth_provider_types_item_data
                oauth_provider_types.append(oauth_provider_types_item)

        sso_id = self.sso_id

        friendly_saml_name = self.friendly_saml_name

        saml_provider_type: str | Unset = UNSET
        if not isinstance(self.saml_provider_type, Unset):
            saml_provider_type = self.saml_provider_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oauth_provider_type is not UNSET:
            field_dict["oauthProviderType"] = oauth_provider_type
        if idp_redirect_url is not UNSET:
            field_dict["idpRedirectUrl"] = idp_redirect_url
        if oauth_provider_types is not UNSET:
            field_dict["oauthProviderTypes"] = oauth_provider_types
        if sso_id is not UNSET:
            field_dict["ssoId"] = sso_id
        if friendly_saml_name is not UNSET:
            field_dict["friendlySamlName"] = friendly_saml_name
        if saml_provider_type is not UNSET:
            field_dict["samlProviderType"] = saml_provider_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _oauth_provider_type = d.pop("oauthProviderType", UNSET)
        oauth_provider_type: SSORequestOauthProviderType | Unset
        if isinstance(_oauth_provider_type, Unset):
            oauth_provider_type = UNSET
        else:
            oauth_provider_type = check_sso_request_oauth_provider_type(_oauth_provider_type)

        idp_redirect_url = d.pop("idpRedirectUrl", UNSET)

        _oauth_provider_types = d.pop("oauthProviderTypes", UNSET)
        oauth_provider_types: list[SSORequestOauthProviderTypesItem] | Unset = UNSET
        if _oauth_provider_types is not UNSET:
            oauth_provider_types = []
            for oauth_provider_types_item_data in _oauth_provider_types:
                oauth_provider_types_item = check_sso_request_oauth_provider_types_item(oauth_provider_types_item_data)

                oauth_provider_types.append(oauth_provider_types_item)

        sso_id = d.pop("ssoId", UNSET)

        friendly_saml_name = d.pop("friendlySamlName", UNSET)

        _saml_provider_type = d.pop("samlProviderType", UNSET)
        saml_provider_type: SSORequestSamlProviderType | Unset
        if isinstance(_saml_provider_type, Unset):
            saml_provider_type = UNSET
        else:
            saml_provider_type = check_sso_request_saml_provider_type(_saml_provider_type)

        sso_request = cls(
            oauth_provider_type=oauth_provider_type,
            idp_redirect_url=idp_redirect_url,
            oauth_provider_types=oauth_provider_types,
            sso_id=sso_id,
            friendly_saml_name=friendly_saml_name,
            saml_provider_type=saml_provider_type,
        )

        sso_request.additional_properties = d
        return sso_request

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
