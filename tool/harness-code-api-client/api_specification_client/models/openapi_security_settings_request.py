from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.settings_vulnerability_scanning_mode import SettingsVulnerabilityScanningMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenapiSecuritySettingsRequest")


@_attrs_define
class OpenapiSecuritySettingsRequest:
    """
    Attributes:
        principal_committer_match (bool | None | Unset):
        secret_scanning_enabled (bool | None | Unset):
        vulnerability_scanning_mode (SettingsVulnerabilityScanningMode | Unset):
    """

    principal_committer_match: bool | None | Unset = UNSET
    secret_scanning_enabled: bool | None | Unset = UNSET
    vulnerability_scanning_mode: SettingsVulnerabilityScanningMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        principal_committer_match: bool | None | Unset
        if isinstance(self.principal_committer_match, Unset):
            principal_committer_match = UNSET
        else:
            principal_committer_match = self.principal_committer_match

        secret_scanning_enabled: bool | None | Unset
        if isinstance(self.secret_scanning_enabled, Unset):
            secret_scanning_enabled = UNSET
        else:
            secret_scanning_enabled = self.secret_scanning_enabled

        vulnerability_scanning_mode: str | Unset = UNSET
        if not isinstance(self.vulnerability_scanning_mode, Unset):
            vulnerability_scanning_mode = self.vulnerability_scanning_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if principal_committer_match is not UNSET:
            field_dict["principal_committer_match"] = principal_committer_match
        if secret_scanning_enabled is not UNSET:
            field_dict["secret_scanning_enabled"] = secret_scanning_enabled
        if vulnerability_scanning_mode is not UNSET:
            field_dict["vulnerability_scanning_mode"] = vulnerability_scanning_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_principal_committer_match(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        principal_committer_match = _parse_principal_committer_match(d.pop("principal_committer_match", UNSET))

        def _parse_secret_scanning_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        secret_scanning_enabled = _parse_secret_scanning_enabled(d.pop("secret_scanning_enabled", UNSET))

        _vulnerability_scanning_mode = d.pop("vulnerability_scanning_mode", UNSET)
        vulnerability_scanning_mode: SettingsVulnerabilityScanningMode | Unset
        if isinstance(_vulnerability_scanning_mode, Unset):
            vulnerability_scanning_mode = UNSET
        else:
            vulnerability_scanning_mode = SettingsVulnerabilityScanningMode(_vulnerability_scanning_mode)

        openapi_security_settings_request = cls(
            principal_committer_match=principal_committer_match,
            secret_scanning_enabled=secret_scanning_enabled,
            vulnerability_scanning_mode=vulnerability_scanning_mode,
        )

        openapi_security_settings_request.additional_properties = d
        return openapi_security_settings_request

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
