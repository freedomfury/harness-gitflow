from typing import Literal, cast

AccountSettingsType = Literal["Connector"]

ACCOUNT_SETTINGS_TYPE_VALUES: set[AccountSettingsType] = {
    "Connector",
}


def check_account_settings_type(value: str) -> AccountSettingsType:
    if value in ACCOUNT_SETTINGS_TYPE_VALUES:
        return cast(AccountSettingsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_SETTINGS_TYPE_VALUES!r}")
