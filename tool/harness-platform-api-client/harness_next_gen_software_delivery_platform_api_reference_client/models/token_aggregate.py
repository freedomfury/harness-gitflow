from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.token import Token


T = TypeVar("T", bound="TokenAggregate")


@_attrs_define
class TokenAggregate:
    """This has token details and metadata.

    Attributes:
        token (Token): This has the API Key Token details defined in Harness.
        expiry_at (int): Expiry time of the Token.
        created_at (int): This is the time at which Token was created.
        last_modified_at (int): This is the time at which Token was last modified.
    """

    token: Token
    expiry_at: int
    created_at: int
    last_modified_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token.to_dict()

        expiry_at = self.expiry_at

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "expiryAt": expiry_at,
                "createdAt": created_at,
                "lastModifiedAt": last_modified_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token import Token

        d = dict(src_dict)
        token = Token.from_dict(d.pop("token"))

        expiry_at = d.pop("expiryAt")

        created_at = d.pop("createdAt")

        last_modified_at = d.pop("lastModifiedAt")

        token_aggregate = cls(
            token=token,
            expiry_at=expiry_at,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

        token_aggregate.additional_properties = d
        return token_aggregate

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
