from typing import Literal, cast

SSOConfigAuthenticationMechanism = Literal["LDAP", "OAUTH", "OIDC", "SAML", "USER_PASSWORD"]

SSO_CONFIG_AUTHENTICATION_MECHANISM_VALUES: set[SSOConfigAuthenticationMechanism] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
    "USER_PASSWORD",
}


def check_sso_config_authentication_mechanism(value: str) -> SSOConfigAuthenticationMechanism:
    if value in SSO_CONFIG_AUTHENTICATION_MECHANISM_VALUES:
        return cast(SSOConfigAuthenticationMechanism, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SSO_CONFIG_AUTHENTICATION_MECHANISM_VALUES!r}")
