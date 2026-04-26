from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceNowRefreshToken")


@_attrs_define
class ServiceNowRefreshToken:
    """This entity contains the details of the Service Now Refresh Token

    Attributes:
        token_url (str):
        refresh_token_ref (str):
        client_id_ref (str):
        client_secret_ref (str | Unset):
        scope (str | Unset):
    """

    token_url: str
    refresh_token_ref: str
    client_id_ref: str
    client_secret_ref: str | Unset = UNSET
    scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_url = self.token_url

        refresh_token_ref = self.refresh_token_ref

        client_id_ref = self.client_id_ref

        client_secret_ref = self.client_secret_ref

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenUrl": token_url,
                "refreshTokenRef": refresh_token_ref,
                "clientIdRef": client_id_ref,
            }
        )
        if client_secret_ref is not UNSET:
            field_dict["clientSecretRef"] = client_secret_ref
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token_url = d.pop("tokenUrl")

        refresh_token_ref = d.pop("refreshTokenRef")

        client_id_ref = d.pop("clientIdRef")

        client_secret_ref = d.pop("clientSecretRef", UNSET)

        scope = d.pop("scope", UNSET)

        service_now_refresh_token = cls(
            token_url=token_url,
            refresh_token_ref=refresh_token_ref,
            client_id_ref=client_id_ref,
            client_secret_ref=client_secret_ref,
            scope=scope,
        )

        service_now_refresh_token.additional_properties = d
        return service_now_refresh_token

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
