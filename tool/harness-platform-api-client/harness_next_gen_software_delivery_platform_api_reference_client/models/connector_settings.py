from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectorSettings")


@_attrs_define
class ConnectorSettings:
    """
    Attributes:
        built_in_sm_disabled (bool | Unset):
    """

    built_in_sm_disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        built_in_sm_disabled = self.built_in_sm_disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if built_in_sm_disabled is not UNSET:
            field_dict["builtInSMDisabled"] = built_in_sm_disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        built_in_sm_disabled = d.pop("builtInSMDisabled", UNSET)

        connector_settings = cls(
            built_in_sm_disabled=built_in_sm_disabled,
        )

        connector_settings.additional_properties = d
        return connector_settings

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
