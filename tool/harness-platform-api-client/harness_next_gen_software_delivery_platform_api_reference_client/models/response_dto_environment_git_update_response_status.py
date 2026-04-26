from typing import Literal, cast

ResponseDTOEnvironmentGitUpdateResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ENVIRONMENT_GIT_UPDATE_RESPONSE_STATUS_VALUES: set[ResponseDTOEnvironmentGitUpdateResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_environment_git_update_response_status(
    value: str,
) -> ResponseDTOEnvironmentGitUpdateResponseStatus:
    if value in RESPONSE_DTO_ENVIRONMENT_GIT_UPDATE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOEnvironmentGitUpdateResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ENVIRONMENT_GIT_UPDATE_RESPONSE_STATUS_VALUES!r}"
    )
