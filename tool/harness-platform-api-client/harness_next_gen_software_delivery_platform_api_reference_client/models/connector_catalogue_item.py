from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connector_catalogue_item_category import (
    ConnectorCatalogueItemCategory,
    check_connector_catalogue_item_category,
)
from ..models.connector_catalogue_item_connectors_item import (
    ConnectorCatalogueItemConnectorsItem,
    check_connector_catalogue_item_connectors_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectorCatalogueItem")


@_attrs_define
class ConnectorCatalogueItem:
    """This has details of the Connector Catalogue in Harness.

    Attributes:
        category (ConnectorCatalogueItemCategory | Unset): Category of this Connector.
        connectors (list[ConnectorCatalogueItemConnectorsItem] | Unset): List of Connector types corresponding to a
            specific category.
    """

    category: ConnectorCatalogueItemCategory | Unset = UNSET
    connectors: list[ConnectorCatalogueItemConnectorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        connectors: list[str] | Unset = UNSET
        if not isinstance(self.connectors, Unset):
            connectors = []
            for connectors_item_data in self.connectors:
                connectors_item: str = connectors_item_data
                connectors.append(connectors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if connectors is not UNSET:
            field_dict["connectors"] = connectors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: ConnectorCatalogueItemCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_connector_catalogue_item_category(_category)

        _connectors = d.pop("connectors", UNSET)
        connectors: list[ConnectorCatalogueItemConnectorsItem] | Unset = UNSET
        if _connectors is not UNSET:
            connectors = []
            for connectors_item_data in _connectors:
                connectors_item = check_connector_catalogue_item_connectors_item(connectors_item_data)

                connectors.append(connectors_item)

        connector_catalogue_item = cls(
            category=category,
            connectors=connectors,
        )

        connector_catalogue_item.additional_properties = d
        return connector_catalogue_item

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
