from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityReferredByInfraSetupUsageDetail")


@_attrs_define
class EntityReferredByInfraSetupUsageDetail:
    """
    Attributes:
        type_ (str):
        environment_identifier (str | Unset):
        environment_name (str | Unset):
    """

    type_: str
    environment_identifier: str | Unset = UNSET
    environment_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        environment_identifier = self.environment_identifier

        environment_name = self.environment_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if environment_identifier is not UNSET:
            field_dict["environmentIdentifier"] = environment_identifier
        if environment_name is not UNSET:
            field_dict["environmentName"] = environment_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        environment_identifier = d.pop("environmentIdentifier", UNSET)

        environment_name = d.pop("environmentName", UNSET)

        entity_referred_by_infra_setup_usage_detail = cls(
            type_=type_,
            environment_identifier=environment_identifier,
            environment_name=environment_name,
        )

        entity_referred_by_infra_setup_usage_detail.additional_properties = d
        return entity_referred_by_infra_setup_usage_detail

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
