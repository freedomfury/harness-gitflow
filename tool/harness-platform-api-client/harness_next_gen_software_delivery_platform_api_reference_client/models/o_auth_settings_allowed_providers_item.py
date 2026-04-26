from typing import Literal, cast

OAuthSettingsAllowedProvidersItem = Literal[
    "AZURE", "BITBUCKET", "GITHUB", "GITLAB", "GOOGLE", "GOOGLE_CHAT", "LINKEDIN"
]

O_AUTH_SETTINGS_ALLOWED_PROVIDERS_ITEM_VALUES: set[OAuthSettingsAllowedProvidersItem] = {
    "AZURE",
    "BITBUCKET",
    "GITHUB",
    "GITLAB",
    "GOOGLE",
    "GOOGLE_CHAT",
    "LINKEDIN",
}


def check_o_auth_settings_allowed_providers_item(value: str) -> OAuthSettingsAllowedProvidersItem:
    if value in O_AUTH_SETTINGS_ALLOWED_PROVIDERS_ITEM_VALUES:
        return cast(OAuthSettingsAllowedProvidersItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {O_AUTH_SETTINGS_ALLOWED_PROVIDERS_ITEM_VALUES!r}")
