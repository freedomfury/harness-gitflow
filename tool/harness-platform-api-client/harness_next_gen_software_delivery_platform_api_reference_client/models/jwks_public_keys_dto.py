from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jwks_public_key_dto import JwksPublicKeyDTO


T = TypeVar("T", bound="JwksPublicKeysDTO")


@_attrs_define
class JwksPublicKeysDTO:
    """
    Attributes:
        keys (list[JwksPublicKeyDTO] | Unset):
    """

    keys: list[JwksPublicKeyDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item = keys_item_data.to_dict()
                keys.append(keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jwks_public_key_dto import JwksPublicKeyDTO

        d = dict(src_dict)
        _keys = d.pop("keys", UNSET)
        keys: list[JwksPublicKeyDTO] | Unset = UNSET
        if _keys is not UNSET:
            keys = []
            for keys_item_data in _keys:
                keys_item = JwksPublicKeyDTO.from_dict(keys_item_data)

                keys.append(keys_item)

        jwks_public_keys_dto = cls(
            keys=keys,
        )

        jwks_public_keys_dto.additional_properties = d
        return jwks_public_keys_dto

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
