from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_status_status import TriggerStatusStatus, check_trigger_status_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polling_subscription_status import PollingSubscriptionStatus
    from ..models.validation_status import ValidationStatus
    from ..models.webhook_auto_registration_status import WebhookAutoRegistrationStatus
    from ..models.webhook_info import WebhookInfo


T = TypeVar("T", bound="TriggerStatus")


@_attrs_define
class TriggerStatus:
    """
    Attributes:
        polling_subscription_status (PollingSubscriptionStatus | Unset):
        validation_status (ValidationStatus | Unset):
        webhook_auto_registration_status (WebhookAutoRegistrationStatus | Unset):
        webhook_info (WebhookInfo | Unset):
        status (TriggerStatusStatus | Unset):
        detail_messages (list[str] | Unset):
        last_polling_update (int | Unset):
        last_polled (list[str] | Unset):
    """

    polling_subscription_status: PollingSubscriptionStatus | Unset = UNSET
    validation_status: ValidationStatus | Unset = UNSET
    webhook_auto_registration_status: WebhookAutoRegistrationStatus | Unset = UNSET
    webhook_info: WebhookInfo | Unset = UNSET
    status: TriggerStatusStatus | Unset = UNSET
    detail_messages: list[str] | Unset = UNSET
    last_polling_update: int | Unset = UNSET
    last_polled: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        polling_subscription_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.polling_subscription_status, Unset):
            polling_subscription_status = self.polling_subscription_status.to_dict()

        validation_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validation_status, Unset):
            validation_status = self.validation_status.to_dict()

        webhook_auto_registration_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_auto_registration_status, Unset):
            webhook_auto_registration_status = self.webhook_auto_registration_status.to_dict()

        webhook_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_info, Unset):
            webhook_info = self.webhook_info.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        detail_messages: list[str] | Unset = UNSET
        if not isinstance(self.detail_messages, Unset):
            detail_messages = self.detail_messages

        last_polling_update = self.last_polling_update

        last_polled: list[str] | Unset = UNSET
        if not isinstance(self.last_polled, Unset):
            last_polled = self.last_polled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if polling_subscription_status is not UNSET:
            field_dict["pollingSubscriptionStatus"] = polling_subscription_status
        if validation_status is not UNSET:
            field_dict["validationStatus"] = validation_status
        if webhook_auto_registration_status is not UNSET:
            field_dict["webhookAutoRegistrationStatus"] = webhook_auto_registration_status
        if webhook_info is not UNSET:
            field_dict["webhookInfo"] = webhook_info
        if status is not UNSET:
            field_dict["status"] = status
        if detail_messages is not UNSET:
            field_dict["detailMessages"] = detail_messages
        if last_polling_update is not UNSET:
            field_dict["lastPollingUpdate"] = last_polling_update
        if last_polled is not UNSET:
            field_dict["lastPolled"] = last_polled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polling_subscription_status import PollingSubscriptionStatus
        from ..models.validation_status import ValidationStatus
        from ..models.webhook_auto_registration_status import WebhookAutoRegistrationStatus
        from ..models.webhook_info import WebhookInfo

        d = dict(src_dict)
        _polling_subscription_status = d.pop("pollingSubscriptionStatus", UNSET)
        polling_subscription_status: PollingSubscriptionStatus | Unset
        if isinstance(_polling_subscription_status, Unset):
            polling_subscription_status = UNSET
        else:
            polling_subscription_status = PollingSubscriptionStatus.from_dict(_polling_subscription_status)

        _validation_status = d.pop("validationStatus", UNSET)
        validation_status: ValidationStatus | Unset
        if isinstance(_validation_status, Unset):
            validation_status = UNSET
        else:
            validation_status = ValidationStatus.from_dict(_validation_status)

        _webhook_auto_registration_status = d.pop("webhookAutoRegistrationStatus", UNSET)
        webhook_auto_registration_status: WebhookAutoRegistrationStatus | Unset
        if isinstance(_webhook_auto_registration_status, Unset):
            webhook_auto_registration_status = UNSET
        else:
            webhook_auto_registration_status = WebhookAutoRegistrationStatus.from_dict(
                _webhook_auto_registration_status
            )

        _webhook_info = d.pop("webhookInfo", UNSET)
        webhook_info: WebhookInfo | Unset
        if isinstance(_webhook_info, Unset):
            webhook_info = UNSET
        else:
            webhook_info = WebhookInfo.from_dict(_webhook_info)

        _status = d.pop("status", UNSET)
        status: TriggerStatusStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_trigger_status_status(_status)

        detail_messages = cast(list[str], d.pop("detailMessages", UNSET))

        last_polling_update = d.pop("lastPollingUpdate", UNSET)

        last_polled = cast(list[str], d.pop("lastPolled", UNSET))

        trigger_status = cls(
            polling_subscription_status=polling_subscription_status,
            validation_status=validation_status,
            webhook_auto_registration_status=webhook_auto_registration_status,
            webhook_info=webhook_info,
            status=status,
            detail_messages=detail_messages,
            last_polling_update=last_polling_update,
            last_polled=last_polled,
        )

        trigger_status.additional_properties = d
        return trigger_status

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
