from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_setting_request_dto_update_type import (
    UserSettingRequestDTOUpdateType,
    check_user_setting_request_dto_update_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSettingRequestDTO")


@_attrs_define
class UserSettingRequestDTO:
    """
    Attributes:
        identifier (str): Identifier of the Setting.
        update_type (UserSettingRequestDTOUpdateType): Type of the update operation. When update type is RESTORE, field
            [value] is ignored
        value (str | Unset): Value of the setting
        enable_across_accounts (bool | Unset):
    """

    identifier: str
    update_type: UserSettingRequestDTOUpdateType
    value: str | Unset = UNSET
    enable_across_accounts: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        update_type: str = self.update_type

        value = self.value

        enable_across_accounts = self.enable_across_accounts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "updateType": update_type,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if enable_across_accounts is not UNSET:
            field_dict["enableAcrossAccounts"] = enable_across_accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier")

        update_type = check_user_setting_request_dto_update_type(d.pop("updateType"))

        value = d.pop("value", UNSET)

        enable_across_accounts = d.pop("enableAcrossAccounts", UNSET)

        user_setting_request_dto = cls(
            identifier=identifier,
            update_type=update_type,
            value=value,
            enable_across_accounts=enable_across_accounts,
        )

        user_setting_request_dto.additional_properties = d
        return user_setting_request_dto

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
