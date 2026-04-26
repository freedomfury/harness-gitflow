from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JwksPublicKeyDTO")


@_attrs_define
class JwksPublicKeyDTO:
    """
    Attributes:
        alg (str | Unset):
        e (str | Unset):
        kid (str | Unset):
        kty (str | Unset):
        n (str | Unset):
        use (str | Unset):
    """

    alg: str | Unset = UNSET
    e: str | Unset = UNSET
    kid: str | Unset = UNSET
    kty: str | Unset = UNSET
    n: str | Unset = UNSET
    use: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alg = self.alg

        e = self.e

        kid = self.kid

        kty = self.kty

        n = self.n

        use = self.use

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alg is not UNSET:
            field_dict["alg"] = alg
        if e is not UNSET:
            field_dict["e"] = e
        if kid is not UNSET:
            field_dict["kid"] = kid
        if kty is not UNSET:
            field_dict["kty"] = kty
        if n is not UNSET:
            field_dict["n"] = n
        if use is not UNSET:
            field_dict["use"] = use

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alg = d.pop("alg", UNSET)

        e = d.pop("e", UNSET)

        kid = d.pop("kid", UNSET)

        kty = d.pop("kty", UNSET)

        n = d.pop("n", UNSET)

        use = d.pop("use", UNSET)

        jwks_public_key_dto = cls(
            alg=alg,
            e=e,
            kid=kid,
            kty=kty,
            n=n,
            use=use,
        )

        jwks_public_key_dto.additional_properties = d
        return jwks_public_key_dto

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
