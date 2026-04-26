from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_mtls_endpoint_request_mode import (
    AgentMtlsEndpointRequestMode,
    check_agent_mtls_endpoint_request_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentMtlsEndpointRequest")


@_attrs_define
class AgentMtlsEndpointRequest:
    """
    Attributes:
        domain_prefix (str | Unset):
        ca_certificates (str | Unset):
        mode (AgentMtlsEndpointRequestMode | Unset):
    """

    domain_prefix: str | Unset = UNSET
    ca_certificates: str | Unset = UNSET
    mode: AgentMtlsEndpointRequestMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_prefix = self.domain_prefix

        ca_certificates = self.ca_certificates

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_prefix is not UNSET:
            field_dict["domainPrefix"] = domain_prefix
        if ca_certificates is not UNSET:
            field_dict["caCertificates"] = ca_certificates
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_prefix = d.pop("domainPrefix", UNSET)

        ca_certificates = d.pop("caCertificates", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: AgentMtlsEndpointRequestMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_agent_mtls_endpoint_request_mode(_mode)

        agent_mtls_endpoint_request = cls(
            domain_prefix=domain_prefix,
            ca_certificates=ca_certificates,
            mode=mode,
        )

        agent_mtls_endpoint_request.additional_properties = d
        return agent_mtls_endpoint_request

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
