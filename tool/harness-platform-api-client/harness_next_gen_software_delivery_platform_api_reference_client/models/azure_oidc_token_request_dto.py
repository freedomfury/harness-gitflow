from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oidc_id_token_custom_attributes_structure import OidcIdTokenCustomAttributesStructure


T = TypeVar("T", bound="AzureOidcTokenRequestDTO")


@_attrs_define
class AzureOidcTokenRequestDTO:
    """
    Attributes:
        account_id (str):
        tenant_id (str | Unset):
        client_id (str | Unset):
        audience (str | Unset):
        subscription_id (str | Unset):
        resource_group (str | Unset):
        oidc_id_token_custom_attributes_structure (OidcIdTokenCustomAttributesStructure | Unset): This includes all the
            ID token custom attributes
    """

    account_id: str
    tenant_id: str | Unset = UNSET
    client_id: str | Unset = UNSET
    audience: str | Unset = UNSET
    subscription_id: str | Unset = UNSET
    resource_group: str | Unset = UNSET
    oidc_id_token_custom_attributes_structure: OidcIdTokenCustomAttributesStructure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        tenant_id = self.tenant_id

        client_id = self.client_id

        audience = self.audience

        subscription_id = self.subscription_id

        resource_group = self.resource_group

        oidc_id_token_custom_attributes_structure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oidc_id_token_custom_attributes_structure, Unset):
            oidc_id_token_custom_attributes_structure = self.oidc_id_token_custom_attributes_structure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
            }
        )
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if audience is not UNSET:
            field_dict["audience"] = audience
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if oidc_id_token_custom_attributes_structure is not UNSET:
            field_dict["oidcIdTokenCustomAttributesStructure"] = oidc_id_token_custom_attributes_structure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_id_token_custom_attributes_structure import OidcIdTokenCustomAttributesStructure

        d = dict(src_dict)
        account_id = d.pop("accountId")

        tenant_id = d.pop("tenantId", UNSET)

        client_id = d.pop("clientId", UNSET)

        audience = d.pop("audience", UNSET)

        subscription_id = d.pop("subscriptionId", UNSET)

        resource_group = d.pop("resourceGroup", UNSET)

        _oidc_id_token_custom_attributes_structure = d.pop("oidcIdTokenCustomAttributesStructure", UNSET)
        oidc_id_token_custom_attributes_structure: OidcIdTokenCustomAttributesStructure | Unset
        if isinstance(_oidc_id_token_custom_attributes_structure, Unset):
            oidc_id_token_custom_attributes_structure = UNSET
        else:
            oidc_id_token_custom_attributes_structure = OidcIdTokenCustomAttributesStructure.from_dict(
                _oidc_id_token_custom_attributes_structure
            )

        azure_oidc_token_request_dto = cls(
            account_id=account_id,
            tenant_id=tenant_id,
            client_id=client_id,
            audience=audience,
            subscription_id=subscription_id,
            resource_group=resource_group,
            oidc_id_token_custom_attributes_structure=oidc_id_token_custom_attributes_structure,
        )

        azure_oidc_token_request_dto.additional_properties = d
        return azure_oidc_token_request_dto

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
