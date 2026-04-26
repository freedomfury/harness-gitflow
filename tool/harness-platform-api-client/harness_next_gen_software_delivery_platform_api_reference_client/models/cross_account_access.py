from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrossAccountAccess")


@_attrs_define
class CrossAccountAccess:
    """This contains AWS connector cross account access details

    Attributes:
        cross_account_role_arn (str):
        external_id (str | Unset):
        assume_role_session_duration (int | Unset): Session duration in seconds for assumed role
    """

    cross_account_role_arn: str
    external_id: str | Unset = UNSET
    assume_role_session_duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cross_account_role_arn = self.cross_account_role_arn

        external_id = self.external_id

        assume_role_session_duration = self.assume_role_session_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "crossAccountRoleArn": cross_account_role_arn,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if assume_role_session_duration is not UNSET:
            field_dict["assumeRoleSessionDuration"] = assume_role_session_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cross_account_role_arn = d.pop("crossAccountRoleArn")

        external_id = d.pop("externalId", UNSET)

        assume_role_session_duration = d.pop("assumeRoleSessionDuration", UNSET)

        cross_account_access = cls(
            cross_account_role_arn=cross_account_role_arn,
            external_id=external_id,
            assume_role_session_duration=assume_role_session_duration,
        )

        cross_account_access.additional_properties = d
        return cross_account_access

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
