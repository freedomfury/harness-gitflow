from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.azure_artifacts_http_credentials import AzureArtifactsHttpCredentials


T = TypeVar("T", bound="AzureArtifactsAuthentication")


@_attrs_define
class AzureArtifactsAuthentication:
    """This contains details of the information needed for Azure DevOps access

    Attributes:
        spec (AzureArtifactsHttpCredentials): This contains details of the AzureArtifacts credentials used via HTTP
            connections
    """

    spec: AzureArtifactsHttpCredentials
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_artifacts_http_credentials import AzureArtifactsHttpCredentials

        d = dict(src_dict)
        spec = AzureArtifactsHttpCredentials.from_dict(d.pop("spec"))

        azure_artifacts_authentication = cls(
            spec=spec,
        )

        azure_artifacts_authentication.additional_properties = d
        return azure_artifacts_authentication

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
