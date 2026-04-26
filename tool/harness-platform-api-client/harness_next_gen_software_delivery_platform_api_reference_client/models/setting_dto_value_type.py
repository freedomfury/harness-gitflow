from typing import Literal, cast

SettingDTOValueType = Literal["Boolean", "Number", "String"]

SETTING_DTO_VALUE_TYPE_VALUES: set[SettingDTOValueType] = {
    "Boolean",
    "Number",
    "String",
}


def check_setting_dto_value_type(value: str) -> SettingDTOValueType:
    if value in SETTING_DTO_VALUE_TYPE_VALUES:
        return cast(SettingDTOValueType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SETTING_DTO_VALUE_TYPE_VALUES!r}")
