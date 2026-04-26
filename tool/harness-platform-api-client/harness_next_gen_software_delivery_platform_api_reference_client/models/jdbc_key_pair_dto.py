from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JDBCKeyPairDTO")


@_attrs_define
class JDBCKeyPairDTO:
    """This entity contains the details of the JDBC Key Pair (PKI) authentication

    Attributes:
        private_key_file_ref (str):
        username (str | Unset):
        username_ref (str | Unset):
        private_key_passphrase_ref (str | Unset):
    """

    private_key_file_ref: str
    username: str | Unset = UNSET
    username_ref: str | Unset = UNSET
    private_key_passphrase_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        private_key_file_ref = self.private_key_file_ref

        username = self.username

        username_ref = self.username_ref

        private_key_passphrase_ref = self.private_key_passphrase_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "privateKeyFileRef": private_key_file_ref,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if username_ref is not UNSET:
            field_dict["usernameRef"] = username_ref
        if private_key_passphrase_ref is not UNSET:
            field_dict["privateKeyPassphraseRef"] = private_key_passphrase_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        private_key_file_ref = d.pop("privateKeyFileRef")

        username = d.pop("username", UNSET)

        username_ref = d.pop("usernameRef", UNSET)

        private_key_passphrase_ref = d.pop("privateKeyPassphraseRef", UNSET)

        jdbc_key_pair_dto = cls(
            private_key_file_ref=private_key_file_ref,
            username=username,
            username_ref=username_ref,
            private_key_passphrase_ref=private_key_passphrase_ref,
        )

        jdbc_key_pair_dto.additional_properties = d
        return jdbc_key_pair_dto

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
