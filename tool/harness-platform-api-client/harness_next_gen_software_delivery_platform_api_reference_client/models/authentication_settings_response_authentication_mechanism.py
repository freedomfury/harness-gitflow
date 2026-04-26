from typing import Literal, cast

AuthenticationSettingsResponseAuthenticationMechanism = Literal["LDAP", "OAUTH", "OIDC", "SAML", "USER_PASSWORD"]

AUTHENTICATION_SETTINGS_RESPONSE_AUTHENTICATION_MECHANISM_VALUES: set[
    AuthenticationSettingsResponseAuthenticationMechanism
] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
    "USER_PASSWORD",
}


def check_authentication_settings_response_authentication_mechanism(
    value: str,
) -> AuthenticationSettingsResponseAuthenticationMechanism:
    if value in AUTHENTICATION_SETTINGS_RESPONSE_AUTHENTICATION_MECHANISM_VALUES:
        return cast(AuthenticationSettingsResponseAuthenticationMechanism, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTHENTICATION_SETTINGS_RESPONSE_AUTHENTICATION_MECHANISM_VALUES!r}"
    )
