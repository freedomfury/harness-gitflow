from typing import Literal, cast

ResponseDTOListBranchSequenceStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_BRANCH_SEQUENCE_STATUS_VALUES: set[ResponseDTOListBranchSequenceStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_branch_sequence_status(value: str) -> ResponseDTOListBranchSequenceStatus:
    if value in RESPONSE_DTO_LIST_BRANCH_SEQUENCE_STATUS_VALUES:
        return cast(ResponseDTOListBranchSequenceStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_BRANCH_SEQUENCE_STATUS_VALUES!r}")
