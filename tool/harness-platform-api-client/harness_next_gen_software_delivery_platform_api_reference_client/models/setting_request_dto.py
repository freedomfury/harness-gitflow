from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.setting_request_dto_update_type import SettingRequestDTOUpdateType, check_setting_request_dto_update_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SettingRequestDTO")


@_attrs_define
class SettingRequestDTO:
    """
    Attributes:
        identifier (str): Identifier of the Setting.
        allow_overrides (bool): Allow override of the Setting in sub-scopes.
        update_type (SettingRequestDTOUpdateType): Type of the update operation. When update type is RESTORE, field
            [value] is ignored
        value (str | Unset): Value of the setting
    """

    identifier: str
    allow_overrides: bool
    update_type: SettingRequestDTOUpdateType
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        allow_overrides = self.allow_overrides

        update_type: str = self.update_type

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "allowOverrides": allow_overrides,
                "updateType": update_type,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier")

        allow_overrides = d.pop("allowOverrides")

        update_type = check_setting_request_dto_update_type(d.pop("updateType"))

        value = d.pop("value", UNSET)

        setting_request_dto = cls(
            identifier=identifier,
            allow_overrides=allow_overrides,
            update_type=update_type,
            value=value,
        )

        setting_request_dto.additional_properties = d
        return setting_request_dto

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
