from typing import Literal, cast

SamlSettingsDTOType = Literal["LDAP", "OAUTH", "OIDC", "SAML"]

SAML_SETTINGS_DTO_TYPE_VALUES: set[SamlSettingsDTOType] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
}


def check_saml_settings_dto_type(value: str) -> SamlSettingsDTOType:
    if value in SAML_SETTINGS_DTO_TYPE_VALUES:
        return cast(SamlSettingsDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SAML_SETTINGS_DTO_TYPE_VALUES!r}")
