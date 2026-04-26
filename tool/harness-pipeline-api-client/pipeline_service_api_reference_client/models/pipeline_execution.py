from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_count import PipelineCount


T = TypeVar("T", bound="PipelineExecution")


@_attrs_define
class PipelineExecution:
    """This is the view of the Pipeline Executions for a particular Date

    Attributes:
        date (int | Unset):
        count (PipelineCount | Unset): This is the view of the Pipeline Execution Count Info for a particular Date
    """

    date: int | Unset = UNSET
    count: PipelineCount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.count, Unset):
            count = self.count.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_count import PipelineCount

        d = dict(src_dict)
        date = d.pop("date", UNSET)

        _count = d.pop("count", UNSET)
        count: PipelineCount | Unset
        if isinstance(_count, Unset):
            count = UNSET
        else:
            count = PipelineCount.from_dict(_count)

        pipeline_execution = cls(
            date=date,
            count=count,
        )

        pipeline_execution.additional_properties = d
        return pipeline_execution

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
