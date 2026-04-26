from typing import Literal, cast

FeatureSetOrBuilderMessageEncoding = Literal["DELIMITED", "LENGTH_PREFIXED", "MESSAGE_ENCODING_UNKNOWN"]

FEATURE_SET_OR_BUILDER_MESSAGE_ENCODING_VALUES: set[FeatureSetOrBuilderMessageEncoding] = {
    "DELIMITED",
    "LENGTH_PREFIXED",
    "MESSAGE_ENCODING_UNKNOWN",
}


def check_feature_set_or_builder_message_encoding(value: str) -> FeatureSetOrBuilderMessageEncoding:
    if value in FEATURE_SET_OR_BUILDER_MESSAGE_ENCODING_VALUES:
        return cast(FeatureSetOrBuilderMessageEncoding, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_OR_BUILDER_MESSAGE_ENCODING_VALUES!r}")
