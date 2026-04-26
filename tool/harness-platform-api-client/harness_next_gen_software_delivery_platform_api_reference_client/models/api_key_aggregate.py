from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key import ApiKey


T = TypeVar("T", bound="ApiKeyAggregate")


@_attrs_define
class ApiKeyAggregate:
    """This has API Key details and metadata.

    Attributes:
        api_key (ApiKey): This has API Key details defined in Harness.
        created_at (int): This is the time at which API Key was created.
        last_modified_at (int): This is the time at which API Key was last modified.
        tokens_count (int | Unset): The number of tokens within an API Key.
    """

    api_key: ApiKey
    created_at: int
    last_modified_at: int
    tokens_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key.to_dict()

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        tokens_count = self.tokens_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "createdAt": created_at,
                "lastModifiedAt": last_modified_at,
            }
        )
        if tokens_count is not UNSET:
            field_dict["tokensCount"] = tokens_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key import ApiKey

        d = dict(src_dict)
        api_key = ApiKey.from_dict(d.pop("apiKey"))

        created_at = d.pop("createdAt")

        last_modified_at = d.pop("lastModifiedAt")

        tokens_count = d.pop("tokensCount", UNSET)

        api_key_aggregate = cls(
            api_key=api_key,
            created_at=created_at,
            last_modified_at=last_modified_at,
            tokens_count=tokens_count,
        )

        api_key_aggregate.additional_properties = d
        return api_key_aggregate

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
