from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.principal_type import PrincipalType, check_principal_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.principal_jwtclaims import PrincipalJwtclaims


T = TypeVar("T", bound="Principal")


@_attrs_define
class Principal:
    """
    Attributes:
        type_ (PrincipalType):
        name (str):
        jwtclaims (PrincipalJwtclaims | Unset):
    """

    type_: PrincipalType
    name: str
    jwtclaims: PrincipalJwtclaims | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        name = self.name

        jwtclaims: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jwtclaims, Unset):
            jwtclaims = self.jwtclaims.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if jwtclaims is not UNSET:
            field_dict["jwtclaims"] = jwtclaims

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.principal_jwtclaims import PrincipalJwtclaims

        d = dict(src_dict)
        type_ = check_principal_type(d.pop("type"))

        name = d.pop("name")

        _jwtclaims = d.pop("jwtclaims", UNSET)
        jwtclaims: PrincipalJwtclaims | Unset
        if isinstance(_jwtclaims, Unset):
            jwtclaims = UNSET
        else:
            jwtclaims = PrincipalJwtclaims.from_dict(_jwtclaims)

        principal = cls(
            type_=type_,
            name=name,
            jwtclaims=jwtclaims,
        )

        principal.additional_properties = d
        return principal

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
