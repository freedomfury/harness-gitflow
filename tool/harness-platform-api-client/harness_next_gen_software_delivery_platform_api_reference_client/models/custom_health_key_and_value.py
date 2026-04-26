from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomHealthKeyAndValue")


@_attrs_define
class CustomHealthKeyAndValue:
    """
    Attributes:
        key (str):
        is_value_encrypted (bool | Unset):
        encrypted_value_ref (str | Unset):
        value (str | Unset):
        value_encrypted (bool | Unset):
    """

    key: str
    is_value_encrypted: bool | Unset = UNSET
    encrypted_value_ref: str | Unset = UNSET
    value: str | Unset = UNSET
    value_encrypted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        is_value_encrypted = self.is_value_encrypted

        encrypted_value_ref = self.encrypted_value_ref

        value = self.value

        value_encrypted = self.value_encrypted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if is_value_encrypted is not UNSET:
            field_dict["isValueEncrypted"] = is_value_encrypted
        if encrypted_value_ref is not UNSET:
            field_dict["encryptedValueRef"] = encrypted_value_ref
        if value is not UNSET:
            field_dict["value"] = value
        if value_encrypted is not UNSET:
            field_dict["valueEncrypted"] = value_encrypted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        is_value_encrypted = d.pop("isValueEncrypted", UNSET)

        encrypted_value_ref = d.pop("encryptedValueRef", UNSET)

        value = d.pop("value", UNSET)

        value_encrypted = d.pop("valueEncrypted", UNSET)

        custom_health_key_and_value = cls(
            key=key,
            is_value_encrypted=is_value_encrypted,
            encrypted_value_ref=encrypted_value_ref,
            value=value,
            value_encrypted=value_encrypted,
        )

        custom_health_key_and_value.additional_properties = d
        return custom_health_key_and_value

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
