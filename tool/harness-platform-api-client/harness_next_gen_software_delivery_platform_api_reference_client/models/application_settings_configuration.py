from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.store_config_wrapper import StoreConfigWrapper


T = TypeVar("T", bound="ApplicationSettingsConfiguration")


@_attrs_define
class ApplicationSettingsConfiguration:
    """
    Attributes:
        store (StoreConfigWrapper):
        metadata (str | Unset):
    """

    store: StoreConfigWrapper
    metadata: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        store = self.store.to_dict()

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "store": store,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.store_config_wrapper import StoreConfigWrapper

        d = dict(src_dict)
        store = StoreConfigWrapper.from_dict(d.pop("store"))

        metadata = d.pop("metadata", UNSET)

        application_settings_configuration = cls(
            store=store,
            metadata=metadata,
        )

        application_settings_configuration.additional_properties = d
        return application_settings_configuration

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
