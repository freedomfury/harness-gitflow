from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_response_status import LdapResponseStatus, check_ldap_response_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapResponse")


@_attrs_define
class LdapResponse:
    """
    Attributes:
        status (LdapResponseStatus | Unset):
        message (str | Unset):
    """

    status: LdapResponseStatus | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: LdapResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_ldap_response_status(_status)

        message = d.pop("message", UNSET)

        ldap_response = cls(
            status=status,
            message=message,
        )

        ldap_response.additional_properties = d
        return ldap_response

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
