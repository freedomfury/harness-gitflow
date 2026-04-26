from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_file_attributes import ConfigFileAttributes


T = TypeVar("T", bound="ConfigFile")


@_attrs_define
class ConfigFile:
    """
    Attributes:
        identifier (str):
        spec (ConfigFileAttributes):
        metadata (str | Unset):
        field_uuid (str | Unset):
    """

    identifier: str
    spec: ConfigFileAttributes
    metadata: str | Unset = UNSET
    field_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        spec = self.spec.to_dict()

        metadata = self.metadata

        field_uuid = self.field_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "spec": spec,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if field_uuid is not UNSET:
            field_dict["__uuid"] = field_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_file_attributes import ConfigFileAttributes

        d = dict(src_dict)
        identifier = d.pop("identifier")

        spec = ConfigFileAttributes.from_dict(d.pop("spec"))

        metadata = d.pop("metadata", UNSET)

        field_uuid = d.pop("__uuid", UNSET)

        config_file = cls(
            identifier=identifier,
            spec=spec,
            metadata=metadata,
            field_uuid=field_uuid,
        )

        config_file.additional_properties = d
        return config_file

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
