from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_mtls_endpoint_details_mode import (
    AgentMtlsEndpointDetailsMode,
    check_agent_mtls_endpoint_details_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentMtlsEndpointDetails")


@_attrs_define
class AgentMtlsEndpointDetails:
    """
    Attributes:
        uuid (str | Unset):
        account_id (str | Unset):
        fqdn (str | Unset):
        ca_certificates (str | Unset):
        mode (AgentMtlsEndpointDetailsMode | Unset):
    """

    uuid: str | Unset = UNSET
    account_id: str | Unset = UNSET
    fqdn: str | Unset = UNSET
    ca_certificates: str | Unset = UNSET
    mode: AgentMtlsEndpointDetailsMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        account_id = self.account_id

        fqdn = self.fqdn

        ca_certificates = self.ca_certificates

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if ca_certificates is not UNSET:
            field_dict["caCertificates"] = ca_certificates
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        account_id = d.pop("accountId", UNSET)

        fqdn = d.pop("fqdn", UNSET)

        ca_certificates = d.pop("caCertificates", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: AgentMtlsEndpointDetailsMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_agent_mtls_endpoint_details_mode(_mode)

        agent_mtls_endpoint_details = cls(
            uuid=uuid,
            account_id=account_id,
            fqdn=fqdn,
            ca_certificates=ca_certificates,
            mode=mode,
        )

        agent_mtls_endpoint_details.additional_properties = d
        return agent_mtls_endpoint_details

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
