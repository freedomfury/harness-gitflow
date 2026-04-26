from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_filter_properties_filter_type import (
    TriggerFilterPropertiesFilterType,
    check_trigger_filter_properties_filter_type,
)
from ..models.trigger_filter_properties_trigger_types_item import (
    TriggerFilterPropertiesTriggerTypesItem,
    check_trigger_filter_properties_trigger_types_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_filter_properties_tags import TriggerFilterPropertiesTags


T = TypeVar("T", bound="TriggerFilterProperties")


@_attrs_define
class TriggerFilterProperties:
    """This contains details of the Trigger Filter

    Attributes:
        filter_type (TriggerFilterPropertiesFilterType): This specifies the corresponding Entity of the filter.
        trigger_names (list[str] | Unset): This is the list of the Trigger names on which the filter will be applied.
        trigger_identifiers (list[str] | Unset): This is the list of the Trigger identifiers on which the filter will be
            applied.
        trigger_types (list[TriggerFilterPropertiesTriggerTypesItem] | Unset): This is the list of the Trigger types on
            which the filter will be applied.
        tags (TriggerFilterPropertiesTags | Unset): Filter tags as a key-value pair.
    """

    filter_type: TriggerFilterPropertiesFilterType
    trigger_names: list[str] | Unset = UNSET
    trigger_identifiers: list[str] | Unset = UNSET
    trigger_types: list[TriggerFilterPropertiesTriggerTypesItem] | Unset = UNSET
    tags: TriggerFilterPropertiesTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type: str = self.filter_type

        trigger_names: list[str] | Unset = UNSET
        if not isinstance(self.trigger_names, Unset):
            trigger_names = self.trigger_names

        trigger_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.trigger_identifiers, Unset):
            trigger_identifiers = self.trigger_identifiers

        trigger_types: list[str] | Unset = UNSET
        if not isinstance(self.trigger_types, Unset):
            trigger_types = []
            for trigger_types_item_data in self.trigger_types:
                trigger_types_item: str = trigger_types_item_data
                trigger_types.append(trigger_types_item)

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
        if trigger_names is not UNSET:
            field_dict["triggerNames"] = trigger_names
        if trigger_identifiers is not UNSET:
            field_dict["triggerIdentifiers"] = trigger_identifiers
        if trigger_types is not UNSET:
            field_dict["triggerTypes"] = trigger_types
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_filter_properties_tags import TriggerFilterPropertiesTags

        d = dict(src_dict)
        filter_type = check_trigger_filter_properties_filter_type(d.pop("filterType"))

        trigger_names = cast(list[str], d.pop("triggerNames", UNSET))

        trigger_identifiers = cast(list[str], d.pop("triggerIdentifiers", UNSET))

        _trigger_types = d.pop("triggerTypes", UNSET)
        trigger_types: list[TriggerFilterPropertiesTriggerTypesItem] | Unset = UNSET
        if _trigger_types is not UNSET:
            trigger_types = []
            for trigger_types_item_data in _trigger_types:
                trigger_types_item = check_trigger_filter_properties_trigger_types_item(trigger_types_item_data)

                trigger_types.append(trigger_types_item)

        _tags = d.pop("tags", UNSET)
        tags: TriggerFilterPropertiesTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = TriggerFilterPropertiesTags.from_dict(_tags)

        trigger_filter_properties = cls(
            filter_type=filter_type,
            trigger_names=trigger_names,
            trigger_identifiers=trigger_identifiers,
            trigger_types=trigger_types,
            tags=tags,
        )

        trigger_filter_properties.additional_properties = d
        return trigger_filter_properties

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
