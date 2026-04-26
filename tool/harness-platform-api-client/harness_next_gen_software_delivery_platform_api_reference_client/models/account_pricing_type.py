from typing import Literal, cast

AccountPricingType = Literal["CLASSIC", "FLEX"]

ACCOUNT_PRICING_TYPE_VALUES: set[AccountPricingType] = {
    "CLASSIC",
    "FLEX",
}


def check_account_pricing_type(value: str) -> AccountPricingType:
    if value in ACCOUNT_PRICING_TYPE_VALUES:
        return cast(AccountPricingType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_PRICING_TYPE_VALUES!r}")
