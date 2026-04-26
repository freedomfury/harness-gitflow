from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trigger_catalog_item import TriggerCatalogItem


T = TypeVar("T", bound="TriggerCatalogResponse")


@_attrs_define
class TriggerCatalogResponse:
    """This has details of the retrieved Trigger Catalog.

    Attributes:
        catalog (list[TriggerCatalogItem]): List of Trigger category and Trigger types corresponding to a specific
            category.
    """

    catalog: list[TriggerCatalogItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog = []
        for catalog_item_data in self.catalog:
            catalog_item = catalog_item_data.to_dict()
            catalog.append(catalog_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog": catalog,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_catalog_item import TriggerCatalogItem

        d = dict(src_dict)
        catalog = []
        _catalog = d.pop("catalog")
        for catalog_item_data in _catalog:
            catalog_item = TriggerCatalogItem.from_dict(catalog_item_data)

            catalog.append(catalog_item)

        trigger_catalog_response = cls(
            catalog=catalog,
        )

        trigger_catalog_response.additional_properties = d
        return trigger_catalog_response

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
