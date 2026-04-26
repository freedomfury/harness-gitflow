from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aws_code_commit_https_credentials_type import (
    AwsCodeCommitHttpsCredentialsType,
    check_aws_code_commit_https_credentials_type,
)

if TYPE_CHECKING:
    from ..models.aws_code_commit_https_credentials_spec import AwsCodeCommitHttpsCredentialsSpec


T = TypeVar("T", bound="AwsCodeCommitHttpsCredentials")


@_attrs_define
class AwsCodeCommitHttpsCredentials:
    """This contains details of the AWS Code Commit credentials used via HTTPS connections

    Attributes:
        type_ (AwsCodeCommitHttpsCredentialsType):
        spec (AwsCodeCommitHttpsCredentialsSpec): This contains details of the AWS Code Commit credentials specs such as
            references of username and password used via HTTPS connections
    """

    type_: AwsCodeCommitHttpsCredentialsType
    spec: AwsCodeCommitHttpsCredentialsSpec
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
        from ..models.aws_code_commit_https_credentials_spec import AwsCodeCommitHttpsCredentialsSpec

        d = dict(src_dict)
        type_ = check_aws_code_commit_https_credentials_type(d.pop("type"))

        spec = AwsCodeCommitHttpsCredentialsSpec.from_dict(d.pop("spec"))

        aws_code_commit_https_credentials = cls(
            type_=type_,
            spec=spec,
        )

        aws_code_commit_https_credentials.additional_properties = d
        return aws_code_commit_https_credentials

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
