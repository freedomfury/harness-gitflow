from typing import Literal, cast

SSORequestOauthProviderType = Literal["AZURE", "BITBUCKET", "GITHUB", "GITLAB", "GOOGLE", "GOOGLE_CHAT", "LINKEDIN"]

SSO_REQUEST_OAUTH_PROVIDER_TYPE_VALUES: set[SSORequestOauthProviderType] = {
    "AZURE",
    "BITBUCKET",
    "GITHUB",
    "GITLAB",
    "GOOGLE",
    "GOOGLE_CHAT",
    "LINKEDIN",
}


def check_sso_request_oauth_provider_type(value: str) -> SSORequestOauthProviderType:
    if value in SSO_REQUEST_OAUTH_PROVIDER_TYPE_VALUES:
        return cast(SSORequestOauthProviderType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SSO_REQUEST_OAUTH_PROVIDER_TYPE_VALUES!r}")
