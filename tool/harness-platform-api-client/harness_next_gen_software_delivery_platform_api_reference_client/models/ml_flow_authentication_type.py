from typing import Literal, cast

MLFlowAuthenticationType = Literal["Anonymous"]

ML_FLOW_AUTHENTICATION_TYPE_VALUES: set[MLFlowAuthenticationType] = {
    "Anonymous",
}


def check_ml_flow_authentication_type(value: str) -> MLFlowAuthenticationType:
    if value in ML_FLOW_AUTHENTICATION_TYPE_VALUES:
        return cast(MLFlowAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ML_FLOW_AUTHENTICATION_TYPE_VALUES!r}")
