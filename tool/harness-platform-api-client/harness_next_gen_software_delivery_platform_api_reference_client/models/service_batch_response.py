from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_failure_response import ServiceFailureResponse
    from ..models.service_response import ServiceResponse


T = TypeVar("T", bound="ServiceBatchResponse")


@_attrs_define
class ServiceBatchResponse:
    """Batch service creation response with partial success support

    Attributes:
        successful_services (list[ServiceResponse] | Unset): List of successfully created services
        failed_services (list[ServiceFailureResponse] | Unset): List of failed service creation attempts with complete
            scope information
        total_requested (int | Unset): Total number of services requested for creation
        total_success (int | Unset): Total number of successfully created services
        total_failed (int | Unset): Total number of failed service creations
    """

    successful_services: list[ServiceResponse] | Unset = UNSET
    failed_services: list[ServiceFailureResponse] | Unset = UNSET
    total_requested: int | Unset = UNSET
    total_success: int | Unset = UNSET
    total_failed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        successful_services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.successful_services, Unset):
            successful_services = []
            for successful_services_item_data in self.successful_services:
                successful_services_item = successful_services_item_data.to_dict()
                successful_services.append(successful_services_item)

        failed_services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_services, Unset):
            failed_services = []
            for failed_services_item_data in self.failed_services:
                failed_services_item = failed_services_item_data.to_dict()
                failed_services.append(failed_services_item)

        total_requested = self.total_requested

        total_success = self.total_success

        total_failed = self.total_failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if successful_services is not UNSET:
            field_dict["successfulServices"] = successful_services
        if failed_services is not UNSET:
            field_dict["failedServices"] = failed_services
        if total_requested is not UNSET:
            field_dict["totalRequested"] = total_requested
        if total_success is not UNSET:
            field_dict["totalSuccess"] = total_success
        if total_failed is not UNSET:
            field_dict["totalFailed"] = total_failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_failure_response import ServiceFailureResponse
        from ..models.service_response import ServiceResponse

        d = dict(src_dict)
        _successful_services = d.pop("successfulServices", UNSET)
        successful_services: list[ServiceResponse] | Unset = UNSET
        if _successful_services is not UNSET:
            successful_services = []
            for successful_services_item_data in _successful_services:
                successful_services_item = ServiceResponse.from_dict(successful_services_item_data)

                successful_services.append(successful_services_item)

        _failed_services = d.pop("failedServices", UNSET)
        failed_services: list[ServiceFailureResponse] | Unset = UNSET
        if _failed_services is not UNSET:
            failed_services = []
            for failed_services_item_data in _failed_services:
                failed_services_item = ServiceFailureResponse.from_dict(failed_services_item_data)

                failed_services.append(failed_services_item)

        total_requested = d.pop("totalRequested", UNSET)

        total_success = d.pop("totalSuccess", UNSET)

        total_failed = d.pop("totalFailed", UNSET)

        service_batch_response = cls(
            successful_services=successful_services,
            failed_services=failed_services,
            total_requested=total_requested,
            total_success=total_success,
            total_failed=total_failed,
        )

        service_batch_response.additional_properties = d
        return service_batch_response

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
