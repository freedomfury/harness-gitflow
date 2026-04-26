from typing import Literal, cast

FieldDescriptorLiteJavaType = Literal[
    "BOOLEAN", "BYTE_STRING", "DOUBLE", "ENUM", "FLOAT", "INT", "LONG", "MESSAGE", "STRING"
]

FIELD_DESCRIPTOR_LITE_JAVA_TYPE_VALUES: set[FieldDescriptorLiteJavaType] = {
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


def check_field_descriptor_lite_java_type(value: str) -> FieldDescriptorLiteJavaType:
    if value in FIELD_DESCRIPTOR_LITE_JAVA_TYPE_VALUES:
        return cast(FieldDescriptorLiteJavaType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_DESCRIPTOR_LITE_JAVA_TYPE_VALUES!r}")
