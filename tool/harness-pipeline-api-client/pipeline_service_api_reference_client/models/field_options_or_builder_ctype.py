from typing import Literal, cast

FieldOptionsOrBuilderCtype = Literal["CORD", "STRING", "STRING_PIECE"]

FIELD_OPTIONS_OR_BUILDER_CTYPE_VALUES: set[FieldOptionsOrBuilderCtype] = {
    "CORD",
    "STRING",
    "STRING_PIECE",
}


def check_field_options_or_builder_ctype(value: str) -> FieldOptionsOrBuilderCtype:
    if value in FIELD_OPTIONS_OR_BUILDER_CTYPE_VALUES:
        return cast(FieldOptionsOrBuilderCtype, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_OR_BUILDER_CTYPE_VALUES!r}")
