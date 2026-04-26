from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TGTPasswordSpecDTO")


@_attrs_define
class TGTPasswordSpecDTO:
    """
    Attributes:
        tgt_generation_method (str):
        password (str | Unset):
    """

    tgt_generation_method: str
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tgt_generation_method = self.tgt_generation_method

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tgtGenerationMethod": tgt_generation_method,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tgt_generation_method = d.pop("tgtGenerationMethod")

        password = d.pop("password", UNSET)

        tgt_password_spec_dto = cls(
            tgt_generation_method=tgt_generation_method,
            password=password,
        )

        tgt_password_spec_dto.additional_properties = d
        return tgt_password_spec_dto

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
