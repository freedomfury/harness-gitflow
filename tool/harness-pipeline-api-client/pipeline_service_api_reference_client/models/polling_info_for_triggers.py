from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.perpetual_task_info_for_triggers import PerpetualTaskInfoForTriggers
    from ..models.polled_response import PolledResponse


T = TypeVar("T", bound="PollingInfoForTriggers")


@_attrs_define
class PollingInfoForTriggers:
    """
    Attributes:
        perpetual_task_id (str | Unset):
        polled_response (PolledResponse | Unset):
        polling_doc_id (str | Unset):
        perpetual_task_info_for_triggers (PerpetualTaskInfoForTriggers | Unset):
    """

    perpetual_task_id: str | Unset = UNSET
    polled_response: PolledResponse | Unset = UNSET
    polling_doc_id: str | Unset = UNSET
    perpetual_task_info_for_triggers: PerpetualTaskInfoForTriggers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        perpetual_task_id = self.perpetual_task_id

        polled_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.polled_response, Unset):
            polled_response = self.polled_response.to_dict()

        polling_doc_id = self.polling_doc_id

        perpetual_task_info_for_triggers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.perpetual_task_info_for_triggers, Unset):
            perpetual_task_info_for_triggers = self.perpetual_task_info_for_triggers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if perpetual_task_id is not UNSET:
            field_dict["perpetualTaskId"] = perpetual_task_id
        if polled_response is not UNSET:
            field_dict["polledResponse"] = polled_response
        if polling_doc_id is not UNSET:
            field_dict["pollingDocId"] = polling_doc_id
        if perpetual_task_info_for_triggers is not UNSET:
            field_dict["perpetualTaskInfoForTriggers"] = perpetual_task_info_for_triggers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.perpetual_task_info_for_triggers import PerpetualTaskInfoForTriggers
        from ..models.polled_response import PolledResponse

        d = dict(src_dict)
        perpetual_task_id = d.pop("perpetualTaskId", UNSET)

        _polled_response = d.pop("polledResponse", UNSET)
        polled_response: PolledResponse | Unset
        if isinstance(_polled_response, Unset):
            polled_response = UNSET
        else:
            polled_response = PolledResponse.from_dict(_polled_response)

        polling_doc_id = d.pop("pollingDocId", UNSET)

        _perpetual_task_info_for_triggers = d.pop("perpetualTaskInfoForTriggers", UNSET)
        perpetual_task_info_for_triggers: PerpetualTaskInfoForTriggers | Unset
        if isinstance(_perpetual_task_info_for_triggers, Unset):
            perpetual_task_info_for_triggers = UNSET
        else:
            perpetual_task_info_for_triggers = PerpetualTaskInfoForTriggers.from_dict(_perpetual_task_info_for_triggers)

        polling_info_for_triggers = cls(
            perpetual_task_id=perpetual_task_id,
            polled_response=polled_response,
            polling_doc_id=polling_doc_id,
            perpetual_task_info_for_triggers=perpetual_task_info_for_triggers,
        )

        polling_info_for_triggers.additional_properties = d
        return polling_info_for_triggers

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
