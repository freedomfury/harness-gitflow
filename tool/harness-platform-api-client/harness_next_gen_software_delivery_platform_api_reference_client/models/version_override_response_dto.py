from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionOverrideResponseDTO")


@_attrs_define
class VersionOverrideResponseDTO:
    """
    Attributes:
        version (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        parent_unique_id (str | Unset):
        tags (list[str] | Unset):
        valid_till_next_release (bool | Unset):
        valid_until (datetime.datetime | Unset):
    """

    version: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    parent_unique_id: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    valid_till_next_release: bool | Unset = UNSET
    valid_until: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        parent_unique_id = self.parent_unique_id

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        valid_till_next_release = self.valid_till_next_release

        valid_until: str | Unset = UNSET
        if not isinstance(self.valid_until, Unset):
            valid_until = self.valid_until.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if parent_unique_id is not UNSET:
            field_dict["parentUniqueId"] = parent_unique_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if valid_till_next_release is not UNSET:
            field_dict["validTillNextRelease"] = valid_till_next_release
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        parent_unique_id = d.pop("parentUniqueId", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        valid_till_next_release = d.pop("validTillNextRelease", UNSET)

        _valid_until = d.pop("validUntil", UNSET)
        valid_until: datetime.datetime | Unset
        if isinstance(_valid_until, Unset):
            valid_until = UNSET
        else:
            valid_until = isoparse(_valid_until)

        version_override_response_dto = cls(
            version=version,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            parent_unique_id=parent_unique_id,
            tags=tags,
            valid_till_next_release=valid_till_next_release,
            valid_until=valid_until,
        )

        version_override_response_dto.additional_properties = d
        return version_override_response_dto

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
