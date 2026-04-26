from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_rule_state import EnumRuleState
from ..models.enum_rule_type import EnumRuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesRuleInfo")


@_attrs_define
class TypesRuleInfo:
    """
    Attributes:
        identifier (str | Unset):
        repo_path (str | Unset):
        space_path (str | Unset):
        state (EnumRuleState | Unset):
        type_ (EnumRuleType | Unset):
    """

    identifier: str | Unset = UNSET
    repo_path: str | Unset = UNSET
    space_path: str | Unset = UNSET
    state: EnumRuleState | Unset = UNSET
    type_: EnumRuleType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        repo_path = self.repo_path

        space_path = self.space_path

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if repo_path is not UNSET:
            field_dict["repo_path"] = repo_path
        if space_path is not UNSET:
            field_dict["space_path"] = space_path
        if state is not UNSET:
            field_dict["state"] = state
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        repo_path = d.pop("repo_path", UNSET)

        space_path = d.pop("space_path", UNSET)

        _state = d.pop("state", UNSET)
        state: EnumRuleState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = EnumRuleState(_state)

        _type_ = d.pop("type", UNSET)
        type_: EnumRuleType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnumRuleType(_type_)

        types_rule_info = cls(
            identifier=identifier,
            repo_path=repo_path,
            space_path=space_path,
            state=state,
            type_=type_,
        )

        types_rule_info.additional_properties = d
        return types_rule_info

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
