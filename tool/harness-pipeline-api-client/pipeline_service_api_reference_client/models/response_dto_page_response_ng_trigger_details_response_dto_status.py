from typing import Literal, cast

ResponseDTOPageResponseNGTriggerDetailsResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_NG_TRIGGER_DETAILS_RESPONSE_DTO_STATUS_VALUES: set[
    ResponseDTOPageResponseNGTriggerDetailsResponseDTOStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_ng_trigger_details_response_dto_status(
    value: str,
) -> ResponseDTOPageResponseNGTriggerDetailsResponseDTOStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_NG_TRIGGER_DETAILS_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOPageResponseNGTriggerDetailsResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_NG_TRIGGER_DETAILS_RESPONSE_DTO_STATUS_VALUES!r}"
    )
