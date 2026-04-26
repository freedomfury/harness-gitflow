from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rancher_authentication_type import RancherAuthenticationType, check_rancher_authentication_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rancher_connector_config_authentication import RancherConnectorConfigAuthentication


T = TypeVar("T", bound="RancherAuthentication")


@_attrs_define
class RancherAuthentication:
    """This contains rancher authentication details

    Attributes:
        type_ (RancherAuthenticationType):
        spec (RancherConnectorConfigAuthentication | Unset): This contains rancher auth credentials
    """

    type_: RancherAuthenticationType
    spec: RancherConnectorConfigAuthentication | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rancher_connector_config_authentication import RancherConnectorConfigAuthentication

        d = dict(src_dict)
        type_ = check_rancher_authentication_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: RancherConnectorConfigAuthentication | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = RancherConnectorConfigAuthentication.from_dict(_spec)

        rancher_authentication = cls(
            type_=type_,
            spec=spec,
        )

        rancher_authentication.additional_properties = d
        return rancher_authentication

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
