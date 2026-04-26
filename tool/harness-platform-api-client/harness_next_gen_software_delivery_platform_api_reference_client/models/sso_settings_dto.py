from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sso_settings_dto_type import SSOSettingsDTOType, check_sso_settings_dto_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SSOSettingsDTO")


@_attrs_define
class SSOSettingsDTO:
    """
    Attributes:
        type_ (SSOSettingsDTOType):
        display_name (str):
        url (str):
        uuid (str | Unset):
        next_iterations (list[int] | Unset):
        account_id (str | Unset):
    """

    type_: SSOSettingsDTOType
    display_name: str
    url: str
    uuid: str | Unset = UNSET
    next_iterations: list[int] | Unset = UNSET
    account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        display_name = self.display_name

        url = self.url

        uuid = self.uuid

        next_iterations: list[int] | Unset = UNSET
        if not isinstance(self.next_iterations, Unset):
            next_iterations = self.next_iterations

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "displayName": display_name,
                "url": url,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if next_iterations is not UNSET:
            field_dict["nextIterations"] = next_iterations
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = check_sso_settings_dto_type(d.pop("type"))

        display_name = d.pop("displayName")

        url = d.pop("url")

        uuid = d.pop("uuid", UNSET)

        next_iterations = cast(list[int], d.pop("nextIterations", UNSET))

        account_id = d.pop("accountId", UNSET)

        sso_settings_dto = cls(
            type_=type_,
            display_name=display_name,
            url=url,
            uuid=uuid,
            next_iterations=next_iterations,
            account_id=account_id,
        )

        sso_settings_dto.additional_properties = d
        return sso_settings_dto

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
