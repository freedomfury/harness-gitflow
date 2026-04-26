from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_webhook_execution_result import EnumWebhookExecutionResult
from ..models.enum_webhook_trigger import EnumWebhookTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_webhook_execution_request import TypesWebhookExecutionRequest
    from ..models.types_webhook_execution_response import TypesWebhookExecutionResponse


T = TypeVar("T", bound="TypesWebhookExecution")


@_attrs_define
class TypesWebhookExecution:
    """
    Attributes:
        created (int | Unset):
        duration (int | Unset):
        error (str | Unset):
        id (int | Unset):
        request (TypesWebhookExecutionRequest | Unset):
        response (TypesWebhookExecutionResponse | Unset):
        result (EnumWebhookExecutionResult | Unset):
        retrigger_of (int | None | Unset):
        retriggerable (bool | Unset):
        trigger_type (EnumWebhookTrigger | Unset):
        webhook_id (int | Unset):
    """

    created: int | Unset = UNSET
    duration: int | Unset = UNSET
    error: str | Unset = UNSET
    id: int | Unset = UNSET
    request: TypesWebhookExecutionRequest | Unset = UNSET
    response: TypesWebhookExecutionResponse | Unset = UNSET
    result: EnumWebhookExecutionResult | Unset = UNSET
    retrigger_of: int | None | Unset = UNSET
    retriggerable: bool | Unset = UNSET
    trigger_type: EnumWebhookTrigger | Unset = UNSET
    webhook_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        duration = self.duration

        error = self.error

        id = self.id

        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        retrigger_of: int | None | Unset
        if isinstance(self.retrigger_of, Unset):
            retrigger_of = UNSET
        else:
            retrigger_of = self.retrigger_of

        retriggerable = self.retriggerable

        trigger_type: str | Unset = UNSET
        if not isinstance(self.trigger_type, Unset):
            trigger_type = self.trigger_type.value

        webhook_id = self.webhook_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if duration is not UNSET:
            field_dict["duration"] = duration
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if request is not UNSET:
            field_dict["request"] = request
        if response is not UNSET:
            field_dict["response"] = response
        if result is not UNSET:
            field_dict["result"] = result
        if retrigger_of is not UNSET:
            field_dict["retrigger_of"] = retrigger_of
        if retriggerable is not UNSET:
            field_dict["retriggerable"] = retriggerable
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type
        if webhook_id is not UNSET:
            field_dict["webhook_id"] = webhook_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_webhook_execution_request import TypesWebhookExecutionRequest
        from ..models.types_webhook_execution_response import TypesWebhookExecutionResponse

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        duration = d.pop("duration", UNSET)

        error = d.pop("error", UNSET)

        id = d.pop("id", UNSET)

        _request = d.pop("request", UNSET)
        request: TypesWebhookExecutionRequest | Unset
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = TypesWebhookExecutionRequest.from_dict(_request)

        _response = d.pop("response", UNSET)
        response: TypesWebhookExecutionResponse | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = TypesWebhookExecutionResponse.from_dict(_response)

        _result = d.pop("result", UNSET)
        result: EnumWebhookExecutionResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = EnumWebhookExecutionResult(_result)

        def _parse_retrigger_of(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retrigger_of = _parse_retrigger_of(d.pop("retrigger_of", UNSET))

        retriggerable = d.pop("retriggerable", UNSET)

        _trigger_type = d.pop("trigger_type", UNSET)
        trigger_type: EnumWebhookTrigger | Unset
        if isinstance(_trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = EnumWebhookTrigger(_trigger_type)

        webhook_id = d.pop("webhook_id", UNSET)

        types_webhook_execution = cls(
            created=created,
            duration=duration,
            error=error,
            id=id,
            request=request,
            response=response,
            result=result,
            retrigger_of=retrigger_of,
            retriggerable=retriggerable,
            trigger_type=trigger_type,
            webhook_id=webhook_id,
        )

        types_webhook_execution.additional_properties = d
        return types_webhook_execution

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
