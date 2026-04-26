from typing import Literal, cast

ResponseDTOPageResponseClusterResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_CLUSTER_RESPONSE_STATUS_VALUES: set[ResponseDTOPageResponseClusterResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_cluster_response_status(
    value: str,
) -> ResponseDTOPageResponseClusterResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_CLUSTER_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseClusterResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_CLUSTER_RESPONSE_STATUS_VALUES!r}"
    )
