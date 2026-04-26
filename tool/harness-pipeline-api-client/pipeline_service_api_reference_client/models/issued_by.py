from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adviser_issuer import AdviserIssuer
    from ..models.manual_issuer import ManualIssuer
    from ..models.system_issuer import SystemIssuer
    from ..models.timeout_issuer import TimeoutIssuer
    from ..models.trigger_issuer import TriggerIssuer


T = TypeVar("T", bound="IssuedBy")


@_attrs_define
class IssuedBy:
    """
    Attributes:
        issue_time (int):
        manual_issuer (ManualIssuer | Unset):
        adviser_issuer (AdviserIssuer | Unset):
        timeout_issuer (TimeoutIssuer | Unset):
        trigger_issuer (TriggerIssuer | Unset):
        system_issuer (SystemIssuer | Unset):
    """

    issue_time: int
    manual_issuer: ManualIssuer | Unset = UNSET
    adviser_issuer: AdviserIssuer | Unset = UNSET
    timeout_issuer: TimeoutIssuer | Unset = UNSET
    trigger_issuer: TriggerIssuer | Unset = UNSET
    system_issuer: SystemIssuer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_time = self.issue_time

        manual_issuer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manual_issuer, Unset):
            manual_issuer = self.manual_issuer.to_dict()

        adviser_issuer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adviser_issuer, Unset):
            adviser_issuer = self.adviser_issuer.to_dict()

        timeout_issuer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timeout_issuer, Unset):
            timeout_issuer = self.timeout_issuer.to_dict()

        trigger_issuer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_issuer, Unset):
            trigger_issuer = self.trigger_issuer.to_dict()

        system_issuer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.system_issuer, Unset):
            system_issuer = self.system_issuer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issueTime": issue_time,
            }
        )
        if manual_issuer is not UNSET:
            field_dict["manualIssuer"] = manual_issuer
        if adviser_issuer is not UNSET:
            field_dict["adviserIssuer"] = adviser_issuer
        if timeout_issuer is not UNSET:
            field_dict["timeoutIssuer"] = timeout_issuer
        if trigger_issuer is not UNSET:
            field_dict["triggerIssuer"] = trigger_issuer
        if system_issuer is not UNSET:
            field_dict["systemIssuer"] = system_issuer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adviser_issuer import AdviserIssuer
        from ..models.manual_issuer import ManualIssuer
        from ..models.system_issuer import SystemIssuer
        from ..models.timeout_issuer import TimeoutIssuer
        from ..models.trigger_issuer import TriggerIssuer

        d = dict(src_dict)
        issue_time = d.pop("issueTime")

        _manual_issuer = d.pop("manualIssuer", UNSET)
        manual_issuer: ManualIssuer | Unset
        if isinstance(_manual_issuer, Unset):
            manual_issuer = UNSET
        else:
            manual_issuer = ManualIssuer.from_dict(_manual_issuer)

        _adviser_issuer = d.pop("adviserIssuer", UNSET)
        adviser_issuer: AdviserIssuer | Unset
        if isinstance(_adviser_issuer, Unset):
            adviser_issuer = UNSET
        else:
            adviser_issuer = AdviserIssuer.from_dict(_adviser_issuer)

        _timeout_issuer = d.pop("timeoutIssuer", UNSET)
        timeout_issuer: TimeoutIssuer | Unset
        if isinstance(_timeout_issuer, Unset):
            timeout_issuer = UNSET
        else:
            timeout_issuer = TimeoutIssuer.from_dict(_timeout_issuer)

        _trigger_issuer = d.pop("triggerIssuer", UNSET)
        trigger_issuer: TriggerIssuer | Unset
        if isinstance(_trigger_issuer, Unset):
            trigger_issuer = UNSET
        else:
            trigger_issuer = TriggerIssuer.from_dict(_trigger_issuer)

        _system_issuer = d.pop("systemIssuer", UNSET)
        system_issuer: SystemIssuer | Unset
        if isinstance(_system_issuer, Unset):
            system_issuer = UNSET
        else:
            system_issuer = SystemIssuer.from_dict(_system_issuer)

        issued_by = cls(
            issue_time=issue_time,
            manual_issuer=manual_issuer,
            adviser_issuer=adviser_issuer,
            timeout_issuer=timeout_issuer,
            trigger_issuer=trigger_issuer,
            system_issuer=system_issuer,
        )

        issued_by.additional_properties = d
        return issued_by

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
