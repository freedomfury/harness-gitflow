from typing import Literal, cast

DelegateSetupDetailsSize = Literal["CCM_SMALL", "LAPTOP", "LARGE", "MEDIUM", "SMALL"]

DELEGATE_SETUP_DETAILS_SIZE_VALUES: set[DelegateSetupDetailsSize] = {
    "CCM_SMALL",
    "LAPTOP",
    "LARGE",
    "MEDIUM",
    "SMALL",
}


def check_delegate_setup_details_size(value: str) -> DelegateSetupDetailsSize:
    if value in DELEGATE_SETUP_DETAILS_SIZE_VALUES:
        return cast(DelegateSetupDetailsSize, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELEGATE_SETUP_DETAILS_SIZE_VALUES!r}")
