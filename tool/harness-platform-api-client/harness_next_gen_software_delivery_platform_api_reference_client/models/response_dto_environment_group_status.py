from typing import Literal, cast

ResponseDTOEnvironmentGroupStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ENVIRONMENT_GROUP_STATUS_VALUES: set[ResponseDTOEnvironmentGroupStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_environment_group_status(value: str) -> ResponseDTOEnvironmentGroupStatus:
    if value in RESPONSE_DTO_ENVIRONMENT_GROUP_STATUS_VALUES:
        return cast(ResponseDTOEnvironmentGroupStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ENVIRONMENT_GROUP_STATUS_VALUES!r}")
