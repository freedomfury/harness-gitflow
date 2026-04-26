from typing import Literal, cast

AppDynamicsConnectorDTOAuthType = Literal["ApiClientToken", "UsernamePassword"]

APP_DYNAMICS_CONNECTOR_DTO_AUTH_TYPE_VALUES: set[AppDynamicsConnectorDTOAuthType] = {
    "ApiClientToken",
    "UsernamePassword",
}


def check_app_dynamics_connector_dto_auth_type(value: str) -> AppDynamicsConnectorDTOAuthType:
    if value in APP_DYNAMICS_CONNECTOR_DTO_AUTH_TYPE_VALUES:
        return cast(AppDynamicsConnectorDTOAuthType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APP_DYNAMICS_CONNECTOR_DTO_AUTH_TYPE_VALUES!r}")
