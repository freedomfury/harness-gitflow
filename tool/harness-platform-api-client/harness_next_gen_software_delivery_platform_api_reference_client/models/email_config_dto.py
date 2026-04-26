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

T = TypeVar("T", bound="EmailConfigDTO")


@_attrs_define
class EmailConfigDTO:
    """
    Attributes:
        group_email (str):
        send_email_to_all_users (bool):
        type_ (NotificationSettingConfigDTOType | Unset):
    """

    group_email: str
    send_email_to_all_users: bool
    type_: NotificationSettingConfigDTOType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_email = self.group_email

        send_email_to_all_users = self.send_email_to_all_users

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupEmail": group_email,
                "sendEmailToAllUsers": send_email_to_all_users,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_email = d.pop("groupEmail")

        send_email_to_all_users = d.pop("sendEmailToAllUsers")

        _type_ = d.pop("type", UNSET)
        type_: NotificationSettingConfigDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_notification_setting_config_dto_type(_type_)

        email_config_dto = cls(
            group_email=group_email,
            send_email_to_all_users=send_email_to_all_users,
            type_=type_,
        )

        email_config_dto.additional_properties = d
        return email_config_dto

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
