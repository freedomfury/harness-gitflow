from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ng_trigger_event_history_base_dto_final_status import (
    NGTriggerEventHistoryBaseDTOFinalStatus,
    check_ng_trigger_event_history_base_dto_final_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ng_trigger_event_history_base_dto_headers import NGTriggerEventHistoryBaseDTOHeaders
    from ..models.trigger_event_status import TriggerEventStatus


T = TypeVar("T", bound="NGTriggerEventHistoryBaseDTO")


@_attrs_define
class NGTriggerEventHistoryBaseDTO:
    """
    Attributes:
        trigger_identifier (str | Unset):
        account_id (str | Unset):
        event_correlation_id (str | Unset):
        payload (str | Unset):
        headers (NGTriggerEventHistoryBaseDTOHeaders | Unset):
        event_created_at (int | Unset):
        final_status (NGTriggerEventHistoryBaseDTOFinalStatus | Unset):
        message (str | Unset):
        exception_occurred (bool | Unset):
        created_at (int | Unset):
        trigger_event_status (TriggerEventStatus | Unset):
    """

    trigger_identifier: str | Unset = UNSET
    account_id: str | Unset = UNSET
    event_correlation_id: str | Unset = UNSET
    payload: str | Unset = UNSET
    headers: NGTriggerEventHistoryBaseDTOHeaders | Unset = UNSET
    event_created_at: int | Unset = UNSET
    final_status: NGTriggerEventHistoryBaseDTOFinalStatus | Unset = UNSET
    message: str | Unset = UNSET
    exception_occurred: bool | Unset = UNSET
    created_at: int | Unset = UNSET
    trigger_event_status: TriggerEventStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_identifier = self.trigger_identifier

        account_id = self.account_id

        event_correlation_id = self.event_correlation_id

        payload = self.payload

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        event_created_at = self.event_created_at

        final_status: str | Unset = UNSET
        if not isinstance(self.final_status, Unset):
            final_status = self.final_status

        message = self.message

        exception_occurred = self.exception_occurred

        created_at = self.created_at

        trigger_event_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_event_status, Unset):
            trigger_event_status = self.trigger_event_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trigger_identifier is not UNSET:
            field_dict["triggerIdentifier"] = trigger_identifier
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if event_correlation_id is not UNSET:
            field_dict["eventCorrelationId"] = event_correlation_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if headers is not UNSET:
            field_dict["headers"] = headers
        if event_created_at is not UNSET:
            field_dict["eventCreatedAt"] = event_created_at
        if final_status is not UNSET:
            field_dict["finalStatus"] = final_status
        if message is not UNSET:
            field_dict["message"] = message
        if exception_occurred is not UNSET:
            field_dict["exceptionOccurred"] = exception_occurred
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if trigger_event_status is not UNSET:
            field_dict["triggerEventStatus"] = trigger_event_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ng_trigger_event_history_base_dto_headers import NGTriggerEventHistoryBaseDTOHeaders
        from ..models.trigger_event_status import TriggerEventStatus

        d = dict(src_dict)
        trigger_identifier = d.pop("triggerIdentifier", UNSET)

        account_id = d.pop("accountId", UNSET)

        event_correlation_id = d.pop("eventCorrelationId", UNSET)

        payload = d.pop("payload", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: NGTriggerEventHistoryBaseDTOHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = NGTriggerEventHistoryBaseDTOHeaders.from_dict(_headers)

        event_created_at = d.pop("eventCreatedAt", UNSET)

        _final_status = d.pop("finalStatus", UNSET)
        final_status: NGTriggerEventHistoryBaseDTOFinalStatus | Unset
        if isinstance(_final_status, Unset):
            final_status = UNSET
        else:
            final_status = check_ng_trigger_event_history_base_dto_final_status(_final_status)

        message = d.pop("message", UNSET)

        exception_occurred = d.pop("exceptionOccurred", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _trigger_event_status = d.pop("triggerEventStatus", UNSET)
        trigger_event_status: TriggerEventStatus | Unset
        if isinstance(_trigger_event_status, Unset):
            trigger_event_status = UNSET
        else:
            trigger_event_status = TriggerEventStatus.from_dict(_trigger_event_status)

        ng_trigger_event_history_base_dto = cls(
            trigger_identifier=trigger_identifier,
            account_id=account_id,
            event_correlation_id=event_correlation_id,
            payload=payload,
            headers=headers,
            event_created_at=event_created_at,
            final_status=final_status,
            message=message,
            exception_occurred=exception_occurred,
            created_at=created_at,
            trigger_event_status=trigger_event_status,
        )

        ng_trigger_event_history_base_dto.additional_properties = d
        return ng_trigger_event_history_base_dto

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
