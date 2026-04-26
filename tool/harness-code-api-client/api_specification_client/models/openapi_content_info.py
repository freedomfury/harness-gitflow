from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.openapi_content_type import OpenapiContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_commit import TypesCommit


T = TypeVar("T", bound="OpenapiContentInfo")


@_attrs_define
class OpenapiContentInfo:
    """
    Attributes:
        latest_commit (TypesCommit | Unset):
        name (str | Unset):
        path (str | Unset):
        sha (str | Unset):
        type_ (OpenapiContentType | Unset):
    """

    latest_commit: TypesCommit | Unset = UNSET
    name: str | Unset = UNSET
    path: str | Unset = UNSET
    sha: str | Unset = UNSET
    type_: OpenapiContentType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_commit, Unset):
            latest_commit = self.latest_commit.to_dict()

        name = self.name

        path = self.path

        sha = self.sha

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_commit is not UNSET:
            field_dict["latest_commit"] = latest_commit
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if sha is not UNSET:
            field_dict["sha"] = sha
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_commit import TypesCommit

        d = dict(src_dict)
        _latest_commit = d.pop("latest_commit", UNSET)
        latest_commit: TypesCommit | Unset
        if isinstance(_latest_commit, Unset):
            latest_commit = UNSET
        else:
            latest_commit = TypesCommit.from_dict(_latest_commit)

        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        sha = d.pop("sha", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: OpenapiContentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OpenapiContentType(_type_)

        openapi_content_info = cls(
            latest_commit=latest_commit,
            name=name,
            path=path,
            sha=sha,
            type_=type_,
        )

        openapi_content_info.additional_properties = d
        return openapi_content_info

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
