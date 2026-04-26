from typing import Literal, cast

ResponseDTONGTriggerDetailsResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTONG_TRIGGER_DETAILS_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTONGTriggerDetailsResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dtong_trigger_details_response_dto_status(
    value: str,
) -> ResponseDTONGTriggerDetailsResponseDTOStatus:
    if value in RESPONSE_DTONG_TRIGGER_DETAILS_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTONGTriggerDetailsResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTONG_TRIGGER_DETAILS_RESPONSE_DTO_STATUS_VALUES!r}"
    )
