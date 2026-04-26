from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SupportedDelegateVersion")


@_attrs_define
class SupportedDelegateVersion:
    """
    Attributes:
        latest_supported_version (str | Unset):
        latest_supported_minimal_version (str | Unset):
    """

    latest_supported_version: str | Unset = UNSET
    latest_supported_minimal_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_supported_version = self.latest_supported_version

        latest_supported_minimal_version = self.latest_supported_minimal_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_supported_version is not UNSET:
            field_dict["latestSupportedVersion"] = latest_supported_version
        if latest_supported_minimal_version is not UNSET:
            field_dict["latestSupportedMinimalVersion"] = latest_supported_minimal_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latest_supported_version = d.pop("latestSupportedVersion", UNSET)

        latest_supported_minimal_version = d.pop("latestSupportedMinimalVersion", UNSET)

        supported_delegate_version = cls(
            latest_supported_version=latest_supported_version,
            latest_supported_minimal_version=latest_supported_minimal_version,
        )

        supported_delegate_version.additional_properties = d
        return supported_delegate_version

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
