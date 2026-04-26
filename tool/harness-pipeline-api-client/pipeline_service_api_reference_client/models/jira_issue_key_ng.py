from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jira_issue_key_ng_ticket_fields import JiraIssueKeyNGTicketFields


T = TypeVar("T", bound="JiraIssueKeyNG")


@_attrs_define
class JiraIssueKeyNG:
    """
    Attributes:
        url (str):
        key (str):
        ticket_fields (JiraIssueKeyNGTicketFields | Unset):
    """

    url: str
    key: str
    ticket_fields: JiraIssueKeyNGTicketFields | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        key = self.key

        ticket_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ticket_fields, Unset):
            ticket_fields = self.ticket_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "key": key,
            }
        )
        if ticket_fields is not UNSET:
            field_dict["ticketFields"] = ticket_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_issue_key_ng_ticket_fields import JiraIssueKeyNGTicketFields

        d = dict(src_dict)
        url = d.pop("url")

        key = d.pop("key")

        _ticket_fields = d.pop("ticketFields", UNSET)
        ticket_fields: JiraIssueKeyNGTicketFields | Unset
        if isinstance(_ticket_fields, Unset):
            ticket_fields = UNSET
        else:
            ticket_fields = JiraIssueKeyNGTicketFields.from_dict(_ticket_fields)

        jira_issue_key_ng = cls(
            url=url,
            key=key,
            ticket_fields=ticket_fields,
        )

        jira_issue_key_ng.additional_properties = d
        return jira_issue_key_ng

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
