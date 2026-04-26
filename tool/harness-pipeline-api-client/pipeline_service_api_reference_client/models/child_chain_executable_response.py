from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.child_chain_executable_response_all_fields import ChildChainExecutableResponseAllFields
    from ..models.descriptor import Descriptor
    from ..models.parser_child_chain_executable_response import ParserChildChainExecutableResponse
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ChildChainExecutableResponse")


@_attrs_define
class ChildChainExecutableResponse:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        pass_through_data (ByteString | Unset):
        last_link (bool | Unset):
        suspend (bool | Unset):
        next_child_id (str | Unset):
        next_child_id_bytes (ByteString | Unset):
        previous_child_id (str | Unset):
        previous_child_id_bytes (ByteString | Unset):
        initialized (bool | Unset):
        default_instance_for_type (ChildChainExecutableResponse | Unset):
        parser_for_type (ParserChildChainExecutableResponse | Unset):
        serialized_size (int | Unset):
        all_fields (ChildChainExecutableResponseAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    pass_through_data: ByteString | Unset = UNSET
    last_link: bool | Unset = UNSET
    suspend: bool | Unset = UNSET
    next_child_id: str | Unset = UNSET
    next_child_id_bytes: ByteString | Unset = UNSET
    previous_child_id: str | Unset = UNSET
    previous_child_id_bytes: ByteString | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: ChildChainExecutableResponse | Unset = UNSET
    parser_for_type: ParserChildChainExecutableResponse | Unset = UNSET
    serialized_size: int | Unset = UNSET
    all_fields: ChildChainExecutableResponseAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        pass_through_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pass_through_data, Unset):
            pass_through_data = self.pass_through_data.to_dict()

        last_link = self.last_link

        suspend = self.suspend

        next_child_id = self.next_child_id

        next_child_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_child_id_bytes, Unset):
            next_child_id_bytes = self.next_child_id_bytes.to_dict()

        previous_child_id = self.previous_child_id

        previous_child_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_child_id_bytes, Unset):
            previous_child_id_bytes = self.previous_child_id_bytes.to_dict()

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        initialization_error_string = self.initialization_error_string

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if pass_through_data is not UNSET:
            field_dict["passThroughData"] = pass_through_data
        if last_link is not UNSET:
            field_dict["lastLink"] = last_link
        if suspend is not UNSET:
            field_dict["suspend"] = suspend
        if next_child_id is not UNSET:
            field_dict["nextChildId"] = next_child_id
        if next_child_id_bytes is not UNSET:
            field_dict["nextChildIdBytes"] = next_child_id_bytes
        if previous_child_id is not UNSET:
            field_dict["previousChildId"] = previous_child_id
        if previous_child_id_bytes is not UNSET:
            field_dict["previousChildIdBytes"] = previous_child_id_bytes
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.byte_string import ByteString
        from ..models.child_chain_executable_response_all_fields import ChildChainExecutableResponseAllFields
        from ..models.descriptor import Descriptor
        from ..models.parser_child_chain_executable_response import ParserChildChainExecutableResponse
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _pass_through_data = d.pop("passThroughData", UNSET)
        pass_through_data: ByteString | Unset
        if isinstance(_pass_through_data, Unset):
            pass_through_data = UNSET
        else:
            pass_through_data = ByteString.from_dict(_pass_through_data)

        last_link = d.pop("lastLink", UNSET)

        suspend = d.pop("suspend", UNSET)

        next_child_id = d.pop("nextChildId", UNSET)

        _next_child_id_bytes = d.pop("nextChildIdBytes", UNSET)
        next_child_id_bytes: ByteString | Unset
        if isinstance(_next_child_id_bytes, Unset):
            next_child_id_bytes = UNSET
        else:
            next_child_id_bytes = ByteString.from_dict(_next_child_id_bytes)

        previous_child_id = d.pop("previousChildId", UNSET)

        _previous_child_id_bytes = d.pop("previousChildIdBytes", UNSET)
        previous_child_id_bytes: ByteString | Unset
        if isinstance(_previous_child_id_bytes, Unset):
            previous_child_id_bytes = UNSET
        else:
            previous_child_id_bytes = ByteString.from_dict(_previous_child_id_bytes)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: ChildChainExecutableResponse | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ChildChainExecutableResponse.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserChildChainExecutableResponse | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserChildChainExecutableResponse.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ChildChainExecutableResponseAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ChildChainExecutableResponseAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        child_chain_executable_response = cls(
            unknown_fields=unknown_fields,
            pass_through_data=pass_through_data,
            last_link=last_link,
            suspend=suspend,
            next_child_id=next_child_id,
            next_child_id_bytes=next_child_id_bytes,
            previous_child_id=previous_child_id,
            previous_child_id_bytes=previous_child_id_bytes,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        child_chain_executable_response.additional_properties = d
        return child_chain_executable_response

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
