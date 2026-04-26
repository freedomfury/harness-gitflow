from typing import Literal, cast

HarnessHttpCredentialsType = Literal["UsernameToken"]

HARNESS_HTTP_CREDENTIALS_TYPE_VALUES: set[HarnessHttpCredentialsType] = {
    "UsernameToken",
}


def check_harness_http_credentials_type(value: str) -> HarnessHttpCredentialsType:
    if value in HARNESS_HTTP_CREDENTIALS_TYPE_VALUES:
        return cast(HarnessHttpCredentialsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HARNESS_HTTP_CREDENTIALS_TYPE_VALUES!r}")
