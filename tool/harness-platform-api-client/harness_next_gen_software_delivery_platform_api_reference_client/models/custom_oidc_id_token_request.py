from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oidc_id_token_custom_attributes_structure import OidcIdTokenCustomAttributesStructure


T = TypeVar("T", bound="CustomOidcIdTokenRequest")


@_attrs_define
class CustomOidcIdTokenRequest:
    """This contains custom OIDC Token request details

    Attributes:
        oidc_id_token_custom_attributes_structure (OidcIdTokenCustomAttributesStructure): This includes all the ID token
            custom attributes
        aud (str): This specifies the audience field in ID token
        account_id (str | Unset): This specifies the Harness Account Id
        sub (str | Unset): This overrides the default subject field in ID token
    """

    oidc_id_token_custom_attributes_structure: OidcIdTokenCustomAttributesStructure
    aud: str
    account_id: str | Unset = UNSET
    sub: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oidc_id_token_custom_attributes_structure = self.oidc_id_token_custom_attributes_structure.to_dict()

        aud = self.aud

        account_id = self.account_id

        sub = self.sub

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oidcIdTokenCustomAttributesStructure": oidc_id_token_custom_attributes_structure,
                "aud": aud,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if sub is not UNSET:
            field_dict["sub"] = sub

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_id_token_custom_attributes_structure import OidcIdTokenCustomAttributesStructure

        d = dict(src_dict)
        oidc_id_token_custom_attributes_structure = OidcIdTokenCustomAttributesStructure.from_dict(
            d.pop("oidcIdTokenCustomAttributesStructure")
        )

        aud = d.pop("aud")

        account_id = d.pop("accountId", UNSET)

        sub = d.pop("sub", UNSET)

        custom_oidc_id_token_request = cls(
            oidc_id_token_custom_attributes_structure=oidc_id_token_custom_attributes_structure,
            aud=aud,
            account_id=account_id,
            sub=sub,
        )

        custom_oidc_id_token_request.additional_properties = d
        return custom_oidc_id_token_request

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
