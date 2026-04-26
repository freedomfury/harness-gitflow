from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_catalog_item_category import TriggerCatalogItemCategory, check_trigger_catalog_item_category
from ..models.trigger_catalog_item_trigger_catalog_type_item import (
    TriggerCatalogItemTriggerCatalogTypeItem,
    check_trigger_catalog_item_trigger_catalog_type_item,
)

T = TypeVar("T", bound="TriggerCatalogItem")


@_attrs_define
class TriggerCatalogItem:
    """This has details of the Trigger Catalog.

    Attributes:
        category (TriggerCatalogItemCategory): Category of this Trigger.
        trigger_catalog_type (list[TriggerCatalogItemTriggerCatalogTypeItem]): List of Trigger types corresponding to a
            specific category.
    """

    category: TriggerCatalogItemCategory
    trigger_catalog_type: list[TriggerCatalogItemTriggerCatalogTypeItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str = self.category

        trigger_catalog_type = []
        for trigger_catalog_type_item_data in self.trigger_catalog_type:
            trigger_catalog_type_item: str = trigger_catalog_type_item_data
            trigger_catalog_type.append(trigger_catalog_type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "triggerCatalogType": trigger_catalog_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = check_trigger_catalog_item_category(d.pop("category"))

        trigger_catalog_type = []
        _trigger_catalog_type = d.pop("triggerCatalogType")
        for trigger_catalog_type_item_data in _trigger_catalog_type:
            trigger_catalog_type_item = check_trigger_catalog_item_trigger_catalog_type_item(
                trigger_catalog_type_item_data
            )

            trigger_catalog_type.append(trigger_catalog_type_item)

        trigger_catalog_item = cls(
            category=category,
            trigger_catalog_type=trigger_catalog_type,
        )

        trigger_catalog_item.additional_properties = d
        return trigger_catalog_item

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
