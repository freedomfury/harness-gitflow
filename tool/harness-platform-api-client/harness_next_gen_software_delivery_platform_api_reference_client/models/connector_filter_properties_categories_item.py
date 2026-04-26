from typing import Literal, cast

ConnectorFilterPropertiesCategoriesItem = Literal[
    "AI",
    "ARTIFACTORY",
    "CLOUD_COST",
    "CLOUD_PROVIDER",
    "CODE_REPO",
    "COMMUNICATION",
    "DATABASE",
    "DOCUMENTATION",
    "MCP",
    "ML_OPS",
    "MONITORING",
    "SECRET_MANAGER",
    "TICKETING",
]

CONNECTOR_FILTER_PROPERTIES_CATEGORIES_ITEM_VALUES: set[ConnectorFilterPropertiesCategoriesItem] = {
    "AI",
    "ARTIFACTORY",
    "CLOUD_COST",
    "CLOUD_PROVIDER",
    "CODE_REPO",
    "COMMUNICATION",
    "DATABASE",
    "DOCUMENTATION",
    "MCP",
    "ML_OPS",
    "MONITORING",
    "SECRET_MANAGER",
    "TICKETING",
}


def check_connector_filter_properties_categories_item(value: str) -> ConnectorFilterPropertiesCategoriesItem:
    if value in CONNECTOR_FILTER_PROPERTIES_CATEGORIES_ITEM_VALUES:
        return cast(ConnectorFilterPropertiesCategoriesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONNECTOR_FILTER_PROPERTIES_CATEGORIES_ITEM_VALUES!r}"
    )
