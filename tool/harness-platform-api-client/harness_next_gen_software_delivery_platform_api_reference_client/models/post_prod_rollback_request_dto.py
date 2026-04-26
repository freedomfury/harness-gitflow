from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostProdRollbackRequestDTO")


@_attrs_define
class PostProdRollbackRequestDTO:
    """
    Attributes:
        instance_key (str):
        infrastructure_mapping_id (str):
    """

    instance_key: str
    infrastructure_mapping_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_key = self.instance_key

        infrastructure_mapping_id = self.infrastructure_mapping_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceKey": instance_key,
                "infrastructureMappingId": infrastructure_mapping_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_key = d.pop("instanceKey")

        infrastructure_mapping_id = d.pop("infrastructureMappingId")

        post_prod_rollback_request_dto = cls(
            instance_key=instance_key,
            infrastructure_mapping_id=infrastructure_mapping_id,
        )

        post_prod_rollback_request_dto.additional_properties = d
        return post_prod_rollback_request_dto

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
