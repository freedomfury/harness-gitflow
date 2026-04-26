from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_setting_dto import UserSettingDTO


T = TypeVar("T", bound="UserSettingUpdateResponseDTO")


@_attrs_define
class UserSettingUpdateResponseDTO:
    """
    Attributes:
        identifier (str): Identifier of the Setting.
        user_setting_dto (UserSettingDTO):
        last_modified_at (int | Unset): Time when the Setting was last modified.
        update_status (bool | Unset): Request status for the corresponding item in batch request
        error_message (str | Unset): Error message
    """

    identifier: str
    user_setting_dto: UserSettingDTO
    last_modified_at: int | Unset = UNSET
    update_status: bool | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        user_setting_dto = self.user_setting_dto.to_dict()

        last_modified_at = self.last_modified_at

        update_status = self.update_status

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "userSettingDTO": user_setting_dto,
            }
        )
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if update_status is not UNSET:
            field_dict["updateStatus"] = update_status
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_setting_dto import UserSettingDTO

        d = dict(src_dict)
        identifier = d.pop("identifier")

        user_setting_dto = UserSettingDTO.from_dict(d.pop("userSettingDTO"))

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        update_status = d.pop("updateStatus", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        user_setting_update_response_dto = cls(
            identifier=identifier,
            user_setting_dto=user_setting_dto,
            last_modified_at=last_modified_at,
            update_status=update_status,
            error_message=error_message,
        )

        user_setting_update_response_dto.additional_properties = d
        return user_setting_update_response_dto

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
