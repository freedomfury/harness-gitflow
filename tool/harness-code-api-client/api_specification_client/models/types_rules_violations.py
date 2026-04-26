from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_rule_violations import TypesRuleViolations


T = TypeVar("T", bound="TypesRulesViolations")


@_attrs_define
class TypesRulesViolations:
    """
    Attributes:
        message (str | Unset):
        violations (list[TypesRuleViolations] | None | Unset):
    """

    message: str | Unset = UNSET
    violations: list[TypesRuleViolations] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        violations: list[dict[str, Any]] | None | Unset
        if isinstance(self.violations, Unset):
            violations = UNSET
        elif isinstance(self.violations, list):
            violations = []
            for violations_type_0_item_data in self.violations:
                violations_type_0_item = violations_type_0_item_data.to_dict()
                violations.append(violations_type_0_item)

        else:
            violations = self.violations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if violations is not UNSET:
            field_dict["violations"] = violations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_rule_violations import TypesRuleViolations

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        def _parse_violations(data: object) -> list[TypesRuleViolations] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                violations_type_0 = []
                _violations_type_0 = data
                for violations_type_0_item_data in _violations_type_0:
                    violations_type_0_item = TypesRuleViolations.from_dict(violations_type_0_item_data)

                    violations_type_0.append(violations_type_0_item)

                return violations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesRuleViolations] | None | Unset, data)

        violations = _parse_violations(d.pop("violations", UNSET))

        types_rules_violations = cls(
            message=message,
            violations=violations,
        )

        types_rules_violations.additional_properties = d
        return types_rules_violations

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
