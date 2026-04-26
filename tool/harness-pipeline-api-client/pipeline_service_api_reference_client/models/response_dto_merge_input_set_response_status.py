from typing import Literal, cast

ResponseDTOMergeInputSetResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_MERGE_INPUT_SET_RESPONSE_STATUS_VALUES: set[ResponseDTOMergeInputSetResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_merge_input_set_response_status(value: str) -> ResponseDTOMergeInputSetResponseStatus:
    if value in RESPONSE_DTO_MERGE_INPUT_SET_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOMergeInputSetResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_MERGE_INPUT_SET_RESPONSE_STATUS_VALUES!r}"
    )
