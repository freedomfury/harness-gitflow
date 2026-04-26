from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_node_summary import ErrorNodeSummary


T = TypeVar("T", bound="ValidateTemplateInputsResponseDTO")


@_attrs_define
class ValidateTemplateInputsResponseDTO:
    """
    Attributes:
        valid_yaml (bool | Unset):
        error_node_summary (ErrorNodeSummary | Unset):
        type_ (str | Unset):
    """

    valid_yaml: bool | Unset = UNSET
    error_node_summary: ErrorNodeSummary | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid_yaml = self.valid_yaml

        error_node_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_node_summary, Unset):
            error_node_summary = self.error_node_summary.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if valid_yaml is not UNSET:
            field_dict["validYaml"] = valid_yaml
        if error_node_summary is not UNSET:
            field_dict["errorNodeSummary"] = error_node_summary
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_node_summary import ErrorNodeSummary

        d = dict(src_dict)
        valid_yaml = d.pop("validYaml", UNSET)

        _error_node_summary = d.pop("errorNodeSummary", UNSET)
        error_node_summary: ErrorNodeSummary | Unset
        if isinstance(_error_node_summary, Unset):
            error_node_summary = UNSET
        else:
            error_node_summary = ErrorNodeSummary.from_dict(_error_node_summary)

        type_ = d.pop("type", UNSET)

        validate_template_inputs_response_dto = cls(
            valid_yaml=valid_yaml,
            error_node_summary=error_node_summary,
            type_=type_,
        )

        validate_template_inputs_response_dto.additional_properties = d
        return validate_template_inputs_response_dto

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
