from typing import Literal, cast

SSOSettingsDTOType = Literal["LDAP", "OAUTH", "OIDC", "SAML"]

SSO_SETTINGS_DTO_TYPE_VALUES: set[SSOSettingsDTOType] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
}


def check_sso_settings_dto_type(value: str) -> SSOSettingsDTOType:
    if value in SSO_SETTINGS_DTO_TYPE_VALUES:
        return cast(SSOSettingsDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SSO_SETTINGS_DTO_TYPE_VALUES!r}")
