from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.unit_progress_status import UnitProgressStatus, check_unit_progress_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_unit_progress import ParserUnitProgress
    from ..models.unit_progress_all_fields import UnitProgressAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="UnitProgress")


@_attrs_define
class UnitProgress:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        end_time (int | Unset):
        initialized (bool | Unset):
        start_time (int | Unset):
        status (UnitProgressStatus | Unset):
        default_instance_for_type (UnitProgress | Unset):
        parser_for_type (ParserUnitProgress | Unset):
        serialized_size (int | Unset):
        unit_name_bytes (ByteString | Unset):
        status_value (int | Unset):
        unit_name (str | Unset):
        all_fields (UnitProgressAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    end_time: int | Unset = UNSET
    initialized: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    status: UnitProgressStatus | Unset = UNSET
    default_instance_for_type: UnitProgress | Unset = UNSET
    parser_for_type: ParserUnitProgress | Unset = UNSET
    serialized_size: int | Unset = UNSET
    unit_name_bytes: ByteString | Unset = UNSET
    status_value: int | Unset = UNSET
    unit_name: str | Unset = UNSET
    all_fields: UnitProgressAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        end_time = self.end_time

        initialized = self.initialized

        start_time = self.start_time

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        unit_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unit_name_bytes, Unset):
            unit_name_bytes = self.unit_name_bytes.to_dict()

        status_value = self.status_value

        unit_name = self.unit_name

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
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if unit_name_bytes is not UNSET:
            field_dict["unitNameBytes"] = unit_name_bytes
        if status_value is not UNSET:
            field_dict["statusValue"] = status_value
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
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
        from ..models.descriptor import Descriptor
        from ..models.parser_unit_progress import ParserUnitProgress
        from ..models.unit_progress_all_fields import UnitProgressAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        end_time = d.pop("endTime", UNSET)

        initialized = d.pop("initialized", UNSET)

        start_time = d.pop("startTime", UNSET)

        _status = d.pop("status", UNSET)
        status: UnitProgressStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_unit_progress_status(_status)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: UnitProgress | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = UnitProgress.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserUnitProgress | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserUnitProgress.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _unit_name_bytes = d.pop("unitNameBytes", UNSET)
        unit_name_bytes: ByteString | Unset
        if isinstance(_unit_name_bytes, Unset):
            unit_name_bytes = UNSET
        else:
            unit_name_bytes = ByteString.from_dict(_unit_name_bytes)

        status_value = d.pop("statusValue", UNSET)

        unit_name = d.pop("unitName", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: UnitProgressAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = UnitProgressAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        unit_progress = cls(
            unknown_fields=unknown_fields,
            end_time=end_time,
            initialized=initialized,
            start_time=start_time,
            status=status,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            unit_name_bytes=unit_name_bytes,
            status_value=status_value,
            unit_name=unit_name,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        unit_progress.additional_properties = d
        return unit_progress

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
