from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesPullReqLabel")


@_attrs_define
class TypesPullReqLabel:
    """
    Attributes:
        created (int | Unset):
        created_by (int | Unset):
        label_id (int | Unset):
        pullreq_id (int | Unset):
        updated (int | Unset):
        updated_by (int | Unset):
        value_id (int | None | Unset):
    """

    created: int | Unset = UNSET
    created_by: int | Unset = UNSET
    label_id: int | Unset = UNSET
    pullreq_id: int | Unset = UNSET
    updated: int | Unset = UNSET
    updated_by: int | Unset = UNSET
    value_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_by = self.created_by

        label_id = self.label_id

        pullreq_id = self.pullreq_id

        updated = self.updated

        updated_by = self.updated_by

        value_id: int | None | Unset
        if isinstance(self.value_id, Unset):
            value_id = UNSET
        else:
            value_id = self.value_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if label_id is not UNSET:
            field_dict["label_id"] = label_id
        if pullreq_id is not UNSET:
            field_dict["pullreq_id"] = pullreq_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if value_id is not UNSET:
            field_dict["value_id"] = value_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        created_by = d.pop("created_by", UNSET)

        label_id = d.pop("label_id", UNSET)

        pullreq_id = d.pop("pullreq_id", UNSET)

        updated = d.pop("updated", UNSET)

        updated_by = d.pop("updated_by", UNSET)

        def _parse_value_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        value_id = _parse_value_id(d.pop("value_id", UNSET))

        types_pull_req_label = cls(
            created=created,
            created_by=created_by,
            label_id=label_id,
            pullreq_id=pullreq_id,
            updated=updated,
            updated_by=updated_by,
            value_id=value_id,
        )

        types_pull_req_label.additional_properties = d
        return types_pull_req_label

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
