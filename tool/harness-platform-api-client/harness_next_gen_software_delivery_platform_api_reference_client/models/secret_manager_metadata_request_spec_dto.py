from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SecretManagerMetadataRequestSpecDTO")


@_attrs_define
class SecretManagerMetadataRequestSpecDTO:
    """Spec of the Secret Manager.

    Attributes:
        encryption_type (str):
    """

    encryption_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption_type = self.encryption_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encryptionType": encryption_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encryption_type = d.pop("encryptionType")

        secret_manager_metadata_request_spec_dto = cls(
            encryption_type=encryption_type,
        )

        secret_manager_metadata_request_spec_dto.additional_properties = d
        return secret_manager_metadata_request_spec_dto

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
