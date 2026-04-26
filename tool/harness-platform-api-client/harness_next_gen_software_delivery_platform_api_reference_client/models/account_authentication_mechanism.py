from typing import Literal, cast

AccountAuthenticationMechanism = Literal["LDAP", "OAUTH", "OIDC", "SAML", "USER_PASSWORD"]

ACCOUNT_AUTHENTICATION_MECHANISM_VALUES: set[AccountAuthenticationMechanism] = {
    "LDAP",
    "OAUTH",
    "OIDC",
    "SAML",
    "USER_PASSWORD",
}


def check_account_authentication_mechanism(value: str) -> AccountAuthenticationMechanism:
    if value in ACCOUNT_AUTHENTICATION_MECHANISM_VALUES:
        return cast(AccountAuthenticationMechanism, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_AUTHENTICATION_MECHANISM_VALUES!r}")
