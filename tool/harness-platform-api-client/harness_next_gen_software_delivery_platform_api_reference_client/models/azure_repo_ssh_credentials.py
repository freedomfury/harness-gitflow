from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AzureRepoSshCredentials")


@_attrs_define
class AzureRepoSshCredentials:
    """This contains details of the AzureRepo credentials used via SSH connections

    Attributes:
        ssh_key_ref (str):
    """

    ssh_key_ref: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssh_key_ref = self.ssh_key_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sshKeyRef": ssh_key_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ssh_key_ref = d.pop("sshKeyRef")

        azure_repo_ssh_credentials = cls(
            ssh_key_ref=ssh_key_ref,
        )

        azure_repo_ssh_credentials.additional_properties = d
        return azure_repo_ssh_credentials

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
