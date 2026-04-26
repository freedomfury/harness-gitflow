from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference_dto import ReferenceDTO


T = TypeVar("T", bound="UsageDataDTO")


@_attrs_define
class UsageDataDTO:
    """
    Attributes:
        count (int | Unset):
        display_name (str | Unset):
        references (list[ReferenceDTO] | Unset):
    """

    count: int | Unset = UNSET
    display_name: str | Unset = UNSET
    references: list[ReferenceDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        display_name = self.display_name

        references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reference_dto import ReferenceDTO

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        display_name = d.pop("displayName", UNSET)

        _references = d.pop("references", UNSET)
        references: list[ReferenceDTO] | Unset = UNSET
        if _references is not UNSET:
            references = []
            for references_item_data in _references:
                references_item = ReferenceDTO.from_dict(references_item_data)

                references.append(references_item)

        usage_data_dto = cls(
            count=count,
            display_name=display_name,
            references=references,
        )

        usage_data_dto.additional_properties = d
        return usage_data_dto

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
