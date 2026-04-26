from typing import Literal, cast

SamlSettingsDTOSamlProviderType = Literal["AZURE", "OKTA", "ONELOGIN", "OTHER"]

SAML_SETTINGS_DTO_SAML_PROVIDER_TYPE_VALUES: set[SamlSettingsDTOSamlProviderType] = {
    "AZURE",
    "OKTA",
    "ONELOGIN",
    "OTHER",
}


def check_saml_settings_dto_saml_provider_type(value: str) -> SamlSettingsDTOSamlProviderType:
    if value in SAML_SETTINGS_DTO_SAML_PROVIDER_TYPE_VALUES:
        return cast(SamlSettingsDTOSamlProviderType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SAML_SETTINGS_DTO_SAML_PROVIDER_TYPE_VALUES!r}")
