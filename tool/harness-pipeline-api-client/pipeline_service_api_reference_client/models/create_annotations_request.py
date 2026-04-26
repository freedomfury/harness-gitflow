from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.annotation_entity import AnnotationEntity


T = TypeVar("T", bound="CreateAnnotationsRequest")


@_attrs_define
class CreateAnnotationsRequest:
    """Request to create or update pipeline annotations

    Attributes:
        org_id (str): Organization identifier
        project_id (str): Project identifier
        pipeline_id (str): Pipeline identifier
        plan_execution_id (str): Plan execution ID
        stage_execution_id (str): Stage execution ID
        annotations (list[AnnotationEntity]): List of annotations to create or update
    """

    org_id: str
    project_id: str
    pipeline_id: str
    plan_execution_id: str
    stage_execution_id: str
    annotations: list[AnnotationEntity]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        project_id = self.project_id

        pipeline_id = self.pipeline_id

        plan_execution_id = self.plan_execution_id

        stage_execution_id = self.stage_execution_id

        annotations = []
        for annotations_item_data in self.annotations:
            annotations_item = annotations_item_data.to_dict()
            annotations.append(annotations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "projectId": project_id,
                "pipelineId": pipeline_id,
                "planExecutionId": plan_execution_id,
                "stageExecutionId": stage_execution_id,
                "annotations": annotations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_entity import AnnotationEntity

        d = dict(src_dict)
        org_id = d.pop("orgId")

        project_id = d.pop("projectId")

        pipeline_id = d.pop("pipelineId")

        plan_execution_id = d.pop("planExecutionId")

        stage_execution_id = d.pop("stageExecutionId")

        annotations = []
        _annotations = d.pop("annotations")
        for annotations_item_data in _annotations:
            annotations_item = AnnotationEntity.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        create_annotations_request = cls(
            org_id=org_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            plan_execution_id=plan_execution_id,
            stage_execution_id=stage_execution_id,
            annotations=annotations,
        )

        create_annotations_request.additional_properties = d
        return create_annotations_request

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
