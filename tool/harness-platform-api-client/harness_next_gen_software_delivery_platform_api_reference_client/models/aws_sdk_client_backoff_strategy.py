from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aws_sdk_client_backoff_strategy_type import (
    AwsSdkClientBackoffStrategyType,
    check_aws_sdk_client_backoff_strategy_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_sdk_client_back_off_strategy_spec import AwsSdkClientBackOffStrategySpec


T = TypeVar("T", bound="AwsSdkClientBackoffStrategy")


@_attrs_define
class AwsSdkClientBackoffStrategy:
    """This contains details of the AWS SDK Client Backoff Strategy

    Attributes:
        type_ (AwsSdkClientBackoffStrategyType):
        spec (AwsSdkClientBackOffStrategySpec | Unset): This contains AWS Sdk Client BackOff strategy spec
    """

    type_: AwsSdkClientBackoffStrategyType
    spec: AwsSdkClientBackOffStrategySpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_sdk_client_back_off_strategy_spec import AwsSdkClientBackOffStrategySpec

        d = dict(src_dict)
        type_ = check_aws_sdk_client_backoff_strategy_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: AwsSdkClientBackOffStrategySpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = AwsSdkClientBackOffStrategySpec.from_dict(_spec)

        aws_sdk_client_backoff_strategy = cls(
            type_=type_,
            spec=spec,
        )

        aws_sdk_client_backoff_strategy.additional_properties = d
        return aws_sdk_client_backoff_strategy

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
