from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_event_processing_details import WebhookEventProcessingDetails
    from ..models.webhook_execution_details_execution_details import WebhookExecutionDetailsExecutionDetails


T = TypeVar("T", bound="WebhookExecutionDetails")


@_attrs_define
class WebhookExecutionDetails:
    """
    Attributes:
        webhook_processing_details (WebhookEventProcessingDetails | Unset):
        execution_details (WebhookExecutionDetailsExecutionDetails | Unset):
        execution_url (str | Unset):
    """

    webhook_processing_details: WebhookEventProcessingDetails | Unset = UNSET
    execution_details: WebhookExecutionDetailsExecutionDetails | Unset = UNSET
    execution_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_processing_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_processing_details, Unset):
            webhook_processing_details = self.webhook_processing_details.to_dict()

        execution_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_details, Unset):
            execution_details = self.execution_details.to_dict()

        execution_url = self.execution_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_processing_details is not UNSET:
            field_dict["webhookProcessingDetails"] = webhook_processing_details
        if execution_details is not UNSET:
            field_dict["executionDetails"] = execution_details
        if execution_url is not UNSET:
            field_dict["executionUrl"] = execution_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_event_processing_details import WebhookEventProcessingDetails
        from ..models.webhook_execution_details_execution_details import WebhookExecutionDetailsExecutionDetails

        d = dict(src_dict)
        _webhook_processing_details = d.pop("webhookProcessingDetails", UNSET)
        webhook_processing_details: WebhookEventProcessingDetails | Unset
        if isinstance(_webhook_processing_details, Unset):
            webhook_processing_details = UNSET
        else:
            webhook_processing_details = WebhookEventProcessingDetails.from_dict(_webhook_processing_details)

        _execution_details = d.pop("executionDetails", UNSET)
        execution_details: WebhookExecutionDetailsExecutionDetails | Unset
        if isinstance(_execution_details, Unset):
            execution_details = UNSET
        else:
            execution_details = WebhookExecutionDetailsExecutionDetails.from_dict(_execution_details)

        execution_url = d.pop("executionUrl", UNSET)

        webhook_execution_details = cls(
            webhook_processing_details=webhook_processing_details,
            execution_details=execution_details,
            execution_url=execution_url,
        )

        webhook_execution_details.additional_properties = d
        return webhook_execution_details

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
