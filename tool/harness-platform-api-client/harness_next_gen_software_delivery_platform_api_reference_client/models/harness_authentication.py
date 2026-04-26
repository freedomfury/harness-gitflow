from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.harness_authentication_type import HarnessAuthenticationType, check_harness_authentication_type

if TYPE_CHECKING:
    from ..models.harness_http_credentials import HarnessHttpCredentials


T = TypeVar("T", bound="HarnessAuthentication")


@_attrs_define
class HarnessAuthentication:
    """This contains details of the information needed for Harness access

    Attributes:
        type_ (HarnessAuthenticationType):
        spec (HarnessHttpCredentials): This contains details of the Harness credentials used via HTTP connections
    """

    type_: HarnessAuthenticationType
    spec: HarnessHttpCredentials
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harness_http_credentials import HarnessHttpCredentials

        d = dict(src_dict)
        type_ = check_harness_authentication_type(d.pop("type"))

        spec = HarnessHttpCredentials.from_dict(d.pop("spec"))

        harness_authentication = cls(
            type_=type_,
            spec=spec,
        )

        harness_authentication.additional_properties = d
        return harness_authentication

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
