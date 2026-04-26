from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.freeze_filter_properties_dto_freeze_status import (
    FreezeFilterPropertiesDTOFreezeStatus,
    check_freeze_filter_properties_dto_freeze_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FreezeFilterPropertiesDTO")


@_attrs_define
class FreezeFilterPropertiesDTO:
    """
    Attributes:
        freeze_identifiers (list[str] | Unset):
        sort (list[str] | Unset):
        freeze_status (FreezeFilterPropertiesDTOFreezeStatus | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        search_term (str | Unset):
    """

    freeze_identifiers: list[str] | Unset = UNSET
    sort: list[str] | Unset = UNSET
    freeze_status: FreezeFilterPropertiesDTOFreezeStatus | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    search_term: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        freeze_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.freeze_identifiers, Unset):
            freeze_identifiers = self.freeze_identifiers

        sort: list[str] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort

        freeze_status: str | Unset = UNSET
        if not isinstance(self.freeze_status, Unset):
            freeze_status = self.freeze_status

        start_time = self.start_time

        end_time = self.end_time

        search_term = self.search_term

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if freeze_identifiers is not UNSET:
            field_dict["freezeIdentifiers"] = freeze_identifiers
        if sort is not UNSET:
            field_dict["sort"] = sort
        if freeze_status is not UNSET:
            field_dict["freezeStatus"] = freeze_status
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if search_term is not UNSET:
            field_dict["searchTerm"] = search_term

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        freeze_identifiers = cast(list[str], d.pop("freezeIdentifiers", UNSET))

        sort = cast(list[str], d.pop("sort", UNSET))

        _freeze_status = d.pop("freezeStatus", UNSET)
        freeze_status: FreezeFilterPropertiesDTOFreezeStatus | Unset
        if isinstance(_freeze_status, Unset):
            freeze_status = UNSET
        else:
            freeze_status = check_freeze_filter_properties_dto_freeze_status(_freeze_status)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        search_term = d.pop("searchTerm", UNSET)

        freeze_filter_properties_dto = cls(
            freeze_identifiers=freeze_identifiers,
            sort=sort,
            freeze_status=freeze_status,
            start_time=start_time,
            end_time=end_time,
            search_term=search_term,
        )

        freeze_filter_properties_dto.additional_properties = d
        return freeze_filter_properties_dto

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
