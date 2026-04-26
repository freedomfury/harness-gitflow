from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureOidcCredentialResponseDTO")


@_attrs_define
class AzureOidcCredentialResponseDTO:
    """
    Attributes:
        token_type (str | Unset):
        expires_in (int | Unset):
        ext_expires_in (int | Unset):
        access_token (str | Unset):
    """

    token_type: str | Unset = UNSET
    expires_in: int | Unset = UNSET
    ext_expires_in: int | Unset = UNSET
    access_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_type = self.token_type

        expires_in = self.expires_in

        ext_expires_in = self.ext_expires_in

        access_token = self.access_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if ext_expires_in is not UNSET:
            field_dict["ext_expires_in"] = ext_expires_in
        if access_token is not UNSET:
            field_dict["access_token"] = access_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token_type = d.pop("token_type", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        ext_expires_in = d.pop("ext_expires_in", UNSET)

        access_token = d.pop("access_token", UNSET)

        azure_oidc_credential_response_dto = cls(
            token_type=token_type,
            expires_in=expires_in,
            ext_expires_in=ext_expires_in,
            access_token=access_token,
        )

        azure_oidc_credential_response_dto.additional_properties = d
        return azure_oidc_credential_response_dto

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
