from typing import Literal, cast

SSORequestOauthProviderTypesItem = Literal[
    "AZURE", "BITBUCKET", "GITHUB", "GITLAB", "GOOGLE", "GOOGLE_CHAT", "LINKEDIN"
]

SSO_REQUEST_OAUTH_PROVIDER_TYPES_ITEM_VALUES: set[SSORequestOauthProviderTypesItem] = {
    "AZURE",
    "BITBUCKET",
    "GITHUB",
    "GITLAB",
    "GOOGLE",
    "GOOGLE_CHAT",
    "LINKEDIN",
}


def check_sso_request_oauth_provider_types_item(value: str) -> SSORequestOauthProviderTypesItem:
    if value in SSO_REQUEST_OAUTH_PROVIDER_TYPES_ITEM_VALUES:
        return cast(SSORequestOauthProviderTypesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SSO_REQUEST_OAUTH_PROVIDER_TYPES_ITEM_VALUES!r}")
