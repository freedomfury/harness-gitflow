from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oidc_id_token_custom_attributes_structure import OidcIdTokenCustomAttributesStructure


T = TypeVar("T", bound="AwsOidcTokenRequest")


@_attrs_define
class AwsOidcTokenRequest:
    """This contains AWS OIDC Token request details

    Attributes:
        account_id (str | Unset): This specifies the Harness Account Id
        oidc_id_token_custom_attributes_structure (OidcIdTokenCustomAttributesStructure | Unset): This includes all the
            ID token custom attributes
        region (str | Unset): This specifies the Aws region
    """

    account_id: str | Unset = UNSET
    oidc_id_token_custom_attributes_structure: OidcIdTokenCustomAttributesStructure | Unset = UNSET
    region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        oidc_id_token_custom_attributes_structure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oidc_id_token_custom_attributes_structure, Unset):
            oidc_id_token_custom_attributes_structure = self.oidc_id_token_custom_attributes_structure.to_dict()

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if oidc_id_token_custom_attributes_structure is not UNSET:
            field_dict["oidcIdTokenCustomAttributesStructure"] = oidc_id_token_custom_attributes_structure
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_id_token_custom_attributes_structure import OidcIdTokenCustomAttributesStructure

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        _oidc_id_token_custom_attributes_structure = d.pop("oidcIdTokenCustomAttributesStructure", UNSET)
        oidc_id_token_custom_attributes_structure: OidcIdTokenCustomAttributesStructure | Unset
        if isinstance(_oidc_id_token_custom_attributes_structure, Unset):
            oidc_id_token_custom_attributes_structure = UNSET
        else:
            oidc_id_token_custom_attributes_structure = OidcIdTokenCustomAttributesStructure.from_dict(
                _oidc_id_token_custom_attributes_structure
            )

        region = d.pop("region", UNSET)

        aws_oidc_token_request = cls(
            account_id=account_id,
            oidc_id_token_custom_attributes_structure=oidc_id_token_custom_attributes_structure,
            region=region,
        )

        aws_oidc_token_request.additional_properties = d
        return aws_oidc_token_request

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
