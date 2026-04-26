from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_repository_core import TypesRepositoryCore
    from ..models.types_space_core import TypesSpaceCore


T = TypeVar("T", bound="TypesScopeData")


@_attrs_define
class TypesScopeData:
    """
    Attributes:
        repository (TypesRepositoryCore | Unset):
        scope (int | Unset):
        space (TypesSpaceCore | Unset):
    """

    repository: TypesRepositoryCore | Unset = UNSET
    scope: int | Unset = UNSET
    space: TypesSpaceCore | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        scope = self.scope

        space: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space, Unset):
            space = self.space.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repository is not UNSET:
            field_dict["repository"] = repository
        if scope is not UNSET:
            field_dict["scope"] = scope
        if space is not UNSET:
            field_dict["space"] = space

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_repository_core import TypesRepositoryCore
        from ..models.types_space_core import TypesSpaceCore

        d = dict(src_dict)
        _repository = d.pop("repository", UNSET)
        repository: TypesRepositoryCore | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = TypesRepositoryCore.from_dict(_repository)

        scope = d.pop("scope", UNSET)

        _space = d.pop("space", UNSET)
        space: TypesSpaceCore | Unset
        if isinstance(_space, Unset):
            space = UNSET
        else:
            space = TypesSpaceCore.from_dict(_space)

        types_scope_data = cls(
            repository=repository,
            scope=scope,
            space=space,
        )

        types_scope_data.additional_properties = d
        return types_scope_data

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
