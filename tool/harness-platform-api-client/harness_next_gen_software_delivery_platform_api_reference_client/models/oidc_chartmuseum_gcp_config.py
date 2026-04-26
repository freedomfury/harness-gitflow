from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OidcChartmuseumGcpConfig")


@_attrs_define
class OidcChartmuseumGcpConfig:
    """
    Attributes:
        type_ (str | Unset):
        audience (str | Unset):
        subject_token_type (str | Unset):
        token_url (str | Unset):
        service_account_impersonation_url (str | Unset):
    """

    type_: str | Unset = UNSET
    audience: str | Unset = UNSET
    subject_token_type: str | Unset = UNSET
    token_url: str | Unset = UNSET
    service_account_impersonation_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        audience = self.audience

        subject_token_type = self.subject_token_type

        token_url = self.token_url

        service_account_impersonation_url = self.service_account_impersonation_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if audience is not UNSET:
            field_dict["audience"] = audience
        if subject_token_type is not UNSET:
            field_dict["subject_token_type"] = subject_token_type
        if token_url is not UNSET:
            field_dict["token_url"] = token_url
        if service_account_impersonation_url is not UNSET:
            field_dict["service_account_impersonation_url"] = service_account_impersonation_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        audience = d.pop("audience", UNSET)

        subject_token_type = d.pop("subject_token_type", UNSET)

        token_url = d.pop("token_url", UNSET)

        service_account_impersonation_url = d.pop("service_account_impersonation_url", UNSET)

        oidc_chartmuseum_gcp_config = cls(
            type_=type_,
            audience=audience,
            subject_token_type=subject_token_type,
            token_url=token_url,
            service_account_impersonation_url=service_account_impersonation_url,
        )

        oidc_chartmuseum_gcp_config.additional_properties = d
        return oidc_chartmuseum_gcp_config

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
