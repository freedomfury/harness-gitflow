from typing import Literal, cast

SSORequestSamlProviderType = Literal["AZURE", "OKTA", "ONELOGIN", "OTHER"]

SSO_REQUEST_SAML_PROVIDER_TYPE_VALUES: set[SSORequestSamlProviderType] = {
    "AZURE",
    "OKTA",
    "ONELOGIN",
    "OTHER",
}


def check_sso_request_saml_provider_type(value: str) -> SSORequestSamlProviderType:
    if value in SSO_REQUEST_SAML_PROVIDER_TYPE_VALUES:
        return cast(SSORequestSamlProviderType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SSO_REQUEST_SAML_PROVIDER_TYPE_VALUES!r}")
