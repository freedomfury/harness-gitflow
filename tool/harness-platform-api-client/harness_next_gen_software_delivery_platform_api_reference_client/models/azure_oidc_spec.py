from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureOidcSpec")


@_attrs_define
class AzureOidcSpec:
    """This contains Azure OIDC credentials connector details

    Attributes:
        tenant_id (str): The Azure Active Directory (AAD) directory ID where you created your application.
        application_id (str): Application ID of the Azure App.
        audience (str | Unset): Audience (Optional)
    """

    tenant_id: str
    application_id: str
    audience: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        application_id = self.application_id

        audience = self.audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenantId": tenant_id,
                "applicationId": application_id,
            }
        )
        if audience is not UNSET:
            field_dict["audience"] = audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_id = d.pop("tenantId")

        application_id = d.pop("applicationId")

        audience = d.pop("audience", UNSET)

        azure_oidc_spec = cls(
            tenant_id=tenant_id,
            application_id=application_id,
            audience=audience,
        )

        azure_oidc_spec.additional_properties = d
        return azure_oidc_spec

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
