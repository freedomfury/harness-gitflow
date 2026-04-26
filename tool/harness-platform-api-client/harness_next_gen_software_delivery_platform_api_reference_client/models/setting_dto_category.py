from typing import Literal, cast

SettingDTOCategory = Literal[
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

SETTING_DTO_CATEGORY_VALUES: set[SettingDTOCategory] = {
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


def check_setting_dto_category(value: str) -> SettingDTOCategory:
    if value in SETTING_DTO_CATEGORY_VALUES:
        return cast(SettingDTOCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SETTING_DTO_CATEGORY_VALUES!r}")
