from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CDModulePropertiesDTO")


@_attrs_define
class CDModulePropertiesDTO:
    """
    Attributes:
        artifact_display_names (list[str] | Unset):
        env_identifiers (list[str] | Unset):
        service_identifiers (list[str] | Unset):
        service_definition_types (list[str] | Unset):
        helm_chart_versions (list[str] | Unset):
        git_ops_app_identifiers (list[str] | Unset):
    """

    artifact_display_names: list[str] | Unset = UNSET
    env_identifiers: list[str] | Unset = UNSET
    service_identifiers: list[str] | Unset = UNSET
    service_definition_types: list[str] | Unset = UNSET
    helm_chart_versions: list[str] | Unset = UNSET
    git_ops_app_identifiers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifact_display_names: list[str] | Unset = UNSET
        if not isinstance(self.artifact_display_names, Unset):
            artifact_display_names = self.artifact_display_names

        env_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.env_identifiers, Unset):
            env_identifiers = self.env_identifiers

        service_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.service_identifiers, Unset):
            service_identifiers = self.service_identifiers

        service_definition_types: list[str] | Unset = UNSET
        if not isinstance(self.service_definition_types, Unset):
            service_definition_types = self.service_definition_types

        helm_chart_versions: list[str] | Unset = UNSET
        if not isinstance(self.helm_chart_versions, Unset):
            helm_chart_versions = self.helm_chart_versions

        git_ops_app_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.git_ops_app_identifiers, Unset):
            git_ops_app_identifiers = self.git_ops_app_identifiers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifact_display_names is not UNSET:
            field_dict["artifactDisplayNames"] = artifact_display_names
        if env_identifiers is not UNSET:
            field_dict["envIdentifiers"] = env_identifiers
        if service_identifiers is not UNSET:
            field_dict["serviceIdentifiers"] = service_identifiers
        if service_definition_types is not UNSET:
            field_dict["serviceDefinitionTypes"] = service_definition_types
        if helm_chart_versions is not UNSET:
            field_dict["helmChartVersions"] = helm_chart_versions
        if git_ops_app_identifiers is not UNSET:
            field_dict["gitOpsAppIdentifiers"] = git_ops_app_identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        artifact_display_names = cast(list[str], d.pop("artifactDisplayNames", UNSET))

        env_identifiers = cast(list[str], d.pop("envIdentifiers", UNSET))

        service_identifiers = cast(list[str], d.pop("serviceIdentifiers", UNSET))

        service_definition_types = cast(list[str], d.pop("serviceDefinitionTypes", UNSET))

        helm_chart_versions = cast(list[str], d.pop("helmChartVersions", UNSET))

        git_ops_app_identifiers = cast(list[str], d.pop("gitOpsAppIdentifiers", UNSET))

        cd_module_properties_dto = cls(
            artifact_display_names=artifact_display_names,
            env_identifiers=env_identifiers,
            service_identifiers=service_identifiers,
            service_definition_types=service_definition_types,
            helm_chart_versions=helm_chart_versions,
            git_ops_app_identifiers=git_ops_app_identifiers,
        )

        cd_module_properties_dto.additional_properties = d
        return cd_module_properties_dto

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
