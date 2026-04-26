from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.update_body_type import UpdateBodyType, check_update_body_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO
    from ..models.update_body_content import UpdateBodyContent


T = TypeVar("T", bound="UpdateBody")


@_attrs_define
class UpdateBody:
    """
    Attributes:
        name (str): Name of the File or Folder
        type_ (UpdateBodyType): This specifies the type of the File
        parent_identifier (str): This specifies parent directory identifier. The value of Root directory identifier is
            Root.
        tags (str | Unset): The File or Folder tags. (See example for expected format)
        identifier (str | Unset): Identifier of the File or Folder
        file_usage (str | Unset): This specifies the file usage
        description (str | Unset): Description of the File or Folder
        mime_type (str | Unset): Mime type of the File
        path (str | Unset): The path of the File or Folder
        created_by (EmbeddedUserDetailsDTO | Unset): Updated by user details
        last_modified_by (EmbeddedUserDetailsDTO | Unset): Updated by user details
        last_modified_at (int | Unset): Last modified time for the File or Folder
        content (UpdateBodyContent | Unset): The content of the File as InputStream
    """

    name: str
    type_: UpdateBodyType
    parent_identifier: str
    tags: str | Unset = UNSET
    identifier: str | Unset = UNSET
    file_usage: str | Unset = UNSET
    description: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    path: str | Unset = UNSET
    created_by: EmbeddedUserDetailsDTO | Unset = UNSET
    last_modified_by: EmbeddedUserDetailsDTO | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    content: UpdateBodyContent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str = self.type_

        parent_identifier = self.parent_identifier

        tags = self.tags

        identifier = self.identifier

        file_usage = self.file_usage

        description = self.description

        mime_type = self.mime_type

        path = self.path

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        last_modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modified_by, Unset):
            last_modified_by = self.last_modified_by.to_dict()

        last_modified_at = self.last_modified_at

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "parentIdentifier": parent_identifier,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if file_usage is not UNSET:
            field_dict["fileUsage"] = file_usage
        if description is not UNSET:
            field_dict["description"] = description
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if path is not UNSET:
            field_dict["path"] = path
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("type", (None, str(self.type_).encode(), "text/plain")))

        files.append(("parentIdentifier", (None, str(self.parent_identifier).encode(), "text/plain")))

        if not isinstance(self.tags, Unset):
            files.append(("tags", (None, str(self.tags).encode(), "text/plain")))

        if not isinstance(self.identifier, Unset):
            files.append(("identifier", (None, str(self.identifier).encode(), "text/plain")))

        if not isinstance(self.file_usage, Unset):
            files.append(("fileUsage", (None, str(self.file_usage).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.mime_type, Unset):
            files.append(("mimeType", (None, str(self.mime_type).encode(), "text/plain")))

        if not isinstance(self.path, Unset):
            files.append(("path", (None, str(self.path).encode(), "text/plain")))

        if not isinstance(self.created_by, Unset):
            files.append(("createdBy", (None, json.dumps(self.created_by.to_dict()).encode(), "application/json")))

        if not isinstance(self.last_modified_by, Unset):
            files.append(
                ("lastModifiedBy", (None, json.dumps(self.last_modified_by.to_dict()).encode(), "application/json"))
            )

        if not isinstance(self.last_modified_at, Unset):
            files.append(("lastModifiedAt", (None, str(self.last_modified_at).encode(), "text/plain")))

        if not isinstance(self.content, Unset):
            files.append(("content", (None, json.dumps(self.content.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO
        from ..models.update_body_content import UpdateBodyContent

        d = dict(src_dict)
        name = d.pop("name")

        type_ = check_update_body_type(d.pop("type"))

        parent_identifier = d.pop("parentIdentifier")

        tags = d.pop("tags", UNSET)

        identifier = d.pop("identifier", UNSET)

        file_usage = d.pop("fileUsage", UNSET)

        description = d.pop("description", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        path = d.pop("path", UNSET)

        _created_by = d.pop("createdBy", UNSET)
        created_by: EmbeddedUserDetailsDTO | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = EmbeddedUserDetailsDTO.from_dict(_created_by)

        _last_modified_by = d.pop("lastModifiedBy", UNSET)
        last_modified_by: EmbeddedUserDetailsDTO | Unset
        if isinstance(_last_modified_by, Unset):
            last_modified_by = UNSET
        else:
            last_modified_by = EmbeddedUserDetailsDTO.from_dict(_last_modified_by)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        _content = d.pop("content", UNSET)
        content: UpdateBodyContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = UpdateBodyContent.from_dict(_content)

        update_body = cls(
            name=name,
            type_=type_,
            parent_identifier=parent_identifier,
            tags=tags,
            identifier=identifier,
            file_usage=file_usage,
            description=description,
            mime_type=mime_type,
            path=path,
            created_by=created_by,
            last_modified_by=last_modified_by,
            last_modified_at=last_modified_at,
            content=content,
        )

        update_body.additional_properties = d
        return update_body

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
