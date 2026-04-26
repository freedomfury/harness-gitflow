from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.secret_manager_metadata_dto_encryption_type import (
    SecretManagerMetadataDTOEncryptionType,
    check_secret_manager_metadata_dto_encryption_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret_manager_metadata_spec_dto import SecretManagerMetadataSpecDTO


T = TypeVar("T", bound="SecretManagerMetadataDTO")


@_attrs_define
class SecretManagerMetadataDTO:
    """
    Attributes:
        encryption_type (SecretManagerMetadataDTOEncryptionType | Unset):
        spec (SecretManagerMetadataSpecDTO | Unset):
    """

    encryption_type: SecretManagerMetadataDTOEncryptionType | Unset = UNSET
    spec: SecretManagerMetadataSpecDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption_type: str | Unset = UNSET
        if not isinstance(self.encryption_type, Unset):
            encryption_type = self.encryption_type

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encryption_type is not UNSET:
            field_dict["encryptionType"] = encryption_type
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secret_manager_metadata_spec_dto import SecretManagerMetadataSpecDTO

        d = dict(src_dict)
        _encryption_type = d.pop("encryptionType", UNSET)
        encryption_type: SecretManagerMetadataDTOEncryptionType | Unset
        if isinstance(_encryption_type, Unset):
            encryption_type = UNSET
        else:
            encryption_type = check_secret_manager_metadata_dto_encryption_type(_encryption_type)

        _spec = d.pop("spec", UNSET)
        spec: SecretManagerMetadataSpecDTO | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = SecretManagerMetadataSpecDTO.from_dict(_spec)

        secret_manager_metadata_dto = cls(
            encryption_type=encryption_type,
            spec=spec,
        )

        secret_manager_metadata_dto.additional_properties = d
        return secret_manager_metadata_dto

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
