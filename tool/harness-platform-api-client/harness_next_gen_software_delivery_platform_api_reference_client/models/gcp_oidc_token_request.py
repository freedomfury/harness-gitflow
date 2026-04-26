from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oidc_id_token_custom_attributes_structure import OidcIdTokenCustomAttributesStructure


T = TypeVar("T", bound="GcpOidcTokenRequest")


@_attrs_define
class GcpOidcTokenRequest:
    """This contains GCP OIDC Token request details

    Attributes:
        account_id (str): This specifies the Harness Account Id
        workload_pool_id (str): This specifies the Workload Pool Id
        provider_id (str): This specifies the OIDC ID Provider
        gcp_project_id (str): This specifies the GCP Project Id
        service_account_email (str | Unset): This specifies the GCP Service Account Email
        oidc_id_token_custom_attributes_structure (OidcIdTokenCustomAttributesStructure | Unset): This includes all the
            ID token custom attributes
    """

    account_id: str
    workload_pool_id: str
    provider_id: str
    gcp_project_id: str
    service_account_email: str | Unset = UNSET
    oidc_id_token_custom_attributes_structure: OidcIdTokenCustomAttributesStructure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        workload_pool_id = self.workload_pool_id

        provider_id = self.provider_id

        gcp_project_id = self.gcp_project_id

        service_account_email = self.service_account_email

        oidc_id_token_custom_attributes_structure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oidc_id_token_custom_attributes_structure, Unset):
            oidc_id_token_custom_attributes_structure = self.oidc_id_token_custom_attributes_structure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "workloadPoolId": workload_pool_id,
                "providerId": provider_id,
                "gcpProjectId": gcp_project_id,
            }
        )
        if service_account_email is not UNSET:
            field_dict["serviceAccountEmail"] = service_account_email
        if oidc_id_token_custom_attributes_structure is not UNSET:
            field_dict["oidcIdTokenCustomAttributesStructure"] = oidc_id_token_custom_attributes_structure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_id_token_custom_attributes_structure import OidcIdTokenCustomAttributesStructure

        d = dict(src_dict)
        account_id = d.pop("accountId")

        workload_pool_id = d.pop("workloadPoolId")

        provider_id = d.pop("providerId")

        gcp_project_id = d.pop("gcpProjectId")

        service_account_email = d.pop("serviceAccountEmail", UNSET)

        _oidc_id_token_custom_attributes_structure = d.pop("oidcIdTokenCustomAttributesStructure", UNSET)
        oidc_id_token_custom_attributes_structure: OidcIdTokenCustomAttributesStructure | Unset
        if isinstance(_oidc_id_token_custom_attributes_structure, Unset):
            oidc_id_token_custom_attributes_structure = UNSET
        else:
            oidc_id_token_custom_attributes_structure = OidcIdTokenCustomAttributesStructure.from_dict(
                _oidc_id_token_custom_attributes_structure
            )

        gcp_oidc_token_request = cls(
            account_id=account_id,
            workload_pool_id=workload_pool_id,
            provider_id=provider_id,
            gcp_project_id=gcp_project_id,
            service_account_email=service_account_email,
            oidc_id_token_custom_attributes_structure=oidc_id_token_custom_attributes_structure,
        )

        gcp_oidc_token_request.additional_properties = d
        return gcp_oidc_token_request

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
