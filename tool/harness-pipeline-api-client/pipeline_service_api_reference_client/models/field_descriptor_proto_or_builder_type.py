from typing import Literal, cast

FieldDescriptorProtoOrBuilderType = Literal[
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

FIELD_DESCRIPTOR_PROTO_OR_BUILDER_TYPE_VALUES: set[FieldDescriptorProtoOrBuilderType] = {
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


def check_field_descriptor_proto_or_builder_type(value: str) -> FieldDescriptorProtoOrBuilderType:
    if value in FIELD_DESCRIPTOR_PROTO_OR_BUILDER_TYPE_VALUES:
        return cast(FieldDescriptorProtoOrBuilderType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_DESCRIPTOR_PROTO_OR_BUILDER_TYPE_VALUES!r}")
