from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_def_bypass import ProtectionDefBypass
    from ..models.protection_def_push import ProtectionDefPush


T = TypeVar("T", bound="ProtectionPush")


@_attrs_define
class ProtectionPush:
    """
    Attributes:
        bypass (ProtectionDefBypass | Unset):
        push (ProtectionDefPush | Unset):
    """

    bypass: ProtectionDefBypass | Unset = UNSET
    push: ProtectionDefPush | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypass: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bypass, Unset):
            bypass = self.bypass.to_dict()

        push: dict[str, Any] | Unset = UNSET
        if not isinstance(self.push, Unset):
            push = self.push.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypass is not UNSET:
            field_dict["bypass"] = bypass
        if push is not UNSET:
            field_dict["push"] = push

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_def_bypass import ProtectionDefBypass
        from ..models.protection_def_push import ProtectionDefPush

        d = dict(src_dict)
        _bypass = d.pop("bypass", UNSET)
        bypass: ProtectionDefBypass | Unset
        if isinstance(_bypass, Unset):
            bypass = UNSET
        else:
            bypass = ProtectionDefBypass.from_dict(_bypass)

        _push = d.pop("push", UNSET)
        push: ProtectionDefPush | Unset
        if isinstance(_push, Unset):
            push = UNSET
        else:
            push = ProtectionDefPush.from_dict(_push)

        protection_push = cls(
            bypass=bypass,
            push=push,
        )

        protection_push.additional_properties = d
        return protection_push

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
