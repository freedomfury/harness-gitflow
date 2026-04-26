from typing import Literal, cast

ParsedPayloadOrBuilderPayloadCase = Literal["BRANCH", "PAYLOAD_NOT_SET", "PR", "PUSH", "RELEASE", "TAG"]

PARSED_PAYLOAD_OR_BUILDER_PAYLOAD_CASE_VALUES: set[ParsedPayloadOrBuilderPayloadCase] = {
    "BRANCH",
    "PAYLOAD_NOT_SET",
    "PR",
    "PUSH",
    "RELEASE",
    "TAG",
}


def check_parsed_payload_or_builder_payload_case(value: str) -> ParsedPayloadOrBuilderPayloadCase:
    if value in PARSED_PAYLOAD_OR_BUILDER_PAYLOAD_CASE_VALUES:
        return cast(ParsedPayloadOrBuilderPayloadCase, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PARSED_PAYLOAD_OR_BUILDER_PAYLOAD_CASE_VALUES!r}")
