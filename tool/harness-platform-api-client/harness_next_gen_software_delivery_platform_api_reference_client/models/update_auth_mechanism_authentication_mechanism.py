from typing import Literal, cast

UpdateAuthMechanismAuthenticationMechanism = Literal["LDAP", "OAUTH", "OIDC", "SAML", "USER_PASSWORD"]

UPDATE_AUTH_MECHANISM_AUTHENTICATION_MECHANISM_VALUES: set[UpdateAuthMechanismAuthenticationMechanism] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
    "USER_PASSWORD",
}


def check_update_auth_mechanism_authentication_mechanism(value: str) -> UpdateAuthMechanismAuthenticationMechanism:
    if value in UPDATE_AUTH_MECHANISM_AUTHENTICATION_MECHANISM_VALUES:
        return cast(UpdateAuthMechanismAuthenticationMechanism, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_AUTH_MECHANISM_AUTHENTICATION_MECHANISM_VALUES!r}"
    )
