from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_error_info import NodeErrorInfo


T = TypeVar("T", bound="YamlSchemaErrorDTO")


@_attrs_define
class YamlSchemaErrorDTO:
    """
    Attributes:
        message (str | Unset):
        message_with_fqn (str | Unset):
        stage_info (NodeErrorInfo | Unset):
        step_info (NodeErrorInfo | Unset):
        fqn (str | Unset):
        hint_message (str | Unset):
    """

    message: str | Unset = UNSET
    message_with_fqn: str | Unset = UNSET
    stage_info: NodeErrorInfo | Unset = UNSET
    step_info: NodeErrorInfo | Unset = UNSET
    fqn: str | Unset = UNSET
    hint_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        message_with_fqn = self.message_with_fqn

        stage_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stage_info, Unset):
            stage_info = self.stage_info.to_dict()

        step_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.step_info, Unset):
            step_info = self.step_info.to_dict()

        fqn = self.fqn

        hint_message = self.hint_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if message_with_fqn is not UNSET:
            field_dict["messageWithFQN"] = message_with_fqn
        if stage_info is not UNSET:
            field_dict["stageInfo"] = stage_info
        if step_info is not UNSET:
            field_dict["stepInfo"] = step_info
        if fqn is not UNSET:
            field_dict["fqn"] = fqn
        if hint_message is not UNSET:
            field_dict["hintMessage"] = hint_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_error_info import NodeErrorInfo

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        message_with_fqn = d.pop("messageWithFQN", UNSET)

        _stage_info = d.pop("stageInfo", UNSET)
        stage_info: NodeErrorInfo | Unset
        if isinstance(_stage_info, Unset):
            stage_info = UNSET
        else:
            stage_info = NodeErrorInfo.from_dict(_stage_info)

        _step_info = d.pop("stepInfo", UNSET)
        step_info: NodeErrorInfo | Unset
        if isinstance(_step_info, Unset):
            step_info = UNSET
        else:
            step_info = NodeErrorInfo.from_dict(_step_info)

        fqn = d.pop("fqn", UNSET)

        hint_message = d.pop("hintMessage", UNSET)

        yaml_schema_error_dto = cls(
            message=message,
            message_with_fqn=message_with_fqn,
            stage_info=stage_info,
            step_info=step_info,
            fqn=fqn,
            hint_message=hint_message,
        )

        yaml_schema_error_dto.additional_properties = d
        return yaml_schema_error_dto

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
