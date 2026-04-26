from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_auth_type import AzureAuthType, check_azure_auth_type

if TYPE_CHECKING:
    from ..models.azure_auth_credential import AzureAuthCredential


T = TypeVar("T", bound="AzureAuth")


@_attrs_define
class AzureAuth:
    """This contains azure auth details

    Attributes:
        type_ (AzureAuthType):
        spec (AzureAuthCredential): This contains azure auth credentials
    """

    type_: AzureAuthType
    spec: AzureAuthCredential
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
        from ..models.azure_auth_credential import AzureAuthCredential

        d = dict(src_dict)
        type_ = check_azure_auth_type(d.pop("type"))

        spec = AzureAuthCredential.from_dict(d.pop("spec"))

        azure_auth = cls(
            type_=type_,
            spec=spec,
        )

        azure_auth.additional_properties = d
        return azure_auth

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
