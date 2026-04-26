from typing import Literal, cast

ResponseDTOSetK8SCommandFlagTypeStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SET_K8S_COMMAND_FLAG_TYPE_STATUS_VALUES: set[ResponseDTOSetK8SCommandFlagTypeStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_set_k8s_command_flag_type_status(value: str) -> ResponseDTOSetK8SCommandFlagTypeStatus:
    if value in RESPONSE_DTO_SET_K8S_COMMAND_FLAG_TYPE_STATUS_VALUES:
        return cast(ResponseDTOSetK8SCommandFlagTypeStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SET_K8S_COMMAND_FLAG_TYPE_STATUS_VALUES!r}"
    )
