from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_catalogue_item import ConnectorCatalogueItem


T = TypeVar("T", bound="ConnectorCatalogueResponse")


@_attrs_define
class ConnectorCatalogueResponse:
    """This has details of the retrieved Connector Catalogue.

    Attributes:
        catalogue (list[ConnectorCatalogueItem] | Unset): List of Connector category and Connector types corresponding
            to a specific category.
    """

    catalogue: list[ConnectorCatalogueItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalogue: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.catalogue, Unset):
            catalogue = []
            for catalogue_item_data in self.catalogue:
                catalogue_item = catalogue_item_data.to_dict()
                catalogue.append(catalogue_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalogue is not UNSET:
            field_dict["catalogue"] = catalogue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_catalogue_item import ConnectorCatalogueItem

        d = dict(src_dict)
        _catalogue = d.pop("catalogue", UNSET)
        catalogue: list[ConnectorCatalogueItem] | Unset = UNSET
        if _catalogue is not UNSET:
            catalogue = []
            for catalogue_item_data in _catalogue:
                catalogue_item = ConnectorCatalogueItem.from_dict(catalogue_item_data)

                catalogue.append(catalogue_item)

        connector_catalogue_response = cls(
            catalogue=catalogue,
        )

        connector_catalogue_response.additional_properties = d
        return connector_catalogue_response

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
