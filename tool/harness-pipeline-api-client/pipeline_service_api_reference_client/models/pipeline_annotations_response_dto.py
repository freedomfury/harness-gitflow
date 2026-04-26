from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pipeline_annotation import PipelineAnnotation


T = TypeVar("T", bound="PipelineAnnotationsResponseDTO")


@_attrs_define
class PipelineAnnotationsResponseDTO:
    """
    Attributes:
        account_id (str):
        org_id (str):
        project_id (str):
        pipeline_id (str):
        plan_execution_id (str):
        annotations (list[PipelineAnnotation]):
        created_at (int):
        last_updated_at (int):
    """

    account_id: str
    org_id: str
    project_id: str
    pipeline_id: str
    plan_execution_id: str
    annotations: list[PipelineAnnotation]
    created_at: int
    last_updated_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        org_id = self.org_id

        project_id = self.project_id

        pipeline_id = self.pipeline_id

        plan_execution_id = self.plan_execution_id

        annotations = []
        for annotations_item_data in self.annotations:
            annotations_item = annotations_item_data.to_dict()
            annotations.append(annotations_item)

        created_at = self.created_at

        last_updated_at = self.last_updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "orgId": org_id,
                "projectId": project_id,
                "pipelineId": pipeline_id,
                "planExecutionId": plan_execution_id,
                "annotations": annotations,
                "createdAt": created_at,
                "lastUpdatedAt": last_updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_annotation import PipelineAnnotation

        d = dict(src_dict)
        account_id = d.pop("accountId")

        org_id = d.pop("orgId")

        project_id = d.pop("projectId")

        pipeline_id = d.pop("pipelineId")

        plan_execution_id = d.pop("planExecutionId")

        annotations = []
        _annotations = d.pop("annotations")
        for annotations_item_data in _annotations:
            annotations_item = PipelineAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        created_at = d.pop("createdAt")

        last_updated_at = d.pop("lastUpdatedAt")

        pipeline_annotations_response_dto = cls(
            account_id=account_id,
            org_id=org_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            plan_execution_id=plan_execution_id,
            annotations=annotations,
            created_at=created_at,
            last_updated_at=last_updated_at,
        )

        pipeline_annotations_response_dto.additional_properties = d
        return pipeline_annotations_response_dto

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
