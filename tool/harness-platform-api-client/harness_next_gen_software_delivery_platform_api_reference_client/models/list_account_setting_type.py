from typing import Literal, cast

ListAccountSettingType = Literal["Connector"]

LIST_ACCOUNT_SETTING_TYPE_VALUES: set[ListAccountSettingType] = {
    "Connector",
}


def check_list_account_setting_type(value: str) -> ListAccountSettingType:
    if value in LIST_ACCOUNT_SETTING_TYPE_VALUES:
        return cast(ListAccountSettingType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ACCOUNT_SETTING_TYPE_VALUES!r}")
