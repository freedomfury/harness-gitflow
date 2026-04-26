from typing import Literal, cast

ResponseDTOSecretManagerMetadataDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SECRET_MANAGER_METADATA_DTO_STATUS_VALUES: set[ResponseDTOSecretManagerMetadataDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_secret_manager_metadata_dto_status(value: str) -> ResponseDTOSecretManagerMetadataDTOStatus:
    if value in RESPONSE_DTO_SECRET_MANAGER_METADATA_DTO_STATUS_VALUES:
        return cast(ResponseDTOSecretManagerMetadataDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SECRET_MANAGER_METADATA_DTO_STATUS_VALUES!r}"
    )
