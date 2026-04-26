from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ng_trigger_events_api_response_ng_trigger_type import (
    NGTriggerEventsApiResponseNgTriggerType,
    check_ng_trigger_events_api_response_ng_trigger_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ng_trigger_meta_data import NGTriggerMetaData
    from ..models.scope import Scope
    from ..models.trigger_event_status import TriggerEventStatus


T = TypeVar("T", bound="NGTriggerEventsApiResponse")


@_attrs_define
class NGTriggerEventsApiResponse:
    """
    Attributes:
        trigger_identifier (str):
        name (str | Unset):
        scope (Scope | Unset):
        event_correlation_id (str | Unset):
        event_created_at (int | Unset):
        message (str | Unset):
        trigger_event_status (TriggerEventStatus | Unset):
        ng_trigger_type (NGTriggerEventsApiResponseNgTriggerType | Unset):
        sub_trigger_type (str | Unset):
        ng_trigger_meta_data (NGTriggerMetaData | Unset):
    """

    trigger_identifier: str
    name: str | Unset = UNSET
    scope: Scope | Unset = UNSET
    event_correlation_id: str | Unset = UNSET
    event_created_at: int | Unset = UNSET
    message: str | Unset = UNSET
    trigger_event_status: TriggerEventStatus | Unset = UNSET
    ng_trigger_type: NGTriggerEventsApiResponseNgTriggerType | Unset = UNSET
    sub_trigger_type: str | Unset = UNSET
    ng_trigger_meta_data: NGTriggerMetaData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_identifier = self.trigger_identifier

        name = self.name

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        event_correlation_id = self.event_correlation_id

        event_created_at = self.event_created_at

        message = self.message

        trigger_event_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_event_status, Unset):
            trigger_event_status = self.trigger_event_status.to_dict()

        ng_trigger_type: str | Unset = UNSET
        if not isinstance(self.ng_trigger_type, Unset):
            ng_trigger_type = self.ng_trigger_type

        sub_trigger_type = self.sub_trigger_type

        ng_trigger_meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ng_trigger_meta_data, Unset):
            ng_trigger_meta_data = self.ng_trigger_meta_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "triggerIdentifier": trigger_identifier,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if event_correlation_id is not UNSET:
            field_dict["eventCorrelationId"] = event_correlation_id
        if event_created_at is not UNSET:
            field_dict["eventCreatedAt"] = event_created_at
        if message is not UNSET:
            field_dict["message"] = message
        if trigger_event_status is not UNSET:
            field_dict["triggerEventStatus"] = trigger_event_status
        if ng_trigger_type is not UNSET:
            field_dict["ngTriggerType"] = ng_trigger_type
        if sub_trigger_type is not UNSET:
            field_dict["subTriggerType"] = sub_trigger_type
        if ng_trigger_meta_data is not UNSET:
            field_dict["ngTriggerMetaData"] = ng_trigger_meta_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ng_trigger_meta_data import NGTriggerMetaData
        from ..models.scope import Scope
        from ..models.trigger_event_status import TriggerEventStatus

        d = dict(src_dict)
        trigger_identifier = d.pop("triggerIdentifier")

        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = Scope.from_dict(_scope)

        event_correlation_id = d.pop("eventCorrelationId", UNSET)

        event_created_at = d.pop("eventCreatedAt", UNSET)

        message = d.pop("message", UNSET)

        _trigger_event_status = d.pop("triggerEventStatus", UNSET)
        trigger_event_status: TriggerEventStatus | Unset
        if isinstance(_trigger_event_status, Unset):
            trigger_event_status = UNSET
        else:
            trigger_event_status = TriggerEventStatus.from_dict(_trigger_event_status)

        _ng_trigger_type = d.pop("ngTriggerType", UNSET)
        ng_trigger_type: NGTriggerEventsApiResponseNgTriggerType | Unset
        if isinstance(_ng_trigger_type, Unset):
            ng_trigger_type = UNSET
        else:
            ng_trigger_type = check_ng_trigger_events_api_response_ng_trigger_type(_ng_trigger_type)

        sub_trigger_type = d.pop("subTriggerType", UNSET)

        _ng_trigger_meta_data = d.pop("ngTriggerMetaData", UNSET)
        ng_trigger_meta_data: NGTriggerMetaData | Unset
        if isinstance(_ng_trigger_meta_data, Unset):
            ng_trigger_meta_data = UNSET
        else:
            ng_trigger_meta_data = NGTriggerMetaData.from_dict(_ng_trigger_meta_data)

        ng_trigger_events_api_response = cls(
            trigger_identifier=trigger_identifier,
            name=name,
            scope=scope,
            event_correlation_id=event_correlation_id,
            event_created_at=event_created_at,
            message=message,
            trigger_event_status=trigger_event_status,
            ng_trigger_type=ng_trigger_type,
            sub_trigger_type=sub_trigger_type,
            ng_trigger_meta_data=ng_trigger_meta_data,
        )

        ng_trigger_events_api_response.additional_properties = d
        return ng_trigger_events_api_response

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
