from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_node_file_usage import FileNodeFileUsage, check_file_node_file_usage
from ..models.file_store_node_type import FileStoreNodeType, check_file_store_node_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO
    from ..models.ng_tag import NGTag


T = TypeVar("T", bound="FileNode")


@_attrs_define
class FileNode:
    """This contains file details

    Attributes:
        identifier (str): Identifier of the File Store Node
        name (str): Name of the File Store Node
        type_ (FileStoreNodeType): Type of the File Store Node
        file_usage (FileNodeFileUsage): File usage of the File Store Node
        parent_identifier (str | Unset): Parent identifier of the File Store Node
        path (str | Unset): Path of the file or folder
        last_modified_at (int | Unset): Last modified time for the File Store Node
        last_modified_by (EmbeddedUserDetailsDTO | Unset): Updated by user details
        description (str | Unset): Description of the File Store Node
        tags (list[NGTag] | Unset): Tags of the File Store Node
        mime_type (str | Unset): Mime type of the File Store Node
        content (str | Unset): Content of the file
        size (int | Unset): The size of the file
    """

    identifier: str
    name: str
    type_: FileStoreNodeType
    file_usage: FileNodeFileUsage
    parent_identifier: str | Unset = UNSET
    path: str | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    last_modified_by: EmbeddedUserDetailsDTO | Unset = UNSET
    description: str | Unset = UNSET
    tags: list[NGTag] | Unset = UNSET
    mime_type: str | Unset = UNSET
    content: str | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        type_: str = self.type_

        file_usage: str = self.file_usage

        parent_identifier = self.parent_identifier

        path = self.path

        last_modified_at = self.last_modified_at

        last_modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modified_by, Unset):
            last_modified_by = self.last_modified_by.to_dict()

        description = self.description

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        mime_type = self.mime_type

        content = self.content

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
                "type": type_,
                "fileUsage": file_usage,
            }
        )
        if parent_identifier is not UNSET:
            field_dict["parentIdentifier"] = parent_identifier
        if path is not UNSET:
            field_dict["path"] = path
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if content is not UNSET:
            field_dict["content"] = content
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO
        from ..models.ng_tag import NGTag

        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        type_ = check_file_store_node_type(d.pop("type"))

        file_usage = check_file_node_file_usage(d.pop("fileUsage"))

        parent_identifier = d.pop("parentIdentifier", UNSET)

        path = d.pop("path", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        _last_modified_by = d.pop("lastModifiedBy", UNSET)
        last_modified_by: EmbeddedUserDetailsDTO | Unset
        if isinstance(_last_modified_by, Unset):
            last_modified_by = UNSET
        else:
            last_modified_by = EmbeddedUserDetailsDTO.from_dict(_last_modified_by)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[NGTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = NGTag.from_dict(tags_item_data)

                tags.append(tags_item)

        mime_type = d.pop("mimeType", UNSET)

        content = d.pop("content", UNSET)

        size = d.pop("size", UNSET)

        file_node = cls(
            identifier=identifier,
            name=name,
            type_=type_,
            file_usage=file_usage,
            parent_identifier=parent_identifier,
            path=path,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            description=description,
            tags=tags,
            mime_type=mime_type,
            content=content,
            size=size,
        )

        file_node.additional_properties = d
        return file_node

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
