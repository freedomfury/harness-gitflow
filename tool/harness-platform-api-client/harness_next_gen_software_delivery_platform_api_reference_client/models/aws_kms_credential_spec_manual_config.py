from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AwsKmsCredentialSpecManualConfig")


@_attrs_define
class AwsKmsCredentialSpecManualConfig:
    """This contains the AWS KMS Secret Manager's secret reference access key and secret key.

    Attributes:
        access_key (str): Access Key for AWS authentication.
        secret_key (str): Secret Key for AWS authentication.
    """

    access_key: str
    secret_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        secret_key = self.secret_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessKey": access_key,
                "secretKey": secret_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("accessKey")

        secret_key = d.pop("secretKey")

        aws_kms_credential_spec_manual_config = cls(
            access_key=access_key,
            secret_key=secret_key,
        )

        aws_kms_credential_spec_manual_config.additional_properties = d
        return aws_kms_credential_spec_manual_config

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
