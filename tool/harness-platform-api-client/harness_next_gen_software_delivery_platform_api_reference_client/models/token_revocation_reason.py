from typing import Literal, cast

TokenRevocationReason = Literal["COMPROMISED", "RETIRED", "SUPERSEDED", "UNKNOWN"]

TOKEN_REVOCATION_REASON_VALUES: set[TokenRevocationReason] = {
    "COMPROMISED",
    "RETIRED",
    "SUPERSEDED",
    "UNKNOWN",
}


def check_token_revocation_reason(value: str) -> TokenRevocationReason:
    if value in TOKEN_REVOCATION_REASON_VALUES:
        return cast(TokenRevocationReason, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TOKEN_REVOCATION_REASON_VALUES!r}")
