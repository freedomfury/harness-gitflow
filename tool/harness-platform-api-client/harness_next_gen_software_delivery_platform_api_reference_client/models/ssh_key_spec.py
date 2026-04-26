from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssh_auth import SSHAuth


T = TypeVar("T", bound="SSHKeySpec")


@_attrs_define
class SSHKeySpec:
    """This is the SSH key authentication details defined in Harness.

    Attributes:
        type_ (str):
        auth (SSHAuth): This is the SSH Authentication specification defined in Harness.
        error_message_for_invalid_yaml (str | Unset):
        port (int | Unset): SSH port
    """

    type_: str
    auth: SSHAuth
    error_message_for_invalid_yaml: str | Unset = UNSET
    port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        auth = self.auth.to_dict()

        error_message_for_invalid_yaml = self.error_message_for_invalid_yaml

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "auth": auth,
            }
        )
        if error_message_for_invalid_yaml is not UNSET:
            field_dict["errorMessageForInvalidYaml"] = error_message_for_invalid_yaml
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ssh_auth import SSHAuth

        d = dict(src_dict)
        type_ = d.pop("type")

        auth = SSHAuth.from_dict(d.pop("auth"))

        error_message_for_invalid_yaml = d.pop("errorMessageForInvalidYaml", UNSET)

        port = d.pop("port", UNSET)

        ssh_key_spec = cls(
            type_=type_,
            auth=auth,
            error_message_for_invalid_yaml=error_message_for_invalid_yaml,
            port=port,
        )

        ssh_key_spec.additional_properties = d
        return ssh_key_spec

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
