from typing import Literal, cast

ResponseDTOInfrastructureImportResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INFRASTRUCTURE_IMPORT_RESPONSE_STATUS_VALUES: set[ResponseDTOInfrastructureImportResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_infrastructure_import_response_status(
    value: str,
) -> ResponseDTOInfrastructureImportResponseStatus:
    if value in RESPONSE_DTO_INFRASTRUCTURE_IMPORT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOInfrastructureImportResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INFRASTRUCTURE_IMPORT_RESPONSE_STATUS_VALUES!r}"
    )
