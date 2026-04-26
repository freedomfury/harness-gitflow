from typing import Literal, cast

UserSettingDTOValueType = Literal["Boolean", "Number", "String"]

USER_SETTING_DTO_VALUE_TYPE_VALUES: set[UserSettingDTOValueType] = {
    "Boolean",
    "Number",
    "String",
}


def check_user_setting_dto_value_type(value: str) -> UserSettingDTOValueType:
    if value in USER_SETTING_DTO_VALUE_TYPE_VALUES:
        return cast(UserSettingDTOValueType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_SETTING_DTO_VALUE_TYPE_VALUES!r}")
