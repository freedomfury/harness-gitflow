from typing import Literal, cast

ResponseDTOPageResponseGitFullSyncEntityInfoStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_GIT_FULL_SYNC_ENTITY_INFO_STATUS_VALUES: set[
    ResponseDTOPageResponseGitFullSyncEntityInfoStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_git_full_sync_entity_info_status(
    value: str,
) -> ResponseDTOPageResponseGitFullSyncEntityInfoStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_GIT_FULL_SYNC_ENTITY_INFO_STATUS_VALUES:
        return cast(ResponseDTOPageResponseGitFullSyncEntityInfoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_GIT_FULL_SYNC_ENTITY_INFO_STATUS_VALUES!r}"
    )
