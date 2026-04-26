from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_metadata import AdditionalMetadata


T = TypeVar("T", bound="SecretFileSpec")


@_attrs_define
class SecretFileSpec:
    """This has details of Secret File defined in harness

    Attributes:
        type_ (str):
        secret_manager_identifier (str): Identifier of the Secret Manager used to manage the secret.
        error_message_for_invalid_yaml (str | Unset):
        additional_metadata (AdditionalMetadata | Unset): Additional metadata for the secret
    """

    type_: str
    secret_manager_identifier: str
    error_message_for_invalid_yaml: str | Unset = UNSET
    additional_metadata: AdditionalMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        secret_manager_identifier = self.secret_manager_identifier

        error_message_for_invalid_yaml = self.error_message_for_invalid_yaml

        additional_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_metadata, Unset):
            additional_metadata = self.additional_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "secretManagerIdentifier": secret_manager_identifier,
            }
        )
        if error_message_for_invalid_yaml is not UNSET:
            field_dict["errorMessageForInvalidYaml"] = error_message_for_invalid_yaml
        if additional_metadata is not UNSET:
            field_dict["additionalMetadata"] = additional_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.additional_metadata import AdditionalMetadata

        d = dict(src_dict)
        type_ = d.pop("type")

        secret_manager_identifier = d.pop("secretManagerIdentifier")

        error_message_for_invalid_yaml = d.pop("errorMessageForInvalidYaml", UNSET)

        _additional_metadata = d.pop("additionalMetadata", UNSET)
        additional_metadata: AdditionalMetadata | Unset
        if isinstance(_additional_metadata, Unset):
            additional_metadata = UNSET
        else:
            additional_metadata = AdditionalMetadata.from_dict(_additional_metadata)

        secret_file_spec = cls(
            type_=type_,
            secret_manager_identifier=secret_manager_identifier,
            error_message_for_invalid_yaml=error_message_for_invalid_yaml,
            additional_metadata=additional_metadata,
        )

        secret_file_spec.additional_properties = d
        return secret_file_spec

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
