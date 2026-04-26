from typing import Literal, cast

ResponseDTOSetKustomizeCommandFlagTypeDataItem = Literal["Build"]

RESPONSE_DTO_SET_KUSTOMIZE_COMMAND_FLAG_TYPE_DATA_ITEM_VALUES: set[ResponseDTOSetKustomizeCommandFlagTypeDataItem] = {
    "Build",
}


def check_response_dto_set_kustomize_command_flag_type_data_item(
    value: str,
) -> ResponseDTOSetKustomizeCommandFlagTypeDataItem:
    if value in RESPONSE_DTO_SET_KUSTOMIZE_COMMAND_FLAG_TYPE_DATA_ITEM_VALUES:
        return cast(ResponseDTOSetKustomizeCommandFlagTypeDataItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SET_KUSTOMIZE_COMMAND_FLAG_TYPE_DATA_ITEM_VALUES!r}"
    )
