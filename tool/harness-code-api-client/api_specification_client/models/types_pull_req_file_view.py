from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesPullReqFileView")


@_attrs_define
class TypesPullReqFileView:
    """
    Attributes:
        obsolete (bool | Unset):
        path (str | Unset):
        sha (str | Unset):
    """

    obsolete: bool | Unset = UNSET
    path: str | Unset = UNSET
    sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        obsolete = self.obsolete

        path = self.path

        sha = self.sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obsolete is not UNSET:
            field_dict["obsolete"] = obsolete
        if path is not UNSET:
            field_dict["path"] = path
        if sha is not UNSET:
            field_dict["sha"] = sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        obsolete = d.pop("obsolete", UNSET)

        path = d.pop("path", UNSET)

        sha = d.pop("sha", UNSET)

        types_pull_req_file_view = cls(
            obsolete=obsolete,
            path=path,
            sha=sha,
        )

        types_pull_req_file_view.additional_properties = d
        return types_pull_req_file_view

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
