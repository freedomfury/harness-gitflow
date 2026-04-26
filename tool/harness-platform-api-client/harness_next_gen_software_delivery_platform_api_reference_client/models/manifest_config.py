from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.manifest_config_type import ManifestConfigType, check_manifest_config_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.manifest_attributes import ManifestAttributes


T = TypeVar("T", bound="ManifestConfig")


@_attrs_define
class ManifestConfig:
    """
    Attributes:
        identifier (str):
        type_ (ManifestConfigType):
        spec (ManifestAttributes):
        metadata (str | Unset):
        field_uuid (str | Unset):
    """

    identifier: str
    type_: ManifestConfigType
    spec: ManifestAttributes
    metadata: str | Unset = UNSET
    field_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        type_: str = self.type_

        spec = self.spec.to_dict()

        metadata = self.metadata

        field_uuid = self.field_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "type": type_,
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
        from ..models.manifest_attributes import ManifestAttributes

        d = dict(src_dict)
        identifier = d.pop("identifier")

        type_ = check_manifest_config_type(d.pop("type"))

        spec = ManifestAttributes.from_dict(d.pop("spec"))

        metadata = d.pop("metadata", UNSET)

        field_uuid = d.pop("__uuid", UNSET)

        manifest_config = cls(
            identifier=identifier,
            type_=type_,
            spec=spec,
            metadata=metadata,
            field_uuid=field_uuid,
        )

        manifest_config.additional_properties = d
        return manifest_config

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
