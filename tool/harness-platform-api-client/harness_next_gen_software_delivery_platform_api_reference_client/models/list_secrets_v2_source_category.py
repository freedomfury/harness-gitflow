from typing import Literal, cast

ListSecretsV2SourceCategory = Literal[
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

LIST_SECRETS_V2_SOURCE_CATEGORY_VALUES: set[ListSecretsV2SourceCategory] = {
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


def check_list_secrets_v2_source_category(value: str) -> ListSecretsV2SourceCategory:
    if value in LIST_SECRETS_V2_SOURCE_CATEGORY_VALUES:
        return cast(ListSecretsV2SourceCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SECRETS_V2_SOURCE_CATEGORY_VALUES!r}")
