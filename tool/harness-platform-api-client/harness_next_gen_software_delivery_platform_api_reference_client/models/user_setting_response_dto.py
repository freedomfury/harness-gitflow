from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_setting_dto import UserSettingDTO


T = TypeVar("T", bound="UserSettingResponseDTO")


@_attrs_define
class UserSettingResponseDTO:
    """
    Attributes:
        user_setting (UserSettingDTO):
        last_modified_at (int | Unset): Time when the Setting was last modified.
    """

    user_setting: UserSettingDTO
    last_modified_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_setting = self.user_setting.to_dict()

        last_modified_at = self.last_modified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userSetting": user_setting,
            }
        )
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_setting_dto import UserSettingDTO

        d = dict(src_dict)
        user_setting = UserSettingDTO.from_dict(d.pop("userSetting"))

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        user_setting_response_dto = cls(
            user_setting=user_setting,
            last_modified_at=last_modified_at,
        )

        user_setting_response_dto.additional_properties = d
        return user_setting_response_dto

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
