from typing import Literal, cast

ConnectorFilterPropertiesFilterType = Literal["Connector"]

CONNECTOR_FILTER_PROPERTIES_FILTER_TYPE_VALUES: set[ConnectorFilterPropertiesFilterType] = {
    "Connector",
}


def check_connector_filter_properties_filter_type(value: str) -> ConnectorFilterPropertiesFilterType:
    if value in CONNECTOR_FILTER_PROPERTIES_FILTER_TYPE_VALUES:
        return cast(ConnectorFilterPropertiesFilterType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTOR_FILTER_PROPERTIES_FILTER_TYPE_VALUES!r}")
