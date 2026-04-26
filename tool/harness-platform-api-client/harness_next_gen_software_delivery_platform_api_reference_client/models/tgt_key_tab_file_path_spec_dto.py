from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TGTKeyTabFilePathSpecDTO")


@_attrs_define
class TGTKeyTabFilePathSpecDTO:
    """
    Attributes:
        tgt_generation_method (str):
        key_path (str | Unset):
    """

    tgt_generation_method: str
    key_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tgt_generation_method = self.tgt_generation_method

        key_path = self.key_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tgtGenerationMethod": tgt_generation_method,
            }
        )
        if key_path is not UNSET:
            field_dict["keyPath"] = key_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tgt_generation_method = d.pop("tgtGenerationMethod")

        key_path = d.pop("keyPath", UNSET)

        tgt_key_tab_file_path_spec_dto = cls(
            tgt_generation_method=tgt_generation_method,
            key_path=key_path,
        )

        tgt_key_tab_file_path_spec_dto.additional_properties = d
        return tgt_key_tab_file_path_spec_dto

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
