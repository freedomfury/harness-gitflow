from typing import Literal, cast

RollbackRequestDTOEnvironmentType = Literal["PreProduction", "Production"]

ROLLBACK_REQUEST_DTO_ENVIRONMENT_TYPE_VALUES: set[RollbackRequestDTOEnvironmentType] = {
    "PreProduction",
    "Production",
}


def check_rollback_request_dto_environment_type(value: str) -> RollbackRequestDTOEnvironmentType:
    if value in ROLLBACK_REQUEST_DTO_ENVIRONMENT_TYPE_VALUES:
        return cast(RollbackRequestDTOEnvironmentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLLBACK_REQUEST_DTO_ENVIRONMENT_TYPE_VALUES!r}")
