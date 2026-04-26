from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_commit import TypesCommit


T = TypeVar("T", bound="TypesPathDetails")


@_attrs_define
class TypesPathDetails:
    """
    Attributes:
        last_commit (TypesCommit | Unset):
        path (str | Unset):
    """

    last_commit: TypesCommit | Unset = UNSET
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_commit, Unset):
            last_commit = self.last_commit.to_dict()

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_commit is not UNSET:
            field_dict["last_commit"] = last_commit
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_commit import TypesCommit

        d = dict(src_dict)
        _last_commit = d.pop("last_commit", UNSET)
        last_commit: TypesCommit | Unset
        if isinstance(_last_commit, Unset):
            last_commit = UNSET
        else:
            last_commit = TypesCommit.from_dict(_last_commit)

        path = d.pop("path", UNSET)

        types_path_details = cls(
            last_commit=last_commit,
            path=path,
        )

        types_path_details.additional_properties = d
        return types_path_details

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
