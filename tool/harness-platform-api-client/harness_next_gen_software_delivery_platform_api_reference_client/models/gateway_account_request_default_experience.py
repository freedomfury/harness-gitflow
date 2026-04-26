from typing import Literal, cast

GatewayAccountRequestDefaultExperience = Literal["CG", "NG"]

GATEWAY_ACCOUNT_REQUEST_DEFAULT_EXPERIENCE_VALUES: set[GatewayAccountRequestDefaultExperience] = {
    "CG",
    "NG",
}


def check_gateway_account_request_default_experience(value: str) -> GatewayAccountRequestDefaultExperience:
    if value in GATEWAY_ACCOUNT_REQUEST_DEFAULT_EXPERIENCE_VALUES:
        return cast(GatewayAccountRequestDefaultExperience, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GATEWAY_ACCOUNT_REQUEST_DEFAULT_EXPERIENCE_VALUES!r}"
    )
