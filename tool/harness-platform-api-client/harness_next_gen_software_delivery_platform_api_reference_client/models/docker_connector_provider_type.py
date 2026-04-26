from typing import Literal, cast

DockerConnectorProviderType = Literal["DockerHub", "Harbor", "Other", "Quay"]

DOCKER_CONNECTOR_PROVIDER_TYPE_VALUES: set[DockerConnectorProviderType] = {
    "DockerHub",
    "Harbor",
    "Other",
    "Quay",
}


def check_docker_connector_provider_type(value: str) -> DockerConnectorProviderType:
    if value in DOCKER_CONNECTOR_PROVIDER_TYPE_VALUES:
        return cast(DockerConnectorProviderType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCKER_CONNECTOR_PROVIDER_TYPE_VALUES!r}")
