from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AwsOidcSpec")


@_attrs_define
class AwsOidcSpec:
    """This contains AWS OIDC credentials connector spec

    Attributes:
        iam_role_arn (str):
    """

    iam_role_arn: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iam_role_arn = self.iam_role_arn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iamRoleArn": iam_role_arn,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        iam_role_arn = d.pop("iamRoleArn")

        aws_oidc_spec = cls(
            iam_role_arn=iam_role_arn,
        )

        aws_oidc_spec.additional_properties = d
        return aws_oidc_spec

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
