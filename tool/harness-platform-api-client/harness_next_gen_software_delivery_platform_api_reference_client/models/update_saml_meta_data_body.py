from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_data_content_disposition import FormDataContentDisposition
    from ..models.update_saml_meta_data_body_file import UpdateSamlMetaDataBodyFile


T = TypeVar("T", bound="UpdateSamlMetaDataBody")


@_attrs_define
class UpdateSamlMetaDataBody:
    """
    Attributes:
        file (UpdateSamlMetaDataBodyFile | Unset): SAML Metadata input file
        file_metadata (FormDataContentDisposition | Unset):
        display_name (str | Unset): Display Name of the SAML
        group_membership_attr (str | Unset): Group membership attribute
        authorization_enabled (bool | Unset): Specify whether or not to enable authorization
        logout_url (str | Unset): Logout URL
        entity_identifier (str | Unset): SAML metadata Identifier
        saml_provider_type (str | Unset): SAML provider type
        client_id (str | Unset): Optional SAML clientId for Azure SSO
        client_secret (str | Unset): Optional SAML clientSecret reference string for Azure SSO
        jit_enabled (bool | Unset): Enable Just in time user provision Default: False.
        jit_validation_key (str | Unset): Optional Key to match in SAML assertion for Just in time user provision
        jit_validation_value (str | Unset): Optional Value to match in SAML assertion for Just in time user provision
    """

    file: UpdateSamlMetaDataBodyFile | Unset = UNSET
    file_metadata: FormDataContentDisposition | Unset = UNSET
    display_name: str | Unset = UNSET
    group_membership_attr: str | Unset = UNSET
    authorization_enabled: bool | Unset = UNSET
    logout_url: str | Unset = UNSET
    entity_identifier: str | Unset = UNSET
    saml_provider_type: str | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    jit_enabled: bool | Unset = False
    jit_validation_key: str | Unset = UNSET
    jit_validation_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        file_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_metadata, Unset):
            file_metadata = self.file_metadata.to_dict()

        display_name = self.display_name

        group_membership_attr = self.group_membership_attr

        authorization_enabled = self.authorization_enabled

        logout_url = self.logout_url

        entity_identifier = self.entity_identifier

        saml_provider_type = self.saml_provider_type

        client_id = self.client_id

        client_secret = self.client_secret

        jit_enabled = self.jit_enabled

        jit_validation_key = self.jit_validation_key

        jit_validation_value = self.jit_validation_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if file_metadata is not UNSET:
            field_dict["fileMetadata"] = file_metadata
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if group_membership_attr is not UNSET:
            field_dict["groupMembershipAttr"] = group_membership_attr
        if authorization_enabled is not UNSET:
            field_dict["authorizationEnabled"] = authorization_enabled
        if logout_url is not UNSET:
            field_dict["logoutUrl"] = logout_url
        if entity_identifier is not UNSET:
            field_dict["entityIdentifier"] = entity_identifier
        if saml_provider_type is not UNSET:
            field_dict["samlProviderType"] = saml_provider_type
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if jit_enabled is not UNSET:
            field_dict["jitEnabled"] = jit_enabled
        if jit_validation_key is not UNSET:
            field_dict["jitValidationKey"] = jit_validation_key
        if jit_validation_value is not UNSET:
            field_dict["jitValidationValue"] = jit_validation_value

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.file, Unset):
            files.append(("file", (None, json.dumps(self.file.to_dict()).encode(), "application/json")))

        if not isinstance(self.file_metadata, Unset):
            files.append(
                ("fileMetadata", (None, json.dumps(self.file_metadata.to_dict()).encode(), "application/json"))
            )

        if not isinstance(self.display_name, Unset):
            files.append(("displayName", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.group_membership_attr, Unset):
            files.append(("groupMembershipAttr", (None, str(self.group_membership_attr).encode(), "text/plain")))

        if not isinstance(self.authorization_enabled, Unset):
            files.append(("authorizationEnabled", (None, str(self.authorization_enabled).encode(), "text/plain")))

        if not isinstance(self.logout_url, Unset):
            files.append(("logoutUrl", (None, str(self.logout_url).encode(), "text/plain")))

        if not isinstance(self.entity_identifier, Unset):
            files.append(("entityIdentifier", (None, str(self.entity_identifier).encode(), "text/plain")))

        if not isinstance(self.saml_provider_type, Unset):
            files.append(("samlProviderType", (None, str(self.saml_provider_type).encode(), "text/plain")))

        if not isinstance(self.client_id, Unset):
            files.append(("clientId", (None, str(self.client_id).encode(), "text/plain")))

        if not isinstance(self.client_secret, Unset):
            files.append(("clientSecret", (None, str(self.client_secret).encode(), "text/plain")))

        if not isinstance(self.jit_enabled, Unset):
            files.append(("jitEnabled", (None, str(self.jit_enabled).encode(), "text/plain")))

        if not isinstance(self.jit_validation_key, Unset):
            files.append(("jitValidationKey", (None, str(self.jit_validation_key).encode(), "text/plain")))

        if not isinstance(self.jit_validation_value, Unset):
            files.append(("jitValidationValue", (None, str(self.jit_validation_value).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_data_content_disposition import FormDataContentDisposition
        from ..models.update_saml_meta_data_body_file import UpdateSamlMetaDataBodyFile

        d = dict(src_dict)
        _file = d.pop("file", UNSET)
        file: UpdateSamlMetaDataBodyFile | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = UpdateSamlMetaDataBodyFile.from_dict(_file)

        _file_metadata = d.pop("fileMetadata", UNSET)
        file_metadata: FormDataContentDisposition | Unset
        if isinstance(_file_metadata, Unset):
            file_metadata = UNSET
        else:
            file_metadata = FormDataContentDisposition.from_dict(_file_metadata)

        display_name = d.pop("displayName", UNSET)

        group_membership_attr = d.pop("groupMembershipAttr", UNSET)

        authorization_enabled = d.pop("authorizationEnabled", UNSET)

        logout_url = d.pop("logoutUrl", UNSET)

        entity_identifier = d.pop("entityIdentifier", UNSET)

        saml_provider_type = d.pop("samlProviderType", UNSET)

        client_id = d.pop("clientId", UNSET)

        client_secret = d.pop("clientSecret", UNSET)

        jit_enabled = d.pop("jitEnabled", UNSET)

        jit_validation_key = d.pop("jitValidationKey", UNSET)

        jit_validation_value = d.pop("jitValidationValue", UNSET)

        update_saml_meta_data_body = cls(
            file=file,
            file_metadata=file_metadata,
            display_name=display_name,
            group_membership_attr=group_membership_attr,
            authorization_enabled=authorization_enabled,
            logout_url=logout_url,
            entity_identifier=entity_identifier,
            saml_provider_type=saml_provider_type,
            client_id=client_id,
            client_secret=client_secret,
            jit_enabled=jit_enabled,
            jit_validation_key=jit_validation_key,
            jit_validation_value=jit_validation_value,
        )

        update_saml_meta_data_body.additional_properties = d
        return update_saml_meta_data_body

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
