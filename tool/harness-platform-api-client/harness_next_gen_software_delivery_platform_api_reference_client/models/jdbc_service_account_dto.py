from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JDBCServiceAccountDTO")


@_attrs_define
class JDBCServiceAccountDTO:
    """This entity contains kubernetes service account details

    Attributes:
        service_account_token_ref (str):
    """

    service_account_token_ref: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_account_token_ref = self.service_account_token_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceAccountTokenRef": service_account_token_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_account_token_ref = d.pop("serviceAccountTokenRef")

        jdbc_service_account_dto = cls(
            service_account_token_ref=service_account_token_ref,
        )

        jdbc_service_account_dto.additional_properties = d
        return jdbc_service_account_dto

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
