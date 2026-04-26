from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ssh_config_credential_type import SSHConfigCredentialType, check_ssh_config_credential_type

if TYPE_CHECKING:
    from ..models.ssh_credential_spec import SSHCredentialSpec


T = TypeVar("T", bound="SSHConfig")


@_attrs_define
class SSHConfig:
    """This is the SSH configuration details defined in Harness.

    Attributes:
        type_ (str):
        credential_type (SSHConfigCredentialType): This specifies SSH credential type as Password, KeyPath or
            KeyReference
        spec (SSHCredentialSpec): This is the SSH credential specification defined in Harness.
    """

    type_: str
    credential_type: SSHConfigCredentialType
    spec: SSHCredentialSpec
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        credential_type: str = self.credential_type

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "credentialType": credential_type,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ssh_credential_spec import SSHCredentialSpec

        d = dict(src_dict)
        type_ = d.pop("type")

        credential_type = check_ssh_config_credential_type(d.pop("credentialType"))

        spec = SSHCredentialSpec.from_dict(d.pop("spec"))

        ssh_config = cls(
            type_=type_,
            credential_type=credential_type,
            spec=spec,
        )

        ssh_config.additional_properties = d
        return ssh_config

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
