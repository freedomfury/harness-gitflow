from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostProdRollbackResponseDTO")


@_attrs_define
class PostProdRollbackResponseDTO:
    """
    Attributes:
        is_rollback_triggered (bool | Unset):
        instance_key (str | Unset):
        infra_mapping_id (str | Unset):
        plan_execution_id (str | Unset):
        message (str | Unset):
        rollback_triggered (bool | Unset):
    """

    is_rollback_triggered: bool | Unset = UNSET
    instance_key: str | Unset = UNSET
    infra_mapping_id: str | Unset = UNSET
    plan_execution_id: str | Unset = UNSET
    message: str | Unset = UNSET
    rollback_triggered: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_rollback_triggered = self.is_rollback_triggered

        instance_key = self.instance_key

        infra_mapping_id = self.infra_mapping_id

        plan_execution_id = self.plan_execution_id

        message = self.message

        rollback_triggered = self.rollback_triggered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_rollback_triggered is not UNSET:
            field_dict["isRollbackTriggered"] = is_rollback_triggered
        if instance_key is not UNSET:
            field_dict["instanceKey"] = instance_key
        if infra_mapping_id is not UNSET:
            field_dict["infraMappingId"] = infra_mapping_id
        if plan_execution_id is not UNSET:
            field_dict["planExecutionId"] = plan_execution_id
        if message is not UNSET:
            field_dict["message"] = message
        if rollback_triggered is not UNSET:
            field_dict["rollbackTriggered"] = rollback_triggered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_rollback_triggered = d.pop("isRollbackTriggered", UNSET)

        instance_key = d.pop("instanceKey", UNSET)

        infra_mapping_id = d.pop("infraMappingId", UNSET)

        plan_execution_id = d.pop("planExecutionId", UNSET)

        message = d.pop("message", UNSET)

        rollback_triggered = d.pop("rollbackTriggered", UNSET)

        post_prod_rollback_response_dto = cls(
            is_rollback_triggered=is_rollback_triggered,
            instance_key=instance_key,
            infra_mapping_id=infra_mapping_id,
            plan_execution_id=plan_execution_id,
            message=message,
            rollback_triggered=rollback_triggered,
        )

        post_prod_rollback_response_dto.additional_properties = d
        return post_prod_rollback_response_dto

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
