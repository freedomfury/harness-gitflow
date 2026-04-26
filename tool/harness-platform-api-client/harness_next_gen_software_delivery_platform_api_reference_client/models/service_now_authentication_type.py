from typing import Literal, cast

ServiceNowAuthenticationType = Literal[
    "AdfsClientCredentialsWithCertificate", "RefreshTokenGrantType", "UsernamePassword"
]

SERVICE_NOW_AUTHENTICATION_TYPE_VALUES: set[ServiceNowAuthenticationType] = {
    "AdfsClientCredentialsWithCertificate",
    "RefreshTokenGrantType",
    "UsernamePassword",
}


def check_service_now_authentication_type(value: str) -> ServiceNowAuthenticationType:
    if value in SERVICE_NOW_AUTHENTICATION_TYPE_VALUES:
        return cast(ServiceNowAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_NOW_AUTHENTICATION_TYPE_VALUES!r}")
