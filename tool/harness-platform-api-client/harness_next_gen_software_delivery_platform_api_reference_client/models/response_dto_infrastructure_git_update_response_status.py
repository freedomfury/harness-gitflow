from typing import Literal, cast

ResponseDTOInfrastructureGitUpdateResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INFRASTRUCTURE_GIT_UPDATE_RESPONSE_STATUS_VALUES: set[ResponseDTOInfrastructureGitUpdateResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_infrastructure_git_update_response_status(
    value: str,
) -> ResponseDTOInfrastructureGitUpdateResponseStatus:
    if value in RESPONSE_DTO_INFRASTRUCTURE_GIT_UPDATE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOInfrastructureGitUpdateResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INFRASTRUCTURE_GIT_UPDATE_RESPONSE_STATUS_VALUES!r}"
    )
