from typing import Literal, cast

GetConnectorListCategory = Literal[
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

GET_CONNECTOR_LIST_CATEGORY_VALUES: set[GetConnectorListCategory] = {
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


def check_get_connector_list_category(value: str) -> GetConnectorListCategory:
    if value in GET_CONNECTOR_LIST_CATEGORY_VALUES:
        return cast(GetConnectorListCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONNECTOR_LIST_CATEGORY_VALUES!r}")
