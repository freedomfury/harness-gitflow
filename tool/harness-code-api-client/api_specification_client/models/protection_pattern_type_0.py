from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionPatternType0")


@_attrs_define
class ProtectionPatternType0:
    """
    Attributes:
        default (bool | Unset):
        exclude (list[str] | Unset):
        include (list[str] | Unset):
    """

    default: bool | Unset = UNSET
    exclude: list[str] | Unset = UNSET
    include: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        exclude: list[str] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = self.exclude

        include: list[str] | Unset = UNSET
        if not isinstance(self.include, Unset):
            include = self.include

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if exclude is not UNSET:
            field_dict["exclude"] = exclude
        if include is not UNSET:
            field_dict["include"] = include

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default = d.pop("default", UNSET)

        exclude = cast(list[str], d.pop("exclude", UNSET))

        include = cast(list[str], d.pop("include", UNSET))

        protection_pattern_type_0 = cls(
            default=default,
            exclude=exclude,
            include=include,
        )

        protection_pattern_type_0.additional_properties = d
        return protection_pattern_type_0

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
