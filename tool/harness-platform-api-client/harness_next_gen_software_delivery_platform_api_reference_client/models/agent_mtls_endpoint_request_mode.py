from typing import Literal, cast

AgentMtlsEndpointRequestMode = Literal["LOOSE", "STRICT"]

AGENT_MTLS_ENDPOINT_REQUEST_MODE_VALUES: set[AgentMtlsEndpointRequestMode] = {
    "LOOSE",
    "STRICT",
}


def check_agent_mtls_endpoint_request_mode(value: str) -> AgentMtlsEndpointRequestMode:
    if value in AGENT_MTLS_ENDPOINT_REQUEST_MODE_VALUES:
        return cast(AgentMtlsEndpointRequestMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_MTLS_ENDPOINT_REQUEST_MODE_VALUES!r}")
