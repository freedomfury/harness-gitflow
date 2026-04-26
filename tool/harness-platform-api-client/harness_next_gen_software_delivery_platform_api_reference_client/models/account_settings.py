from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_settings_type import AccountSettingsType, check_account_settings_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_setting_config import AccountSettingConfig


T = TypeVar("T", bound="AccountSettings")


@_attrs_define
class AccountSettings:
    """This is the view of Account Settings in Harness.

    Attributes:
        account_identifier (str): Account Identifier for the Entity.
        config (AccountSettingConfig): Configuration of the Account Settings.
        type_ (AccountSettingsType): This is the type of resource for which Account Setting is created.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
    """

    account_identifier: str
    config: AccountSettingConfig
    type_: AccountSettingsType
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        config = self.config.to_dict()

        type_: str = self.type_

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountIdentifier": account_identifier,
                "config": config,
                "type": type_,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_setting_config import AccountSettingConfig

        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier")

        config = AccountSettingConfig.from_dict(d.pop("config"))

        type_ = check_account_settings_type(d.pop("type"))

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        account_settings = cls(
            account_identifier=account_identifier,
            config=config,
            type_=type_,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
        )

        account_settings.additional_properties = d
        return account_settings

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
