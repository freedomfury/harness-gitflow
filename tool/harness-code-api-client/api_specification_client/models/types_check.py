from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_check_status import EnumCheckStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_check_payload import TypesCheckPayload
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0


T = TypeVar("T", bound="TypesCheck")


@_attrs_define
class TypesCheck:
    """
    Attributes:
        created (int | Unset):
        ended (int | Unset):
        id (int | Unset):
        identifier (str | Unset):
        link (str | Unset):
        metadata (Any | Unset):
        payload (TypesCheckPayload | Unset):
        reported_by (None | TypesPrincipalInfoType0 | Unset):
        started (int | Unset):
        status (EnumCheckStatus | Unset):
        summary (str | Unset):
        updated (int | Unset):
    """

    created: int | Unset = UNSET
    ended: int | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    link: str | Unset = UNSET
    metadata: Any | Unset = UNSET
    payload: TypesCheckPayload | Unset = UNSET
    reported_by: None | TypesPrincipalInfoType0 | Unset = UNSET
    started: int | Unset = UNSET
    status: EnumCheckStatus | Unset = UNSET
    summary: str | Unset = UNSET
    updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        created = self.created

        ended = self.ended

        id = self.id

        identifier = self.identifier

        link = self.link

        metadata = self.metadata

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        reported_by: dict[str, Any] | None | Unset
        if isinstance(self.reported_by, Unset):
            reported_by = UNSET
        elif isinstance(self.reported_by, TypesPrincipalInfoType0):
            reported_by = self.reported_by.to_dict()
        else:
            reported_by = self.reported_by

        started = self.started

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        summary = self.summary

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if ended is not UNSET:
            field_dict["ended"] = ended
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if link is not UNSET:
            field_dict["link"] = link
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if payload is not UNSET:
            field_dict["payload"] = payload
        if reported_by is not UNSET:
            field_dict["reported_by"] = reported_by
        if started is not UNSET:
            field_dict["started"] = started
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_check_payload import TypesCheckPayload
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        ended = d.pop("ended", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        link = d.pop("link", UNSET)

        metadata = d.pop("metadata", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: TypesCheckPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = TypesCheckPayload.from_dict(_payload)

        def _parse_reported_by(data: object) -> None | TypesPrincipalInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_types_principal_info_type_0 = TypesPrincipalInfoType0.from_dict(data)

                return componentsschemas_types_principal_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TypesPrincipalInfoType0 | Unset, data)

        reported_by = _parse_reported_by(d.pop("reported_by", UNSET))

        started = d.pop("started", UNSET)

        _status = d.pop("status", UNSET)
        status: EnumCheckStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EnumCheckStatus(_status)

        summary = d.pop("summary", UNSET)

        updated = d.pop("updated", UNSET)

        types_check = cls(
            created=created,
            ended=ended,
            id=id,
            identifier=identifier,
            link=link,
            metadata=metadata,
            payload=payload,
            reported_by=reported_by,
            started=started,
            status=status,
            summary=summary,
            updated=updated,
        )

        types_check.additional_properties = d
        return types_check

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
