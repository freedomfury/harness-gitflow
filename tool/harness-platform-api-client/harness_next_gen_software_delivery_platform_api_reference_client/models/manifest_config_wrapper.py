from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.manifest_config import ManifestConfig


T = TypeVar("T", bound="ManifestConfigWrapper")


@_attrs_define
class ManifestConfigWrapper:
    """
    Attributes:
        manifest (ManifestConfig | Unset):
        field_uuid (str | Unset):
        metadata (str | Unset):
    """

    manifest: ManifestConfig | Unset = UNSET
    field_uuid: str | Unset = UNSET
    metadata: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manifest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manifest, Unset):
            manifest = self.manifest.to_dict()

        field_uuid = self.field_uuid

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if field_uuid is not UNSET:
            field_dict["__uuid"] = field_uuid
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.manifest_config import ManifestConfig

        d = dict(src_dict)
        _manifest = d.pop("manifest", UNSET)
        manifest: ManifestConfig | Unset
        if isinstance(_manifest, Unset):
            manifest = UNSET
        else:
            manifest = ManifestConfig.from_dict(_manifest)

        field_uuid = d.pop("__uuid", UNSET)

        metadata = d.pop("metadata", UNSET)

        manifest_config_wrapper = cls(
            manifest=manifest,
            field_uuid=field_uuid,
            metadata=metadata,
        )

        manifest_config_wrapper.additional_properties = d
        return manifest_config_wrapper

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
