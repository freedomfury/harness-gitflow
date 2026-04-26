from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_auto_registration_status_registration_result import (
    WebhookAutoRegistrationStatusRegistrationResult,
    check_webhook_auto_registration_status_registration_result,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookAutoRegistrationStatus")


@_attrs_define
class WebhookAutoRegistrationStatus:
    """
    Attributes:
        registration_result (WebhookAutoRegistrationStatusRegistrationResult | Unset):
        detailed_message (str | Unset):
    """

    registration_result: WebhookAutoRegistrationStatusRegistrationResult | Unset = UNSET
    detailed_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registration_result: str | Unset = UNSET
        if not isinstance(self.registration_result, Unset):
            registration_result = self.registration_result

        detailed_message = self.detailed_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if registration_result is not UNSET:
            field_dict["registrationResult"] = registration_result
        if detailed_message is not UNSET:
            field_dict["detailedMessage"] = detailed_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _registration_result = d.pop("registrationResult", UNSET)
        registration_result: WebhookAutoRegistrationStatusRegistrationResult | Unset
        if isinstance(_registration_result, Unset):
            registration_result = UNSET
        else:
            registration_result = check_webhook_auto_registration_status_registration_result(_registration_result)

        detailed_message = d.pop("detailedMessage", UNSET)

        webhook_auto_registration_status = cls(
            registration_result=registration_result,
            detailed_message=detailed_message,
        )

        webhook_auto_registration_status.additional_properties = d
        return webhook_auto_registration_status

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
