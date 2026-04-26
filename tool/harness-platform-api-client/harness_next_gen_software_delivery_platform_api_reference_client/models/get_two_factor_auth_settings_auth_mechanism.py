from typing import Literal, cast

GetTwoFactorAuthSettingsAuthMechanism = Literal["TOTP"]

GET_TWO_FACTOR_AUTH_SETTINGS_AUTH_MECHANISM_VALUES: set[GetTwoFactorAuthSettingsAuthMechanism] = {
    "TOTP",
}


def check_get_two_factor_auth_settings_auth_mechanism(value: str) -> GetTwoFactorAuthSettingsAuthMechanism:
    if value in GET_TWO_FACTOR_AUTH_SETTINGS_AUTH_MECHANISM_VALUES:
        return cast(GetTwoFactorAuthSettingsAuthMechanism, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TWO_FACTOR_AUTH_SETTINGS_AUTH_MECHANISM_VALUES!r}"
    )
