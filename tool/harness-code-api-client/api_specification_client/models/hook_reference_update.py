from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HookReferenceUpdate")


@_attrs_define
class HookReferenceUpdate:
    """
    Attributes:
        new (str | Unset): Git object hash
        old (str | Unset): Git object hash
        ref (str | Unset):
    """

    new: str | Unset = UNSET
    old: str | Unset = UNSET
    ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new = self.new

        old = self.old

        ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new is not UNSET:
            field_dict["new"] = new
        if old is not UNSET:
            field_dict["old"] = old
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new = d.pop("new", UNSET)

        old = d.pop("old", UNSET)

        ref = d.pop("ref", UNSET)

        hook_reference_update = cls(
            new=new,
            old=old,
            ref=ref,
        )

        hook_reference_update.additional_properties = d
        return hook_reference_update

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
