from typing import Literal, cast

HarnessApiAccessType = Literal["Jwt_Token", "Token"]

HARNESS_API_ACCESS_TYPE_VALUES: set[HarnessApiAccessType] = {
    "Jwt_Token",
    "Token",
}


def check_harness_api_access_type(value: str) -> HarnessApiAccessType:
    if value in HARNESS_API_ACCESS_TYPE_VALUES:
        return cast(HarnessApiAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HARNESS_API_ACCESS_TYPE_VALUES!r}")
