from typing import Literal, cast

ResponseDTOPluginInfoResponseDtoStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PLUGIN_INFO_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOPluginInfoResponseDtoStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_plugin_info_response_dto_status(value: str) -> ResponseDTOPluginInfoResponseDtoStatus:
    if value in RESPONSE_DTO_PLUGIN_INFO_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOPluginInfoResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PLUGIN_INFO_RESPONSE_DTO_STATUS_VALUES!r}"
    )
