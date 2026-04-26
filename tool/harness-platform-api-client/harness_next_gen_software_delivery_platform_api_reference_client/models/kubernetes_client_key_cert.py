from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesClientKeyCert")


@_attrs_define
class KubernetesClientKeyCert:
    """This contains kubernetes client key certificate details

    Attributes:
        client_cert_ref (str):
        client_key_ref (str):
        ca_cert_ref (str | Unset):
        client_key_passphrase_ref (str | Unset):
        client_key_algo (str | Unset):
    """

    client_cert_ref: str
    client_key_ref: str
    ca_cert_ref: str | Unset = UNSET
    client_key_passphrase_ref: str | Unset = UNSET
    client_key_algo: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_cert_ref = self.client_cert_ref

        client_key_ref = self.client_key_ref

        ca_cert_ref = self.ca_cert_ref

        client_key_passphrase_ref = self.client_key_passphrase_ref

        client_key_algo = self.client_key_algo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientCertRef": client_cert_ref,
                "clientKeyRef": client_key_ref,
            }
        )
        if ca_cert_ref is not UNSET:
            field_dict["caCertRef"] = ca_cert_ref
        if client_key_passphrase_ref is not UNSET:
            field_dict["clientKeyPassphraseRef"] = client_key_passphrase_ref
        if client_key_algo is not UNSET:
            field_dict["clientKeyAlgo"] = client_key_algo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_cert_ref = d.pop("clientCertRef")

        client_key_ref = d.pop("clientKeyRef")

        ca_cert_ref = d.pop("caCertRef", UNSET)

        client_key_passphrase_ref = d.pop("clientKeyPassphraseRef", UNSET)

        client_key_algo = d.pop("clientKeyAlgo", UNSET)

        kubernetes_client_key_cert = cls(
            client_cert_ref=client_cert_ref,
            client_key_ref=client_key_ref,
            ca_cert_ref=ca_cert_ref,
            client_key_passphrase_ref=client_key_passphrase_ref,
            client_key_algo=client_key_algo,
        )

        kubernetes_client_key_cert.additional_properties = d
        return kubernetes_client_key_cert

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
