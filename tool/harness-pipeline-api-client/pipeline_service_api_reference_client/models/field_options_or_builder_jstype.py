from typing import Literal, cast

FieldOptionsOrBuilderJstype = Literal["JS_NORMAL", "JS_NUMBER", "JS_STRING"]

FIELD_OPTIONS_OR_BUILDER_JSTYPE_VALUES: set[FieldOptionsOrBuilderJstype] = {
    "JS_NORMAL",
    "JS_NUMBER",
    "JS_STRING",
}


def check_field_options_or_builder_jstype(value: str) -> FieldOptionsOrBuilderJstype:
    if value in FIELD_OPTIONS_OR_BUILDER_JSTYPE_VALUES:
        return cast(FieldOptionsOrBuilderJstype, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_OR_BUILDER_JSTYPE_VALUES!r}")
