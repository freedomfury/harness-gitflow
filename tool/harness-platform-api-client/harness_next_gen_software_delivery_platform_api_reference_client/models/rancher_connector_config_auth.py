from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rancher_authentication import RancherAuthentication


T = TypeVar("T", bound="RancherConnectorConfigAuth")


@_attrs_define
class RancherConnectorConfigAuth:
    """This contains rancher connector authentication details

    Attributes:
        rancher_url (str):
        auth (RancherAuthentication): This contains rancher authentication details
    """

    rancher_url: str
    auth: RancherAuthentication
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rancher_url = self.rancher_url

        auth = self.auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rancherUrl": rancher_url,
                "auth": auth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rancher_authentication import RancherAuthentication

        d = dict(src_dict)
        rancher_url = d.pop("rancherUrl")

        auth = RancherAuthentication.from_dict(d.pop("auth"))

        rancher_connector_config_auth = cls(
            rancher_url=rancher_url,
            auth=auth,
        )

        rancher_connector_config_auth.additional_properties = d
        return rancher_connector_config_auth

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
