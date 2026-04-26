from typing import Literal, cast

KeyRevocationReason = Literal["COMPROMISED", "RETIRED", "SUPERSEDED", "UNKNOWN"]

KEY_REVOCATION_REASON_VALUES: set[KeyRevocationReason] = {
    "COMPROMISED",
    "RETIRED",
    "SUPERSEDED",
    "UNKNOWN",
}


def check_key_revocation_reason(value: str) -> KeyRevocationReason:
    if value in KEY_REVOCATION_REASON_VALUES:
        return cast(KeyRevocationReason, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {KEY_REVOCATION_REASON_VALUES!r}")
