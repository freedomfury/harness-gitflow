from typing import Literal, cast

FieldOptionsCtype = Literal["CORD", "STRING", "STRING_PIECE"]

FIELD_OPTIONS_CTYPE_VALUES: set[FieldOptionsCtype] = {
    "CORD",
    "STRING",
    "STRING_PIECE",
}


def check_field_options_ctype(value: str) -> FieldOptionsCtype:
    if value in FIELD_OPTIONS_CTYPE_VALUES:
        return cast(FieldOptionsCtype, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_CTYPE_VALUES!r}")
