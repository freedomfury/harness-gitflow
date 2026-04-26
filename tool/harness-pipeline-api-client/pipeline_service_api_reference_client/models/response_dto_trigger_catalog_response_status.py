from typing import Literal, cast

ResponseDTOTriggerCatalogResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_TRIGGER_CATALOG_RESPONSE_STATUS_VALUES: set[ResponseDTOTriggerCatalogResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_trigger_catalog_response_status(value: str) -> ResponseDTOTriggerCatalogResponseStatus:
    if value in RESPONSE_DTO_TRIGGER_CATALOG_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOTriggerCatalogResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_TRIGGER_CATALOG_RESPONSE_STATUS_VALUES!r}"
    )
