from typing import Literal, cast

LoginTypeResponseAuthenticationMechanism = Literal["LDAP", "OAUTH", "OIDC", "SAML", "USER_PASSWORD"]

LOGIN_TYPE_RESPONSE_AUTHENTICATION_MECHANISM_VALUES: set[LoginTypeResponseAuthenticationMechanism] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
    "USER_PASSWORD",
}


def check_login_type_response_authentication_mechanism(value: str) -> LoginTypeResponseAuthenticationMechanism:
    if value in LOGIN_TYPE_RESPONSE_AUTHENTICATION_MECHANISM_VALUES:
        return cast(LoginTypeResponseAuthenticationMechanism, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOGIN_TYPE_RESPONSE_AUTHENTICATION_MECHANISM_VALUES!r}"
    )
