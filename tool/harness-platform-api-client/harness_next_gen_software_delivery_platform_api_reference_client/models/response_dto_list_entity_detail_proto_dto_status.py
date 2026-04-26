from typing import Literal, cast

ResponseDTOListEntityDetailProtoDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_ENTITY_DETAIL_PROTO_DTO_STATUS_VALUES: set[ResponseDTOListEntityDetailProtoDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_entity_detail_proto_dto_status(value: str) -> ResponseDTOListEntityDetailProtoDTOStatus:
    if value in RESPONSE_DTO_LIST_ENTITY_DETAIL_PROTO_DTO_STATUS_VALUES:
        return cast(ResponseDTOListEntityDetailProtoDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_ENTITY_DETAIL_PROTO_DTO_STATUS_VALUES!r}"
    )
