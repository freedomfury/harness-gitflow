from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ssh_auth_type import SSHAuthType, check_ssh_auth_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_ssh_spec import BaseSSHSpec


T = TypeVar("T", bound="SSHAuth")


@_attrs_define
class SSHAuth:
    """This is the SSH Authentication specification defined in Harness.

    Attributes:
        spec (BaseSSHSpec): This is the SSH specification details as defined in Harness.
        type_ (SSHAuthType): Specifies authentication scheme, SSH or Kerberos
        use_ssh_client (bool | Unset):
        use_sshj (bool | Unset):
    """

    spec: BaseSSHSpec
    type_: SSHAuthType
    use_ssh_client: bool | Unset = UNSET
    use_sshj: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spec = self.spec.to_dict()

        type_: str = self.type_

        use_ssh_client = self.use_ssh_client

        use_sshj = self.use_sshj

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spec": spec,
                "type": type_,
            }
        )
        if use_ssh_client is not UNSET:
            field_dict["useSshClient"] = use_ssh_client
        if use_sshj is not UNSET:
            field_dict["useSshj"] = use_sshj

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_ssh_spec import BaseSSHSpec

        d = dict(src_dict)
        spec = BaseSSHSpec.from_dict(d.pop("spec"))

        type_ = check_ssh_auth_type(d.pop("type"))

        use_ssh_client = d.pop("useSshClient", UNSET)

        use_sshj = d.pop("useSshj", UNSET)

        ssh_auth = cls(
            spec=spec,
            type_=type_,
            use_ssh_client=use_ssh_client,
            use_sshj=use_sshj,
        )

        ssh_auth.additional_properties = d
        return ssh_auth

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
