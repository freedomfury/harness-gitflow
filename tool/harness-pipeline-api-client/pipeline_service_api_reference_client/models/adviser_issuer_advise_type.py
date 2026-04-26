from typing import Literal, cast

AdviserIssuerAdviseType = Literal[
    "END_PLAN",
    "IGNORE_FAILURE",
    "INTERVENTION_WAIT",
    "MARK_AS_FAILURE",
    "MARK_SUCCESS",
    "NEXT_STEP",
    "PROCEED_WITH_DEFAULT",
    "RETRY",
    "UNKNOWN",
    "UNRECOGNIZED",
]

ADVISER_ISSUER_ADVISE_TYPE_VALUES: set[AdviserIssuerAdviseType] = {
    "END_PLAN",
    "IGNORE_FAILURE",
    "INTERVENTION_WAIT",
    "MARK_AS_FAILURE",
    "MARK_SUCCESS",
    "NEXT_STEP",
    "PROCEED_WITH_DEFAULT",
    "RETRY",
    "UNKNOWN",
    "UNRECOGNIZED",
}


def check_adviser_issuer_advise_type(value: str) -> AdviserIssuerAdviseType:
    if value in ADVISER_ISSUER_ADVISE_TYPE_VALUES:
        return cast(AdviserIssuerAdviseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADVISER_ISSUER_ADVISE_TYPE_VALUES!r}")
