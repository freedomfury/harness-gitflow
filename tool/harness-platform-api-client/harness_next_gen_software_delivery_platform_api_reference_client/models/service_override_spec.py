from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_settings_configuration import ApplicationSettingsConfiguration
    from ..models.config_file_wrapper import ConfigFileWrapper
    from ..models.connection_strings_configuration import ConnectionStringsConfiguration
    from ..models.manifest_config_wrapper import ManifestConfigWrapper
    from ..models.ng_variable import NGVariable


T = TypeVar("T", bound="ServiceOverrideSpec")


@_attrs_define
class ServiceOverrideSpec:
    """This is the Service Override Spec entity defined in Harness

    Attributes:
        variables (list[NGVariable] | Unset):
        manifests (list[ManifestConfigWrapper] | Unset):
        config_files (list[ConfigFileWrapper] | Unset):
        application_settings (ApplicationSettingsConfiguration | Unset):
        connection_strings (ConnectionStringsConfiguration | Unset):
        cli_environment_variables (list[NGVariable] | Unset):
        metadata (str | Unset):
    """

    variables: list[NGVariable] | Unset = UNSET
    manifests: list[ManifestConfigWrapper] | Unset = UNSET
    config_files: list[ConfigFileWrapper] | Unset = UNSET
    application_settings: ApplicationSettingsConfiguration | Unset = UNSET
    connection_strings: ConnectionStringsConfiguration | Unset = UNSET
    cli_environment_variables: list[NGVariable] | Unset = UNSET
    metadata: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        manifests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.manifests, Unset):
            manifests = []
            for manifests_item_data in self.manifests:
                manifests_item = manifests_item_data.to_dict()
                manifests.append(manifests_item)

        config_files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.config_files, Unset):
            config_files = []
            for config_files_item_data in self.config_files:
                config_files_item = config_files_item_data.to_dict()
                config_files.append(config_files_item)

        application_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application_settings, Unset):
            application_settings = self.application_settings.to_dict()

        connection_strings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connection_strings, Unset):
            connection_strings = self.connection_strings.to_dict()

        cli_environment_variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cli_environment_variables, Unset):
            cli_environment_variables = []
            for cli_environment_variables_item_data in self.cli_environment_variables:
                cli_environment_variables_item = cli_environment_variables_item_data.to_dict()
                cli_environment_variables.append(cli_environment_variables_item)

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variables is not UNSET:
            field_dict["variables"] = variables
        if manifests is not UNSET:
            field_dict["manifests"] = manifests
        if config_files is not UNSET:
            field_dict["configFiles"] = config_files
        if application_settings is not UNSET:
            field_dict["applicationSettings"] = application_settings
        if connection_strings is not UNSET:
            field_dict["connectionStrings"] = connection_strings
        if cli_environment_variables is not UNSET:
            field_dict["cliEnvironmentVariables"] = cli_environment_variables
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_settings_configuration import ApplicationSettingsConfiguration
        from ..models.config_file_wrapper import ConfigFileWrapper
        from ..models.connection_strings_configuration import ConnectionStringsConfiguration
        from ..models.manifest_config_wrapper import ManifestConfigWrapper
        from ..models.ng_variable import NGVariable

        d = dict(src_dict)
        _variables = d.pop("variables", UNSET)
        variables: list[NGVariable] | Unset = UNSET
        if _variables is not UNSET:
            variables = []
            for variables_item_data in _variables:
                variables_item = NGVariable.from_dict(variables_item_data)

                variables.append(variables_item)

        _manifests = d.pop("manifests", UNSET)
        manifests: list[ManifestConfigWrapper] | Unset = UNSET
        if _manifests is not UNSET:
            manifests = []
            for manifests_item_data in _manifests:
                manifests_item = ManifestConfigWrapper.from_dict(manifests_item_data)

                manifests.append(manifests_item)

        _config_files = d.pop("configFiles", UNSET)
        config_files: list[ConfigFileWrapper] | Unset = UNSET
        if _config_files is not UNSET:
            config_files = []
            for config_files_item_data in _config_files:
                config_files_item = ConfigFileWrapper.from_dict(config_files_item_data)

                config_files.append(config_files_item)

        _application_settings = d.pop("applicationSettings", UNSET)
        application_settings: ApplicationSettingsConfiguration | Unset
        if isinstance(_application_settings, Unset):
            application_settings = UNSET
        else:
            application_settings = ApplicationSettingsConfiguration.from_dict(_application_settings)

        _connection_strings = d.pop("connectionStrings", UNSET)
        connection_strings: ConnectionStringsConfiguration | Unset
        if isinstance(_connection_strings, Unset):
            connection_strings = UNSET
        else:
            connection_strings = ConnectionStringsConfiguration.from_dict(_connection_strings)

        _cli_environment_variables = d.pop("cliEnvironmentVariables", UNSET)
        cli_environment_variables: list[NGVariable] | Unset = UNSET
        if _cli_environment_variables is not UNSET:
            cli_environment_variables = []
            for cli_environment_variables_item_data in _cli_environment_variables:
                cli_environment_variables_item = NGVariable.from_dict(cli_environment_variables_item_data)

                cli_environment_variables.append(cli_environment_variables_item)

        metadata = d.pop("metadata", UNSET)

        service_override_spec = cls(
            variables=variables,
            manifests=manifests,
            config_files=config_files,
            application_settings=application_settings,
            connection_strings=connection_strings,
            cli_environment_variables=cli_environment_variables,
            metadata=metadata,
        )

        service_override_spec.additional_properties = d
        return service_override_spec

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
