from typing import Literal, cast

ResponseDTOSetEmbeddedUserDetailsDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SET_EMBEDDED_USER_DETAILS_DTO_STATUS_VALUES: set[ResponseDTOSetEmbeddedUserDetailsDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_set_embedded_user_details_dto_status(value: str) -> ResponseDTOSetEmbeddedUserDetailsDTOStatus:
    if value in RESPONSE_DTO_SET_EMBEDDED_USER_DETAILS_DTO_STATUS_VALUES:
        return cast(ResponseDTOSetEmbeddedUserDetailsDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SET_EMBEDDED_USER_DETAILS_DTO_STATUS_VALUES!r}"
    )
