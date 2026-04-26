from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_sdk_back_off_strategy_spec import AwsSdkBackOffStrategySpec


T = TypeVar("T", bound="AwsSdkRetryPolicySpec")


@_attrs_define
class AwsSdkRetryPolicySpec:
    """Retry policy for aws sdk calls

    Attributes:
        back_off_strategy_type (str | Unset):
        back_off_strategy (AwsSdkBackOffStrategySpec | Unset): This contains AWS Sdk BackOff strategy spec
    """

    back_off_strategy_type: str | Unset = UNSET
    back_off_strategy: AwsSdkBackOffStrategySpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        back_off_strategy_type = self.back_off_strategy_type

        back_off_strategy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.back_off_strategy, Unset):
            back_off_strategy = self.back_off_strategy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if back_off_strategy_type is not UNSET:
            field_dict["backOffStrategyType"] = back_off_strategy_type
        if back_off_strategy is not UNSET:
            field_dict["backOffStrategy"] = back_off_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_sdk_back_off_strategy_spec import AwsSdkBackOffStrategySpec

        d = dict(src_dict)
        back_off_strategy_type = d.pop("backOffStrategyType", UNSET)

        _back_off_strategy = d.pop("backOffStrategy", UNSET)
        back_off_strategy: AwsSdkBackOffStrategySpec | Unset
        if isinstance(_back_off_strategy, Unset):
            back_off_strategy = UNSET
        else:
            back_off_strategy = AwsSdkBackOffStrategySpec.from_dict(_back_off_strategy)

        aws_sdk_retry_policy_spec = cls(
            back_off_strategy_type=back_off_strategy_type,
            back_off_strategy=back_off_strategy,
        )

        aws_sdk_retry_policy_spec.additional_properties = d
        return aws_sdk_retry_policy_spec

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
