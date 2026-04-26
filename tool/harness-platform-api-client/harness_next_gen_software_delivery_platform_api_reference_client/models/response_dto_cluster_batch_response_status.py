from typing import Literal, cast

ResponseDTOClusterBatchResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CLUSTER_BATCH_RESPONSE_STATUS_VALUES: set[ResponseDTOClusterBatchResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_cluster_batch_response_status(value: str) -> ResponseDTOClusterBatchResponseStatus:
    if value in RESPONSE_DTO_CLUSTER_BATCH_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOClusterBatchResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CLUSTER_BATCH_RESPONSE_STATUS_VALUES!r}"
    )
