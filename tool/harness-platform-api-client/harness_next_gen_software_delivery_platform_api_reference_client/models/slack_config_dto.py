from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_setting_config_dto_type import (
    NotificationSettingConfigDTOType,
    check_notification_setting_config_dto_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlackConfigDTO")


@_attrs_define
class SlackConfigDTO:
    """
    Attributes:
        slack_webhook_url (str):
        type_ (NotificationSettingConfigDTOType | Unset):
    """

    slack_webhook_url: str
    type_: NotificationSettingConfigDTOType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slack_webhook_url = self.slack_webhook_url

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slackWebhookUrl": slack_webhook_url,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slack_webhook_url = d.pop("slackWebhookUrl")

        _type_ = d.pop("type", UNSET)
        type_: NotificationSettingConfigDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_notification_setting_config_dto_type(_type_)

        slack_config_dto = cls(
            slack_webhook_url=slack_webhook_url,
            type_=type_,
        )

        slack_config_dto.additional_properties = d
        return slack_config_dto

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
