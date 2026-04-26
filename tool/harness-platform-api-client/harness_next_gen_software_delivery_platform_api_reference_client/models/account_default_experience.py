from typing import Literal, cast

AccountDefaultExperience = Literal["CG", "NG"]

ACCOUNT_DEFAULT_EXPERIENCE_VALUES: set[AccountDefaultExperience] = {
    "CG",
    "NG",
}


def check_account_default_experience(value: str) -> AccountDefaultExperience:
    if value in ACCOUNT_DEFAULT_EXPERIENCE_VALUES:
        return cast(AccountDefaultExperience, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_DEFAULT_EXPERIENCE_VALUES!r}")
