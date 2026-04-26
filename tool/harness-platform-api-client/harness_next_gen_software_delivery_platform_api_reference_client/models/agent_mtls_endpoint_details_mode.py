from typing import Literal, cast

AgentMtlsEndpointDetailsMode = Literal["LOOSE", "STRICT"]

AGENT_MTLS_ENDPOINT_DETAILS_MODE_VALUES: set[AgentMtlsEndpointDetailsMode] = {
    "LOOSE",
    "STRICT",
}


def check_agent_mtls_endpoint_details_mode(value: str) -> AgentMtlsEndpointDetailsMode:
    if value in AGENT_MTLS_ENDPOINT_DETAILS_MODE_VALUES:
        return cast(AgentMtlsEndpointDetailsMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_MTLS_ENDPOINT_DETAILS_MODE_VALUES!r}")
