from typing import Literal, cast

MethodOptionsIdempotencyLevel = Literal["IDEMPOTENCY_UNKNOWN", "IDEMPOTENT", "NO_SIDE_EFFECTS"]

METHOD_OPTIONS_IDEMPOTENCY_LEVEL_VALUES: set[MethodOptionsIdempotencyLevel] = {
    "IDEMPOTENCY_UNKNOWN",
    "IDEMPOTENT",
    "NO_SIDE_EFFECTS",
}


def check_method_options_idempotency_level(value: str) -> MethodOptionsIdempotencyLevel:
    if value in METHOD_OPTIONS_IDEMPOTENCY_LEVEL_VALUES:
        return cast(MethodOptionsIdempotencyLevel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {METHOD_OPTIONS_IDEMPOTENCY_LEVEL_VALUES!r}")
