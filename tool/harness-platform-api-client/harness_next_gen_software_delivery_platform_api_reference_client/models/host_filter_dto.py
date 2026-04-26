from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.host_filter_dto_type import HostFilterDTOType, check_host_filter_dto_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostFilterDTO")


@_attrs_define
class HostFilterDTO:
    """
    Attributes:
        type_ (HostFilterDTOType | Unset):
        filter_ (str | Unset):
        match_criteria (str | Unset):
    """

    type_: HostFilterDTOType | Unset = UNSET
    filter_: str | Unset = UNSET
    match_criteria: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        filter_ = self.filter_

        match_criteria = self.match_criteria

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if match_criteria is not UNSET:
            field_dict["matchCriteria"] = match_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: HostFilterDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_host_filter_dto_type(_type_)

        filter_ = d.pop("filter", UNSET)

        match_criteria = d.pop("matchCriteria", UNSET)

        host_filter_dto = cls(
            type_=type_,
            filter_=filter_,
            match_criteria=match_criteria,
        )

        host_filter_dto.additional_properties = d
        return host_filter_dto

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
