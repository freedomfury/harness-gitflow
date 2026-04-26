from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineImportRequest")


@_attrs_define
class PipelineImportRequest:
    """Contains basic information required to be linked with imported Pipeline YAML

    Attributes:
        pipeline_name (str | Unset): Expected Name of the Pipeline to be imported
        pipeline_description (str | Unset): Expected Description of the Pipeline to be imported
        version (str | Unset): YAML Version of the Pipeline
    """

    pipeline_name: str | Unset = UNSET
    pipeline_description: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pipeline_name = self.pipeline_name

        pipeline_description = self.pipeline_description

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_name is not UNSET:
            field_dict["pipelineName"] = pipeline_name
        if pipeline_description is not UNSET:
            field_dict["pipelineDescription"] = pipeline_description
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pipeline_name = d.pop("pipelineName", UNSET)

        pipeline_description = d.pop("pipelineDescription", UNSET)

        version = d.pop("version", UNSET)

        pipeline_import_request = cls(
            pipeline_name=pipeline_name,
            pipeline_description=pipeline_description,
            version=version,
        )

        pipeline_import_request.additional_properties = d
        return pipeline_import_request

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
