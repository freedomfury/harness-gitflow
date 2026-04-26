from typing import Literal, cast

ConnectorCatalogueItemCategory = Literal[
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

CONNECTOR_CATALOGUE_ITEM_CATEGORY_VALUES: set[ConnectorCatalogueItemCategory] = {
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


def check_connector_catalogue_item_category(value: str) -> ConnectorCatalogueItemCategory:
    if value in CONNECTOR_CATALOGUE_ITEM_CATEGORY_VALUES:
        return cast(ConnectorCatalogueItemCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTOR_CATALOGUE_ITEM_CATEGORY_VALUES!r}")
