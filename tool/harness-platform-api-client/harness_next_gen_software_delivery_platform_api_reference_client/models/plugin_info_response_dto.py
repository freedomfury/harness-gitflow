from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_item import ResourceItem


T = TypeVar("T", bound="PluginInfoResponseDto")


@_attrs_define
class PluginInfoResponseDto:
    """
    Attributes:
        runtime_language (list[ResourceItem] | Unset):
        serverless_version (list[ResourceItem] | Unset):
    """

    runtime_language: list[ResourceItem] | Unset = UNSET
    serverless_version: list[ResourceItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runtime_language: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.runtime_language, Unset):
            runtime_language = []
            for runtime_language_item_data in self.runtime_language:
                runtime_language_item = runtime_language_item_data.to_dict()
                runtime_language.append(runtime_language_item)

        serverless_version: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.serverless_version, Unset):
            serverless_version = []
            for serverless_version_item_data in self.serverless_version:
                serverless_version_item = serverless_version_item_data.to_dict()
                serverless_version.append(serverless_version_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if runtime_language is not UNSET:
            field_dict["runtimeLanguage"] = runtime_language
        if serverless_version is not UNSET:
            field_dict["serverlessVersion"] = serverless_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_item import ResourceItem

        d = dict(src_dict)
        _runtime_language = d.pop("runtimeLanguage", UNSET)
        runtime_language: list[ResourceItem] | Unset = UNSET
        if _runtime_language is not UNSET:
            runtime_language = []
            for runtime_language_item_data in _runtime_language:
                runtime_language_item = ResourceItem.from_dict(runtime_language_item_data)

                runtime_language.append(runtime_language_item)

        _serverless_version = d.pop("serverlessVersion", UNSET)
        serverless_version: list[ResourceItem] | Unset = UNSET
        if _serverless_version is not UNSET:
            serverless_version = []
            for serverless_version_item_data in _serverless_version:
                serverless_version_item = ResourceItem.from_dict(serverless_version_item_data)

                serverless_version.append(serverless_version_item)

        plugin_info_response_dto = cls(
            runtime_language=runtime_language,
            serverless_version=serverless_version,
        )

        plugin_info_response_dto.additional_properties = d
        return plugin_info_response_dto

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
