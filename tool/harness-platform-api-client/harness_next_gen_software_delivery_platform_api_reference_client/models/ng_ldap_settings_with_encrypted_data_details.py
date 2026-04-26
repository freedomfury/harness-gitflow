from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.encrypted_data_detail import EncryptedDataDetail
    from ..models.ldap_settings_dto import LdapSettingsDTO


T = TypeVar("T", bound="NGLdapSettingsWithEncryptedDataDetails")


@_attrs_define
class NGLdapSettingsWithEncryptedDataDetails:
    """
    Attributes:
        ldap_settings (LdapSettingsDTO): Ldap Settings DTO
        encrypted_data_detail (EncryptedDataDetail):
    """

    ldap_settings: LdapSettingsDTO
    encrypted_data_detail: EncryptedDataDetail
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ldap_settings = self.ldap_settings.to_dict()

        encrypted_data_detail = self.encrypted_data_detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ldapSettings": ldap_settings,
                "encryptedDataDetail": encrypted_data_detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encrypted_data_detail import EncryptedDataDetail
        from ..models.ldap_settings_dto import LdapSettingsDTO

        d = dict(src_dict)
        ldap_settings = LdapSettingsDTO.from_dict(d.pop("ldapSettings"))

        encrypted_data_detail = EncryptedDataDetail.from_dict(d.pop("encryptedDataDetail"))

        ng_ldap_settings_with_encrypted_data_details = cls(
            ldap_settings=ldap_settings,
            encrypted_data_detail=encrypted_data_detail,
        )

        ng_ldap_settings_with_encrypted_data_details.additional_properties = d
        return ng_ldap_settings_with_encrypted_data_details

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
