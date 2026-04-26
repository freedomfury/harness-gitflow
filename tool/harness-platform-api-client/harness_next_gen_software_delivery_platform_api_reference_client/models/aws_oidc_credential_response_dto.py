from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsOidcCredentialResponseDto")


@_attrs_define
class AwsOidcCredentialResponseDto:
    """
    Attributes:
        access_key (str | Unset):
        secret_access_key (str | Unset):
        session_token (str | Unset):
    """

    access_key: str | Unset = UNSET
    secret_access_key: str | Unset = UNSET
    session_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        secret_access_key = self.secret_access_key

        session_token = self.session_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key is not UNSET:
            field_dict["access_key"] = access_key
        if secret_access_key is not UNSET:
            field_dict["secret_access_key"] = secret_access_key
        if session_token is not UNSET:
            field_dict["session_token"] = session_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("access_key", UNSET)

        secret_access_key = d.pop("secret_access_key", UNSET)

        session_token = d.pop("session_token", UNSET)

        aws_oidc_credential_response_dto = cls(
            access_key=access_key,
            secret_access_key=secret_access_key,
            session_token=session_token,
        )

        aws_oidc_credential_response_dto.additional_properties = d
        return aws_oidc_credential_response_dto

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
