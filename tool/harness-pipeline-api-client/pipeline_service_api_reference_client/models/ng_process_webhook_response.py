from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NGProcessWebhookResponse")


@_attrs_define
class NGProcessWebhookResponse:
    """This contains details about the triggered webhook

    Attributes:
        event_correlation_id (str | Unset):
        api_url (str | Unset):
        ui_url (str | Unset):
        ui_setup_url (str | Unset):
    """

    event_correlation_id: str | Unset = UNSET
    api_url: str | Unset = UNSET
    ui_url: str | Unset = UNSET
    ui_setup_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_correlation_id = self.event_correlation_id

        api_url = self.api_url

        ui_url = self.ui_url

        ui_setup_url = self.ui_setup_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_correlation_id is not UNSET:
            field_dict["eventCorrelationId"] = event_correlation_id
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url
        if ui_url is not UNSET:
            field_dict["uiUrl"] = ui_url
        if ui_setup_url is not UNSET:
            field_dict["uiSetupUrl"] = ui_setup_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_correlation_id = d.pop("eventCorrelationId", UNSET)

        api_url = d.pop("apiUrl", UNSET)

        ui_url = d.pop("uiUrl", UNSET)

        ui_setup_url = d.pop("uiSetupUrl", UNSET)

        ng_process_webhook_response = cls(
            event_correlation_id=event_correlation_id,
            api_url=api_url,
            ui_url=ui_url,
            ui_setup_url=ui_setup_url,
        )

        ng_process_webhook_response.additional_properties = d
        return ng_process_webhook_response

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
