from typing import Literal, cast

FieldOptionsJstype = Literal["JS_NORMAL", "JS_NUMBER", "JS_STRING"]

FIELD_OPTIONS_JSTYPE_VALUES: set[FieldOptionsJstype] = {
    "JS_NORMAL",
    "JS_NUMBER",
    "JS_STRING",
}


def check_field_options_jstype(value: str) -> FieldOptionsJstype:
    if value in FIELD_OPTIONS_JSTYPE_VALUES:
        return cast(FieldOptionsJstype, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_JSTYPE_VALUES!r}")
