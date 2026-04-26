from typing import Literal, cast

SecretTextSpecValueType = Literal["CustomSecretManagerValues", "Inline", "Reference"]

SECRET_TEXT_SPEC_VALUE_TYPE_VALUES: set[SecretTextSpecValueType] = {
    "CustomSecretManagerValues",
    "Inline",
    "Reference",
}


def check_secret_text_spec_value_type(value: str) -> SecretTextSpecValueType:
    if value in SECRET_TEXT_SPEC_VALUE_TYPE_VALUES:
        return cast(SecretTextSpecValueType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_TEXT_SPEC_VALUE_TYPE_VALUES!r}")
