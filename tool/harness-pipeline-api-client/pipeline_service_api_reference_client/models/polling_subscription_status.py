from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polling_subscription_status_status_result import (
    PollingSubscriptionStatusStatusResult,
    check_polling_subscription_status_status_result,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PollingSubscriptionStatus")


@_attrs_define
class PollingSubscriptionStatus:
    """
    Attributes:
        status_result (PollingSubscriptionStatusStatusResult | Unset):
        detailed_message (str | Unset):
        last_polled (list[str] | Unset):
        last_polling_update (int | Unset):
        error_status_valid_until (int | Unset):
    """

    status_result: PollingSubscriptionStatusStatusResult | Unset = UNSET
    detailed_message: str | Unset = UNSET
    last_polled: list[str] | Unset = UNSET
    last_polling_update: int | Unset = UNSET
    error_status_valid_until: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_result: str | Unset = UNSET
        if not isinstance(self.status_result, Unset):
            status_result = self.status_result

        detailed_message = self.detailed_message

        last_polled: list[str] | Unset = UNSET
        if not isinstance(self.last_polled, Unset):
            last_polled = self.last_polled

        last_polling_update = self.last_polling_update

        error_status_valid_until = self.error_status_valid_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_result is not UNSET:
            field_dict["statusResult"] = status_result
        if detailed_message is not UNSET:
            field_dict["detailedMessage"] = detailed_message
        if last_polled is not UNSET:
            field_dict["lastPolled"] = last_polled
        if last_polling_update is not UNSET:
            field_dict["lastPollingUpdate"] = last_polling_update
        if error_status_valid_until is not UNSET:
            field_dict["errorStatusValidUntil"] = error_status_valid_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status_result = d.pop("statusResult", UNSET)
        status_result: PollingSubscriptionStatusStatusResult | Unset
        if isinstance(_status_result, Unset):
            status_result = UNSET
        else:
            status_result = check_polling_subscription_status_status_result(_status_result)

        detailed_message = d.pop("detailedMessage", UNSET)

        last_polled = cast(list[str], d.pop("lastPolled", UNSET))

        last_polling_update = d.pop("lastPollingUpdate", UNSET)

        error_status_valid_until = d.pop("errorStatusValidUntil", UNSET)

        polling_subscription_status = cls(
            status_result=status_result,
            detailed_message=detailed_message,
            last_polled=last_polled,
            last_polling_update=last_polling_update,
            error_status_valid_until=error_status_valid_until,
        )

        polling_subscription_status.additional_properties = d
        return polling_subscription_status

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
