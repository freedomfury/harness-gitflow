from typing import Literal, cast

HarnessConnectorType = Literal["Account", "Repo"]

HARNESS_CONNECTOR_TYPE_VALUES: set[HarnessConnectorType] = {
    "Account",
    "Repo",
}


def check_harness_connector_type(value: str) -> HarnessConnectorType:
    if value in HARNESS_CONNECTOR_TYPE_VALUES:
        return cast(HarnessConnectorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HARNESS_CONNECTOR_TYPE_VALUES!r}")
