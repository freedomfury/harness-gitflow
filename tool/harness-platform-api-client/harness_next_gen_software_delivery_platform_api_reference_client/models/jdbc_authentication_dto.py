from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jdbc_authentication_dto_type import JDBCAuthenticationDTOType, check_jdbc_authentication_dto_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jdbc_auth_credentials_dto import JDBCAuthCredentialsDTO


T = TypeVar("T", bound="JDBCAuthenticationDTO")


@_attrs_define
class JDBCAuthenticationDTO:
    """This entity contains the details for JDBC Authentication

    Attributes:
        type_ (JDBCAuthenticationDTOType):
        spec (JDBCAuthCredentialsDTO | Unset): This contains details of credentials for JDBC Authentication
    """

    type_: JDBCAuthenticationDTOType
    spec: JDBCAuthCredentialsDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jdbc_auth_credentials_dto import JDBCAuthCredentialsDTO

        d = dict(src_dict)
        type_ = check_jdbc_authentication_dto_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: JDBCAuthCredentialsDTO | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = JDBCAuthCredentialsDTO.from_dict(_spec)

        jdbc_authentication_dto = cls(
            type_=type_,
            spec=spec,
        )

        jdbc_authentication_dto.additional_properties = d
        return jdbc_authentication_dto

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
