from typing import Literal, cast

ResponseDTOInputSetGitUpdateResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INPUT_SET_GIT_UPDATE_RESPONSE_STATUS_VALUES: set[ResponseDTOInputSetGitUpdateResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_input_set_git_update_response_status(value: str) -> ResponseDTOInputSetGitUpdateResponseStatus:
    if value in RESPONSE_DTO_INPUT_SET_GIT_UPDATE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOInputSetGitUpdateResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INPUT_SET_GIT_UPDATE_RESPONSE_STATUS_VALUES!r}"
    )
