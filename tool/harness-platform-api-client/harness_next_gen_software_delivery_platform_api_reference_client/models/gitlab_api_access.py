from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gitlab_api_access_type import GitlabApiAccessType, check_gitlab_api_access_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gitlab_api_access_spec import GitlabApiAccessSpec


T = TypeVar("T", bound="GitlabApiAccess")


@_attrs_define
class GitlabApiAccess:
    """This contains details of the information needed for Gitlab API access

    Attributes:
        type_ (GitlabApiAccessType):
        spec (GitlabApiAccessSpec | Unset): This contains details of the information such as references of username and
            password needed for Gitlab API access
    """

    type_: GitlabApiAccessType
    spec: GitlabApiAccessSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gitlab_api_access_spec import GitlabApiAccessSpec

        d = dict(src_dict)
        type_ = check_gitlab_api_access_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: GitlabApiAccessSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = GitlabApiAccessSpec.from_dict(_spec)

        gitlab_api_access = cls(
            type_=type_,
            spec=spec,
        )

        gitlab_api_access.additional_properties = d
        return gitlab_api_access

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
