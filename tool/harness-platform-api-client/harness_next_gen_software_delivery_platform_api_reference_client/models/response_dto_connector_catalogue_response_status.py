from typing import Literal, cast

ResponseDTOConnectorCatalogueResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CONNECTOR_CATALOGUE_RESPONSE_STATUS_VALUES: set[ResponseDTOConnectorCatalogueResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_connector_catalogue_response_status(value: str) -> ResponseDTOConnectorCatalogueResponseStatus:
    if value in RESPONSE_DTO_CONNECTOR_CATALOGUE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOConnectorCatalogueResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CONNECTOR_CATALOGUE_RESPONSE_STATUS_VALUES!r}"
    )
