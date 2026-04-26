from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SalesforceJwtCredentialDetails")


@_attrs_define
class SalesforceJwtCredentialDetails:
    """This contains salesforce JWT credentials connector details

    Attributes:
        username (str | Unset):
        login_url (str | Unset):
        client_id (str | Unset):
        jwt_key_file_ref (str | Unset):
    """

    username: str | Unset = UNSET
    login_url: str | Unset = UNSET
    client_id: str | Unset = UNSET
    jwt_key_file_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        login_url = self.login_url

        client_id = self.client_id

        jwt_key_file_ref = self.jwt_key_file_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if login_url is not UNSET:
            field_dict["loginUrl"] = login_url
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if jwt_key_file_ref is not UNSET:
            field_dict["jwtKeyFileRef"] = jwt_key_file_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        login_url = d.pop("loginUrl", UNSET)

        client_id = d.pop("clientId", UNSET)

        jwt_key_file_ref = d.pop("jwtKeyFileRef", UNSET)

        salesforce_jwt_credential_details = cls(
            username=username,
            login_url=login_url,
            client_id=client_id,
            jwt_key_file_ref=jwt_key_file_ref,
        )

        salesforce_jwt_credential_details.additional_properties = d
        return salesforce_jwt_credential_details

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
