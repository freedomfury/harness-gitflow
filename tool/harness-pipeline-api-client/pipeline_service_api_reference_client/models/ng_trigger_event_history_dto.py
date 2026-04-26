from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ng_trigger_event_history_dto_final_status import (
    NGTriggerEventHistoryDTOFinalStatus,
    check_ng_trigger_event_history_dto_final_status,
)
from ..models.ng_trigger_event_history_dto_type import (
    NGTriggerEventHistoryDTOType,
    check_ng_trigger_event_history_dto_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ng_trigger_event_history_dto_headers import NGTriggerEventHistoryDTOHeaders
    from ..models.ng_trigger_event_info import NGTriggerEventInfo
    from ..models.target_execution_summary import TargetExecutionSummary
    from ..models.trigger_event_status import TriggerEventStatus


T = TypeVar("T", bound="NGTriggerEventHistoryDTO")


@_attrs_define
class NGTriggerEventHistoryDTO:
    """
    Attributes:
        trigger_identifier (str | Unset):
        account_id (str | Unset):
        event_correlation_id (str | Unset):
        payload (str | Unset):
        headers (NGTriggerEventHistoryDTOHeaders | Unset):
        event_created_at (int | Unset):
        final_status (NGTriggerEventHistoryDTOFinalStatus | Unset):
        message (str | Unset):
        exception_occurred (bool | Unset):
        created_at (int | Unset):
        trigger_event_status (TriggerEventStatus | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        target_identifier (str | Unset):
        target_execution_summary (TargetExecutionSummary | Unset):
        type_ (NGTriggerEventHistoryDTOType | Unset):
        ng_trigger_event_info (NGTriggerEventInfo | Unset):
    """

    trigger_identifier: str | Unset = UNSET
    account_id: str | Unset = UNSET
    event_correlation_id: str | Unset = UNSET
    payload: str | Unset = UNSET
    headers: NGTriggerEventHistoryDTOHeaders | Unset = UNSET
    event_created_at: int | Unset = UNSET
    final_status: NGTriggerEventHistoryDTOFinalStatus | Unset = UNSET
    message: str | Unset = UNSET
    exception_occurred: bool | Unset = UNSET
    created_at: int | Unset = UNSET
    trigger_event_status: TriggerEventStatus | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    target_identifier: str | Unset = UNSET
    target_execution_summary: TargetExecutionSummary | Unset = UNSET
    type_: NGTriggerEventHistoryDTOType | Unset = UNSET
    ng_trigger_event_info: NGTriggerEventInfo | Unset = UNSET
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

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        target_identifier = self.target_identifier

        target_execution_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_execution_summary, Unset):
            target_execution_summary = self.target_execution_summary.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        ng_trigger_event_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ng_trigger_event_info, Unset):
            ng_trigger_event_info = self.ng_trigger_event_info.to_dict()

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
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if target_identifier is not UNSET:
            field_dict["targetIdentifier"] = target_identifier
        if target_execution_summary is not UNSET:
            field_dict["targetExecutionSummary"] = target_execution_summary
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ng_trigger_event_info is not UNSET:
            field_dict["ngTriggerEventInfo"] = ng_trigger_event_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ng_trigger_event_history_dto_headers import NGTriggerEventHistoryDTOHeaders
        from ..models.ng_trigger_event_info import NGTriggerEventInfo
        from ..models.target_execution_summary import TargetExecutionSummary
        from ..models.trigger_event_status import TriggerEventStatus

        d = dict(src_dict)
        trigger_identifier = d.pop("triggerIdentifier", UNSET)

        account_id = d.pop("accountId", UNSET)

        event_correlation_id = d.pop("eventCorrelationId", UNSET)

        payload = d.pop("payload", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: NGTriggerEventHistoryDTOHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = NGTriggerEventHistoryDTOHeaders.from_dict(_headers)

        event_created_at = d.pop("eventCreatedAt", UNSET)

        _final_status = d.pop("finalStatus", UNSET)
        final_status: NGTriggerEventHistoryDTOFinalStatus | Unset
        if isinstance(_final_status, Unset):
            final_status = UNSET
        else:
            final_status = check_ng_trigger_event_history_dto_final_status(_final_status)

        message = d.pop("message", UNSET)

        exception_occurred = d.pop("exceptionOccurred", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _trigger_event_status = d.pop("triggerEventStatus", UNSET)
        trigger_event_status: TriggerEventStatus | Unset
        if isinstance(_trigger_event_status, Unset):
            trigger_event_status = UNSET
        else:
            trigger_event_status = TriggerEventStatus.from_dict(_trigger_event_status)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        target_identifier = d.pop("targetIdentifier", UNSET)

        _target_execution_summary = d.pop("targetExecutionSummary", UNSET)
        target_execution_summary: TargetExecutionSummary | Unset
        if isinstance(_target_execution_summary, Unset):
            target_execution_summary = UNSET
        else:
            target_execution_summary = TargetExecutionSummary.from_dict(_target_execution_summary)

        _type_ = d.pop("type", UNSET)
        type_: NGTriggerEventHistoryDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_ng_trigger_event_history_dto_type(_type_)

        _ng_trigger_event_info = d.pop("ngTriggerEventInfo", UNSET)
        ng_trigger_event_info: NGTriggerEventInfo | Unset
        if isinstance(_ng_trigger_event_info, Unset):
            ng_trigger_event_info = UNSET
        else:
            ng_trigger_event_info = NGTriggerEventInfo.from_dict(_ng_trigger_event_info)

        ng_trigger_event_history_dto = cls(
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
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            target_identifier=target_identifier,
            target_execution_summary=target_execution_summary,
            type_=type_,
            ng_trigger_event_info=ng_trigger_event_info,
        )

        ng_trigger_event_history_dto.additional_properties = d
        return ng_trigger_event_history_dto

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
