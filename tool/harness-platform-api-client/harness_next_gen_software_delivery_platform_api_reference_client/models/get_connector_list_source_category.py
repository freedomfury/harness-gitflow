from typing import Literal, cast

GetConnectorListSourceCategory = Literal[
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

GET_CONNECTOR_LIST_SOURCE_CATEGORY_VALUES: set[GetConnectorListSourceCategory] = {
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


def check_get_connector_list_source_category(value: str) -> GetConnectorListSourceCategory:
    if value in GET_CONNECTOR_LIST_SOURCE_CATEGORY_VALUES:
        return cast(GetConnectorListSourceCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONNECTOR_LIST_SOURCE_CATEGORY_VALUES!r}")
