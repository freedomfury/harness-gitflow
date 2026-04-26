from typing import Literal, cast

FeatureSetMessageEncoding = Literal["DELIMITED", "LENGTH_PREFIXED", "MESSAGE_ENCODING_UNKNOWN"]

FEATURE_SET_MESSAGE_ENCODING_VALUES: set[FeatureSetMessageEncoding] = {
    "DELIMITED",
    "LENGTH_PREFIXED",
    "MESSAGE_ENCODING_UNKNOWN",
}


def check_feature_set_message_encoding(value: str) -> FeatureSetMessageEncoding:
    if value in FEATURE_SET_MESSAGE_ENCODING_VALUES:
        return cast(FeatureSetMessageEncoding, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_MESSAGE_ENCODING_VALUES!r}")
