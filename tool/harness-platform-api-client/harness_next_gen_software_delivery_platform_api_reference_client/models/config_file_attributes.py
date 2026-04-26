from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_field_store_config_wrapper import ParameterFieldStoreConfigWrapper


T = TypeVar("T", bound="ConfigFileAttributes")


@_attrs_define
class ConfigFileAttributes:
    """
    Attributes:
        store (ParameterFieldStoreConfigWrapper):
        field_uuid (str | Unset):
        metadata (str | Unset):
    """

    store: ParameterFieldStoreConfigWrapper
    field_uuid: str | Unset = UNSET
    metadata: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        store = self.store.to_dict()

        field_uuid = self.field_uuid

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "store": store,
            }
        )
        if field_uuid is not UNSET:
            field_dict["__uuid"] = field_uuid
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parameter_field_store_config_wrapper import ParameterFieldStoreConfigWrapper

        d = dict(src_dict)
        store = ParameterFieldStoreConfigWrapper.from_dict(d.pop("store"))

        field_uuid = d.pop("__uuid", UNSET)

        metadata = d.pop("metadata", UNSET)

        config_file_attributes = cls(
            store=store,
            field_uuid=field_uuid,
            metadata=metadata,
        )

        config_file_attributes.additional_properties = d
        return config_file_attributes

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
