from typing import Literal, cast

UpdatePublicKeyRequestRevocationReason = Literal["COMPROMISED", "RETIRED", "SUPERSEDED", "UNKNOWN"]

UPDATE_PUBLIC_KEY_REQUEST_REVOCATION_REASON_VALUES: set[UpdatePublicKeyRequestRevocationReason] = {
    "COMPROMISED",
    "RETIRED",
    "SUPERSEDED",
    "UNKNOWN",
}


def check_update_public_key_request_revocation_reason(value: str) -> UpdatePublicKeyRequestRevocationReason:
    if value in UPDATE_PUBLIC_KEY_REQUEST_REVOCATION_REASON_VALUES:
        return cast(UpdatePublicKeyRequestRevocationReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PUBLIC_KEY_REQUEST_REVOCATION_REASON_VALUES!r}"
    )
