from typing import Literal, cast

OAuthSettingsSettingsType = Literal["LDAP", "OAUTH", "OIDC", "SAML", "USER_PASSWORD"]

O_AUTH_SETTINGS_SETTINGS_TYPE_VALUES: set[OAuthSettingsSettingsType] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
    "USER_PASSWORD",
}


def check_o_auth_settings_settings_type(value: str) -> OAuthSettingsSettingsType:
    if value in O_AUTH_SETTINGS_SETTINGS_TYPE_VALUES:
        return cast(OAuthSettingsSettingsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {O_AUTH_SETTINGS_SETTINGS_TYPE_VALUES!r}")
