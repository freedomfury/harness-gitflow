from typing import Literal, cast

GetAccountSettingType = Literal["Connector"]

GET_ACCOUNT_SETTING_TYPE_VALUES: set[GetAccountSettingType] = {
    "Connector",
}


def check_get_account_setting_type(value: str) -> GetAccountSettingType:
    if value in GET_ACCOUNT_SETTING_TYPE_VALUES:
        return cast(GetAccountSettingType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ACCOUNT_SETTING_TYPE_VALUES!r}")
