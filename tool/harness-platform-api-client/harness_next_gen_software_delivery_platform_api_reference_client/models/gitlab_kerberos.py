from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GitlabKerberos")


@_attrs_define
class GitlabKerberos:
    """This contains details of the Gitlab credentials Specs such as references of Keberos key

    Attributes:
        kerberos_key_ref (str):
    """

    kerberos_key_ref: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kerberos_key_ref = self.kerberos_key_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kerberosKeyRef": kerberos_key_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kerberos_key_ref = d.pop("kerberosKeyRef")

        gitlab_kerberos = cls(
            kerberos_key_ref=kerberos_key_ref,
        )

        gitlab_kerberos.additional_properties = d
        return gitlab_kerberos

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
