from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cache_response_metadata_cache_state import (
    CacheResponseMetadataCacheState,
    check_cache_response_metadata_cache_state,
)

T = TypeVar("T", bound="CacheResponseMetadata")


@_attrs_define
class CacheResponseMetadata:
    """This tells the state of the cache from which the template was fetched.

    Attributes:
        cache_state (CacheResponseMetadataCacheState):
        ttl_left (int):
        last_updated_at (int):
        is_sync_enabled (bool):
    """

    cache_state: CacheResponseMetadataCacheState
    ttl_left: int
    last_updated_at: int
    is_sync_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cache_state: str = self.cache_state

        ttl_left = self.ttl_left

        last_updated_at = self.last_updated_at

        is_sync_enabled = self.is_sync_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cacheState": cache_state,
                "ttlLeft": ttl_left,
                "lastUpdatedAt": last_updated_at,
                "isSyncEnabled": is_sync_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cache_state = check_cache_response_metadata_cache_state(d.pop("cacheState"))

        ttl_left = d.pop("ttlLeft")

        last_updated_at = d.pop("lastUpdatedAt")

        is_sync_enabled = d.pop("isSyncEnabled")

        cache_response_metadata = cls(
            cache_state=cache_state,
            ttl_left=ttl_left,
            last_updated_at=last_updated_at,
            is_sync_enabled=is_sync_enabled,
        )

        cache_response_metadata.additional_properties = d
        return cache_response_metadata

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
