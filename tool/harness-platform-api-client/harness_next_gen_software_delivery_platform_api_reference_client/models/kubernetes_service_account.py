from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesServiceAccount")


@_attrs_define
class KubernetesServiceAccount:
    """This contains kubernetes service account details

    Attributes:
        service_account_token_ref (str):
        ca_cert_ref (str | Unset):
    """

    service_account_token_ref: str
    ca_cert_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_account_token_ref = self.service_account_token_ref

        ca_cert_ref = self.ca_cert_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceAccountTokenRef": service_account_token_ref,
            }
        )
        if ca_cert_ref is not UNSET:
            field_dict["caCertRef"] = ca_cert_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_account_token_ref = d.pop("serviceAccountTokenRef")

        ca_cert_ref = d.pop("caCertRef", UNSET)

        kubernetes_service_account = cls(
            service_account_token_ref=service_account_token_ref,
            ca_cert_ref=ca_cert_ref,
        )

        kubernetes_service_account.additional_properties = d
        return kubernetes_service_account

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
