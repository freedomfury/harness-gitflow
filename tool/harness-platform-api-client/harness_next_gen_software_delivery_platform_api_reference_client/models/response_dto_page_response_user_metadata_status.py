from typing import Literal, cast

ResponseDTOPageResponseUserMetadataStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_USER_METADATA_STATUS_VALUES: set[ResponseDTOPageResponseUserMetadataStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_user_metadata_status(value: str) -> ResponseDTOPageResponseUserMetadataStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_USER_METADATA_STATUS_VALUES:
        return cast(ResponseDTOPageResponseUserMetadataStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_USER_METADATA_STATUS_VALUES!r}"
    )
