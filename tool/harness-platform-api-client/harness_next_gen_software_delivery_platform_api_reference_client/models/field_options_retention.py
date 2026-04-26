from typing import Literal, cast

FieldOptionsRetention = Literal["RETENTION_RUNTIME", "RETENTION_SOURCE", "RETENTION_UNKNOWN"]

FIELD_OPTIONS_RETENTION_VALUES: set[FieldOptionsRetention] = {
    "RETENTION_RUNTIME",
    "RETENTION_SOURCE",
    "RETENTION_UNKNOWN",
}


def check_field_options_retention(value: str) -> FieldOptionsRetention:
    if value in FIELD_OPTIONS_RETENTION_VALUES:
        return cast(FieldOptionsRetention, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_RETENTION_VALUES!r}")
