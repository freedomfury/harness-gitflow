from typing import Literal, cast

NGAuthSettingsSettingsType = Literal["LDAP", "OAUTH", "OIDC", "SAML", "USER_PASSWORD"]

NG_AUTH_SETTINGS_SETTINGS_TYPE_VALUES: set[NGAuthSettingsSettingsType] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
    "USER_PASSWORD",
}


def check_ng_auth_settings_settings_type(value: str) -> NGAuthSettingsSettingsType:
    if value in NG_AUTH_SETTINGS_SETTINGS_TYPE_VALUES:
        return cast(NGAuthSettingsSettingsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NG_AUTH_SETTINGS_SETTINGS_TYPE_VALUES!r}")
