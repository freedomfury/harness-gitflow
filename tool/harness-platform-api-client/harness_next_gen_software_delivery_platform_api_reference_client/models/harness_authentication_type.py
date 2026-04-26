from typing import Literal, cast

HarnessAuthenticationType = Literal["Http", "Ssh"]

HARNESS_AUTHENTICATION_TYPE_VALUES: set[HarnessAuthenticationType] = {
    "Http",
    "Ssh",
}


def check_harness_authentication_type(value: str) -> HarnessAuthenticationType:
    if value in HARNESS_AUTHENTICATION_TYPE_VALUES:
        return cast(HarnessAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HARNESS_AUTHENTICATION_TYPE_VALUES!r}")
