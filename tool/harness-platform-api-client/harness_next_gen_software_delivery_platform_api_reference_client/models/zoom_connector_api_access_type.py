from typing import Literal, cast

ZoomConnectorApiAccessType = Literal["OAUTH", "TOKEN"]

ZOOM_CONNECTOR_API_ACCESS_TYPE_VALUES: set[ZoomConnectorApiAccessType] = {
    "OAUTH",
    "TOKEN",
}


def check_zoom_connector_api_access_type(value: str) -> ZoomConnectorApiAccessType:
    if value in ZOOM_CONNECTOR_API_ACCESS_TYPE_VALUES:
        return cast(ZoomConnectorApiAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ZOOM_CONNECTOR_API_ACCESS_TYPE_VALUES!r}")
