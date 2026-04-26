from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_pull_req_state import EnumPullReqState
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenapiStatePullReqRequest")


@_attrs_define
class OpenapiStatePullReqRequest:
    """
    Attributes:
        is_draft (bool | Unset):
        state (EnumPullReqState | Unset):
    """

    is_draft: bool | Unset = UNSET
    state: EnumPullReqState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_draft = self.is_draft

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_draft is not UNSET:
            field_dict["is_draft"] = is_draft
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_draft = d.pop("is_draft", UNSET)

        _state = d.pop("state", UNSET)
        state: EnumPullReqState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = EnumPullReqState(_state)

        openapi_state_pull_req_request = cls(
            is_draft=is_draft,
            state=state,
        )

        openapi_state_pull_req_request.additional_properties = d
        return openapi_state_pull_req_request

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
