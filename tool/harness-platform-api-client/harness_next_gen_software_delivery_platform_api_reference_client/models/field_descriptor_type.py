from typing import Literal, cast

FieldDescriptorType = Literal[
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

FIELD_DESCRIPTOR_TYPE_VALUES: set[FieldDescriptorType] = {
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


def check_field_descriptor_type(value: str) -> FieldDescriptorType:
    if value in FIELD_DESCRIPTOR_TYPE_VALUES:
        return cast(FieldDescriptorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_DESCRIPTOR_TYPE_VALUES!r}")
