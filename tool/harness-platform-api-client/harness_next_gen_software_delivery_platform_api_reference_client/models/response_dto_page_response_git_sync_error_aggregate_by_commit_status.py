from typing import Literal, cast

ResponseDTOPageResponseGitSyncErrorAggregateByCommitStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_GIT_SYNC_ERROR_AGGREGATE_BY_COMMIT_STATUS_VALUES: set[
    ResponseDTOPageResponseGitSyncErrorAggregateByCommitStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_git_sync_error_aggregate_by_commit_status(
    value: str,
) -> ResponseDTOPageResponseGitSyncErrorAggregateByCommitStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_GIT_SYNC_ERROR_AGGREGATE_BY_COMMIT_STATUS_VALUES:
        return cast(ResponseDTOPageResponseGitSyncErrorAggregateByCommitStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_GIT_SYNC_ERROR_AGGREGATE_BY_COMMIT_STATUS_VALUES!r}"
    )
