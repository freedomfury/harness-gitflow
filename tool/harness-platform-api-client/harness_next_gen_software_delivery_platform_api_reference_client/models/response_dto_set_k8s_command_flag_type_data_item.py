from typing import Literal, cast

ResponseDTOSetK8SCommandFlagTypeDataItem = Literal["Apply", "Delete", "Diff", "Patch", "Rollout"]

RESPONSE_DTO_SET_K8S_COMMAND_FLAG_TYPE_DATA_ITEM_VALUES: set[ResponseDTOSetK8SCommandFlagTypeDataItem] = {
    "Apply",
    "Delete",
    "Diff",
    "Patch",
    "Rollout",
}


def check_response_dto_set_k8s_command_flag_type_data_item(value: str) -> ResponseDTOSetK8SCommandFlagTypeDataItem:
    if value in RESPONSE_DTO_SET_K8S_COMMAND_FLAG_TYPE_DATA_ITEM_VALUES:
        return cast(ResponseDTOSetK8SCommandFlagTypeDataItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SET_K8S_COMMAND_FLAG_TYPE_DATA_ITEM_VALUES!r}"
    )
