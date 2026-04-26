from typing import Literal, cast

LoginTypeResponseDefaultExperience = Literal["CG", "NG"]

LOGIN_TYPE_RESPONSE_DEFAULT_EXPERIENCE_VALUES: set[LoginTypeResponseDefaultExperience] = {
    "CG",
    "NG",
}


def check_login_type_response_default_experience(value: str) -> LoginTypeResponseDefaultExperience:
    if value in LOGIN_TYPE_RESPONSE_DEFAULT_EXPERIENCE_VALUES:
        return cast(LoginTypeResponseDefaultExperience, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOGIN_TYPE_RESPONSE_DEFAULT_EXPERIENCE_VALUES!r}")
