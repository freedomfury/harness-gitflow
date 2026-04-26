from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceNowADFS")


@_attrs_define
class ServiceNowADFS:
    """This entity contains the details of the Service Now ADFS

    Attributes:
        certificate_ref (str):
        private_key_ref (str):
        client_id_ref (str):
        resource_id_ref (str):
        adfs_url (str):
    """

    certificate_ref: str
    private_key_ref: str
    client_id_ref: str
    resource_id_ref: str
    adfs_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate_ref = self.certificate_ref

        private_key_ref = self.private_key_ref

        client_id_ref = self.client_id_ref

        resource_id_ref = self.resource_id_ref

        adfs_url = self.adfs_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certificateRef": certificate_ref,
                "privateKeyRef": private_key_ref,
                "clientIdRef": client_id_ref,
                "resourceIdRef": resource_id_ref,
                "adfsUrl": adfs_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate_ref = d.pop("certificateRef")

        private_key_ref = d.pop("privateKeyRef")

        client_id_ref = d.pop("clientIdRef")

        resource_id_ref = d.pop("resourceIdRef")

        adfs_url = d.pop("adfsUrl")

        service_now_adfs = cls(
            certificate_ref=certificate_ref,
            private_key_ref=private_key_ref,
            client_id_ref=client_id_ref,
            resource_id_ref=resource_id_ref,
            adfs_url=adfs_url,
        )

        service_now_adfs.additional_properties = d
        return service_now_adfs

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
