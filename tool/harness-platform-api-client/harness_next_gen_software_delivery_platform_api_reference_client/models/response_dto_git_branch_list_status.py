from typing import Literal, cast

ResponseDTOGitBranchListStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_GIT_BRANCH_LIST_STATUS_VALUES: set[ResponseDTOGitBranchListStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_git_branch_list_status(value: str) -> ResponseDTOGitBranchListStatus:
    if value in RESPONSE_DTO_GIT_BRANCH_LIST_STATUS_VALUES:
        return cast(ResponseDTOGitBranchListStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_GIT_BRANCH_LIST_STATUS_VALUES!r}")
