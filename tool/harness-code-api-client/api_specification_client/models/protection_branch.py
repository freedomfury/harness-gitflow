from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_def_branch_lifecycle import ProtectionDefBranchLifecycle
    from ..models.protection_def_bypass import ProtectionDefBypass
    from ..models.protection_def_pull_req import ProtectionDefPullReq


T = TypeVar("T", bound="ProtectionBranch")


@_attrs_define
class ProtectionBranch:
    """
    Attributes:
        bypass (ProtectionDefBypass | Unset):
        lifecycle (ProtectionDefBranchLifecycle | Unset):
        pullreq (ProtectionDefPullReq | Unset):
    """

    bypass: ProtectionDefBypass | Unset = UNSET
    lifecycle: ProtectionDefBranchLifecycle | Unset = UNSET
    pullreq: ProtectionDefPullReq | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypass: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bypass, Unset):
            bypass = self.bypass.to_dict()

        lifecycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.to_dict()

        pullreq: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pullreq, Unset):
            pullreq = self.pullreq.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypass is not UNSET:
            field_dict["bypass"] = bypass
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if pullreq is not UNSET:
            field_dict["pullreq"] = pullreq

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_def_branch_lifecycle import ProtectionDefBranchLifecycle
        from ..models.protection_def_bypass import ProtectionDefBypass
        from ..models.protection_def_pull_req import ProtectionDefPullReq

        d = dict(src_dict)
        _bypass = d.pop("bypass", UNSET)
        bypass: ProtectionDefBypass | Unset
        if isinstance(_bypass, Unset):
            bypass = UNSET
        else:
            bypass = ProtectionDefBypass.from_dict(_bypass)

        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: ProtectionDefBranchLifecycle | Unset
        if isinstance(_lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = ProtectionDefBranchLifecycle.from_dict(_lifecycle)

        _pullreq = d.pop("pullreq", UNSET)
        pullreq: ProtectionDefPullReq | Unset
        if isinstance(_pullreq, Unset):
            pullreq = UNSET
        else:
            pullreq = ProtectionDefPullReq.from_dict(_pullreq)

        protection_branch = cls(
            bypass=bypass,
            lifecycle=lifecycle,
            pullreq=pullreq,
        )

        protection_branch.additional_properties = d
        return protection_branch

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
