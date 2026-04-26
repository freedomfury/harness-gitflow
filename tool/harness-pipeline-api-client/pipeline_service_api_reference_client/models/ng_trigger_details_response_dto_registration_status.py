from typing import Literal, cast

NGTriggerDetailsResponseDTORegistrationStatus = Literal["ERROR", "FAILED", "SUCCESS", "TIMEOUT", "UNAVAILABLE"]

NG_TRIGGER_DETAILS_RESPONSE_DTO_REGISTRATION_STATUS_VALUES: set[NGTriggerDetailsResponseDTORegistrationStatus] = {
    "ERROR",
    "FAILED",
    "SUCCESS",
    "TIMEOUT",
    "UNAVAILABLE",
}


def check_ng_trigger_details_response_dto_registration_status(
    value: str,
) -> NGTriggerDetailsResponseDTORegistrationStatus:
    if value in NG_TRIGGER_DETAILS_RESPONSE_DTO_REGISTRATION_STATUS_VALUES:
        return cast(NGTriggerDetailsResponseDTORegistrationStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NG_TRIGGER_DETAILS_RESPONSE_DTO_REGISTRATION_STATUS_VALUES!r}"
    )
