from typing import Literal, cast

ResponseDTOPageResponseCcmK8SConnectorResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_CCM_K8S_CONNECTOR_RESPONSE_STATUS_VALUES: set[
    ResponseDTOPageResponseCcmK8SConnectorResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_ccm_k8s_connector_response_status(
    value: str,
) -> ResponseDTOPageResponseCcmK8SConnectorResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_CCM_K8S_CONNECTOR_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseCcmK8SConnectorResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_CCM_K8S_CONNECTOR_RESPONSE_STATUS_VALUES!r}"
    )
