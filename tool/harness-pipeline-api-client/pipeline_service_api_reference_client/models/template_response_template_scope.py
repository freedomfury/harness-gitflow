from typing import Literal, cast

TemplateResponseTemplateScope = Literal["account", "org", "project", "unknown"]

TEMPLATE_RESPONSE_TEMPLATE_SCOPE_VALUES: set[TemplateResponseTemplateScope] = {
    "account",
    "org",
    "project",
    "unknown",
}


def check_template_response_template_scope(value: str) -> TemplateResponseTemplateScope:
    if value in TEMPLATE_RESPONSE_TEMPLATE_SCOPE_VALUES:
        return cast(TemplateResponseTemplateScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEMPLATE_RESPONSE_TEMPLATE_SCOPE_VALUES!r}")
