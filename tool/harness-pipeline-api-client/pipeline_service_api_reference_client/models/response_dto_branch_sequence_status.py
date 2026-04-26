from typing import Literal, cast

ResponseDTOBranchSequenceStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_BRANCH_SEQUENCE_STATUS_VALUES: set[ResponseDTOBranchSequenceStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_branch_sequence_status(value: str) -> ResponseDTOBranchSequenceStatus:
    if value in RESPONSE_DTO_BRANCH_SEQUENCE_STATUS_VALUES:
        return cast(ResponseDTOBranchSequenceStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_BRANCH_SEQUENCE_STATUS_VALUES!r}")
