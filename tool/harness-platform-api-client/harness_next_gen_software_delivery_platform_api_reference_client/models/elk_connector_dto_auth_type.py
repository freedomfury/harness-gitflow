from typing import Literal, cast

ELKConnectorDTOAuthType = Literal["ApiClientToken", "Bearer Token(HTTP Header)", "None", "UsernamePassword"]

ELK_CONNECTOR_DTO_AUTH_TYPE_VALUES: set[ELKConnectorDTOAuthType] = {
    "ApiClientToken",
    "Bearer Token(HTTP Header)",
    "None",
    "UsernamePassword",
}


def check_elk_connector_dto_auth_type(value: str) -> ELKConnectorDTOAuthType:
    if value in ELK_CONNECTOR_DTO_AUTH_TYPE_VALUES:
        return cast(ELKConnectorDTOAuthType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ELK_CONNECTOR_DTO_AUTH_TYPE_VALUES!r}")
