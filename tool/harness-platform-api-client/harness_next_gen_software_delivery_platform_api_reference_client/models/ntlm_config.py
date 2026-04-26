from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NTLMConfig")


@_attrs_define
class NTLMConfig:
    """This is the NTLM configuration details defined in Harness.

    Attributes:
        type_ (str):
        domain (str): This is the NTLM domain name.
        username (str): This is the NTLM user name.
        password (str):
        use_ssl (bool | Unset): This is the NTLM either to use SSL/https .
        skip_cert_checks (bool | Unset): This is the NTLM either to skip certificate checks .
        use_no_profile (bool | Unset): This is the NTLM powershell runs without loading profile .
    """

    type_: str
    domain: str
    username: str
    password: str
    use_ssl: bool | Unset = UNSET
    skip_cert_checks: bool | Unset = UNSET
    use_no_profile: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        domain = self.domain

        username = self.username

        password = self.password

        use_ssl = self.use_ssl

        skip_cert_checks = self.skip_cert_checks

        use_no_profile = self.use_no_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "domain": domain,
                "username": username,
                "password": password,
            }
        )
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl
        if skip_cert_checks is not UNSET:
            field_dict["skipCertChecks"] = skip_cert_checks
        if use_no_profile is not UNSET:
            field_dict["useNoProfile"] = use_no_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        domain = d.pop("domain")

        username = d.pop("username")

        password = d.pop("password")

        use_ssl = d.pop("useSSL", UNSET)

        skip_cert_checks = d.pop("skipCertChecks", UNSET)

        use_no_profile = d.pop("useNoProfile", UNSET)

        ntlm_config = cls(
            type_=type_,
            domain=domain,
            username=username,
            password=password,
            use_ssl=use_ssl,
            skip_cert_checks=skip_cert_checks,
            use_no_profile=use_no_profile,
        )

        ntlm_config.additional_properties = d
        return ntlm_config

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
