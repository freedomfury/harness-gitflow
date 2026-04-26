from typing import Literal, cast

ResponseDTOGcpOidcServiceAccountAccessTokenResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_GCP_OIDC_SERVICE_ACCOUNT_ACCESS_TOKEN_RESPONSE_STATUS_VALUES: set[
    ResponseDTOGcpOidcServiceAccountAccessTokenResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_gcp_oidc_service_account_access_token_response_status(
    value: str,
) -> ResponseDTOGcpOidcServiceAccountAccessTokenResponseStatus:
    if value in RESPONSE_DTO_GCP_OIDC_SERVICE_ACCOUNT_ACCESS_TOKEN_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOGcpOidcServiceAccountAccessTokenResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_GCP_OIDC_SERVICE_ACCOUNT_ACCESS_TOKEN_RESPONSE_STATUS_VALUES!r}"
    )
