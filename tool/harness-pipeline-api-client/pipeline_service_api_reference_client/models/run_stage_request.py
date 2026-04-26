from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_stage_request_expression_values import RunStageRequestExpressionValues


T = TypeVar("T", bound="RunStageRequest")


@_attrs_define
class RunStageRequest:
    """Request Parameters needed to run specific Stages of a Pipeline

    Attributes:
        runtime_input_yaml (str | Unset):
        stage_identifiers (list[str] | Unset):
        expression_values (RunStageRequestExpressionValues | Unset):
    """

    runtime_input_yaml: str | Unset = UNSET
    stage_identifiers: list[str] | Unset = UNSET
    expression_values: RunStageRequestExpressionValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runtime_input_yaml = self.runtime_input_yaml

        stage_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.stage_identifiers, Unset):
            stage_identifiers = self.stage_identifiers

        expression_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expression_values, Unset):
            expression_values = self.expression_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if runtime_input_yaml is not UNSET:
            field_dict["runtimeInputYaml"] = runtime_input_yaml
        if stage_identifiers is not UNSET:
            field_dict["stageIdentifiers"] = stage_identifiers
        if expression_values is not UNSET:
            field_dict["expressionValues"] = expression_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_stage_request_expression_values import RunStageRequestExpressionValues

        d = dict(src_dict)
        runtime_input_yaml = d.pop("runtimeInputYaml", UNSET)

        stage_identifiers = cast(list[str], d.pop("stageIdentifiers", UNSET))

        _expression_values = d.pop("expressionValues", UNSET)
        expression_values: RunStageRequestExpressionValues | Unset
        if isinstance(_expression_values, Unset):
            expression_values = UNSET
        else:
            expression_values = RunStageRequestExpressionValues.from_dict(_expression_values)

        run_stage_request = cls(
            runtime_input_yaml=runtime_input_yaml,
            stage_identifiers=stage_identifiers,
            expression_values=expression_values,
        )

        run_stage_request.additional_properties = d
        return run_stage_request

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
