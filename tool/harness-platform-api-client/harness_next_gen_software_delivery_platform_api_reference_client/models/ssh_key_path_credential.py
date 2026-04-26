from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSHKeyPathCredential")


@_attrs_define
class SSHKeyPathCredential:
    """This is SSH KeyPath credential specification as defined in harness

    Attributes:
        credential_type (str):
        user_name (str): SSH Username.
        key_path (str): Path of the key file.
        encrypted_passphrase (str | Unset): This is the passphrase provided while creating the SSH key for local
            encryption.
    """

    credential_type: str
    user_name: str
    key_path: str
    encrypted_passphrase: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential_type = self.credential_type

        user_name = self.user_name

        key_path = self.key_path

        encrypted_passphrase = self.encrypted_passphrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialType": credential_type,
                "userName": user_name,
                "keyPath": key_path,
            }
        )
        if encrypted_passphrase is not UNSET:
            field_dict["encryptedPassphrase"] = encrypted_passphrase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential_type = d.pop("credentialType")

        user_name = d.pop("userName")

        key_path = d.pop("keyPath")

        encrypted_passphrase = d.pop("encryptedPassphrase", UNSET)

        ssh_key_path_credential = cls(
            credential_type=credential_type,
            user_name=user_name,
            key_path=key_path,
            encrypted_passphrase=encrypted_passphrase,
        )

        ssh_key_path_credential.additional_properties = d
        return ssh_key_path_credential

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
