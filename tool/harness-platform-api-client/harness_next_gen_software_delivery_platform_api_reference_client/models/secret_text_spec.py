from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.secret_text_spec_value_type import SecretTextSpecValueType, check_secret_text_spec_value_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_metadata import AdditionalMetadata


T = TypeVar("T", bound="SecretTextSpec")


@_attrs_define
class SecretTextSpec:
    """This has details of encrypted text secret.

    Attributes:
        type_ (str):
        secret_manager_identifier (str): Identifier of the Secret Manager used to manage the secret.
        value_type (SecretTextSpecValueType): This has details to specify if the secret value is inline or referenced.
        error_message_for_invalid_yaml (str | Unset):
        value (str | Unset): Value of the Secret [Required]
        additional_metadata (AdditionalMetadata | Unset): Additional metadata for the secret
    """

    type_: str
    secret_manager_identifier: str
    value_type: SecretTextSpecValueType
    error_message_for_invalid_yaml: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_metadata: AdditionalMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        secret_manager_identifier = self.secret_manager_identifier

        value_type: str = self.value_type

        error_message_for_invalid_yaml = self.error_message_for_invalid_yaml

        value = self.value

        additional_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_metadata, Unset):
            additional_metadata = self.additional_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "secretManagerIdentifier": secret_manager_identifier,
                "valueType": value_type,
            }
        )
        if error_message_for_invalid_yaml is not UNSET:
            field_dict["errorMessageForInvalidYaml"] = error_message_for_invalid_yaml
        if value is not UNSET:
            field_dict["value"] = value
        if additional_metadata is not UNSET:
            field_dict["additionalMetadata"] = additional_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.additional_metadata import AdditionalMetadata

        d = dict(src_dict)
        type_ = d.pop("type")

        secret_manager_identifier = d.pop("secretManagerIdentifier")

        value_type = check_secret_text_spec_value_type(d.pop("valueType"))

        error_message_for_invalid_yaml = d.pop("errorMessageForInvalidYaml", UNSET)

        value = d.pop("value", UNSET)

        _additional_metadata = d.pop("additionalMetadata", UNSET)
        additional_metadata: AdditionalMetadata | Unset
        if isinstance(_additional_metadata, Unset):
            additional_metadata = UNSET
        else:
            additional_metadata = AdditionalMetadata.from_dict(_additional_metadata)

        secret_text_spec = cls(
            type_=type_,
            secret_manager_identifier=secret_manager_identifier,
            value_type=value_type,
            error_message_for_invalid_yaml=error_message_for_invalid_yaml,
            value=value,
            additional_metadata=additional_metadata,
        )

        secret_text_spec.additional_properties = d
        return secret_text_spec

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
