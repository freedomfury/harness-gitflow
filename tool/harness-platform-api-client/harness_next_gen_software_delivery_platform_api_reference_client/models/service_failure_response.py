from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_failure_response_error_code import (
    ServiceFailureResponseErrorCode,
    check_service_failure_response_error_code,
)
from ..models.service_failure_response_status import ServiceFailureResponseStatus, check_service_failure_response_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceFailureResponse")


@_attrs_define
class ServiceFailureResponse:
    """Failed service creation/update details with complete scope information

    Attributes:
        account_id (str): Account identifier where the service operation failed
        identifier (str): Service identifier that failed
        status (ServiceFailureResponseStatus): Failure status
        error_message (str): Detailed error message explaining why the service operation failed
        org_identifier (str | Unset): Organization identifier where the service operation failed
        project_identifier (str | Unset): Project identifier where the service operation failed
        error_code (ServiceFailureResponseErrorCode | Unset): Error code representing the type of failure
        correlation_id (str | Unset): Correlation ID for tracking the failure across logs
        git_ops_enabled (bool | Unset): Indicates if GitOps is enabled for the existing duplicate service
    """

    account_id: str
    identifier: str
    status: ServiceFailureResponseStatus
    error_message: str
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    error_code: ServiceFailureResponseErrorCode | Unset = UNSET
    correlation_id: str | Unset = UNSET
    git_ops_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        identifier = self.identifier

        status: str = self.status

        error_message = self.error_message

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code

        correlation_id = self.correlation_id

        git_ops_enabled = self.git_ops_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "identifier": identifier,
                "status": status,
                "errorMessage": error_message,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id
        if git_ops_enabled is not UNSET:
            field_dict["gitOpsEnabled"] = git_ops_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        identifier = d.pop("identifier")

        status = check_service_failure_response_status(d.pop("status"))

        error_message = d.pop("errorMessage")

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: ServiceFailureResponseErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = check_service_failure_response_error_code(_error_code)

        correlation_id = d.pop("correlationId", UNSET)

        git_ops_enabled = d.pop("gitOpsEnabled", UNSET)

        service_failure_response = cls(
            account_id=account_id,
            identifier=identifier,
            status=status,
            error_message=error_message,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            error_code=error_code,
            correlation_id=correlation_id,
            git_ops_enabled=git_ops_enabled,
        )

        service_failure_response.additional_properties = d
        return service_failure_response

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
