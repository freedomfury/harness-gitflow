from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmtpConfig")


@_attrs_define
class SmtpConfig:
    """This has the SMTP configuration details defined in Harness.

    Attributes:
        host (str): This is the host of the SMTP server.
        port (int): This is the port of the SMTP server.
        from_address (str | Unset): From address of the email that needs to be send.
        use_ssl (bool | Unset): Specify whether or not to use SSL certificate.
        start_tls (bool | Unset): Specify whether or not to use TLS.
        username (str | Unset): Username credential to authenticate with SMTP server.
        password (list[str] | Unset): Password credential to authenticate with SMTP server.
        delegate_selectors (list[str] | Unset): List of delegate selectors of delegates used by SMTP server as
            connectivity mode.
    """

    host: str
    port: int
    from_address: str | Unset = UNSET
    use_ssl: bool | Unset = UNSET
    start_tls: bool | Unset = UNSET
    username: str | Unset = UNSET
    password: list[str] | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        from_address = self.from_address

        use_ssl = self.use_ssl

        start_tls = self.start_tls

        username = self.username

        password: list[str] | Unset = UNSET
        if not isinstance(self.password, Unset):
            password = self.password

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "port": port,
            }
        )
        if from_address is not UNSET:
            field_dict["fromAddress"] = from_address
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl
        if start_tls is not UNSET:
            field_dict["startTLS"] = start_tls
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        port = d.pop("port")

        from_address = d.pop("fromAddress", UNSET)

        use_ssl = d.pop("useSSL", UNSET)

        start_tls = d.pop("startTLS", UNSET)

        username = d.pop("username", UNSET)

        password = cast(list[str], d.pop("password", UNSET))

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        smtp_config = cls(
            host=host,
            port=port,
            from_address=from_address,
            use_ssl=use_ssl,
            start_tls=start_tls,
            username=username,
            password=password,
            delegate_selectors=delegate_selectors,
        )

        smtp_config.additional_properties = d
        return smtp_config

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
