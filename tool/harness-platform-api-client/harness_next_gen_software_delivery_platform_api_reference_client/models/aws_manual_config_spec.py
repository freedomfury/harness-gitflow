from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsManualConfigSpec")


@_attrs_define
class AwsManualConfigSpec:
    """This contains AWS manual credentials connector spec

    Attributes:
        secret_key_ref (str):
        access_key (str | Unset):
        access_key_ref (str | Unset):
        session_token_ref (str | Unset):
    """

    secret_key_ref: str
    access_key: str | Unset = UNSET
    access_key_ref: str | Unset = UNSET
    session_token_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_key_ref = self.secret_key_ref

        access_key = self.access_key

        access_key_ref = self.access_key_ref

        session_token_ref = self.session_token_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secretKeyRef": secret_key_ref,
            }
        )
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if access_key_ref is not UNSET:
            field_dict["accessKeyRef"] = access_key_ref
        if session_token_ref is not UNSET:
            field_dict["sessionTokenRef"] = session_token_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret_key_ref = d.pop("secretKeyRef")

        access_key = d.pop("accessKey", UNSET)

        access_key_ref = d.pop("accessKeyRef", UNSET)

        session_token_ref = d.pop("sessionTokenRef", UNSET)

        aws_manual_config_spec = cls(
            secret_key_ref=secret_key_ref,
            access_key=access_key,
            access_key_ref=access_key_ref,
            session_token_ref=session_token_ref,
        )

        aws_manual_config_spec.additional_properties = d
        return aws_manual_config_spec

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
