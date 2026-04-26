from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_check_status import EnumCheckStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_check_payload import TypesCheckPayload


T = TypeVar("T", bound="ReportStatusCheckResultsBody")


@_attrs_define
class ReportStatusCheckResultsBody:
    """
    Attributes:
        check_uid (str | Unset):
        ended (int | Unset):
        identifier (str | Unset):
        link (str | Unset):
        payload (TypesCheckPayload | Unset):
        started (int | Unset):
        status (EnumCheckStatus | Unset):
        summary (str | Unset):
    """

    check_uid: str | Unset = UNSET
    ended: int | Unset = UNSET
    identifier: str | Unset = UNSET
    link: str | Unset = UNSET
    payload: TypesCheckPayload | Unset = UNSET
    started: int | Unset = UNSET
    status: EnumCheckStatus | Unset = UNSET
    summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_uid = self.check_uid

        ended = self.ended

        identifier = self.identifier

        link = self.link

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        started = self.started

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_uid is not UNSET:
            field_dict["check_uid"] = check_uid
        if ended is not UNSET:
            field_dict["ended"] = ended
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if link is not UNSET:
            field_dict["link"] = link
        if payload is not UNSET:
            field_dict["payload"] = payload
        if started is not UNSET:
            field_dict["started"] = started
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_check_payload import TypesCheckPayload

        d = dict(src_dict)
        check_uid = d.pop("check_uid", UNSET)

        ended = d.pop("ended", UNSET)

        identifier = d.pop("identifier", UNSET)

        link = d.pop("link", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: TypesCheckPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = TypesCheckPayload.from_dict(_payload)

        started = d.pop("started", UNSET)

        _status = d.pop("status", UNSET)
        status: EnumCheckStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EnumCheckStatus(_status)

        summary = d.pop("summary", UNSET)

        report_status_check_results_body = cls(
            check_uid=check_uid,
            ended=ended,
            identifier=identifier,
            link=link,
            payload=payload,
            started=started,
            status=status,
            summary=summary,
        )

        report_status_check_results_body.additional_properties = d
        return report_status_check_results_body

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
