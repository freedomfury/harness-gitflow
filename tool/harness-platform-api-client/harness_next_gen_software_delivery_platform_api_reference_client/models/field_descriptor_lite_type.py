from typing import Literal, cast

FieldDescriptorLiteType = Literal[
    "BOOL",
    "BYTES",
    "DOUBLE",
    "ENUM",
    "FIXED32",
    "FIXED64",
    "FLOAT",
    "GROUP",
    "INT32",
    "INT64",
    "MESSAGE",
    "SFIXED32",
    "SFIXED64",
    "SINT32",
    "SINT64",
    "STRING",
    "UINT32",
    "UINT64",
]

FIELD_DESCRIPTOR_LITE_TYPE_VALUES: set[FieldDescriptorLiteType] = {
    "BOOL",
    "BYTES",
    "DOUBLE",
    "ENUM",
    "FIXED32",
    "FIXED64",
    "FLOAT",
    "GROUP",
    "INT32",
    "INT64",
    "MESSAGE",
    "SFIXED32",
    "SFIXED64",
    "SINT32",
    "SINT64",
    "STRING",
    "UINT32",
    "UINT64",
}


def check_field_descriptor_lite_type(value: str) -> FieldDescriptorLiteType:
    if value in FIELD_DESCRIPTOR_LITE_TYPE_VALUES:
        return cast(FieldDescriptorLiteType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_DESCRIPTOR_LITE_TYPE_VALUES!r}")
