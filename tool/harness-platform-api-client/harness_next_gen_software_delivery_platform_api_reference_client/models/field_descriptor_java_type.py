from typing import Literal, cast

FieldDescriptorJavaType = Literal[
    "BOOLEAN", "BYTE_STRING", "DOUBLE", "ENUM", "FLOAT", "INT", "LONG", "MESSAGE", "STRING"
]

FIELD_DESCRIPTOR_JAVA_TYPE_VALUES: set[FieldDescriptorJavaType] = {
    "BOOLEAN",
    "BYTE_STRING",
    "DOUBLE",
    "ENUM",
    "FLOAT",
    "INT",
    "LONG",
    "MESSAGE",
    "STRING",
}


def check_field_descriptor_java_type(value: str) -> FieldDescriptorJavaType:
    if value in FIELD_DESCRIPTOR_JAVA_TYPE_VALUES:
        return cast(FieldDescriptorJavaType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_DESCRIPTOR_JAVA_TYPE_VALUES!r}")
