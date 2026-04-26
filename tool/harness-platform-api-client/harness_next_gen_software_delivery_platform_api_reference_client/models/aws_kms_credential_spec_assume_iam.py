from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AwsKmsCredentialSpecAssumeIAM")


@_attrs_define
class AwsKmsCredentialSpecAssumeIAM:
    """Returns the Delegate Selectors used by this AWS KMS Secret Manager Connector.

    Attributes:
        delegate_selectors (list[str]): List of Delegate Selectors that belong to the same Delegate and are used to
            connect to the Secret Manager.
    """

    delegate_selectors: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delegate_selectors = self.delegate_selectors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delegateSelectors": delegate_selectors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delegate_selectors = cast(list[str], d.pop("delegateSelectors"))

        aws_kms_credential_spec_assume_iam = cls(
            delegate_selectors=delegate_selectors,
        )

        aws_kms_credential_spec_assume_iam.additional_properties = d
        return aws_kms_credential_spec_assume_iam

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
