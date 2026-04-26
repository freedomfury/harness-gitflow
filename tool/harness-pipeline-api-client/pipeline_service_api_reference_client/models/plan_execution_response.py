from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_git_details import EntityGitDetails
    from ..models.plan_execution import PlanExecution


T = TypeVar("T", bound="PlanExecutionResponse")


@_attrs_define
class PlanExecutionResponse:
    """This contains info about the Pipeline Execution

    Attributes:
        plan_execution (PlanExecution | Unset):
        git_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
    """

    plan_execution: PlanExecution | Unset = UNSET
    git_details: EntityGitDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_execution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plan_execution, Unset):
            plan_execution = self.plan_execution.to_dict()

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_execution is not UNSET:
            field_dict["planExecution"] = plan_execution
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_git_details import EntityGitDetails
        from ..models.plan_execution import PlanExecution

        d = dict(src_dict)
        _plan_execution = d.pop("planExecution", UNSET)
        plan_execution: PlanExecution | Unset
        if isinstance(_plan_execution, Unset):
            plan_execution = UNSET
        else:
            plan_execution = PlanExecution.from_dict(_plan_execution)

        _git_details = d.pop("gitDetails", UNSET)
        git_details: EntityGitDetails | Unset
        if isinstance(_git_details, Unset):
            git_details = UNSET
        else:
            git_details = EntityGitDetails.from_dict(_git_details)

        plan_execution_response = cls(
            plan_execution=plan_execution,
            git_details=git_details,
        )

        plan_execution_response.additional_properties = d
        return plan_execution_response

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
