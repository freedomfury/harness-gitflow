from typing import Literal, cast

LdapResponseStatus = Literal["FAILURE", "SUCCESS"]

LDAP_RESPONSE_STATUS_VALUES: set[LdapResponseStatus] = {
    "FAILURE",
    "SUCCESS",
}


def check_ldap_response_status(value: str) -> LdapResponseStatus:
    if value in LDAP_RESPONSE_STATUS_VALUES:
        return cast(LdapResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LDAP_RESPONSE_STATUS_VALUES!r}")
