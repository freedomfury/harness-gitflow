from typing import Literal, cast

EntityReferenceScope = Literal["account", "org", "project", "unknown"]

ENTITY_REFERENCE_SCOPE_VALUES: set[EntityReferenceScope] = {
    "account",
    "org",
    "project",
    "unknown",
}


def check_entity_reference_scope(value: str) -> EntityReferenceScope:
    if value in ENTITY_REFERENCE_SCOPE_VALUES:
        return cast(EntityReferenceScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENTITY_REFERENCE_SCOPE_VALUES!r}")
