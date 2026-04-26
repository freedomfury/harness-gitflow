from typing import Literal, cast

TemplateReferenceProtoDTOOrBuilderScope = Literal["ACCOUNT", "ORG", "PROJECT", "UNKNOWN", "UNRECOGNIZED"]

TEMPLATE_REFERENCE_PROTO_DTO_OR_BUILDER_SCOPE_VALUES: set[TemplateReferenceProtoDTOOrBuilderScope] = {
    "ACCOUNT",
    "ORG",
    "PROJECT",
    "UNKNOWN",
    "UNRECOGNIZED",
}


def check_template_reference_proto_dto_or_builder_scope(value: str) -> TemplateReferenceProtoDTOOrBuilderScope:
    if value in TEMPLATE_REFERENCE_PROTO_DTO_OR_BUILDER_SCOPE_VALUES:
        return cast(TemplateReferenceProtoDTOOrBuilderScope, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TEMPLATE_REFERENCE_PROTO_DTO_OR_BUILDER_SCOPE_VALUES!r}"
    )
