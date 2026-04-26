from typing import Literal, cast

FieldDescriptorProtoLabel = Literal["LABEL_OPTIONAL", "LABEL_REPEATED", "LABEL_REQUIRED"]

FIELD_DESCRIPTOR_PROTO_LABEL_VALUES: set[FieldDescriptorProtoLabel] = {
    "LABEL_OPTIONAL",
    "LABEL_REPEATED",
    "LABEL_REQUIRED",
}


def check_field_descriptor_proto_label(value: str) -> FieldDescriptorProtoLabel:
    if value in FIELD_DESCRIPTOR_PROTO_LABEL_VALUES:
        return cast(FieldDescriptorProtoLabel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_DESCRIPTOR_PROTO_LABEL_VALUES!r}")
