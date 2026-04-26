from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.anthropic_authentication_dto_type import (
    AnthropicAuthenticationDTOType,
    check_anthropic_authentication_dto_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anthropic_auth_credentials_dto import AnthropicAuthCredentialsDTO


T = TypeVar("T", bound="AnthropicAuthenticationDTO")


@_attrs_define
class AnthropicAuthenticationDTO:
    """This entity contains the details for Anthropic Authentication

    Attributes:
        type_ (AnthropicAuthenticationDTOType):
        spec (AnthropicAuthCredentialsDTO | Unset): This contains details of credentials for Anthropic Authentication
    """

    type_: AnthropicAuthenticationDTOType
    spec: AnthropicAuthCredentialsDTO | Unset = UNSET
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
        from ..models.anthropic_auth_credentials_dto import AnthropicAuthCredentialsDTO

        d = dict(src_dict)
        type_ = check_anthropic_authentication_dto_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: AnthropicAuthCredentialsDTO | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = AnthropicAuthCredentialsDTO.from_dict(_spec)

        anthropic_authentication_dto = cls(
            type_=type_,
            spec=spec,
        )

        anthropic_authentication_dto.additional_properties = d
        return anthropic_authentication_dto

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
