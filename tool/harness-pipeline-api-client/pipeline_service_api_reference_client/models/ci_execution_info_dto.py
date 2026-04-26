from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ci_pull_request_dto import CIPullRequestDTO


T = TypeVar("T", bound="CIExecutionInfoDTO")


@_attrs_define
class CIExecutionInfoDTO:
    """
    Attributes:
        event (str | Unset):
        pull_request (CIPullRequestDTO | Unset):
    """

    event: str | Unset = UNSET
    pull_request: CIPullRequestDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        pull_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pull_request, Unset):
            pull_request = self.pull_request.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if pull_request is not UNSET:
            field_dict["pullRequest"] = pull_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ci_pull_request_dto import CIPullRequestDTO

        d = dict(src_dict)
        event = d.pop("event", UNSET)

        _pull_request = d.pop("pullRequest", UNSET)
        pull_request: CIPullRequestDTO | Unset
        if isinstance(_pull_request, Unset):
            pull_request = UNSET
        else:
            pull_request = CIPullRequestDTO.from_dict(_pull_request)

        ci_execution_info_dto = cls(
            event=event,
            pull_request=pull_request,
        )

        ci_execution_info_dto.additional_properties = d
        return ci_execution_info_dto

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
