from typing import Literal, cast

TemplateReferenceProtoDTOScope = Literal["ACCOUNT", "ORG", "PROJECT", "UNKNOWN", "UNRECOGNIZED"]

TEMPLATE_REFERENCE_PROTO_DTO_SCOPE_VALUES: set[TemplateReferenceProtoDTOScope] = {
    "ACCOUNT",
    "ORG",
    "PROJECT",
    "UNKNOWN",
    "UNRECOGNIZED",
}


def check_template_reference_proto_dto_scope(value: str) -> TemplateReferenceProtoDTOScope:
    if value in TEMPLATE_REFERENCE_PROTO_DTO_SCOPE_VALUES:
        return cast(TemplateReferenceProtoDTOScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEMPLATE_REFERENCE_PROTO_DTO_SCOPE_VALUES!r}")
