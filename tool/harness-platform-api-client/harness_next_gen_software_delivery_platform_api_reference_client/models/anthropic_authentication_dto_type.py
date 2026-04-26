from typing import Literal, cast

AnthropicAuthenticationDTOType = Literal["Token"]

ANTHROPIC_AUTHENTICATION_DTO_TYPE_VALUES: set[AnthropicAuthenticationDTOType] = {
    "Token",
}


def check_anthropic_authentication_dto_type(value: str) -> AnthropicAuthenticationDTOType:
    if value in ANTHROPIC_AUTHENTICATION_DTO_TYPE_VALUES:
        return cast(AnthropicAuthenticationDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ANTHROPIC_AUTHENTICATION_DTO_TYPE_VALUES!r}")
