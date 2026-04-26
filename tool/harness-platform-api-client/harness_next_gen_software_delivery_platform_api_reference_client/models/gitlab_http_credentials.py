from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gitlab_http_credentials_type import GitlabHttpCredentialsType, check_gitlab_http_credentials_type

if TYPE_CHECKING:
    from ..models.gitlab_http_credentials_spec import GitlabHttpCredentialsSpec


T = TypeVar("T", bound="GitlabHttpCredentials")


@_attrs_define
class GitlabHttpCredentials:
    """This contains details of the Gitlab credentials used via HTTP connections

    Attributes:
        type_ (GitlabHttpCredentialsType):
        spec (GitlabHttpCredentialsSpec): This is a interface for details of the Gitlab credentials Specs such as
            references of username and password
    """

    type_: GitlabHttpCredentialsType
    spec: GitlabHttpCredentialsSpec
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gitlab_http_credentials_spec import GitlabHttpCredentialsSpec

        d = dict(src_dict)
        type_ = check_gitlab_http_credentials_type(d.pop("type"))

        spec = GitlabHttpCredentialsSpec.from_dict(d.pop("spec"))

        gitlab_http_credentials = cls(
            type_=type_,
            spec=spec,
        )

        gitlab_http_credentials.additional_properties = d
        return gitlab_http_credentials

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
