from typing import Literal, cast

ResponseDTOSetServiceHookActionDataItem = Literal["FetchFiles", "SteadyStateCheck", "TemplateManifest"]

RESPONSE_DTO_SET_SERVICE_HOOK_ACTION_DATA_ITEM_VALUES: set[ResponseDTOSetServiceHookActionDataItem] = {
    "FetchFiles",
    "SteadyStateCheck",
    "TemplateManifest",
}


def check_response_dto_set_service_hook_action_data_item(value: str) -> ResponseDTOSetServiceHookActionDataItem:
    if value in RESPONSE_DTO_SET_SERVICE_HOOK_ACTION_DATA_ITEM_VALUES:
        return cast(ResponseDTOSetServiceHookActionDataItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SET_SERVICE_HOOK_ACTION_DATA_ITEM_VALUES!r}"
    )
