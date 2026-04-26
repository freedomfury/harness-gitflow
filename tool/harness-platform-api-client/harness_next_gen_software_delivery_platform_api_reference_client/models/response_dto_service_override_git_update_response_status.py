from typing import Literal, cast

ResponseDTOServiceOverrideGitUpdateResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_OVERRIDE_GIT_UPDATE_RESPONSE_STATUS_VALUES: set[
    ResponseDTOServiceOverrideGitUpdateResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_override_git_update_response_status(
    value: str,
) -> ResponseDTOServiceOverrideGitUpdateResponseStatus:
    if value in RESPONSE_DTO_SERVICE_OVERRIDE_GIT_UPDATE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOServiceOverrideGitUpdateResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_OVERRIDE_GIT_UPDATE_RESPONSE_STATUS_VALUES!r}"
    )
