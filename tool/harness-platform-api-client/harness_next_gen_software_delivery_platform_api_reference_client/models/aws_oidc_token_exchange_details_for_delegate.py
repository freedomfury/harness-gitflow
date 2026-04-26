from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsOidcTokenExchangeDetailsForDelegate")


@_attrs_define
class AwsOidcTokenExchangeDetailsForDelegate:
    """
    Attributes:
        oidc_id_token (str | Unset):
        id_token_expiry_time (int | Unset):
    """

    oidc_id_token: str | Unset = UNSET
    id_token_expiry_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oidc_id_token = self.oidc_id_token

        id_token_expiry_time = self.id_token_expiry_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oidc_id_token is not UNSET:
            field_dict["oidcIdToken"] = oidc_id_token
        if id_token_expiry_time is not UNSET:
            field_dict["idTokenExpiryTime"] = id_token_expiry_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        oidc_id_token = d.pop("oidcIdToken", UNSET)

        id_token_expiry_time = d.pop("idTokenExpiryTime", UNSET)

        aws_oidc_token_exchange_details_for_delegate = cls(
            oidc_id_token=oidc_id_token,
            id_token_expiry_time=id_token_expiry_time,
        )

        aws_oidc_token_exchange_details_for_delegate.additional_properties = d
        return aws_oidc_token_exchange_details_for_delegate

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
