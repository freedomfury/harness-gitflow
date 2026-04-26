from typing import Literal, cast

SettingDTOSettingSource = Literal["ACCOUNT", "DEFAULT", "ORG", "PROJECT"]

SETTING_DTO_SETTING_SOURCE_VALUES: set[SettingDTOSettingSource] = {
    "ACCOUNT",
    "DEFAULT",
    "ORG",
    "PROJECT",
}


def check_setting_dto_setting_source(value: str) -> SettingDTOSettingSource:
    if value in SETTING_DTO_SETTING_SOURCE_VALUES:
        return cast(SettingDTOSettingSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SETTING_DTO_SETTING_SOURCE_VALUES!r}")
