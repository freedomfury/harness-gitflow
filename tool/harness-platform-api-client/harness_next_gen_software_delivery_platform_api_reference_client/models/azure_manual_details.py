from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.azure_auth import AzureAuth


T = TypeVar("T", bound="AzureManualDetails")


@_attrs_define
class AzureManualDetails:
    """This contains Azure manual credentials connector details

    Attributes:
        application_id (str): Application ID of the Azure App.
        tenant_id (str): The Azure Active Directory (AAD) directory ID where you created your application.
        auth (AzureAuth): This contains azure auth details
    """

    application_id: str
    tenant_id: str
    auth: AzureAuth
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        tenant_id = self.tenant_id

        auth = self.auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicationId": application_id,
                "tenantId": tenant_id,
                "auth": auth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_auth import AzureAuth

        d = dict(src_dict)
        application_id = d.pop("applicationId")

        tenant_id = d.pop("tenantId")

        auth = AzureAuth.from_dict(d.pop("auth"))

        azure_manual_details = cls(
            application_id=application_id,
            tenant_id=tenant_id,
            auth=auth,
        )

        azure_manual_details.additional_properties = d
        return azure_manual_details

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
