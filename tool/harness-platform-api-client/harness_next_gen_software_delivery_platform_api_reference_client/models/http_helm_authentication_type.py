from typing import Literal, cast

HttpHelmAuthenticationType = Literal["Anonymous", "UsernamePassword"]

HTTP_HELM_AUTHENTICATION_TYPE_VALUES: set[HttpHelmAuthenticationType] = {
    "Anonymous",
    "UsernamePassword",
}


def check_http_helm_authentication_type(value: str) -> HttpHelmAuthenticationType:
    if value in HTTP_HELM_AUTHENTICATION_TYPE_VALUES:
        return cast(HttpHelmAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HTTP_HELM_AUTHENTICATION_TYPE_VALUES!r}")
