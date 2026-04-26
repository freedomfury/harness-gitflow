from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.azure_oidc_token_request_dto import AzureOidcTokenRequestDTO


T = TypeVar("T", bound="AzureOidcCredentialExchangeRequestDTO")


@_attrs_define
class AzureOidcCredentialExchangeRequestDTO:
    """
    Attributes:
        tenant_id (str):
        client_id (str):
        azure_oidc_token_request_dto (AzureOidcTokenRequestDTO):
        oidc_token (str | Unset):
        resource (str | Unset):
        retry_policy (str | Unset):
    """

    tenant_id: str
    client_id: str
    azure_oidc_token_request_dto: AzureOidcTokenRequestDTO
    oidc_token: str | Unset = UNSET
    resource: str | Unset = UNSET
    retry_policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        client_id = self.client_id

        azure_oidc_token_request_dto = self.azure_oidc_token_request_dto.to_dict()

        oidc_token = self.oidc_token

        resource = self.resource

        retry_policy = self.retry_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenantId": tenant_id,
                "clientId": client_id,
                "azureOidcTokenRequestDTO": azure_oidc_token_request_dto,
            }
        )
        if oidc_token is not UNSET:
            field_dict["oidcToken"] = oidc_token
        if resource is not UNSET:
            field_dict["resource"] = resource
        if retry_policy is not UNSET:
            field_dict["retryPolicy"] = retry_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_oidc_token_request_dto import AzureOidcTokenRequestDTO

        d = dict(src_dict)
        tenant_id = d.pop("tenantId")

        client_id = d.pop("clientId")

        azure_oidc_token_request_dto = AzureOidcTokenRequestDTO.from_dict(d.pop("azureOidcTokenRequestDTO"))

        oidc_token = d.pop("oidcToken", UNSET)

        resource = d.pop("resource", UNSET)

        retry_policy = d.pop("retryPolicy", UNSET)

        azure_oidc_credential_exchange_request_dto = cls(
            tenant_id=tenant_id,
            client_id=client_id,
            azure_oidc_token_request_dto=azure_oidc_token_request_dto,
            oidc_token=oidc_token,
            resource=resource,
            retry_policy=retry_policy,
        )

        azure_oidc_credential_exchange_request_dto.additional_properties = d
        return azure_oidc_credential_exchange_request_dto

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
