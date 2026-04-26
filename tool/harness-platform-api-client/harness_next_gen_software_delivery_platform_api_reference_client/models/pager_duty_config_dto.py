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

T = TypeVar("T", bound="PagerDutyConfigDTO")


@_attrs_define
class PagerDutyConfigDTO:
    """
    Attributes:
        pager_duty_key (str):
        type_ (NotificationSettingConfigDTOType | Unset):
    """

    pager_duty_key: str
    type_: NotificationSettingConfigDTOType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager_duty_key = self.pager_duty_key

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagerDutyKey": pager_duty_key,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pager_duty_key = d.pop("pagerDutyKey")

        _type_ = d.pop("type", UNSET)
        type_: NotificationSettingConfigDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_notification_setting_config_dto_type(_type_)

        pager_duty_config_dto = cls(
            pager_duty_key=pager_duty_key,
            type_=type_,
        )

        pager_duty_config_dto.additional_properties = d
        return pager_duty_config_dto

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
