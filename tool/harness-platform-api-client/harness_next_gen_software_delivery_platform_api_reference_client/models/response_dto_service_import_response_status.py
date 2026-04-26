from typing import Literal, cast

ResponseDTOServiceImportResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_IMPORT_RESPONSE_STATUS_VALUES: set[ResponseDTOServiceImportResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_import_response_status(value: str) -> ResponseDTOServiceImportResponseStatus:
    if value in RESPONSE_DTO_SERVICE_IMPORT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOServiceImportResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_IMPORT_RESPONSE_STATUS_VALUES!r}"
    )
