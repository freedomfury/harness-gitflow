from typing import Literal, cast

FieldDescriptorProtoType = Literal[
    "TYPE_BOOL",
    "TYPE_BYTES",
    "TYPE_DOUBLE",
    "TYPE_ENUM",
    "TYPE_FIXED32",
    "TYPE_FIXED64",
    "TYPE_FLOAT",
    "TYPE_GROUP",
    "TYPE_INT32",
    "TYPE_INT64",
    "TYPE_MESSAGE",
    "TYPE_SFIXED32",
    "TYPE_SFIXED64",
    "TYPE_SINT32",
    "TYPE_SINT64",
    "TYPE_STRING",
    "TYPE_UINT32",
    "TYPE_UINT64",
]

FIELD_DESCRIPTOR_PROTO_TYPE_VALUES: set[FieldDescriptorProtoType] = {
    "TYPE_BOOL",
    "TYPE_BYTES",
    "TYPE_DOUBLE",
    "TYPE_ENUM",
    "TYPE_FIXED32",
    "TYPE_FIXED64",
    "TYPE_FLOAT",
    "TYPE_GROUP",
    "TYPE_INT32",
    "TYPE_INT64",
    "TYPE_MESSAGE",
    "TYPE_SFIXED32",
    "TYPE_SFIXED64",
    "TYPE_SINT32",
    "TYPE_SINT64",
    "TYPE_STRING",
    "TYPE_UINT32",
    "TYPE_UINT64",
}


def check_field_descriptor_proto_type(value: str) -> FieldDescriptorProtoType:
    if value in FIELD_DESCRIPTOR_PROTO_TYPE_VALUES:
        return cast(FieldDescriptorProtoType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_DESCRIPTOR_PROTO_TYPE_VALUES!r}")
