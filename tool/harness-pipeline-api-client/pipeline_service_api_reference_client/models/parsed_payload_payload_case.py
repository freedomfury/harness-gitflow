from typing import Literal, cast

ParsedPayloadPayloadCase = Literal["BRANCH", "PAYLOAD_NOT_SET", "PR", "PUSH", "RELEASE", "TAG"]

PARSED_PAYLOAD_PAYLOAD_CASE_VALUES: set[ParsedPayloadPayloadCase] = {
    "BRANCH",
    "PAYLOAD_NOT_SET",
    "PR",
    "PUSH",
    "RELEASE",
    "TAG",
}


def check_parsed_payload_payload_case(value: str) -> ParsedPayloadPayloadCase:
    if value in PARSED_PAYLOAD_PAYLOAD_CASE_VALUES:
        return cast(ParsedPayloadPayloadCase, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PARSED_PAYLOAD_PAYLOAD_CASE_VALUES!r}")
