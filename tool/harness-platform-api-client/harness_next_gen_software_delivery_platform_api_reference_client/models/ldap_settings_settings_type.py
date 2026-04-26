from typing import Literal, cast

LDAPSettingsSettingsType = Literal["LDAP", "OAUTH", "OIDC", "SAML", "USER_PASSWORD"]

LDAP_SETTINGS_SETTINGS_TYPE_VALUES: set[LDAPSettingsSettingsType] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
    "USER_PASSWORD",
}


def check_ldap_settings_settings_type(value: str) -> LDAPSettingsSettingsType:
    if value in LDAP_SETTINGS_SETTINGS_TYPE_VALUES:
        return cast(LDAPSettingsSettingsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LDAP_SETTINGS_SETTINGS_TYPE_VALUES!r}")
