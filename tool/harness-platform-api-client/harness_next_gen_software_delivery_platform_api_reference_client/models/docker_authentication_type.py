from typing import Literal, cast

DockerAuthenticationType = Literal["Anonymous", "UsernamePassword"]

DOCKER_AUTHENTICATION_TYPE_VALUES: set[DockerAuthenticationType] = {
    "Anonymous",
    "UsernamePassword",
}


def check_docker_authentication_type(value: str) -> DockerAuthenticationType:
    if value in DOCKER_AUTHENTICATION_TYPE_VALUES:
        return cast(DockerAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCKER_AUTHENTICATION_TYPE_VALUES!r}")
