from typing import Literal, cast

FieldOptionsOrBuilderRetention = Literal["RETENTION_RUNTIME", "RETENTION_SOURCE", "RETENTION_UNKNOWN"]

FIELD_OPTIONS_OR_BUILDER_RETENTION_VALUES: set[FieldOptionsOrBuilderRetention] = {
    "RETENTION_RUNTIME",
    "RETENTION_SOURCE",
    "RETENTION_UNKNOWN",
}


def check_field_options_or_builder_retention(value: str) -> FieldOptionsOrBuilderRetention:
    if value in FIELD_OPTIONS_OR_BUILDER_RETENTION_VALUES:
        return cast(FieldOptionsOrBuilderRetention, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_OR_BUILDER_RETENTION_VALUES!r}")
