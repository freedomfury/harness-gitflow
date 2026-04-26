from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_now_ticket_key_ng_ticket_fields import ServiceNowTicketKeyNGTicketFields


T = TypeVar("T", bound="ServiceNowTicketKeyNG")


@_attrs_define
class ServiceNowTicketKeyNG:
    """
    Attributes:
        url (str):
        key (str):
        ticket_type (str):
        ticket_fields (ServiceNowTicketKeyNGTicketFields | Unset):
    """

    url: str
    key: str
    ticket_type: str
    ticket_fields: ServiceNowTicketKeyNGTicketFields | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        key = self.key

        ticket_type = self.ticket_type

        ticket_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ticket_fields, Unset):
            ticket_fields = self.ticket_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "key": key,
                "ticketType": ticket_type,
            }
        )
        if ticket_fields is not UNSET:
            field_dict["ticketFields"] = ticket_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_now_ticket_key_ng_ticket_fields import ServiceNowTicketKeyNGTicketFields

        d = dict(src_dict)
        url = d.pop("url")

        key = d.pop("key")

        ticket_type = d.pop("ticketType")

        _ticket_fields = d.pop("ticketFields", UNSET)
        ticket_fields: ServiceNowTicketKeyNGTicketFields | Unset
        if isinstance(_ticket_fields, Unset):
            ticket_fields = UNSET
        else:
            ticket_fields = ServiceNowTicketKeyNGTicketFields.from_dict(_ticket_fields)

        service_now_ticket_key_ng = cls(
            url=url,
            key=key,
            ticket_type=ticket_type,
            ticket_fields=ticket_fields,
        )

        service_now_ticket_key_ng.additional_properties = d
        return service_now_ticket_key_ng

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
