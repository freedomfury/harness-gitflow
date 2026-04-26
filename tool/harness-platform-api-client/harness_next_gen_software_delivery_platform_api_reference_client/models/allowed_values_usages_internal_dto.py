from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_list_with_allowed_values_response import EntityListWithAllowedValuesResponse


T = TypeVar("T", bound="AllowedValuesUsagesInternalDTO")


@_attrs_define
class AllowedValuesUsagesInternalDTO:
    """This is the list of all entries in one kind of entity which are using the allowedValues

    Attributes:
        used_in (list[EntityListWithAllowedValuesResponse] | Unset):
        all_entries_checked (bool | Unset):
    """

    used_in: list[EntityListWithAllowedValuesResponse] | Unset = UNSET
    all_entries_checked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used_in: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.used_in, Unset):
            used_in = []
            for used_in_item_data in self.used_in:
                used_in_item = used_in_item_data.to_dict()
                used_in.append(used_in_item)

        all_entries_checked = self.all_entries_checked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_in is not UNSET:
            field_dict["usedIn"] = used_in
        if all_entries_checked is not UNSET:
            field_dict["allEntriesChecked"] = all_entries_checked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_list_with_allowed_values_response import EntityListWithAllowedValuesResponse

        d = dict(src_dict)
        _used_in = d.pop("usedIn", UNSET)
        used_in: list[EntityListWithAllowedValuesResponse] | Unset = UNSET
        if _used_in is not UNSET:
            used_in = []
            for used_in_item_data in _used_in:
                used_in_item = EntityListWithAllowedValuesResponse.from_dict(used_in_item_data)

                used_in.append(used_in_item)

        all_entries_checked = d.pop("allEntriesChecked", UNSET)

        allowed_values_usages_internal_dto = cls(
            used_in=used_in,
            all_entries_checked=all_entries_checked,
        )

        allowed_values_usages_internal_dto.additional_properties = d
        return allowed_values_usages_internal_dto

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
