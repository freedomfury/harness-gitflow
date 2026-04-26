from typing import Literal, cast

ResponseDTOSetKustomizeCommandFlagTypeStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SET_KUSTOMIZE_COMMAND_FLAG_TYPE_STATUS_VALUES: set[ResponseDTOSetKustomizeCommandFlagTypeStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_set_kustomize_command_flag_type_status(
    value: str,
) -> ResponseDTOSetKustomizeCommandFlagTypeStatus:
    if value in RESPONSE_DTO_SET_KUSTOMIZE_COMMAND_FLAG_TYPE_STATUS_VALUES:
        return cast(ResponseDTOSetKustomizeCommandFlagTypeStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SET_KUSTOMIZE_COMMAND_FLAG_TYPE_STATUS_VALUES!r}"
    )
