from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_properties_filter_type import FilterPropertiesFilterType, check_filter_properties_filter_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_properties_tags import FilterPropertiesTags


T = TypeVar("T", bound="FilterProperties")


@_attrs_define
class FilterProperties:
    """Properties of the Filter entity defined in Harness.

    Attributes:
        filter_type (FilterPropertiesFilterType): This specifies the corresponding Entity of the filter.
        tags (FilterPropertiesTags | Unset): Filter tags as a key-value pair.
    """

    filter_type: FilterPropertiesFilterType
    tags: FilterPropertiesTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type: str = self.filter_type

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filterType": filter_type,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_properties_tags import FilterPropertiesTags

        d = dict(src_dict)
        filter_type = check_filter_properties_filter_type(d.pop("filterType"))

        _tags = d.pop("tags", UNSET)
        tags: FilterPropertiesTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = FilterPropertiesTags.from_dict(_tags)

        filter_properties = cls(
            filter_type=filter_type,
            tags=tags,
        )

        filter_properties.additional_properties = d
        return filter_properties

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
