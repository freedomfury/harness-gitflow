from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_setting_dto_category import UserSettingDTOCategory, check_user_setting_dto_category
from ..models.user_setting_dto_value_type import UserSettingDTOValueType, check_user_setting_dto_value_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSettingDTO")


@_attrs_define
class UserSettingDTO:
    """
    Attributes:
        identifier (str): Identifier of the Setting.
        category (UserSettingDTOCategory): Category of the Setting.
        value_type (UserSettingDTOValueType): Type of Value of the Setting.
        group_identifier (str): Group Id of the setting
        allowed_values (list[str] | Unset): Set of Values allowed for the Setting.
        value (str | Unset): Value of the setting
        user_id (str | Unset): userID
    """

    identifier: str
    category: UserSettingDTOCategory
    value_type: UserSettingDTOValueType
    group_identifier: str
    allowed_values: list[str] | Unset = UNSET
    value: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        category: str = self.category

        value_type: str = self.value_type

        group_identifier = self.group_identifier

        allowed_values: list[str] | Unset = UNSET
        if not isinstance(self.allowed_values, Unset):
            allowed_values = self.allowed_values

        value = self.value

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "category": category,
                "valueType": value_type,
                "groupIdentifier": group_identifier,
            }
        )
        if allowed_values is not UNSET:
            field_dict["allowedValues"] = allowed_values
        if value is not UNSET:
            field_dict["value"] = value
        if user_id is not UNSET:
            field_dict["userID"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier")

        category = check_user_setting_dto_category(d.pop("category"))

        value_type = check_user_setting_dto_value_type(d.pop("valueType"))

        group_identifier = d.pop("groupIdentifier")

        allowed_values = cast(list[str], d.pop("allowedValues", UNSET))

        value = d.pop("value", UNSET)

        user_id = d.pop("userID", UNSET)

        user_setting_dto = cls(
            identifier=identifier,
            category=category,
            value_type=value_type,
            group_identifier=group_identifier,
            allowed_values=allowed_values,
            value=value,
            user_id=user_id,
        )

        user_setting_dto.additional_properties = d
        return user_setting_dto

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
