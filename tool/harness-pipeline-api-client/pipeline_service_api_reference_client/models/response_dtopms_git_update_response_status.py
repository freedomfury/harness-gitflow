from typing import Literal, cast

ResponseDTOPMSGitUpdateResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTOPMS_GIT_UPDATE_RESPONSE_STATUS_VALUES: set[ResponseDTOPMSGitUpdateResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dtopms_git_update_response_status(value: str) -> ResponseDTOPMSGitUpdateResponseStatus:
    if value in RESPONSE_DTOPMS_GIT_UPDATE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPMSGitUpdateResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTOPMS_GIT_UPDATE_RESPONSE_STATUS_VALUES!r}"
    )
