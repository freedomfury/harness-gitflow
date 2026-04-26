from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JDBCGcpOidcSpecDTO")


@_attrs_define
class JDBCGcpOidcSpecDTO:
    """GCP OIDC configuration for JDBC authentication

    Attributes:
        type_ (str):
        project_number (str): GCP project number (numeric) Example: 145904791365.
        workload_pool_id (str): Workload Identity Pool ID Example: harness-identity-pool.
        provider_id (str): OIDC Provider ID within the pool Example: harness-oidc-provider.
        service_account_email (str): GCP Service Account email for impersonation Example: db-
            sa@project.iam.gserviceaccount.com.
    """

    type_: str
    project_number: str
    workload_pool_id: str
    provider_id: str
    service_account_email: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        project_number = self.project_number

        workload_pool_id = self.workload_pool_id

        provider_id = self.provider_id

        service_account_email = self.service_account_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "projectNumber": project_number,
                "workloadPoolId": workload_pool_id,
                "providerId": provider_id,
                "serviceAccountEmail": service_account_email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        project_number = d.pop("projectNumber")

        workload_pool_id = d.pop("workloadPoolId")

        provider_id = d.pop("providerId")

        service_account_email = d.pop("serviceAccountEmail")

        jdbc_gcp_oidc_spec_dto = cls(
            type_=type_,
            project_number=project_number,
            workload_pool_id=workload_pool_id,
            provider_id=provider_id,
            service_account_email=service_account_email,
        )

        jdbc_gcp_oidc_spec_dto.additional_properties = d
        return jdbc_gcp_oidc_spec_dto

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
