from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEventProcessingDetails")


@_attrs_define
class WebhookEventProcessingDetails:
    """
    Attributes:
        event_found (bool | Unset):
        event_id (str | Unset):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        trigger_identifier (str | Unset):
        pipeline_identifier (str | Unset):
        pipeline_execution_id (str | Unset):
        exception_occured (bool | Unset):
        status (str | Unset):
        message (str | Unset):
        payload (str | Unset):
        event_created_at (int | Unset):
        runtime_input (str | Unset):
        warning_msg (str | Unset):
    """

    event_found: bool | Unset = UNSET
    event_id: str | Unset = UNSET
    account_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    trigger_identifier: str | Unset = UNSET
    pipeline_identifier: str | Unset = UNSET
    pipeline_execution_id: str | Unset = UNSET
    exception_occured: bool | Unset = UNSET
    status: str | Unset = UNSET
    message: str | Unset = UNSET
    payload: str | Unset = UNSET
    event_created_at: int | Unset = UNSET
    runtime_input: str | Unset = UNSET
    warning_msg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_found = self.event_found

        event_id = self.event_id

        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        trigger_identifier = self.trigger_identifier

        pipeline_identifier = self.pipeline_identifier

        pipeline_execution_id = self.pipeline_execution_id

        exception_occured = self.exception_occured

        status = self.status

        message = self.message

        payload = self.payload

        event_created_at = self.event_created_at

        runtime_input = self.runtime_input

        warning_msg = self.warning_msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_found is not UNSET:
            field_dict["eventFound"] = event_found
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if trigger_identifier is not UNSET:
            field_dict["triggerIdentifier"] = trigger_identifier
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if pipeline_execution_id is not UNSET:
            field_dict["pipelineExecutionId"] = pipeline_execution_id
        if exception_occured is not UNSET:
            field_dict["exceptionOccured"] = exception_occured
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if payload is not UNSET:
            field_dict["payload"] = payload
        if event_created_at is not UNSET:
            field_dict["eventCreatedAt"] = event_created_at
        if runtime_input is not UNSET:
            field_dict["runtimeInput"] = runtime_input
        if warning_msg is not UNSET:
            field_dict["warningMsg"] = warning_msg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_found = d.pop("eventFound", UNSET)

        event_id = d.pop("eventId", UNSET)

        account_identifier = d.pop("accountIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        trigger_identifier = d.pop("triggerIdentifier", UNSET)

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        pipeline_execution_id = d.pop("pipelineExecutionId", UNSET)

        exception_occured = d.pop("exceptionOccured", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        payload = d.pop("payload", UNSET)

        event_created_at = d.pop("eventCreatedAt", UNSET)

        runtime_input = d.pop("runtimeInput", UNSET)

        warning_msg = d.pop("warningMsg", UNSET)

        webhook_event_processing_details = cls(
            event_found=event_found,
            event_id=event_id,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            trigger_identifier=trigger_identifier,
            pipeline_identifier=pipeline_identifier,
            pipeline_execution_id=pipeline_execution_id,
            exception_occured=exception_occured,
            status=status,
            message=message,
            payload=payload,
            event_created_at=event_created_at,
            runtime_input=runtime_input,
            warning_msg=warning_msg,
        )

        webhook_event_processing_details.additional_properties = d
        return webhook_event_processing_details

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
