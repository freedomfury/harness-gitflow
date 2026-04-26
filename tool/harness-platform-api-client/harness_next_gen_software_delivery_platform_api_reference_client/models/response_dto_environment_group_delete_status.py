from typing import Literal, cast

ResponseDTOEnvironmentGroupDeleteStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ENVIRONMENT_GROUP_DELETE_STATUS_VALUES: set[ResponseDTOEnvironmentGroupDeleteStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_environment_group_delete_status(value: str) -> ResponseDTOEnvironmentGroupDeleteStatus:
    if value in RESPONSE_DTO_ENVIRONMENT_GROUP_DELETE_STATUS_VALUES:
        return cast(ResponseDTOEnvironmentGroupDeleteStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ENVIRONMENT_GROUP_DELETE_STATUS_VALUES!r}"
    )
