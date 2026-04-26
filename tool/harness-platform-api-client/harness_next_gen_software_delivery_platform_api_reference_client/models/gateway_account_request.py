from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gateway_account_request_default_experience import (
    GatewayAccountRequestDefaultExperience,
    check_gateway_account_request_default_experience,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayAccountRequest")


@_attrs_define
class GatewayAccountRequest:
    """Returns Gateway account request details like uuid, account name, company name, default experience, whether or not
    created from NextGen and whether NextGen is enabled or not.

        Attributes:
            uuid (str | Unset):
            account_name (str | Unset):
            company_name (str | Unset):
            default_experience (GatewayAccountRequestDefaultExperience | Unset):
            created_from_ng (bool | Unset):
            is_next_gen_enabled (bool | Unset):
            next_gen_enabled (bool | Unset):
    """

    uuid: str | Unset = UNSET
    account_name: str | Unset = UNSET
    company_name: str | Unset = UNSET
    default_experience: GatewayAccountRequestDefaultExperience | Unset = UNSET
    created_from_ng: bool | Unset = UNSET
    is_next_gen_enabled: bool | Unset = UNSET
    next_gen_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        account_name = self.account_name

        company_name = self.company_name

        default_experience: str | Unset = UNSET
        if not isinstance(self.default_experience, Unset):
            default_experience = self.default_experience

        created_from_ng = self.created_from_ng

        is_next_gen_enabled = self.is_next_gen_enabled

        next_gen_enabled = self.next_gen_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if default_experience is not UNSET:
            field_dict["defaultExperience"] = default_experience
        if created_from_ng is not UNSET:
            field_dict["createdFromNG"] = created_from_ng
        if is_next_gen_enabled is not UNSET:
            field_dict["isNextGenEnabled"] = is_next_gen_enabled
        if next_gen_enabled is not UNSET:
            field_dict["nextGenEnabled"] = next_gen_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        account_name = d.pop("accountName", UNSET)

        company_name = d.pop("companyName", UNSET)

        _default_experience = d.pop("defaultExperience", UNSET)
        default_experience: GatewayAccountRequestDefaultExperience | Unset
        if isinstance(_default_experience, Unset):
            default_experience = UNSET
        else:
            default_experience = check_gateway_account_request_default_experience(_default_experience)

        created_from_ng = d.pop("createdFromNG", UNSET)

        is_next_gen_enabled = d.pop("isNextGenEnabled", UNSET)

        next_gen_enabled = d.pop("nextGenEnabled", UNSET)

        gateway_account_request = cls(
            uuid=uuid,
            account_name=account_name,
            company_name=company_name,
            default_experience=default_experience,
            created_from_ng=created_from_ng,
            is_next_gen_enabled=is_next_gen_enabled,
            next_gen_enabled=next_gen_enabled,
        )

        gateway_account_request.additional_properties = d
        return gateway_account_request

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
