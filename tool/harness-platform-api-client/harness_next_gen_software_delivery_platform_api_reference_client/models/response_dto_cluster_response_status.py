from typing import Literal, cast

ResponseDTOClusterResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CLUSTER_RESPONSE_STATUS_VALUES: set[ResponseDTOClusterResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_cluster_response_status(value: str) -> ResponseDTOClusterResponseStatus:
    if value in RESPONSE_DTO_CLUSTER_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOClusterResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CLUSTER_RESPONSE_STATUS_VALUES!r}")
