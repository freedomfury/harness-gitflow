from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsKmsCredentialSpecAssumeSTS")


@_attrs_define
class AwsKmsCredentialSpecAssumeSTS:
    """Returns Delegate selectors, Role ARN and STS role duration used by AWS KMS Secret Manager.

    Attributes:
        delegate_selectors (list[str]): List of Delegate Selectors that belong to the same Delegate and are used to
            connect to the Secret Manager.
        role_arn (str): Role ARN for the Delegate with STS Role.
        external_name (str | Unset): External Name.
        assume_sts_role_duration (int | Unset): This is the time duration for STS Role.
    """

    delegate_selectors: list[str]
    role_arn: str
    external_name: str | Unset = UNSET
    assume_sts_role_duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delegate_selectors = self.delegate_selectors

        role_arn = self.role_arn

        external_name = self.external_name

        assume_sts_role_duration = self.assume_sts_role_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delegateSelectors": delegate_selectors,
                "roleArn": role_arn,
            }
        )
        if external_name is not UNSET:
            field_dict["externalName"] = external_name
        if assume_sts_role_duration is not UNSET:
            field_dict["assumeStsRoleDuration"] = assume_sts_role_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delegate_selectors = cast(list[str], d.pop("delegateSelectors"))

        role_arn = d.pop("roleArn")

        external_name = d.pop("externalName", UNSET)

        assume_sts_role_duration = d.pop("assumeStsRoleDuration", UNSET)

        aws_kms_credential_spec_assume_sts = cls(
            delegate_selectors=delegate_selectors,
            role_arn=role_arn,
            external_name=external_name,
            assume_sts_role_duration=assume_sts_role_duration,
        )

        aws_kms_credential_spec_assume_sts.additional_properties = d
        return aws_kms_credential_spec_assume_sts

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
