from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ng_auth_settings_settings_type import NGAuthSettingsSettingsType, check_ng_auth_settings_settings_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="NGAuthSettings")


@_attrs_define
class NGAuthSettings:
    """This has the details of Authentication Settings supported in NG.

    Attributes:
        settings_type (NGAuthSettingsSettingsType | Unset):
    """

    settings_type: NGAuthSettingsSettingsType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings_type: str | Unset = UNSET
        if not isinstance(self.settings_type, Unset):
            settings_type = self.settings_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings_type is not UNSET:
            field_dict["settingsType"] = settings_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _settings_type = d.pop("settingsType", UNSET)
        settings_type: NGAuthSettingsSettingsType | Unset
        if isinstance(_settings_type, Unset):
            settings_type = UNSET
        else:
            settings_type = check_ng_auth_settings_settings_type(_settings_type)

        ng_auth_settings = cls(
            settings_type=settings_type,
        )

        ng_auth_settings.additional_properties = d
        return ng_auth_settings

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
