from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitlabOnPremProviderRequestInfo")


@_attrs_define
class GitlabOnPremProviderRequestInfo:
    """
    Attributes:
        type_ (str):
        domain (str | Unset):
        delegate_selectors (list[str] | Unset):
        secret_manager_ref (str | Unset):
        client_id (str | Unset):
        client_secret_ref (str | Unset):
    """

    type_: str
    domain: str | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    secret_manager_ref: str | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        domain = self.domain

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        secret_manager_ref = self.secret_manager_ref

        client_id = self.client_id

        client_secret_ref = self.client_secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if secret_manager_ref is not UNSET:
            field_dict["secretManagerRef"] = secret_manager_ref
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret_ref is not UNSET:
            field_dict["clientSecretRef"] = client_secret_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        domain = d.pop("domain", UNSET)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        secret_manager_ref = d.pop("secretManagerRef", UNSET)

        client_id = d.pop("clientId", UNSET)

        client_secret_ref = d.pop("clientSecretRef", UNSET)

        gitlab_on_prem_provider_request_info = cls(
            type_=type_,
            domain=domain,
            delegate_selectors=delegate_selectors,
            secret_manager_ref=secret_manager_ref,
            client_id=client_id,
            client_secret_ref=client_secret_ref,
        )

        gitlab_on_prem_provider_request_info.additional_properties = d
        return gitlab_on_prem_provider_request_info

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
