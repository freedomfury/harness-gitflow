from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.encrypted_record_data_backup_encryption_type import (
    EncryptedRecordDataBackupEncryptionType,
    check_encrypted_record_data_backup_encryption_type,
)
from ..models.encrypted_record_data_encryption_type import (
    EncryptedRecordDataEncryptionType,
    check_encrypted_record_data_encryption_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_metadata import AdditionalMetadata
    from ..models.encrypted_data_params import EncryptedDataParams


T = TypeVar("T", bound="EncryptedRecordData")


@_attrs_define
class EncryptedRecordData:
    """
    Attributes:
        uuid (str | Unset):
        name (str | Unset):
        path (str | Unset):
        parameters (list[EncryptedDataParams] | Unset):
        encryption_key (str | Unset):
        encrypted_value (list[str] | Unset):
        kms_id (str | Unset):
        encryption_type (EncryptedRecordDataEncryptionType | Unset):
        backup_encrypted_value (list[str] | Unset):
        backup_encryption_key (str | Unset):
        backup_kms_id (str | Unset):
        backup_encryption_type (EncryptedRecordDataBackupEncryptionType | Unset):
        base_64_encoded (bool | Unset):
        additional_metadata (AdditionalMetadata | Unset): Additional metadata for the secret
    """

    uuid: str | Unset = UNSET
    name: str | Unset = UNSET
    path: str | Unset = UNSET
    parameters: list[EncryptedDataParams] | Unset = UNSET
    encryption_key: str | Unset = UNSET
    encrypted_value: list[str] | Unset = UNSET
    kms_id: str | Unset = UNSET
    encryption_type: EncryptedRecordDataEncryptionType | Unset = UNSET
    backup_encrypted_value: list[str] | Unset = UNSET
    backup_encryption_key: str | Unset = UNSET
    backup_kms_id: str | Unset = UNSET
    backup_encryption_type: EncryptedRecordDataBackupEncryptionType | Unset = UNSET
    base_64_encoded: bool | Unset = UNSET
    additional_metadata: AdditionalMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

        path = self.path

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        encryption_key = self.encryption_key

        encrypted_value: list[str] | Unset = UNSET
        if not isinstance(self.encrypted_value, Unset):
            encrypted_value = self.encrypted_value

        kms_id = self.kms_id

        encryption_type: str | Unset = UNSET
        if not isinstance(self.encryption_type, Unset):
            encryption_type = self.encryption_type

        backup_encrypted_value: list[str] | Unset = UNSET
        if not isinstance(self.backup_encrypted_value, Unset):
            backup_encrypted_value = self.backup_encrypted_value

        backup_encryption_key = self.backup_encryption_key

        backup_kms_id = self.backup_kms_id

        backup_encryption_type: str | Unset = UNSET
        if not isinstance(self.backup_encryption_type, Unset):
            backup_encryption_type = self.backup_encryption_type

        base_64_encoded = self.base_64_encoded

        additional_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_metadata, Unset):
            additional_metadata = self.additional_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if encryption_key is not UNSET:
            field_dict["encryptionKey"] = encryption_key
        if encrypted_value is not UNSET:
            field_dict["encryptedValue"] = encrypted_value
        if kms_id is not UNSET:
            field_dict["kmsId"] = kms_id
        if encryption_type is not UNSET:
            field_dict["encryptionType"] = encryption_type
        if backup_encrypted_value is not UNSET:
            field_dict["backupEncryptedValue"] = backup_encrypted_value
        if backup_encryption_key is not UNSET:
            field_dict["backupEncryptionKey"] = backup_encryption_key
        if backup_kms_id is not UNSET:
            field_dict["backupKmsId"] = backup_kms_id
        if backup_encryption_type is not UNSET:
            field_dict["backupEncryptionType"] = backup_encryption_type
        if base_64_encoded is not UNSET:
            field_dict["base64Encoded"] = base_64_encoded
        if additional_metadata is not UNSET:
            field_dict["additionalMetadata"] = additional_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.additional_metadata import AdditionalMetadata
        from ..models.encrypted_data_params import EncryptedDataParams

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[EncryptedDataParams] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = EncryptedDataParams.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        encryption_key = d.pop("encryptionKey", UNSET)

        encrypted_value = cast(list[str], d.pop("encryptedValue", UNSET))

        kms_id = d.pop("kmsId", UNSET)

        _encryption_type = d.pop("encryptionType", UNSET)
        encryption_type: EncryptedRecordDataEncryptionType | Unset
        if isinstance(_encryption_type, Unset):
            encryption_type = UNSET
        else:
            encryption_type = check_encrypted_record_data_encryption_type(_encryption_type)

        backup_encrypted_value = cast(list[str], d.pop("backupEncryptedValue", UNSET))

        backup_encryption_key = d.pop("backupEncryptionKey", UNSET)

        backup_kms_id = d.pop("backupKmsId", UNSET)

        _backup_encryption_type = d.pop("backupEncryptionType", UNSET)
        backup_encryption_type: EncryptedRecordDataBackupEncryptionType | Unset
        if isinstance(_backup_encryption_type, Unset):
            backup_encryption_type = UNSET
        else:
            backup_encryption_type = check_encrypted_record_data_backup_encryption_type(_backup_encryption_type)

        base_64_encoded = d.pop("base64Encoded", UNSET)

        _additional_metadata = d.pop("additionalMetadata", UNSET)
        additional_metadata: AdditionalMetadata | Unset
        if isinstance(_additional_metadata, Unset):
            additional_metadata = UNSET
        else:
            additional_metadata = AdditionalMetadata.from_dict(_additional_metadata)

        encrypted_record_data = cls(
            uuid=uuid,
            name=name,
            path=path,
            parameters=parameters,
            encryption_key=encryption_key,
            encrypted_value=encrypted_value,
            kms_id=kms_id,
            encryption_type=encryption_type,
            backup_encrypted_value=backup_encrypted_value,
            backup_encryption_key=backup_encryption_key,
            backup_kms_id=backup_kms_id,
            backup_encryption_type=backup_encryption_type,
            base_64_encoded=base_64_encoded,
            additional_metadata=additional_metadata,
        )

        encrypted_record_data.additional_properties = d
        return encrypted_record_data

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
