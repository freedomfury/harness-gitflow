from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.store_config_wrapper_type import StoreConfigWrapperType, check_store_config_wrapper_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.store_config import StoreConfig


T = TypeVar("T", bound="StoreConfigWrapper")


@_attrs_define
class StoreConfigWrapper:
    """
    Attributes:
        spec (StoreConfig):
        type_ (StoreConfigWrapperType):
        metadata (str | Unset):
        field_uuid (str | Unset):
    """

    spec: StoreConfig
    type_: StoreConfigWrapperType
    metadata: str | Unset = UNSET
    field_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spec = self.spec.to_dict()

        type_: str = self.type_

        metadata = self.metadata

        field_uuid = self.field_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spec": spec,
                "type": type_,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if field_uuid is not UNSET:
            field_dict["__uuid"] = field_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.store_config import StoreConfig

        d = dict(src_dict)
        spec = StoreConfig.from_dict(d.pop("spec"))

        type_ = check_store_config_wrapper_type(d.pop("type"))

        metadata = d.pop("metadata", UNSET)

        field_uuid = d.pop("__uuid", UNSET)

        store_config_wrapper = cls(
            spec=spec,
            type_=type_,
            metadata=metadata,
            field_uuid=field_uuid,
        )

        store_config_wrapper.additional_properties = d
        return store_config_wrapper

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
