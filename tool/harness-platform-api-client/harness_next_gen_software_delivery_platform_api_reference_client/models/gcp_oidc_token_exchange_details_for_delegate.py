from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oidc_chartmuseum_gcp_config import OidcChartmuseumGcpConfig
    from ..models.oidc_workload_access_token_request import OidcWorkloadAccessTokenRequest


T = TypeVar("T", bound="GcpOidcTokenExchangeDetailsForDelegate")


@_attrs_define
class GcpOidcTokenExchangeDetailsForDelegate:
    """
    Attributes:
        oidc_id_token (str | Unset):
        oidc_access_token_sts_endpoint (str | Unset):
        oidc_access_token_iam_sa_endpoint (str | Unset):
        gcp_service_account_email (str | Unset):
        oidc_workload_access_token_request_structure (OidcWorkloadAccessTokenRequest | Unset):
        oidc_chartmuseum_gcp_config_structure (OidcChartmuseumGcpConfig | Unset):
        id_token_expiry_time (int | Unset):
    """

    oidc_id_token: str | Unset = UNSET
    oidc_access_token_sts_endpoint: str | Unset = UNSET
    oidc_access_token_iam_sa_endpoint: str | Unset = UNSET
    gcp_service_account_email: str | Unset = UNSET
    oidc_workload_access_token_request_structure: OidcWorkloadAccessTokenRequest | Unset = UNSET
    oidc_chartmuseum_gcp_config_structure: OidcChartmuseumGcpConfig | Unset = UNSET
    id_token_expiry_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oidc_id_token = self.oidc_id_token

        oidc_access_token_sts_endpoint = self.oidc_access_token_sts_endpoint

        oidc_access_token_iam_sa_endpoint = self.oidc_access_token_iam_sa_endpoint

        gcp_service_account_email = self.gcp_service_account_email

        oidc_workload_access_token_request_structure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oidc_workload_access_token_request_structure, Unset):
            oidc_workload_access_token_request_structure = self.oidc_workload_access_token_request_structure.to_dict()

        oidc_chartmuseum_gcp_config_structure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oidc_chartmuseum_gcp_config_structure, Unset):
            oidc_chartmuseum_gcp_config_structure = self.oidc_chartmuseum_gcp_config_structure.to_dict()

        id_token_expiry_time = self.id_token_expiry_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oidc_id_token is not UNSET:
            field_dict["oidcIdToken"] = oidc_id_token
        if oidc_access_token_sts_endpoint is not UNSET:
            field_dict["oidcAccessTokenStsEndpoint"] = oidc_access_token_sts_endpoint
        if oidc_access_token_iam_sa_endpoint is not UNSET:
            field_dict["oidcAccessTokenIamSaEndpoint"] = oidc_access_token_iam_sa_endpoint
        if gcp_service_account_email is not UNSET:
            field_dict["gcpServiceAccountEmail"] = gcp_service_account_email
        if oidc_workload_access_token_request_structure is not UNSET:
            field_dict["oidcWorkloadAccessTokenRequestStructure"] = oidc_workload_access_token_request_structure
        if oidc_chartmuseum_gcp_config_structure is not UNSET:
            field_dict["oidcChartmuseumGcpConfigStructure"] = oidc_chartmuseum_gcp_config_structure
        if id_token_expiry_time is not UNSET:
            field_dict["idTokenExpiryTime"] = id_token_expiry_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_chartmuseum_gcp_config import OidcChartmuseumGcpConfig
        from ..models.oidc_workload_access_token_request import OidcWorkloadAccessTokenRequest

        d = dict(src_dict)
        oidc_id_token = d.pop("oidcIdToken", UNSET)

        oidc_access_token_sts_endpoint = d.pop("oidcAccessTokenStsEndpoint", UNSET)

        oidc_access_token_iam_sa_endpoint = d.pop("oidcAccessTokenIamSaEndpoint", UNSET)

        gcp_service_account_email = d.pop("gcpServiceAccountEmail", UNSET)

        _oidc_workload_access_token_request_structure = d.pop("oidcWorkloadAccessTokenRequestStructure", UNSET)
        oidc_workload_access_token_request_structure: OidcWorkloadAccessTokenRequest | Unset
        if isinstance(_oidc_workload_access_token_request_structure, Unset):
            oidc_workload_access_token_request_structure = UNSET
        else:
            oidc_workload_access_token_request_structure = OidcWorkloadAccessTokenRequest.from_dict(
                _oidc_workload_access_token_request_structure
            )

        _oidc_chartmuseum_gcp_config_structure = d.pop("oidcChartmuseumGcpConfigStructure", UNSET)
        oidc_chartmuseum_gcp_config_structure: OidcChartmuseumGcpConfig | Unset
        if isinstance(_oidc_chartmuseum_gcp_config_structure, Unset):
            oidc_chartmuseum_gcp_config_structure = UNSET
        else:
            oidc_chartmuseum_gcp_config_structure = OidcChartmuseumGcpConfig.from_dict(
                _oidc_chartmuseum_gcp_config_structure
            )

        id_token_expiry_time = d.pop("idTokenExpiryTime", UNSET)

        gcp_oidc_token_exchange_details_for_delegate = cls(
            oidc_id_token=oidc_id_token,
            oidc_access_token_sts_endpoint=oidc_access_token_sts_endpoint,
            oidc_access_token_iam_sa_endpoint=oidc_access_token_iam_sa_endpoint,
            gcp_service_account_email=gcp_service_account_email,
            oidc_workload_access_token_request_structure=oidc_workload_access_token_request_structure,
            oidc_chartmuseum_gcp_config_structure=oidc_chartmuseum_gcp_config_structure,
            id_token_expiry_time=id_token_expiry_time,
        )

        gcp_oidc_token_exchange_details_for_delegate.additional_properties = d
        return gcp_oidc_token_exchange_details_for_delegate

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
