from typing import Literal, cast

ResponseDTOPasswordChangeResponseData = Literal[
    "INCORRECT_CURRENT_PASSWORD", "PASSWORD_CHANGED", "PASSWORD_STRENGTH_VIOLATED"
]

RESPONSE_DTO_PASSWORD_CHANGE_RESPONSE_DATA_VALUES: set[ResponseDTOPasswordChangeResponseData] = {
    "INCORRECT_CURRENT_PASSWORD",
    "PASSWORD_CHANGED",
    "PASSWORD_STRENGTH_VIOLATED",
}


def check_response_dto_password_change_response_data(value: str) -> ResponseDTOPasswordChangeResponseData:
    if value in RESPONSE_DTO_PASSWORD_CHANGE_RESPONSE_DATA_VALUES:
        return cast(ResponseDTOPasswordChangeResponseData, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PASSWORD_CHANGE_RESPONSE_DATA_VALUES!r}"
    )
