from typing import Literal, cast

MethodOptionsOrBuilderIdempotencyLevel = Literal["IDEMPOTENCY_UNKNOWN", "IDEMPOTENT", "NO_SIDE_EFFECTS"]

METHOD_OPTIONS_OR_BUILDER_IDEMPOTENCY_LEVEL_VALUES: set[MethodOptionsOrBuilderIdempotencyLevel] = {
    "IDEMPOTENCY_UNKNOWN",
    "IDEMPOTENT",
    "NO_SIDE_EFFECTS",
}


def check_method_options_or_builder_idempotency_level(value: str) -> MethodOptionsOrBuilderIdempotencyLevel:
    if value in METHOD_OPTIONS_OR_BUILDER_IDEMPOTENCY_LEVEL_VALUES:
        return cast(MethodOptionsOrBuilderIdempotencyLevel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {METHOD_OPTIONS_OR_BUILDER_IDEMPOTENCY_LEVEL_VALUES!r}"
    )
