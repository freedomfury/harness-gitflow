from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.version_override_response_dto import VersionOverrideResponseDTO


T = TypeVar("T", bound="VersionOverridesResponse")


@_attrs_define
class VersionOverridesResponse:
    """
    Attributes:
        version_overrides (list[VersionOverrideResponseDTO] | Unset):
    """

    version_overrides: list[VersionOverrideResponseDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version_overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.version_overrides, Unset):
            version_overrides = []
            for version_overrides_item_data in self.version_overrides:
                version_overrides_item = version_overrides_item_data.to_dict()
                version_overrides.append(version_overrides_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version_overrides is not UNSET:
            field_dict["versionOverrides"] = version_overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.version_override_response_dto import VersionOverrideResponseDTO

        d = dict(src_dict)
        _version_overrides = d.pop("versionOverrides", UNSET)
        version_overrides: list[VersionOverrideResponseDTO] | Unset = UNSET
        if _version_overrides is not UNSET:
            version_overrides = []
            for version_overrides_item_data in _version_overrides:
                version_overrides_item = VersionOverrideResponseDTO.from_dict(version_overrides_item_data)

                version_overrides.append(version_overrides_item)

        version_overrides_response = cls(
            version_overrides=version_overrides,
        )

        version_overrides_response.additional_properties = d
        return version_overrides_response

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
