from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.azure_msi_auth import AzureMSIAuth


T = TypeVar("T", bound="AzureInheritFromDelegateDetails")


@_attrs_define
class AzureInheritFromDelegateDetails:
    """This contains Azure inherit from delegate credentials connector details

    Attributes:
        auth (AzureMSIAuth): This contains azure MSI auth details
    """

    auth: AzureMSIAuth
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth = self.auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth": auth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_msi_auth import AzureMSIAuth

        d = dict(src_dict)
        auth = AzureMSIAuth.from_dict(d.pop("auth"))

        azure_inherit_from_delegate_details = cls(
            auth=auth,
        )

        azure_inherit_from_delegate_details.additional_properties = d
        return azure_inherit_from_delegate_details

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
