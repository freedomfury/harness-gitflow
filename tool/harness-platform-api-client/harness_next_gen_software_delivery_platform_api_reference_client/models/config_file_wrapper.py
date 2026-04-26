from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_file import ConfigFile


T = TypeVar("T", bound="ConfigFileWrapper")


@_attrs_define
class ConfigFileWrapper:
    """
    Attributes:
        field_uuid (str | Unset):
        config_file (ConfigFile | Unset):
        metadata (str | Unset):
    """

    field_uuid: str | Unset = UNSET
    config_file: ConfigFile | Unset = UNSET
    metadata: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_uuid = self.field_uuid

        config_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config_file, Unset):
            config_file = self.config_file.to_dict()

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_uuid is not UNSET:
            field_dict["__uuid"] = field_uuid
        if config_file is not UNSET:
            field_dict["configFile"] = config_file
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_file import ConfigFile

        d = dict(src_dict)
        field_uuid = d.pop("__uuid", UNSET)

        _config_file = d.pop("configFile", UNSET)
        config_file: ConfigFile | Unset
        if isinstance(_config_file, Unset):
            config_file = UNSET
        else:
            config_file = ConfigFile.from_dict(_config_file)

        metadata = d.pop("metadata", UNSET)

        config_file_wrapper = cls(
            field_uuid=field_uuid,
            config_file=config_file,
            metadata=metadata,
        )

        config_file_wrapper.additional_properties = d
        return config_file_wrapper

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
