from typing import Literal, cast

CreateConnectorStoreType = Literal["INLINE", "INLINE_HC", "REMOTE"]

CREATE_CONNECTOR_STORE_TYPE_VALUES: set[CreateConnectorStoreType] = {
    "INLINE",
    "INLINE_HC",
    "REMOTE",
}


def check_create_connector_store_type(value: str) -> CreateConnectorStoreType:
    if value in CREATE_CONNECTOR_STORE_TYPE_VALUES:
        return cast(CreateConnectorStoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_CONNECTOR_STORE_TYPE_VALUES!r}")
