from typing import Literal, cast

IdentifierRefProtoDTOScope = Literal["ACCOUNT", "ORG", "PROJECT", "UNKNOWN", "UNRECOGNIZED"]

IDENTIFIER_REF_PROTO_DTO_SCOPE_VALUES: set[IdentifierRefProtoDTOScope] = {
    "ACCOUNT",
    "ORG",
    "PROJECT",
    "UNKNOWN",
    "UNRECOGNIZED",
}


def check_identifier_ref_proto_dto_scope(value: str) -> IdentifierRefProtoDTOScope:
    if value in IDENTIFIER_REF_PROTO_DTO_SCOPE_VALUES:
        return cast(IdentifierRefProtoDTOScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTIFIER_REF_PROTO_DTO_SCOPE_VALUES!r}")
