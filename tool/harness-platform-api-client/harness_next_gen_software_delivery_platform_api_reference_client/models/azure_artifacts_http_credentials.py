from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_artifacts_http_credentials_type import (
    AzureArtifactsHttpCredentialsType,
    check_azure_artifacts_http_credentials_type,
)

if TYPE_CHECKING:
    from ..models.azure_artifacts_username_token import AzureArtifactsUsernameToken


T = TypeVar("T", bound="AzureArtifactsHttpCredentials")


@_attrs_define
class AzureArtifactsHttpCredentials:
    """This contains details of the AzureArtifacts credentials used via HTTP connections

    Attributes:
        type_ (AzureArtifactsHttpCredentialsType):
        spec (AzureArtifactsUsernameToken): This contains details of the AzureArtifacts credentials Specs such as
            references of username and token
    """

    type_: AzureArtifactsHttpCredentialsType
    spec: AzureArtifactsUsernameToken
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_artifacts_username_token import AzureArtifactsUsernameToken

        d = dict(src_dict)
        type_ = check_azure_artifacts_http_credentials_type(d.pop("type"))

        spec = AzureArtifactsUsernameToken.from_dict(d.pop("spec"))

        azure_artifacts_http_credentials = cls(
            type_=type_,
            spec=spec,
        )

        azure_artifacts_http_credentials.additional_properties = d
        return azure_artifacts_http_credentials

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
