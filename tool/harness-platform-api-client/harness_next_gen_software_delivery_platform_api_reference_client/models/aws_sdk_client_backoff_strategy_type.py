from typing import Literal, cast

AwsSdkClientBackoffStrategyType = Literal[
    "EqualJitterBackoffStrategy", "FixedDelayBackoffStrategy", "FullJitterBackoffStrategy"
]

AWS_SDK_CLIENT_BACKOFF_STRATEGY_TYPE_VALUES: set[AwsSdkClientBackoffStrategyType] = {
    "EqualJitterBackoffStrategy",
    "FixedDelayBackoffStrategy",
    "FullJitterBackoffStrategy",
}


def check_aws_sdk_client_backoff_strategy_type(value: str) -> AwsSdkClientBackoffStrategyType:
    if value in AWS_SDK_CLIENT_BACKOFF_STRATEGY_TYPE_VALUES:
        return cast(AwsSdkClientBackoffStrategyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AWS_SDK_CLIENT_BACKOFF_STRATEGY_TYPE_VALUES!r}")
