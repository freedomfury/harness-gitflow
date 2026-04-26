from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connector_filter_properties_categories_item import (
    ConnectorFilterPropertiesCategoriesItem,
    check_connector_filter_properties_categories_item,
)
from ..models.connector_filter_properties_connectivity_statuses_item import (
    ConnectorFilterPropertiesConnectivityStatusesItem,
    check_connector_filter_properties_connectivity_statuses_item,
)
from ..models.connector_filter_properties_connector_connectivity_modes_item import (
    ConnectorFilterPropertiesConnectorConnectivityModesItem,
    check_connector_filter_properties_connector_connectivity_modes_item,
)
from ..models.connector_filter_properties_filter_type import (
    ConnectorFilterPropertiesFilterType,
    check_connector_filter_properties_filter_type,
)
from ..models.connector_filter_properties_types_item import (
    ConnectorFilterPropertiesTypesItem,
    check_connector_filter_properties_types_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_filter_properties_tags import ConnectorFilterPropertiesTags


T = TypeVar("T", bound="ConnectorFilterProperties")


@_attrs_define
class ConnectorFilterProperties:
    """Properties of the Connector Filter defined in Harness

    Attributes:
        connector_names (list[str] | Unset): This is the list of the Connector names on which the filter will be
            applied.
        connector_identifiers (list[str] | Unset): This is the list of the Connector identifiers on which the filter
            will be applied.
        description (str | Unset): Description of filter created.
        types (list[ConnectorFilterPropertiesTypesItem] | Unset): This is the list of the Connector types on which the
            filter will be applied.
        categories (list[ConnectorFilterPropertiesCategoriesItem] | Unset): This is the list of the Connector category
            on which the filter will be applied.
        connectivity_statuses (list[ConnectorFilterPropertiesConnectivityStatusesItem] | Unset): This is the list of the
            Connector status on which the filter will be applied.
        inheriting_credentials_from_delegate (bool | Unset): Boolean value to indicate if the Connector is using
            credentials from the Delegate to connect.
        connector_connectivity_modes (list[ConnectorFilterPropertiesConnectorConnectivityModesItem] | Unset): Connector
            connectivity mode on which the filter is applied
        tags (ConnectorFilterPropertiesTags | Unset): Filter tags as a key-value pair.
        filter_type (ConnectorFilterPropertiesFilterType | Unset):
    """

    connector_names: list[str] | Unset = UNSET
    connector_identifiers: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    types: list[ConnectorFilterPropertiesTypesItem] | Unset = UNSET
    categories: list[ConnectorFilterPropertiesCategoriesItem] | Unset = UNSET
    connectivity_statuses: list[ConnectorFilterPropertiesConnectivityStatusesItem] | Unset = UNSET
    inheriting_credentials_from_delegate: bool | Unset = UNSET
    connector_connectivity_modes: list[ConnectorFilterPropertiesConnectorConnectivityModesItem] | Unset = UNSET
    tags: ConnectorFilterPropertiesTags | Unset = UNSET
    filter_type: ConnectorFilterPropertiesFilterType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_names: list[str] | Unset = UNSET
        if not isinstance(self.connector_names, Unset):
            connector_names = self.connector_names

        connector_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.connector_identifiers, Unset):
            connector_identifiers = self.connector_identifiers

        description = self.description

        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item: str = types_item_data
                types.append(types_item)

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item: str = categories_item_data
                categories.append(categories_item)

        connectivity_statuses: list[str] | Unset = UNSET
        if not isinstance(self.connectivity_statuses, Unset):
            connectivity_statuses = []
            for connectivity_statuses_item_data in self.connectivity_statuses:
                connectivity_statuses_item: str = connectivity_statuses_item_data
                connectivity_statuses.append(connectivity_statuses_item)

        inheriting_credentials_from_delegate = self.inheriting_credentials_from_delegate

        connector_connectivity_modes: list[str] | Unset = UNSET
        if not isinstance(self.connector_connectivity_modes, Unset):
            connector_connectivity_modes = []
            for connector_connectivity_modes_item_data in self.connector_connectivity_modes:
                connector_connectivity_modes_item: str = connector_connectivity_modes_item_data
                connector_connectivity_modes.append(connector_connectivity_modes_item)

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        filter_type: str | Unset = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connector_names is not UNSET:
            field_dict["connectorNames"] = connector_names
        if connector_identifiers is not UNSET:
            field_dict["connectorIdentifiers"] = connector_identifiers
        if description is not UNSET:
            field_dict["description"] = description
        if types is not UNSET:
            field_dict["types"] = types
        if categories is not UNSET:
            field_dict["categories"] = categories
        if connectivity_statuses is not UNSET:
            field_dict["connectivityStatuses"] = connectivity_statuses
        if inheriting_credentials_from_delegate is not UNSET:
            field_dict["inheritingCredentialsFromDelegate"] = inheriting_credentials_from_delegate
        if connector_connectivity_modes is not UNSET:
            field_dict["connectorConnectivityModes"] = connector_connectivity_modes
        if tags is not UNSET:
            field_dict["tags"] = tags
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_filter_properties_tags import ConnectorFilterPropertiesTags

        d = dict(src_dict)
        connector_names = cast(list[str], d.pop("connectorNames", UNSET))

        connector_identifiers = cast(list[str], d.pop("connectorIdentifiers", UNSET))

        description = d.pop("description", UNSET)

        _types = d.pop("types", UNSET)
        types: list[ConnectorFilterPropertiesTypesItem] | Unset = UNSET
        if _types is not UNSET:
            types = []
            for types_item_data in _types:
                types_item = check_connector_filter_properties_types_item(types_item_data)

                types.append(types_item)

        _categories = d.pop("categories", UNSET)
        categories: list[ConnectorFilterPropertiesCategoriesItem] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = check_connector_filter_properties_categories_item(categories_item_data)

                categories.append(categories_item)

        _connectivity_statuses = d.pop("connectivityStatuses", UNSET)
        connectivity_statuses: list[ConnectorFilterPropertiesConnectivityStatusesItem] | Unset = UNSET
        if _connectivity_statuses is not UNSET:
            connectivity_statuses = []
            for connectivity_statuses_item_data in _connectivity_statuses:
                connectivity_statuses_item = check_connector_filter_properties_connectivity_statuses_item(
                    connectivity_statuses_item_data
                )

                connectivity_statuses.append(connectivity_statuses_item)

        inheriting_credentials_from_delegate = d.pop("inheritingCredentialsFromDelegate", UNSET)

        _connector_connectivity_modes = d.pop("connectorConnectivityModes", UNSET)
        connector_connectivity_modes: list[ConnectorFilterPropertiesConnectorConnectivityModesItem] | Unset = UNSET
        if _connector_connectivity_modes is not UNSET:
            connector_connectivity_modes = []
            for connector_connectivity_modes_item_data in _connector_connectivity_modes:
                connector_connectivity_modes_item = check_connector_filter_properties_connector_connectivity_modes_item(
                    connector_connectivity_modes_item_data
                )

                connector_connectivity_modes.append(connector_connectivity_modes_item)

        _tags = d.pop("tags", UNSET)
        tags: ConnectorFilterPropertiesTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ConnectorFilterPropertiesTags.from_dict(_tags)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: ConnectorFilterPropertiesFilterType | Unset
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = check_connector_filter_properties_filter_type(_filter_type)

        connector_filter_properties = cls(
            connector_names=connector_names,
            connector_identifiers=connector_identifiers,
            description=description,
            types=types,
            categories=categories,
            connectivity_statuses=connectivity_statuses,
            inheriting_credentials_from_delegate=inheriting_credentials_from_delegate,
            connector_connectivity_modes=connector_connectivity_modes,
            tags=tags,
            filter_type=filter_type,
        )

        connector_filter_properties.additional_properties = d
        return connector_filter_properties

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
