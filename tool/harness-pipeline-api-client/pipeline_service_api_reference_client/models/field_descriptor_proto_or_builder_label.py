from typing import Literal, cast

FieldDescriptorProtoOrBuilderLabel = Literal["LABEL_OPTIONAL", "LABEL_REPEATED", "LABEL_REQUIRED"]

FIELD_DESCRIPTOR_PROTO_OR_BUILDER_LABEL_VALUES: set[FieldDescriptorProtoOrBuilderLabel] = {
    "LABEL_OPTIONAL",
    "LABEL_REPEATED",
    "LABEL_REQUIRED",
}


def check_field_descriptor_proto_or_builder_label(value: str) -> FieldDescriptorProtoOrBuilderLabel:
    if value in FIELD_DESCRIPTOR_PROTO_OR_BUILDER_LABEL_VALUES:
        return cast(FieldDescriptorProtoOrBuilderLabel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_DESCRIPTOR_PROTO_OR_BUILDER_LABEL_VALUES!r}")
