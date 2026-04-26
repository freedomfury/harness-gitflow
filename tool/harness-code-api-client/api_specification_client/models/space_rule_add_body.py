from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_rule_state import EnumRuleState
from ..models.openapi_rule_type import OpenapiRuleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_branch import ProtectionBranch
    from ..models.protection_pattern_type_0 import ProtectionPatternType0
    from ..models.protection_push import ProtectionPush
    from ..models.protection_repo_target_type_0 import ProtectionRepoTargetType0
    from ..models.protection_tag import ProtectionTag


T = TypeVar("T", bound="SpaceRuleAddBody")


@_attrs_define
class SpaceRuleAddBody:
    """
    Attributes:
        definition (ProtectionBranch | ProtectionPush | ProtectionTag | Unset):
        description (str | Unset):
        identifier (str | Unset):
        pattern (None | ProtectionPatternType0 | Unset):
        repo_target (None | ProtectionRepoTargetType0 | Unset):
        state (EnumRuleState | Unset):
        type_ (OpenapiRuleType | Unset):
        uid (str | Unset):
    """

    definition: ProtectionBranch | ProtectionPush | ProtectionTag | Unset = UNSET
    description: str | Unset = UNSET
    identifier: str | Unset = UNSET
    pattern: None | ProtectionPatternType0 | Unset = UNSET
    repo_target: None | ProtectionRepoTargetType0 | Unset = UNSET
    state: EnumRuleState | Unset = UNSET
    type_: OpenapiRuleType | Unset = UNSET
    uid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.protection_branch import ProtectionBranch
        from ..models.protection_pattern_type_0 import ProtectionPatternType0
        from ..models.protection_repo_target_type_0 import ProtectionRepoTargetType0
        from ..models.protection_tag import ProtectionTag

        definition: dict[str, Any] | Unset
        if isinstance(self.definition, Unset):
            definition = UNSET
        elif isinstance(self.definition, ProtectionBranch):
            definition = self.definition.to_dict()
        elif isinstance(self.definition, ProtectionTag):
            definition = self.definition.to_dict()
        else:
            definition = self.definition.to_dict()

        description = self.description

        identifier = self.identifier

        pattern: dict[str, Any] | None | Unset
        if isinstance(self.pattern, Unset):
            pattern = UNSET
        elif isinstance(self.pattern, ProtectionPatternType0):
            pattern = self.pattern.to_dict()
        else:
            pattern = self.pattern

        repo_target: dict[str, Any] | None | Unset
        if isinstance(self.repo_target, Unset):
            repo_target = UNSET
        elif isinstance(self.repo_target, ProtectionRepoTargetType0):
            repo_target = self.repo_target.to_dict()
        else:
            repo_target = self.repo_target

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if definition is not UNSET:
            field_dict["definition"] = definition
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if repo_target is not UNSET:
            field_dict["repo_target"] = repo_target
        if state is not UNSET:
            field_dict["state"] = state
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_branch import ProtectionBranch
        from ..models.protection_pattern_type_0 import ProtectionPatternType0
        from ..models.protection_push import ProtectionPush
        from ..models.protection_repo_target_type_0 import ProtectionRepoTargetType0
        from ..models.protection_tag import ProtectionTag

        d = dict(src_dict)

        def _parse_definition(data: object) -> ProtectionBranch | ProtectionPush | ProtectionTag | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_openapi_rule_definition_type_0 = ProtectionBranch.from_dict(data)

                return componentsschemas_openapi_rule_definition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_openapi_rule_definition_type_1 = ProtectionTag.from_dict(data)

                return componentsschemas_openapi_rule_definition_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_openapi_rule_definition_type_2 = ProtectionPush.from_dict(data)

            return componentsschemas_openapi_rule_definition_type_2

        definition = _parse_definition(d.pop("definition", UNSET))

        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        def _parse_pattern(data: object) -> None | ProtectionPatternType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_protection_pattern_type_0 = ProtectionPatternType0.from_dict(data)

                return componentsschemas_protection_pattern_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProtectionPatternType0 | Unset, data)

        pattern = _parse_pattern(d.pop("pattern", UNSET))

        def _parse_repo_target(data: object) -> None | ProtectionRepoTargetType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_protection_repo_target_type_0 = ProtectionRepoTargetType0.from_dict(data)

                return componentsschemas_protection_repo_target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProtectionRepoTargetType0 | Unset, data)

        repo_target = _parse_repo_target(d.pop("repo_target", UNSET))

        _state = d.pop("state", UNSET)
        state: EnumRuleState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = EnumRuleState(_state)

        _type_ = d.pop("type", UNSET)
        type_: OpenapiRuleType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OpenapiRuleType(_type_)

        uid = d.pop("uid", UNSET)

        space_rule_add_body = cls(
            definition=definition,
            description=description,
            identifier=identifier,
            pattern=pattern,
            repo_target=repo_target,
            state=state,
            type_=type_,
            uid=uid,
        )

        space_rule_add_body.additional_properties = d
        return space_rule_add_body

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
