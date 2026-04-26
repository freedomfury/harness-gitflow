from typing import Literal, cast

ResponseDTOPostProdRollbackCheckDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_POST_PROD_ROLLBACK_CHECK_DTO_STATUS_VALUES: set[ResponseDTOPostProdRollbackCheckDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_post_prod_rollback_check_dto_status(value: str) -> ResponseDTOPostProdRollbackCheckDTOStatus:
    if value in RESPONSE_DTO_POST_PROD_ROLLBACK_CHECK_DTO_STATUS_VALUES:
        return cast(ResponseDTOPostProdRollbackCheckDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_POST_PROD_ROLLBACK_CHECK_DTO_STATUS_VALUES!r}"
    )
