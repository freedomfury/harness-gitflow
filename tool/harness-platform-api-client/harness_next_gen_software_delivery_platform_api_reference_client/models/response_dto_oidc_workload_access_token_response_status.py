from typing import Literal, cast

ResponseDTOOidcWorkloadAccessTokenResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_OIDC_WORKLOAD_ACCESS_TOKEN_RESPONSE_STATUS_VALUES: set[
    ResponseDTOOidcWorkloadAccessTokenResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_oidc_workload_access_token_response_status(
    value: str,
) -> ResponseDTOOidcWorkloadAccessTokenResponseStatus:
    if value in RESPONSE_DTO_OIDC_WORKLOAD_ACCESS_TOKEN_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOOidcWorkloadAccessTokenResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_OIDC_WORKLOAD_ACCESS_TOKEN_RESPONSE_STATUS_VALUES!r}"
    )
