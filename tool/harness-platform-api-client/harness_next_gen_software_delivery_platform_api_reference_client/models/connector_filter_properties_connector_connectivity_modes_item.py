from typing import Literal, cast

ConnectorFilterPropertiesConnectorConnectivityModesItem = Literal["DELEGATE", "MANAGER"]

CONNECTOR_FILTER_PROPERTIES_CONNECTOR_CONNECTIVITY_MODES_ITEM_VALUES: set[
    ConnectorFilterPropertiesConnectorConnectivityModesItem
] = {
    "DELEGATE",
    "MANAGER",
}


def check_connector_filter_properties_connector_connectivity_modes_item(
    value: str,
) -> ConnectorFilterPropertiesConnectorConnectivityModesItem:
    if value in CONNECTOR_FILTER_PROPERTIES_CONNECTOR_CONNECTIVITY_MODES_ITEM_VALUES:
        return cast(ConnectorFilterPropertiesConnectorConnectivityModesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONNECTOR_FILTER_PROPERTIES_CONNECTOR_CONNECTIVITY_MODES_ITEM_VALUES!r}"
    )
