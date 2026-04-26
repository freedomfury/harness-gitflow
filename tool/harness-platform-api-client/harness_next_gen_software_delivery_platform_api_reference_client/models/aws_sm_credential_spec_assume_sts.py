from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsSMCredentialSpecAssumeSTS")


@_attrs_define
class AwsSMCredentialSpecAssumeSTS:
    """Returns credentials for the AWS Secret Manager for the IAM role.

    Attributes:
        role_arn (str): Role ARN for the Delegate with STS Role.
        external_id (str | Unset): External Name.
        assume_sts_role_duration (int | Unset): This is the time duration for STS Role.
    """

    role_arn: str
    external_id: str | Unset = UNSET
    assume_sts_role_duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_arn = self.role_arn

        external_id = self.external_id

        assume_sts_role_duration = self.assume_sts_role_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roleArn": role_arn,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if assume_sts_role_duration is not UNSET:
            field_dict["assumeStsRoleDuration"] = assume_sts_role_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role_arn = d.pop("roleArn")

        external_id = d.pop("externalId", UNSET)

        assume_sts_role_duration = d.pop("assumeStsRoleDuration", UNSET)

        aws_sm_credential_spec_assume_sts = cls(
            role_arn=role_arn,
            external_id=external_id,
            assume_sts_role_duration=assume_sts_role_duration,
        )

        aws_sm_credential_spec_assume_sts.additional_properties = d
        return aws_sm_credential_spec_assume_sts

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
