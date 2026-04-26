from typing import Literal, cast

ResponseMessageLevel = Literal["ERROR", "INFO"]

RESPONSE_MESSAGE_LEVEL_VALUES: set[ResponseMessageLevel] = {
    "ERROR",
    "INFO",
}


def check_response_message_level(value: str) -> ResponseMessageLevel:
    if value in RESPONSE_MESSAGE_LEVEL_VALUES:
        return cast(ResponseMessageLevel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_MESSAGE_LEVEL_VALUES!r}")
