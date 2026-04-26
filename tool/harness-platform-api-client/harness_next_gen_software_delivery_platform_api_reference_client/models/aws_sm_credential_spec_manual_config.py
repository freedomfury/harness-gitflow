from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsSMCredentialSpecManualConfig")


@_attrs_define
class AwsSMCredentialSpecManualConfig:
    """Returns secret reference access key and secret key of AWS Secret Manager.

    Attributes:
        secret_key (str): Secret Key for AWS authentication.
        access_key (str | Unset): Access Key for AWS authentication.
        access_key_plain_text (str | Unset): Access Key for AWS authentication as plain text.
    """

    secret_key: str
    access_key: str | Unset = UNSET
    access_key_plain_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_key = self.secret_key

        access_key = self.access_key

        access_key_plain_text = self.access_key_plain_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secretKey": secret_key,
            }
        )
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if access_key_plain_text is not UNSET:
            field_dict["accessKeyPlainText"] = access_key_plain_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret_key = d.pop("secretKey")

        access_key = d.pop("accessKey", UNSET)

        access_key_plain_text = d.pop("accessKeyPlainText", UNSET)

        aws_sm_credential_spec_manual_config = cls(
            secret_key=secret_key,
            access_key=access_key,
            access_key_plain_text=access_key_plain_text,
        )

        aws_sm_credential_spec_manual_config.additional_properties = d
        return aws_sm_credential_spec_manual_config

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
