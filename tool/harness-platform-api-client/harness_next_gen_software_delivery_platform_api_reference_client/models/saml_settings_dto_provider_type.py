from typing import Literal, cast

SamlSettingsDTOProviderType = Literal["AZURE", "OKTA", "ONELOGIN", "OTHER"]

SAML_SETTINGS_DTO_PROVIDER_TYPE_VALUES: set[SamlSettingsDTOProviderType] = {
    "AZURE",
    "OKTA",
    "ONELOGIN",
    "OTHER",
}


def check_saml_settings_dto_provider_type(value: str) -> SamlSettingsDTOProviderType:
    if value in SAML_SETTINGS_DTO_PROVIDER_TYPE_VALUES:
        return cast(SamlSettingsDTOProviderType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SAML_SETTINGS_DTO_PROVIDER_TYPE_VALUES!r}")
