from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsFullJitterBackoffStrategy")


@_attrs_define
class AwsFullJitterBackoffStrategy:
    """Backoff strategy that uses a full jitter strategy for computing the next backoff delay.

    Attributes:
        base_delay (int | Unset):
        max_backoff_time (int | Unset):
        retry_count (int | Unset):
    """

    base_delay: int | Unset = UNSET
    max_backoff_time: int | Unset = UNSET
    retry_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_delay = self.base_delay

        max_backoff_time = self.max_backoff_time

        retry_count = self.retry_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_delay is not UNSET:
            field_dict["baseDelay"] = base_delay
        if max_backoff_time is not UNSET:
            field_dict["maxBackoffTime"] = max_backoff_time
        if retry_count is not UNSET:
            field_dict["retryCount"] = retry_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_delay = d.pop("baseDelay", UNSET)

        max_backoff_time = d.pop("maxBackoffTime", UNSET)

        retry_count = d.pop("retryCount", UNSET)

        aws_full_jitter_backoff_strategy = cls(
            base_delay=base_delay,
            max_backoff_time=max_backoff_time,
            retry_count=retry_count,
        )

        aws_full_jitter_backoff_strategy.additional_properties = d
        return aws_full_jitter_backoff_strategy

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
