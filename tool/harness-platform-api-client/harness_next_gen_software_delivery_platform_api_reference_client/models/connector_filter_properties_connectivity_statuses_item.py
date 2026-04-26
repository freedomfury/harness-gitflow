from typing import Literal, cast

ConnectorFilterPropertiesConnectivityStatusesItem = Literal["FAILURE", "PARTIAL", "PENDING", "SUCCESS", "UNKNOWN"]

CONNECTOR_FILTER_PROPERTIES_CONNECTIVITY_STATUSES_ITEM_VALUES: set[
    ConnectorFilterPropertiesConnectivityStatusesItem
] = {
    "FAILURE",
    "PARTIAL",
    "PENDING",
    "SUCCESS",
    "UNKNOWN",
}


def check_connector_filter_properties_connectivity_statuses_item(
    value: str,
) -> ConnectorFilterPropertiesConnectivityStatusesItem:
    if value in CONNECTOR_FILTER_PROPERTIES_CONNECTIVITY_STATUSES_ITEM_VALUES:
        return cast(ConnectorFilterPropertiesConnectivityStatusesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONNECTOR_FILTER_PROPERTIES_CONNECTIVITY_STATUSES_ITEM_VALUES!r}"
    )
