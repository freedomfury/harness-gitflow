from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.secret_manager_metadata_request_encryption_type import (
    SecretManagerMetadataRequestEncryptionType,
    check_secret_manager_metadata_request_encryption_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret_manager_metadata_request_spec_dto import SecretManagerMetadataRequestSpecDTO


T = TypeVar("T", bound="SecretManagerMetadataRequest")


@_attrs_define
class SecretManagerMetadataRequest:
    """This is the view of the SecretManagerMetadataRequest entity defined in Harness

    Attributes:
        encryption_type (SecretManagerMetadataRequestEncryptionType): This specifies the type of encryption used by the
            Secret Manager to encrypt Secrets.
        identifier (str): Identifier of the SecretManager metadata.
        spec (SecretManagerMetadataRequestSpecDTO): Spec of the Secret Manager.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
    """

    encryption_type: SecretManagerMetadataRequestEncryptionType
    identifier: str
    spec: SecretManagerMetadataRequestSpecDTO
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption_type: str = self.encryption_type

        identifier = self.identifier

        spec = self.spec.to_dict()

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encryptionType": encryption_type,
                "identifier": identifier,
                "spec": spec,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secret_manager_metadata_request_spec_dto import SecretManagerMetadataRequestSpecDTO

        d = dict(src_dict)
        encryption_type = check_secret_manager_metadata_request_encryption_type(d.pop("encryptionType"))

        identifier = d.pop("identifier")

        spec = SecretManagerMetadataRequestSpecDTO.from_dict(d.pop("spec"))

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        secret_manager_metadata_request = cls(
            encryption_type=encryption_type,
            identifier=identifier,
            spec=spec,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
        )

        secret_manager_metadata_request.additional_properties = d
        return secret_manager_metadata_request

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
