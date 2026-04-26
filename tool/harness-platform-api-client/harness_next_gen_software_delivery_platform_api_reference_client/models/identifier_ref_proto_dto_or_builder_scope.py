from typing import Literal, cast

IdentifierRefProtoDTOOrBuilderScope = Literal["ACCOUNT", "ORG", "PROJECT", "UNKNOWN", "UNRECOGNIZED"]

IDENTIFIER_REF_PROTO_DTO_OR_BUILDER_SCOPE_VALUES: set[IdentifierRefProtoDTOOrBuilderScope] = {
    "ACCOUNT",
    "ORG",
    "PROJECT",
    "UNKNOWN",
    "UNRECOGNIZED",
}


def check_identifier_ref_proto_dto_or_builder_scope(value: str) -> IdentifierRefProtoDTOOrBuilderScope:
    if value in IDENTIFIER_REF_PROTO_DTO_OR_BUILDER_SCOPE_VALUES:
        return cast(IdentifierRefProtoDTOOrBuilderScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTIFIER_REF_PROTO_DTO_OR_BUILDER_SCOPE_VALUES!r}")
