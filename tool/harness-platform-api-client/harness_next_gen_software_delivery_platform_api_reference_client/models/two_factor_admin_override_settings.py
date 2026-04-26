from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TwoFactorAdminOverrideSettings")


@_attrs_define
class TwoFactorAdminOverrideSettings:
    """This contains the information about the Two Factor Admin Override in Harness.

    Attributes:
        admin_override_two_factor_enabled (bool | Unset): This value is true if Admin Override for Two Factor
            Authentication is enabled. Otherwise, it is false.
    """

    admin_override_two_factor_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_override_two_factor_enabled = self.admin_override_two_factor_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_override_two_factor_enabled is not UNSET:
            field_dict["adminOverrideTwoFactorEnabled"] = admin_override_two_factor_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_override_two_factor_enabled = d.pop("adminOverrideTwoFactorEnabled", UNSET)

        two_factor_admin_override_settings = cls(
            admin_override_two_factor_enabled=admin_override_two_factor_enabled,
        )

        two_factor_admin_override_settings.additional_properties = d
        return two_factor_admin_override_settings

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
