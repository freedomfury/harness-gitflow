from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.encryption_config_encryption_type import (
    EncryptionConfigEncryptionType,
    check_encryption_config_encryption_type,
)
from ..models.encryption_config_type import EncryptionConfigType, check_encryption_config_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="EncryptionConfig")


@_attrs_define
class EncryptionConfig:
    """
    Attributes:
        encryption_type (EncryptionConfigEncryptionType | Unset):
        num_of_encrypted_value (int | Unset):
        encryption_service_url (str | Unset):
        validation_criteria (str | Unset):
        global_kms (bool | Unset):
        name (str | Unset):
        type_ (EncryptionConfigType | Unset):
        default (bool | Unset):
        account_id (str | Unset):
        uuid (str | Unset):
    """

    encryption_type: EncryptionConfigEncryptionType | Unset = UNSET
    num_of_encrypted_value: int | Unset = UNSET
    encryption_service_url: str | Unset = UNSET
    validation_criteria: str | Unset = UNSET
    global_kms: bool | Unset = UNSET
    name: str | Unset = UNSET
    type_: EncryptionConfigType | Unset = UNSET
    default: bool | Unset = UNSET
    account_id: str | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption_type: str | Unset = UNSET
        if not isinstance(self.encryption_type, Unset):
            encryption_type = self.encryption_type

        num_of_encrypted_value = self.num_of_encrypted_value

        encryption_service_url = self.encryption_service_url

        validation_criteria = self.validation_criteria

        global_kms = self.global_kms

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        default = self.default

        account_id = self.account_id

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encryption_type is not UNSET:
            field_dict["encryptionType"] = encryption_type
        if num_of_encrypted_value is not UNSET:
            field_dict["numOfEncryptedValue"] = num_of_encrypted_value
        if encryption_service_url is not UNSET:
            field_dict["encryptionServiceUrl"] = encryption_service_url
        if validation_criteria is not UNSET:
            field_dict["validationCriteria"] = validation_criteria
        if global_kms is not UNSET:
            field_dict["globalKms"] = global_kms
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if default is not UNSET:
            field_dict["default"] = default
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _encryption_type = d.pop("encryptionType", UNSET)
        encryption_type: EncryptionConfigEncryptionType | Unset
        if isinstance(_encryption_type, Unset):
            encryption_type = UNSET
        else:
            encryption_type = check_encryption_config_encryption_type(_encryption_type)

        num_of_encrypted_value = d.pop("numOfEncryptedValue", UNSET)

        encryption_service_url = d.pop("encryptionServiceUrl", UNSET)

        validation_criteria = d.pop("validationCriteria", UNSET)

        global_kms = d.pop("globalKms", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EncryptionConfigType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_encryption_config_type(_type_)

        default = d.pop("default", UNSET)

        account_id = d.pop("accountId", UNSET)

        uuid = d.pop("uuid", UNSET)

        encryption_config = cls(
            encryption_type=encryption_type,
            num_of_encrypted_value=num_of_encrypted_value,
            encryption_service_url=encryption_service_url,
            validation_criteria=validation_criteria,
            global_kms=global_kms,
            name=name,
            type_=type_,
            default=default,
            account_id=account_id,
            uuid=uuid,
        )

        encryption_config.additional_properties = d
        return encryption_config

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
