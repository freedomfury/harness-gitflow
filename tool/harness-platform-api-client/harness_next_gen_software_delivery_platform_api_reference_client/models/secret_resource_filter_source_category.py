from typing import Literal, cast

SecretResourceFilterSourceCategory = Literal[
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

SECRET_RESOURCE_FILTER_SOURCE_CATEGORY_VALUES: set[SecretResourceFilterSourceCategory] = {
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


def check_secret_resource_filter_source_category(value: str) -> SecretResourceFilterSourceCategory:
    if value in SECRET_RESOURCE_FILTER_SOURCE_CATEGORY_VALUES:
        return cast(SecretResourceFilterSourceCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_RESOURCE_FILTER_SOURCE_CATEGORY_VALUES!r}")
