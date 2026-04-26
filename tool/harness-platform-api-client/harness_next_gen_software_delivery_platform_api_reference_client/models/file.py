from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_type import FileType, check_file_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO
    from ..models.ng_tag import NGTag


T = TypeVar("T", bound="File")


@_attrs_define
class File:
    """This is details of the File or Folder entity defined in Harness.

    Attributes:
        name (str): Name of the File or Folder
        type_ (FileType): This specifies the type of the File
        parent_identifier (str): This specifies parent directory identifier. The value of Root directory identifier is
            Root.
        account_identifier (str | Unset): Account Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        identifier (str | Unset): Identifier of the File or Folder
        file_usage (str | Unset): This specifies the file usage
        description (str | Unset): Description of the File or Folder
        tags (list[NGTag] | Unset): Tags
        mime_type (str | Unset): Mime type of the File
        path (str | Unset): The path of the File or Folder
        draft (bool | Unset): Whether File is draft or not
        created_by (EmbeddedUserDetailsDTO | Unset): Updated by user details
        last_modified_by (EmbeddedUserDetailsDTO | Unset): Updated by user details
        last_modified_at (int | Unset): Last modified time for the File or Folder
    """

    name: str
    type_: FileType
    parent_identifier: str
    account_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    identifier: str | Unset = UNSET
    file_usage: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: list[NGTag] | Unset = UNSET
    mime_type: str | Unset = UNSET
    path: str | Unset = UNSET
    draft: bool | Unset = UNSET
    created_by: EmbeddedUserDetailsDTO | Unset = UNSET
    last_modified_by: EmbeddedUserDetailsDTO | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str = self.type_

        parent_identifier = self.parent_identifier

        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        identifier = self.identifier

        file_usage = self.file_usage

        description = self.description

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        mime_type = self.mime_type

        path = self.path

        draft = self.draft

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        last_modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modified_by, Unset):
            last_modified_by = self.last_modified_by.to_dict()

        last_modified_at = self.last_modified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "parentIdentifier": parent_identifier,
            }
        )
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if file_usage is not UNSET:
            field_dict["fileUsage"] = file_usage
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if path is not UNSET:
            field_dict["path"] = path
        if draft is not UNSET:
            field_dict["draft"] = draft
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO
        from ..models.ng_tag import NGTag

        d = dict(src_dict)
        name = d.pop("name")

        type_ = check_file_type(d.pop("type"))

        parent_identifier = d.pop("parentIdentifier")

        account_identifier = d.pop("accountIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        identifier = d.pop("identifier", UNSET)

        file_usage = d.pop("fileUsage", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[NGTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = NGTag.from_dict(tags_item_data)

                tags.append(tags_item)

        mime_type = d.pop("mimeType", UNSET)

        path = d.pop("path", UNSET)

        draft = d.pop("draft", UNSET)

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

        file = cls(
            name=name,
            type_=type_,
            parent_identifier=parent_identifier,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            identifier=identifier,
            file_usage=file_usage,
            description=description,
            tags=tags,
            mime_type=mime_type,
            path=path,
            draft=draft,
            created_by=created_by,
            last_modified_by=last_modified_by,
            last_modified_at=last_modified_at,
        )

        file.additional_properties = d
        return file

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
