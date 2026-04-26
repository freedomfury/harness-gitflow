from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OidcConfiguration")


@_attrs_define
class OidcConfiguration:
    """
    Attributes:
        issuer (str | Unset):
        jwks_uri (str | Unset):
        subject_types_supported (list[str] | Unset):
        response_types_supported (list[str] | Unset):
        claims_supported (list[str] | Unset):
        id_token_signing_alg_values_supported (list[str] | Unset):
        scopes_supported (list[str] | Unset):
    """

    issuer: str | Unset = UNSET
    jwks_uri: str | Unset = UNSET
    subject_types_supported: list[str] | Unset = UNSET
    response_types_supported: list[str] | Unset = UNSET
    claims_supported: list[str] | Unset = UNSET
    id_token_signing_alg_values_supported: list[str] | Unset = UNSET
    scopes_supported: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuer = self.issuer

        jwks_uri = self.jwks_uri

        subject_types_supported: list[str] | Unset = UNSET
        if not isinstance(self.subject_types_supported, Unset):
            subject_types_supported = self.subject_types_supported

        response_types_supported: list[str] | Unset = UNSET
        if not isinstance(self.response_types_supported, Unset):
            response_types_supported = self.response_types_supported

        claims_supported: list[str] | Unset = UNSET
        if not isinstance(self.claims_supported, Unset):
            claims_supported = self.claims_supported

        id_token_signing_alg_values_supported: list[str] | Unset = UNSET
        if not isinstance(self.id_token_signing_alg_values_supported, Unset):
            id_token_signing_alg_values_supported = self.id_token_signing_alg_values_supported

        scopes_supported: list[str] | Unset = UNSET
        if not isinstance(self.scopes_supported, Unset):
            scopes_supported = self.scopes_supported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if jwks_uri is not UNSET:
            field_dict["jwks_uri"] = jwks_uri
        if subject_types_supported is not UNSET:
            field_dict["subject_types_supported"] = subject_types_supported
        if response_types_supported is not UNSET:
            field_dict["response_types_supported"] = response_types_supported
        if claims_supported is not UNSET:
            field_dict["claims_supported"] = claims_supported
        if id_token_signing_alg_values_supported is not UNSET:
            field_dict["id_token_signing_alg_values_supported"] = id_token_signing_alg_values_supported
        if scopes_supported is not UNSET:
            field_dict["scopes_supported"] = scopes_supported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issuer = d.pop("issuer", UNSET)

        jwks_uri = d.pop("jwks_uri", UNSET)

        subject_types_supported = cast(list[str], d.pop("subject_types_supported", UNSET))

        response_types_supported = cast(list[str], d.pop("response_types_supported", UNSET))

        claims_supported = cast(list[str], d.pop("claims_supported", UNSET))

        id_token_signing_alg_values_supported = cast(list[str], d.pop("id_token_signing_alg_values_supported", UNSET))

        scopes_supported = cast(list[str], d.pop("scopes_supported", UNSET))

        oidc_configuration = cls(
            issuer=issuer,
            jwks_uri=jwks_uri,
            subject_types_supported=subject_types_supported,
            response_types_supported=response_types_supported,
            claims_supported=claims_supported,
            id_token_signing_alg_values_supported=id_token_signing_alg_values_supported,
            scopes_supported=scopes_supported,
        )

        oidc_configuration.additional_properties = d
        return oidc_configuration

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
