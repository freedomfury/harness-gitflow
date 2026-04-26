from typing import Literal, cast

ResponseDTOPostProdRollbackResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_POST_PROD_ROLLBACK_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOPostProdRollbackResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_post_prod_rollback_response_dto_status(
    value: str,
) -> ResponseDTOPostProdRollbackResponseDTOStatus:
    if value in RESPONSE_DTO_POST_PROD_ROLLBACK_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOPostProdRollbackResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_POST_PROD_ROLLBACK_RESPONSE_DTO_STATUS_VALUES!r}"
    )
