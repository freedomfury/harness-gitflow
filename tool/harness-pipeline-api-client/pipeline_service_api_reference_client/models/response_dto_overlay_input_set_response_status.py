from typing import Literal, cast

ResponseDTOOverlayInputSetResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_OVERLAY_INPUT_SET_RESPONSE_STATUS_VALUES: set[ResponseDTOOverlayInputSetResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_overlay_input_set_response_status(value: str) -> ResponseDTOOverlayInputSetResponseStatus:
    if value in RESPONSE_DTO_OVERLAY_INPUT_SET_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOOverlayInputSetResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_OVERLAY_INPUT_SET_RESPONSE_STATUS_VALUES!r}"
    )
