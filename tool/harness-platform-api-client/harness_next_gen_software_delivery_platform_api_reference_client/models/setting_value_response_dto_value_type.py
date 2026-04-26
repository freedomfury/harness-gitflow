from typing import Literal, cast

SettingValueResponseDTOValueType = Literal["Boolean", "Number", "String"]

SETTING_VALUE_RESPONSE_DTO_VALUE_TYPE_VALUES: set[SettingValueResponseDTOValueType] = {
    "Boolean",
    "Number",
    "String",
}


def check_setting_value_response_dto_value_type(value: str) -> SettingValueResponseDTOValueType:
    if value in SETTING_VALUE_RESPONSE_DTO_VALUE_TYPE_VALUES:
        return cast(SettingValueResponseDTOValueType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SETTING_VALUE_RESPONSE_DTO_VALUE_TYPE_VALUES!r}")
