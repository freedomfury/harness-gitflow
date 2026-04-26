from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_message import ResponseMessage
    from ..models.rest_response_version_overrides_response_meta_data import RestResponseVersionOverridesResponseMetaData
    from ..models.version_overrides_response import VersionOverridesResponse


T = TypeVar("T", bound="RestResponseVersionOverridesResponse")


@_attrs_define
class RestResponseVersionOverridesResponse:
    """
    Attributes:
        meta_data (RestResponseVersionOverridesResponseMetaData | Unset):
        resource (VersionOverridesResponse | Unset):
        response_messages (list[ResponseMessage] | Unset):
    """

    meta_data: RestResponseVersionOverridesResponseMetaData | Unset = UNSET
    resource: VersionOverridesResponse | Unset = UNSET
    response_messages: list[ResponseMessage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        response_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.response_messages, Unset):
            response_messages = []
            for response_messages_item_data in self.response_messages:
                response_messages_item = response_messages_item_data.to_dict()
                response_messages.append(response_messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if resource is not UNSET:
            field_dict["resource"] = resource
        if response_messages is not UNSET:
            field_dict["responseMessages"] = response_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_message import ResponseMessage
        from ..models.rest_response_version_overrides_response_meta_data import (
            RestResponseVersionOverridesResponseMetaData,
        )
        from ..models.version_overrides_response import VersionOverridesResponse

        d = dict(src_dict)
        _meta_data = d.pop("metaData", UNSET)
        meta_data: RestResponseVersionOverridesResponseMetaData | Unset
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = RestResponseVersionOverridesResponseMetaData.from_dict(_meta_data)

        _resource = d.pop("resource", UNSET)
        resource: VersionOverridesResponse | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = VersionOverridesResponse.from_dict(_resource)

        _response_messages = d.pop("responseMessages", UNSET)
        response_messages: list[ResponseMessage] | Unset = UNSET
        if _response_messages is not UNSET:
            response_messages = []
            for response_messages_item_data in _response_messages:
                response_messages_item = ResponseMessage.from_dict(response_messages_item_data)

                response_messages.append(response_messages_item)

        rest_response_version_overrides_response = cls(
            meta_data=meta_data,
            resource=resource,
            response_messages=response_messages,
        )

        rest_response_version_overrides_response.additional_properties = d
        return rest_response_version_overrides_response

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
