from typing import Literal, cast

RancherAuthenticationType = Literal["BearerToken"]

RANCHER_AUTHENTICATION_TYPE_VALUES: set[RancherAuthenticationType] = {
    "BearerToken",
}


def check_rancher_authentication_type(value: str) -> RancherAuthenticationType:
    if value in RANCHER_AUTHENTICATION_TYPE_VALUES:
        return cast(RancherAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RANCHER_AUTHENTICATION_TYPE_VALUES!r}")
