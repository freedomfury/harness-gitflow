from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.files_filter_properties_dto_file_usage import (
    FilesFilterPropertiesDTOFileUsage,
    check_files_filter_properties_dto_file_usage,
)
from ..models.files_filter_properties_dto_filter_type import (
    FilesFilterPropertiesDTOFilterType,
    check_files_filter_properties_dto_filter_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO
    from ..models.files_filter_properties_dto_tags import FilesFilterPropertiesDTOTags
    from ..models.referenced_by_dto import ReferencedByDTO


T = TypeVar("T", bound="FilesFilterPropertiesDTO")


@_attrs_define
class FilesFilterPropertiesDTO:
    """Properties of the Files Filter defined in Harness

    Attributes:
        filter_type (FilesFilterPropertiesDTOFilterType): This specifies the corresponding Entity of the filter.
        file_usage (FilesFilterPropertiesDTOFileUsage | Unset): This specifies the file usage
        created_by (EmbeddedUserDetailsDTO | Unset): Updated by user details
        referenced_by (ReferencedByDTO | Unset): File referenced by other entity
        tags (FilesFilterPropertiesDTOTags | Unset): Filter tags as a key-value pair.
    """

    filter_type: FilesFilterPropertiesDTOFilterType
    file_usage: FilesFilterPropertiesDTOFileUsage | Unset = UNSET
    created_by: EmbeddedUserDetailsDTO | Unset = UNSET
    referenced_by: ReferencedByDTO | Unset = UNSET
    tags: FilesFilterPropertiesDTOTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type: str = self.filter_type

        file_usage: str | Unset = UNSET
        if not isinstance(self.file_usage, Unset):
            file_usage = self.file_usage

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        referenced_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.referenced_by, Unset):
            referenced_by = self.referenced_by.to_dict()

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filterType": filter_type,
            }
        )
        if file_usage is not UNSET:
            field_dict["fileUsage"] = file_usage
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if referenced_by is not UNSET:
            field_dict["referencedBy"] = referenced_by
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO
        from ..models.files_filter_properties_dto_tags import FilesFilterPropertiesDTOTags
        from ..models.referenced_by_dto import ReferencedByDTO

        d = dict(src_dict)
        filter_type = check_files_filter_properties_dto_filter_type(d.pop("filterType"))

        _file_usage = d.pop("fileUsage", UNSET)
        file_usage: FilesFilterPropertiesDTOFileUsage | Unset
        if isinstance(_file_usage, Unset):
            file_usage = UNSET
        else:
            file_usage = check_files_filter_properties_dto_file_usage(_file_usage)

        _created_by = d.pop("createdBy", UNSET)
        created_by: EmbeddedUserDetailsDTO | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = EmbeddedUserDetailsDTO.from_dict(_created_by)

        _referenced_by = d.pop("referencedBy", UNSET)
        referenced_by: ReferencedByDTO | Unset
        if isinstance(_referenced_by, Unset):
            referenced_by = UNSET
        else:
            referenced_by = ReferencedByDTO.from_dict(_referenced_by)

        _tags = d.pop("tags", UNSET)
        tags: FilesFilterPropertiesDTOTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = FilesFilterPropertiesDTOTags.from_dict(_tags)

        files_filter_properties_dto = cls(
            filter_type=filter_type,
            file_usage=file_usage,
            created_by=created_by,
            referenced_by=referenced_by,
            tags=tags,
        )

        files_filter_properties_dto.additional_properties = d
        return files_filter_properties_dto

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
