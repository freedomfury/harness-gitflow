from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_full_sync_entity_info_filter_entity_types_item import (
    GitFullSyncEntityInfoFilterEntityTypesItem,
    check_git_full_sync_entity_info_filter_entity_types_item,
)
from ..models.git_full_sync_entity_info_filter_sync_status import (
    GitFullSyncEntityInfoFilterSyncStatus,
    check_git_full_sync_entity_info_filter_sync_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitFullSyncEntityInfoFilter")


@_attrs_define
class GitFullSyncEntityInfoFilter:
    """Filter details for Git Full Sync.

    Attributes:
        entity_types (list[GitFullSyncEntityInfoFilterEntityTypesItem] | Unset): List of entity Types to filter on the
            entities.
        sync_status (GitFullSyncEntityInfoFilterSyncStatus | Unset): Sync Status of the Entity that may be QUEUED,
            SUCCESS or FAILED.
    """

    entity_types: list[GitFullSyncEntityInfoFilterEntityTypesItem] | Unset = UNSET
    sync_status: GitFullSyncEntityInfoFilterSyncStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_types: list[str] | Unset = UNSET
        if not isinstance(self.entity_types, Unset):
            entity_types = []
            for entity_types_item_data in self.entity_types:
                entity_types_item: str = entity_types_item_data
                entity_types.append(entity_types_item)

        sync_status: str | Unset = UNSET
        if not isinstance(self.sync_status, Unset):
            sync_status = self.sync_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_types is not UNSET:
            field_dict["entityTypes"] = entity_types
        if sync_status is not UNSET:
            field_dict["syncStatus"] = sync_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _entity_types = d.pop("entityTypes", UNSET)
        entity_types: list[GitFullSyncEntityInfoFilterEntityTypesItem] | Unset = UNSET
        if _entity_types is not UNSET:
            entity_types = []
            for entity_types_item_data in _entity_types:
                entity_types_item = check_git_full_sync_entity_info_filter_entity_types_item(entity_types_item_data)

                entity_types.append(entity_types_item)

        _sync_status = d.pop("syncStatus", UNSET)
        sync_status: GitFullSyncEntityInfoFilterSyncStatus | Unset
        if isinstance(_sync_status, Unset):
            sync_status = UNSET
        else:
            sync_status = check_git_full_sync_entity_info_filter_sync_status(_sync_status)

        git_full_sync_entity_info_filter = cls(
            entity_types=entity_types,
            sync_status=sync_status,
        )

        git_full_sync_entity_info_filter.additional_properties = d
        return git_full_sync_entity_info_filter

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
