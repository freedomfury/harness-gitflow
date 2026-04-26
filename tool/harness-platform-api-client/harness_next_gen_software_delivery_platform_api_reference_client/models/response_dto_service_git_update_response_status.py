from typing import Literal, cast

ResponseDTOServiceGitUpdateResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_GIT_UPDATE_RESPONSE_STATUS_VALUES: set[ResponseDTOServiceGitUpdateResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_git_update_response_status(value: str) -> ResponseDTOServiceGitUpdateResponseStatus:
    if value in RESPONSE_DTO_SERVICE_GIT_UPDATE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOServiceGitUpdateResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_GIT_UPDATE_RESPONSE_STATUS_VALUES!r}"
    )
