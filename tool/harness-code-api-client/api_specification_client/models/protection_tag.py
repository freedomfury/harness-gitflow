from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_def_bypass import ProtectionDefBypass
    from ..models.protection_def_tag_lifecycle import ProtectionDefTagLifecycle


T = TypeVar("T", bound="ProtectionTag")


@_attrs_define
class ProtectionTag:
    """
    Attributes:
        bypass (ProtectionDefBypass | Unset):
        lifecycle (ProtectionDefTagLifecycle | Unset):
    """

    bypass: ProtectionDefBypass | Unset = UNSET
    lifecycle: ProtectionDefTagLifecycle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypass: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bypass, Unset):
            bypass = self.bypass.to_dict()

        lifecycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypass is not UNSET:
            field_dict["bypass"] = bypass
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_def_bypass import ProtectionDefBypass
        from ..models.protection_def_tag_lifecycle import ProtectionDefTagLifecycle

        d = dict(src_dict)
        _bypass = d.pop("bypass", UNSET)
        bypass: ProtectionDefBypass | Unset
        if isinstance(_bypass, Unset):
            bypass = UNSET
        else:
            bypass = ProtectionDefBypass.from_dict(_bypass)

        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: ProtectionDefTagLifecycle | Unset
        if isinstance(_lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = ProtectionDefTagLifecycle.from_dict(_lifecycle)

        protection_tag = cls(
            bypass=bypass,
            lifecycle=lifecycle,
        )

        protection_tag.additional_properties = d
        return protection_tag

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
