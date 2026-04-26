from typing import Literal, cast

ResponseDTOApprovalInstanceResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_APPROVAL_INSTANCE_RESPONSE_STATUS_VALUES: set[ResponseDTOApprovalInstanceResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_approval_instance_response_status(value: str) -> ResponseDTOApprovalInstanceResponseStatus:
    if value in RESPONSE_DTO_APPROVAL_INSTANCE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOApprovalInstanceResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_APPROVAL_INSTANCE_RESPONSE_STATUS_VALUES!r}"
    )
