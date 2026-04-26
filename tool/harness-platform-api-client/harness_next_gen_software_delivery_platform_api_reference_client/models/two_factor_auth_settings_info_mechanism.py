from typing import Literal, cast

TwoFactorAuthSettingsInfoMechanism = Literal["TOTP"]

TWO_FACTOR_AUTH_SETTINGS_INFO_MECHANISM_VALUES: set[TwoFactorAuthSettingsInfoMechanism] = {
    "TOTP",
}


def check_two_factor_auth_settings_info_mechanism(value: str) -> TwoFactorAuthSettingsInfoMechanism:
    if value in TWO_FACTOR_AUTH_SETTINGS_INFO_MECHANISM_VALUES:
        return cast(TwoFactorAuthSettingsInfoMechanism, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TWO_FACTOR_AUTH_SETTINGS_INFO_MECHANISM_VALUES!r}")
