from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GcpOidcDetails")


@_attrs_define
class GcpOidcDetails:
    """This contains GCP OIDC details

    Attributes:
        workload_pool_id (str):
        provider_id (str):
        gcp_project_id (str):
        service_account_email (str):
    """

    workload_pool_id: str
    provider_id: str
    gcp_project_id: str
    service_account_email: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workload_pool_id = self.workload_pool_id

        provider_id = self.provider_id

        gcp_project_id = self.gcp_project_id

        service_account_email = self.service_account_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workloadPoolId": workload_pool_id,
                "providerId": provider_id,
                "gcpProjectId": gcp_project_id,
                "serviceAccountEmail": service_account_email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workload_pool_id = d.pop("workloadPoolId")

        provider_id = d.pop("providerId")

        gcp_project_id = d.pop("gcpProjectId")

        service_account_email = d.pop("serviceAccountEmail")

        gcp_oidc_details = cls(
            workload_pool_id=workload_pool_id,
            provider_id=provider_id,
            gcp_project_id=gcp_project_id,
            service_account_email=service_account_email,
        )

        gcp_oidc_details.additional_properties = d
        return gcp_oidc_details

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
