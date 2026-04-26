from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionDataResponse")


@_attrs_define
class ExecutionDataResponse:
    """This contains Execution metadata details.

    Attributes:
        execution_id (str | Unset): The plan ExecutionID
        execution_yaml (str | Unset): Execution YAML - Prepared after resolving runtime inputs and templates.
    """

    execution_id: str | Unset = UNSET
    execution_yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        execution_yaml = self.execution_yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if execution_yaml is not UNSET:
            field_dict["executionYaml"] = execution_yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("executionId", UNSET)

        execution_yaml = d.pop("executionYaml", UNSET)

        execution_data_response = cls(
            execution_id=execution_id,
            execution_yaml=execution_yaml,
        )

        execution_data_response.additional_properties = d
        return execution_data_response

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
