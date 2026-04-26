from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_failure_response import EnvironmentFailureResponse
    from ..models.environment_response import EnvironmentResponse


T = TypeVar("T", bound="EnvironmentBatchResponse")


@_attrs_define
class EnvironmentBatchResponse:
    """Response for batch environment creation with partial success support

    Attributes:
        successful (list[EnvironmentResponse] | Unset): List of successfully created environments
        failed (list[EnvironmentFailureResponse] | Unset): List of environments that failed with error details and scope
            information
        total_requested (int | Unset): Total number of environments in the request
        total_successful (int | Unset): Total number successfully created
        total_failed (int | Unset): Total number that failed
    """

    successful: list[EnvironmentResponse] | Unset = UNSET
    failed: list[EnvironmentFailureResponse] | Unset = UNSET
    total_requested: int | Unset = UNSET
    total_successful: int | Unset = UNSET
    total_failed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        successful: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.successful, Unset):
            successful = []
            for successful_item_data in self.successful:
                successful_item = successful_item_data.to_dict()
                successful.append(successful_item)

        failed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed, Unset):
            failed = []
            for failed_item_data in self.failed:
                failed_item = failed_item_data.to_dict()
                failed.append(failed_item)

        total_requested = self.total_requested

        total_successful = self.total_successful

        total_failed = self.total_failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if successful is not UNSET:
            field_dict["successful"] = successful
        if failed is not UNSET:
            field_dict["failed"] = failed
        if total_requested is not UNSET:
            field_dict["totalRequested"] = total_requested
        if total_successful is not UNSET:
            field_dict["totalSuccessful"] = total_successful
        if total_failed is not UNSET:
            field_dict["totalFailed"] = total_failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_failure_response import EnvironmentFailureResponse
        from ..models.environment_response import EnvironmentResponse

        d = dict(src_dict)
        _successful = d.pop("successful", UNSET)
        successful: list[EnvironmentResponse] | Unset = UNSET
        if _successful is not UNSET:
            successful = []
            for successful_item_data in _successful:
                successful_item = EnvironmentResponse.from_dict(successful_item_data)

                successful.append(successful_item)

        _failed = d.pop("failed", UNSET)
        failed: list[EnvironmentFailureResponse] | Unset = UNSET
        if _failed is not UNSET:
            failed = []
            for failed_item_data in _failed:
                failed_item = EnvironmentFailureResponse.from_dict(failed_item_data)

                failed.append(failed_item)

        total_requested = d.pop("totalRequested", UNSET)

        total_successful = d.pop("totalSuccessful", UNSET)

        total_failed = d.pop("totalFailed", UNSET)

        environment_batch_response = cls(
            successful=successful,
            failed=failed,
            total_requested=total_requested,
            total_successful=total_successful,
            total_failed=total_failed,
        )

        environment_batch_response.additional_properties = d
        return environment_batch_response

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
