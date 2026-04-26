from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_settings import AccountSettings


T = TypeVar("T", bound="AccountSettingResponse")


@_attrs_define
class AccountSettingResponse:
    """This has the Account Setting details along with its metadata.

    Attributes:
        account_settings (AccountSettings | Unset): This is the view of Account Settings in Harness.
        created_at (int | Unset): This is the time at which account setting was created.
        last_modified_at (int | Unset): This is the time at which account setting was last modified.
    """

    account_settings: AccountSettings | Unset = UNSET
    created_at: int | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_settings, Unset):
            account_settings = self.account_settings.to_dict()

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_settings is not UNSET:
            field_dict["accountSettings"] = account_settings
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_settings import AccountSettings

        d = dict(src_dict)
        _account_settings = d.pop("accountSettings", UNSET)
        account_settings: AccountSettings | Unset
        if isinstance(_account_settings, Unset):
            account_settings = UNSET
        else:
            account_settings = AccountSettings.from_dict(_account_settings)

        created_at = d.pop("createdAt", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        account_setting_response = cls(
            account_settings=account_settings,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

        account_setting_response.additional_properties = d
        return account_setting_response

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
