from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_repo_authentication_type import AzureRepoAuthenticationType, check_azure_repo_authentication_type

if TYPE_CHECKING:
    from ..models.azure_repo_credentials import AzureRepoCredentials


T = TypeVar("T", bound="AzureRepoAuthentication")


@_attrs_define
class AzureRepoAuthentication:
    """This contains details of the information needed for Azure DevOps access

    Attributes:
        type_ (AzureRepoAuthenticationType):
        spec (AzureRepoCredentials): This is a interface for details of the Azure DevOps credentials
    """

    type_: AzureRepoAuthenticationType
    spec: AzureRepoCredentials
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
        from ..models.azure_repo_credentials import AzureRepoCredentials

        d = dict(src_dict)
        type_ = check_azure_repo_authentication_type(d.pop("type"))

        spec = AzureRepoCredentials.from_dict(d.pop("spec"))

        azure_repo_authentication = cls(
            type_=type_,
            spec=spec,
        )

        azure_repo_authentication.additional_properties = d
        return azure_repo_authentication

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
