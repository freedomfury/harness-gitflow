from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encrypted_record_data import EncryptedRecordData
    from ..models.encryption_config import EncryptionConfig
    from ..models.secret_unique_identifier import SecretUniqueIdentifier


T = TypeVar("T", bound="EncryptedDataDetail")


@_attrs_define
class EncryptedDataDetail:
    """
    Attributes:
        encrypted_data (EncryptedRecordData | Unset):
        encryption_config (EncryptionConfig | Unset):
        field_name (str | Unset):
        identifier (SecretUniqueIdentifier | Unset):
    """

    encrypted_data: EncryptedRecordData | Unset = UNSET
    encryption_config: EncryptionConfig | Unset = UNSET
    field_name: str | Unset = UNSET
    identifier: SecretUniqueIdentifier | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encrypted_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encrypted_data, Unset):
            encrypted_data = self.encrypted_data.to_dict()

        encryption_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encryption_config, Unset):
            encryption_config = self.encryption_config.to_dict()

        field_name = self.field_name

        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encrypted_data is not UNSET:
            field_dict["encryptedData"] = encrypted_data
        if encryption_config is not UNSET:
            field_dict["encryptionConfig"] = encryption_config
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encrypted_record_data import EncryptedRecordData
        from ..models.encryption_config import EncryptionConfig
        from ..models.secret_unique_identifier import SecretUniqueIdentifier

        d = dict(src_dict)
        _encrypted_data = d.pop("encryptedData", UNSET)
        encrypted_data: EncryptedRecordData | Unset
        if isinstance(_encrypted_data, Unset):
            encrypted_data = UNSET
        else:
            encrypted_data = EncryptedRecordData.from_dict(_encrypted_data)

        _encryption_config = d.pop("encryptionConfig", UNSET)
        encryption_config: EncryptionConfig | Unset
        if isinstance(_encryption_config, Unset):
            encryption_config = UNSET
        else:
            encryption_config = EncryptionConfig.from_dict(_encryption_config)

        field_name = d.pop("fieldName", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: SecretUniqueIdentifier | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = SecretUniqueIdentifier.from_dict(_identifier)

        encrypted_data_detail = cls(
            encrypted_data=encrypted_data,
            encryption_config=encryption_config,
            field_name=field_name,
            identifier=identifier,
        )

        encrypted_data_detail.additional_properties = d
        return encrypted_data_detail

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
