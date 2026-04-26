from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_provider_response_type import GetProviderResponseType, check_get_provider_response_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_response_info import ProviderResponseInfo


T = TypeVar("T", bound="GetProviderResponse")


@_attrs_define
class GetProviderResponse:
    """
    Attributes:
        account_identifier (str | Unset):
        name (str | Unset):
        description (str | Unset):
        identifier (str | Unset):
        type_ (GetProviderResponseType | Unset):
        last_modified_at (int | Unset):
        provider_response_info (ProviderResponseInfo | Unset):
    """

    account_identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    identifier: str | Unset = UNSET
    type_: GetProviderResponseType | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    provider_response_info: ProviderResponseInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        name = self.name

        description = self.description

        identifier = self.identifier

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        last_modified_at = self.last_modified_at

        provider_response_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_response_info, Unset):
            provider_response_info = self.provider_response_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if type_ is not UNSET:
            field_dict["type"] = type_
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if provider_response_info is not UNSET:
            field_dict["providerResponseInfo"] = provider_response_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_response_info import ProviderResponseInfo

        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GetProviderResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_get_provider_response_type(_type_)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        _provider_response_info = d.pop("providerResponseInfo", UNSET)
        provider_response_info: ProviderResponseInfo | Unset
        if isinstance(_provider_response_info, Unset):
            provider_response_info = UNSET
        else:
            provider_response_info = ProviderResponseInfo.from_dict(_provider_response_info)

        get_provider_response = cls(
            account_identifier=account_identifier,
            name=name,
            description=description,
            identifier=identifier,
            type_=type_,
            last_modified_at=last_modified_at,
            provider_response_info=provider_response_info,
        )

        get_provider_response.additional_properties = d
        return get_provider_response

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
