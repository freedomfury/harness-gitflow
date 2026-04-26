from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_content_encoding_type import EnumContentEncodingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepoFileContent")


@_attrs_define
class RepoFileContent:
    """
    Attributes:
        data (str | Unset):
        data_size (int | Unset):
        encoding (EnumContentEncodingType | Unset):
        lfs_object_id (str | Unset):
        lfs_object_size (int | Unset):
        size (int | Unset):
    """

    data: str | Unset = UNSET
    data_size: int | Unset = UNSET
    encoding: EnumContentEncodingType | Unset = UNSET
    lfs_object_id: str | Unset = UNSET
    lfs_object_size: int | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        data_size = self.data_size

        encoding: str | Unset = UNSET
        if not isinstance(self.encoding, Unset):
            encoding = self.encoding.value

        lfs_object_id = self.lfs_object_id

        lfs_object_size = self.lfs_object_size

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if data_size is not UNSET:
            field_dict["data_size"] = data_size
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if lfs_object_id is not UNSET:
            field_dict["lfs_object_id"] = lfs_object_id
        if lfs_object_size is not UNSET:
            field_dict["lfs_object_size"] = lfs_object_size
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        data_size = d.pop("data_size", UNSET)

        _encoding = d.pop("encoding", UNSET)
        encoding: EnumContentEncodingType | Unset
        if isinstance(_encoding, Unset):
            encoding = UNSET
        else:
            encoding = EnumContentEncodingType(_encoding)

        lfs_object_id = d.pop("lfs_object_id", UNSET)

        lfs_object_size = d.pop("lfs_object_size", UNSET)

        size = d.pop("size", UNSET)

        repo_file_content = cls(
            data=data,
            data_size=data_size,
            encoding=encoding,
            lfs_object_id=lfs_object_id,
            lfs_object_size=lfs_object_size,
            size=size,
        )

        repo_file_content.additional_properties = d
        return repo_file_content

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
