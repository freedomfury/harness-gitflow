from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesOpenIdConnect")


@_attrs_define
class KubernetesOpenIdConnect:
    """This contains kubernetes open id connect details

    Attributes:
        oidc_issuer_url (str):
        oidc_client_id_ref (str):
        oidc_password_ref (str):
        oidc_username (str | Unset):
        oidc_username_ref (str | Unset):
        oidc_secret_ref (str | Unset):
        oidc_scopes (str | Unset):
    """

    oidc_issuer_url: str
    oidc_client_id_ref: str
    oidc_password_ref: str
    oidc_username: str | Unset = UNSET
    oidc_username_ref: str | Unset = UNSET
    oidc_secret_ref: str | Unset = UNSET
    oidc_scopes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oidc_issuer_url = self.oidc_issuer_url

        oidc_client_id_ref = self.oidc_client_id_ref

        oidc_password_ref = self.oidc_password_ref

        oidc_username = self.oidc_username

        oidc_username_ref = self.oidc_username_ref

        oidc_secret_ref = self.oidc_secret_ref

        oidc_scopes = self.oidc_scopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oidcIssuerUrl": oidc_issuer_url,
                "oidcClientIdRef": oidc_client_id_ref,
                "oidcPasswordRef": oidc_password_ref,
            }
        )
        if oidc_username is not UNSET:
            field_dict["oidcUsername"] = oidc_username
        if oidc_username_ref is not UNSET:
            field_dict["oidcUsernameRef"] = oidc_username_ref
        if oidc_secret_ref is not UNSET:
            field_dict["oidcSecretRef"] = oidc_secret_ref
        if oidc_scopes is not UNSET:
            field_dict["oidcScopes"] = oidc_scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        oidc_issuer_url = d.pop("oidcIssuerUrl")

        oidc_client_id_ref = d.pop("oidcClientIdRef")

        oidc_password_ref = d.pop("oidcPasswordRef")

        oidc_username = d.pop("oidcUsername", UNSET)

        oidc_username_ref = d.pop("oidcUsernameRef", UNSET)

        oidc_secret_ref = d.pop("oidcSecretRef", UNSET)

        oidc_scopes = d.pop("oidcScopes", UNSET)

        kubernetes_open_id_connect = cls(
            oidc_issuer_url=oidc_issuer_url,
            oidc_client_id_ref=oidc_client_id_ref,
            oidc_password_ref=oidc_password_ref,
            oidc_username=oidc_username,
            oidc_username_ref=oidc_username_ref,
            oidc_secret_ref=oidc_secret_ref,
            oidc_scopes=oidc_scopes,
        )

        kubernetes_open_id_connect.additional_properties = d
        return kubernetes_open_id_connect

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
