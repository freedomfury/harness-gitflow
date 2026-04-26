from typing import Literal, cast

UserSettingDTOCategory = Literal[
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

USER_SETTING_DTO_CATEGORY_VALUES: set[UserSettingDTOCategory] = {
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


def check_user_setting_dto_category(value: str) -> UserSettingDTOCategory:
    if value in USER_SETTING_DTO_CATEGORY_VALUES:
        return cast(UserSettingDTOCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_SETTING_DTO_CATEGORY_VALUES!r}")
