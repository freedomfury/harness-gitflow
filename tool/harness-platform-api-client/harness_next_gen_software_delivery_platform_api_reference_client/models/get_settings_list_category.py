from typing import Literal, cast

GetSettingsListCategory = Literal[
    "AR",
    "CD",
    "CE",
    "CF",
    "CHAOS",
    "CI",
    "CONNECTORS",
    "CORE",
    "CV",
    "DBOPS",
    "EULA",
    "GIT_EXPERIENCE",
    "GOVERNANCE",
    "IR",
    "MODULES_VISIBILITY",
    "NOTIFICATIONS",
    "PMS",
    "SCIM",
    "STO",
    "SUPPLY_CHAIN_ASSURANCE",
    "TEMPLATESERVICE",
    "USER",
]

GET_SETTINGS_LIST_CATEGORY_VALUES: set[GetSettingsListCategory] = {
    "AR",
    "CD",
    "CE",
    "CF",
    "CHAOS",
    "CI",
    "CONNECTORS",
    "CORE",
    "CV",
    "DBOPS",
    "EULA",
    "GIT_EXPERIENCE",
    "GOVERNANCE",
    "IR",
    "MODULES_VISIBILITY",
    "NOTIFICATIONS",
    "PMS",
    "SCIM",
    "STO",
    "SUPPLY_CHAIN_ASSURANCE",
    "TEMPLATESERVICE",
    "USER",
}


def check_get_settings_list_category(value: str) -> GetSettingsListCategory:
    if value in GET_SETTINGS_LIST_CATEGORY_VALUES:
        return cast(GetSettingsListCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_SETTINGS_LIST_CATEGORY_VALUES!r}")
