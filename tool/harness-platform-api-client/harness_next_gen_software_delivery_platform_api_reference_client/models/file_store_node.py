from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_store_node_type import FileStoreNodeType, check_file_store_node_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO


T = TypeVar("T", bound="FileStoreNode")


@_attrs_define
class FileStoreNode:
    """This is the view of the file store node entity defined in Harness

    Attributes:
        identifier (str): Identifier of the File Store Node
        name (str): Name of the File Store Node
        type_ (FileStoreNodeType): Type of the File Store Node
        parent_identifier (str | Unset): Parent identifier of the File Store Node
        path (str | Unset): Path of the file or folder
        last_modified_at (int | Unset): Last modified time for the File Store Node
        last_modified_by (EmbeddedUserDetailsDTO | Unset): Updated by user details
    """

    identifier: str
    name: str
    type_: FileStoreNodeType
    parent_identifier: str | Unset = UNSET
    path: str | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    last_modified_by: EmbeddedUserDetailsDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        type_: str = self.type_

        parent_identifier = self.parent_identifier

        path = self.path

        last_modified_at = self.last_modified_at

        last_modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modified_by, Unset):
            last_modified_by = self.last_modified_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
                "type": type_,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_user_details_dto import EmbeddedUserDetailsDTO

        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        type_ = check_file_store_node_type(d.pop("type"))

        parent_identifier = d.pop("parentIdentifier", UNSET)

        path = d.pop("path", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        _last_modified_by = d.pop("lastModifiedBy", UNSET)
        last_modified_by: EmbeddedUserDetailsDTO | Unset
        if isinstance(_last_modified_by, Unset):
            last_modified_by = UNSET
        else:
            last_modified_by = EmbeddedUserDetailsDTO.from_dict(_last_modified_by)

        file_store_node = cls(
            identifier=identifier,
            name=name,
            type_=type_,
            parent_identifier=parent_identifier,
            path=path,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
        )

        file_store_node.additional_properties = d
        return file_store_node

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
