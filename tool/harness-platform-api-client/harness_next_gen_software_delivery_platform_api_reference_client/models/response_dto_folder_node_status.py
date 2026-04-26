from typing import Literal, cast

ResponseDTOFolderNodeStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_FOLDER_NODE_STATUS_VALUES: set[ResponseDTOFolderNodeStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_folder_node_status(value: str) -> ResponseDTOFolderNodeStatus:
    if value in RESPONSE_DTO_FOLDER_NODE_STATUS_VALUES:
        return cast(ResponseDTOFolderNodeStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_FOLDER_NODE_STATUS_VALUES!r}")
