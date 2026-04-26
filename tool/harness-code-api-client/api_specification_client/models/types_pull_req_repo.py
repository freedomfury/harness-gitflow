from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_pull_req import TypesPullReq
    from ..models.types_repository_core import TypesRepositoryCore


T = TypeVar("T", bound="TypesPullReqRepo")


@_attrs_define
class TypesPullReqRepo:
    """
    Attributes:
        pull_request (TypesPullReq | Unset):
        repository (TypesRepositoryCore | Unset):
    """

    pull_request: TypesPullReq | Unset = UNSET
    repository: TypesRepositoryCore | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pull_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pull_request, Unset):
            pull_request = self.pull_request.to_dict()

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pull_request is not UNSET:
            field_dict["pull_request"] = pull_request
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_pull_req import TypesPullReq
        from ..models.types_repository_core import TypesRepositoryCore

        d = dict(src_dict)
        _pull_request = d.pop("pull_request", UNSET)
        pull_request: TypesPullReq | Unset
        if isinstance(_pull_request, Unset):
            pull_request = UNSET
        else:
            pull_request = TypesPullReq.from_dict(_pull_request)

        _repository = d.pop("repository", UNSET)
        repository: TypesRepositoryCore | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = TypesRepositoryCore.from_dict(_repository)

        types_pull_req_repo = cls(
            pull_request=pull_request,
            repository=repository,
        )

        types_pull_req_repo.additional_properties = d
        return types_pull_req_repo

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
