from typing import Literal, cast

EntityDetailProtoDTOEntityRefCase = Literal[
    "ENTITYREF_NOT_SET", "IDENTIFIERREF", "INFRADEFREF", "INPUTSETREF", "TEMPLATEREF", "TRIGGERREF"
]

ENTITY_DETAIL_PROTO_DTO_ENTITY_REF_CASE_VALUES: set[EntityDetailProtoDTOEntityRefCase] = {
    "ENTITYREF_NOT_SET",
    "IDENTIFIERREF",
    "INFRADEFREF",
    "INPUTSETREF",
    "TEMPLATEREF",
    "TRIGGERREF",
}


def check_entity_detail_proto_dto_entity_ref_case(value: str) -> EntityDetailProtoDTOEntityRefCase:
    if value in ENTITY_DETAIL_PROTO_DTO_ENTITY_REF_CASE_VALUES:
        return cast(EntityDetailProtoDTOEntityRefCase, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENTITY_DETAIL_PROTO_DTO_ENTITY_REF_CASE_VALUES!r}")
