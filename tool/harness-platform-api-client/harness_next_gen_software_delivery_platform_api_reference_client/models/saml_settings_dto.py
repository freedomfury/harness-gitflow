from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saml_settings_dto_provider_type import SamlSettingsDTOProviderType, check_saml_settings_dto_provider_type
from ..models.saml_settings_dto_saml_provider_type import (
    SamlSettingsDTOSamlProviderType,
    check_saml_settings_dto_saml_provider_type,
)
from ..models.saml_settings_dto_type import SamlSettingsDTOType, check_saml_settings_dto_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SamlSettingsDTO")


@_attrs_define
class SamlSettingsDTO:
    """
    Attributes:
        type_ (SamlSettingsDTOType):
        display_name (str):
        url (str):
        account_id (str):
        origin (str):
        meta_data_file (str | Unset):
        group_membership_attr (str | Unset):
        logout_url (str | Unset):
        entity_identifier (str | Unset):
        provider_type (SamlSettingsDTOProviderType | Unset):
        client_id (str | Unset):
        client_secret (list[str] | Unset):
        friendly_saml_name (str | Unset):
        jit_enabled (bool | Unset):
        jit_validation_key (str | Unset):
        jit_validation_value (str | Unset):
        uuid (str | Unset):
        next_iterations (list[int] | Unset):
        saml_provider_type (SamlSettingsDTOSamlProviderType | Unset):
        encrypted_client_secret (str | Unset):
        configured_from_ng (bool | Unset):
        authentication_enabled (bool | Unset):
        authorization_enabled (bool | Unset):
    """

    type_: SamlSettingsDTOType
    display_name: str
    url: str
    account_id: str
    origin: str
    meta_data_file: str | Unset = UNSET
    group_membership_attr: str | Unset = UNSET
    logout_url: str | Unset = UNSET
    entity_identifier: str | Unset = UNSET
    provider_type: SamlSettingsDTOProviderType | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret: list[str] | Unset = UNSET
    friendly_saml_name: str | Unset = UNSET
    jit_enabled: bool | Unset = UNSET
    jit_validation_key: str | Unset = UNSET
    jit_validation_value: str | Unset = UNSET
    uuid: str | Unset = UNSET
    next_iterations: list[int] | Unset = UNSET
    saml_provider_type: SamlSettingsDTOSamlProviderType | Unset = UNSET
    encrypted_client_secret: str | Unset = UNSET
    configured_from_ng: bool | Unset = UNSET
    authentication_enabled: bool | Unset = UNSET
    authorization_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        display_name = self.display_name

        url = self.url

        account_id = self.account_id

        origin = self.origin

        meta_data_file = self.meta_data_file

        group_membership_attr = self.group_membership_attr

        logout_url = self.logout_url

        entity_identifier = self.entity_identifier

        provider_type: str | Unset = UNSET
        if not isinstance(self.provider_type, Unset):
            provider_type = self.provider_type

        client_id = self.client_id

        client_secret: list[str] | Unset = UNSET
        if not isinstance(self.client_secret, Unset):
            client_secret = self.client_secret

        friendly_saml_name = self.friendly_saml_name

        jit_enabled = self.jit_enabled

        jit_validation_key = self.jit_validation_key

        jit_validation_value = self.jit_validation_value

        uuid = self.uuid

        next_iterations: list[int] | Unset = UNSET
        if not isinstance(self.next_iterations, Unset):
            next_iterations = self.next_iterations

        saml_provider_type: str | Unset = UNSET
        if not isinstance(self.saml_provider_type, Unset):
            saml_provider_type = self.saml_provider_type

        encrypted_client_secret = self.encrypted_client_secret

        configured_from_ng = self.configured_from_ng

        authentication_enabled = self.authentication_enabled

        authorization_enabled = self.authorization_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "displayName": display_name,
                "url": url,
                "accountId": account_id,
                "origin": origin,
            }
        )
        if meta_data_file is not UNSET:
            field_dict["metaDataFile"] = meta_data_file
        if group_membership_attr is not UNSET:
            field_dict["groupMembershipAttr"] = group_membership_attr
        if logout_url is not UNSET:
            field_dict["logoutUrl"] = logout_url
        if entity_identifier is not UNSET:
            field_dict["entityIdentifier"] = entity_identifier
        if provider_type is not UNSET:
            field_dict["providerType"] = provider_type
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if friendly_saml_name is not UNSET:
            field_dict["friendlySamlName"] = friendly_saml_name
        if jit_enabled is not UNSET:
            field_dict["jitEnabled"] = jit_enabled
        if jit_validation_key is not UNSET:
            field_dict["jitValidationKey"] = jit_validation_key
        if jit_validation_value is not UNSET:
            field_dict["jitValidationValue"] = jit_validation_value
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if next_iterations is not UNSET:
            field_dict["nextIterations"] = next_iterations
        if saml_provider_type is not UNSET:
            field_dict["samlProviderType"] = saml_provider_type
        if encrypted_client_secret is not UNSET:
            field_dict["encryptedClientSecret"] = encrypted_client_secret
        if configured_from_ng is not UNSET:
            field_dict["configuredFromNG"] = configured_from_ng
        if authentication_enabled is not UNSET:
            field_dict["authenticationEnabled"] = authentication_enabled
        if authorization_enabled is not UNSET:
            field_dict["authorizationEnabled"] = authorization_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = check_saml_settings_dto_type(d.pop("type"))

        display_name = d.pop("displayName")

        url = d.pop("url")

        account_id = d.pop("accountId")

        origin = d.pop("origin")

        meta_data_file = d.pop("metaDataFile", UNSET)

        group_membership_attr = d.pop("groupMembershipAttr", UNSET)

        logout_url = d.pop("logoutUrl", UNSET)

        entity_identifier = d.pop("entityIdentifier", UNSET)

        _provider_type = d.pop("providerType", UNSET)
        provider_type: SamlSettingsDTOProviderType | Unset
        if isinstance(_provider_type, Unset):
            provider_type = UNSET
        else:
            provider_type = check_saml_settings_dto_provider_type(_provider_type)

        client_id = d.pop("clientId", UNSET)

        client_secret = cast(list[str], d.pop("clientSecret", UNSET))

        friendly_saml_name = d.pop("friendlySamlName", UNSET)

        jit_enabled = d.pop("jitEnabled", UNSET)

        jit_validation_key = d.pop("jitValidationKey", UNSET)

        jit_validation_value = d.pop("jitValidationValue", UNSET)

        uuid = d.pop("uuid", UNSET)

        next_iterations = cast(list[int], d.pop("nextIterations", UNSET))

        _saml_provider_type = d.pop("samlProviderType", UNSET)
        saml_provider_type: SamlSettingsDTOSamlProviderType | Unset
        if isinstance(_saml_provider_type, Unset):
            saml_provider_type = UNSET
        else:
            saml_provider_type = check_saml_settings_dto_saml_provider_type(_saml_provider_type)

        encrypted_client_secret = d.pop("encryptedClientSecret", UNSET)

        configured_from_ng = d.pop("configuredFromNG", UNSET)

        authentication_enabled = d.pop("authenticationEnabled", UNSET)

        authorization_enabled = d.pop("authorizationEnabled", UNSET)

        saml_settings_dto = cls(
            type_=type_,
            display_name=display_name,
            url=url,
            account_id=account_id,
            origin=origin,
            meta_data_file=meta_data_file,
            group_membership_attr=group_membership_attr,
            logout_url=logout_url,
            entity_identifier=entity_identifier,
            provider_type=provider_type,
            client_id=client_id,
            client_secret=client_secret,
            friendly_saml_name=friendly_saml_name,
            jit_enabled=jit_enabled,
            jit_validation_key=jit_validation_key,
            jit_validation_value=jit_validation_value,
            uuid=uuid,
            next_iterations=next_iterations,
            saml_provider_type=saml_provider_type,
            encrypted_client_secret=encrypted_client_secret,
            configured_from_ng=configured_from_ng,
            authentication_enabled=authentication_enabled,
            authorization_enabled=authorization_enabled,
        )

        saml_settings_dto.additional_properties = d
        return saml_settings_dto

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
