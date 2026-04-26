from typing import Literal, cast

NexusAuthenticationType = Literal["Anonymous", "UsernamePassword"]

NEXUS_AUTHENTICATION_TYPE_VALUES: set[NexusAuthenticationType] = {
    "Anonymous",
    "UsernamePassword",
}


def check_nexus_authentication_type(value: str) -> NexusAuthenticationType:
    if value in NEXUS_AUTHENTICATION_TYPE_VALUES:
        return cast(NexusAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEXUS_AUTHENTICATION_TYPE_VALUES!r}")
