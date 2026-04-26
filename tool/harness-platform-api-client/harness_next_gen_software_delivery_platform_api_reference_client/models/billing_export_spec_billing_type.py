from typing import Literal, cast

BillingExportSpecBillingType = Literal["ACTUAL", "AMORTIZED"]

BILLING_EXPORT_SPEC_BILLING_TYPE_VALUES: set[BillingExportSpecBillingType] = {
    "ACTUAL",
    "AMORTIZED",
}


def check_billing_export_spec_billing_type(value: str) -> BillingExportSpecBillingType:
    if value in BILLING_EXPORT_SPEC_BILLING_TYPE_VALUES:
        return cast(BillingExportSpecBillingType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLING_EXPORT_SPEC_BILLING_TYPE_VALUES!r}")
