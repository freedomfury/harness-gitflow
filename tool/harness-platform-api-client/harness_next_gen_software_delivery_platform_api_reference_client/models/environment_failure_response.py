from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment_failure_response_error_code import (
    EnvironmentFailureResponseErrorCode,
    check_environment_failure_response_error_code,
)
from ..models.environment_failure_response_status import (
    EnvironmentFailureResponseStatus,
    check_environment_failure_response_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentFailureResponse")


@_attrs_define
class EnvironmentFailureResponse:
    """Failed environment creation/update details with complete scope information

    Attributes:
        account_id (str): Account identifier where the environment operation failed
        identifier (str): Environment identifier that failed
        status (EnvironmentFailureResponseStatus): Failure status
        error_message (str): Detailed error message explaining why the environment operation failed
        org_identifier (str | Unset): Organization identifier where the environment operation failed
        project_identifier (str | Unset): Project identifier where the environment operation failed
        error_code (EnvironmentFailureResponseErrorCode | Unset): Error code representing the type of failure
    """

    account_id: str
    identifier: str
    status: EnvironmentFailureResponseStatus
    error_message: str
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    error_code: EnvironmentFailureResponseErrorCode | Unset = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        identifier = d.pop("identifier")

        status = check_environment_failure_response_status(d.pop("status"))

        error_message = d.pop("errorMessage")

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: EnvironmentFailureResponseErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = check_environment_failure_response_error_code(_error_code)

        environment_failure_response = cls(
            account_id=account_id,
            identifier=identifier,
            status=status,
            error_message=error_message,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            error_code=error_code,
        )

        environment_failure_response.additional_properties = d
        return environment_failure_response

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
