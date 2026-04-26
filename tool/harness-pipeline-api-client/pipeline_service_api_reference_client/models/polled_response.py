from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolledResponse")


@_attrs_define
class PolledResponse:
    """
    Attributes:
        all_polled_keys (list[str] | Unset):
    """

    all_polled_keys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_polled_keys: list[str] | Unset = UNSET
        if not isinstance(self.all_polled_keys, Unset):
            all_polled_keys = self.all_polled_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_polled_keys is not UNSET:
            field_dict["allPolledKeys"] = all_polled_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_polled_keys = cast(list[str], d.pop("allPolledKeys", UNSET))

        polled_response = cls(
            all_polled_keys=all_polled_keys,
        )

        polled_response.additional_properties = d
        return polled_response

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
