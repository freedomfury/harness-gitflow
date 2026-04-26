from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_principal_info_principal_type import (
    ExecutionPrincipalInfoPrincipalType,
    check_execution_principal_info_principal_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.execution_principal_info_all_fields import ExecutionPrincipalInfoAllFields
    from ..models.parser_execution_principal_info import ParserExecutionPrincipalInfo
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ExecutionPrincipalInfo")


@_attrs_define
class ExecutionPrincipalInfo:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        initialized (bool | Unset):
        default_instance_for_type (ExecutionPrincipalInfo | Unset):
        parser_for_type (ParserExecutionPrincipalInfo | Unset):
        serialized_size (int | Unset):
        principal (str | Unset):
        principal_bytes (ByteString | Unset):
        principal_type_value (int | Unset):
        principal_type (ExecutionPrincipalInfoPrincipalType | Unset):
        should_validate_rbac (bool | Unset):
        all_fields (ExecutionPrincipalInfoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: ExecutionPrincipalInfo | Unset = UNSET
    parser_for_type: ParserExecutionPrincipalInfo | Unset = UNSET
    serialized_size: int | Unset = UNSET
    principal: str | Unset = UNSET
    principal_bytes: ByteString | Unset = UNSET
    principal_type_value: int | Unset = UNSET
    principal_type: ExecutionPrincipalInfoPrincipalType | Unset = UNSET
    should_validate_rbac: bool | Unset = UNSET
    all_fields: ExecutionPrincipalInfoAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        principal = self.principal

        principal_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.principal_bytes, Unset):
            principal_bytes = self.principal_bytes.to_dict()

        principal_type_value = self.principal_type_value

        principal_type: str | Unset = UNSET
        if not isinstance(self.principal_type, Unset):
            principal_type = self.principal_type

        should_validate_rbac = self.should_validate_rbac

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
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if principal is not UNSET:
            field_dict["principal"] = principal
        if principal_bytes is not UNSET:
            field_dict["principalBytes"] = principal_bytes
        if principal_type_value is not UNSET:
            field_dict["principalTypeValue"] = principal_type_value
        if principal_type is not UNSET:
            field_dict["principalType"] = principal_type
        if should_validate_rbac is not UNSET:
            field_dict["shouldValidateRbac"] = should_validate_rbac
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
        from ..models.execution_principal_info_all_fields import ExecutionPrincipalInfoAllFields
        from ..models.parser_execution_principal_info import ParserExecutionPrincipalInfo
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: ExecutionPrincipalInfo | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ExecutionPrincipalInfo.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserExecutionPrincipalInfo | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserExecutionPrincipalInfo.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        principal = d.pop("principal", UNSET)

        _principal_bytes = d.pop("principalBytes", UNSET)
        principal_bytes: ByteString | Unset
        if isinstance(_principal_bytes, Unset):
            principal_bytes = UNSET
        else:
            principal_bytes = ByteString.from_dict(_principal_bytes)

        principal_type_value = d.pop("principalTypeValue", UNSET)

        _principal_type = d.pop("principalType", UNSET)
        principal_type: ExecutionPrincipalInfoPrincipalType | Unset
        if isinstance(_principal_type, Unset):
            principal_type = UNSET
        else:
            principal_type = check_execution_principal_info_principal_type(_principal_type)

        should_validate_rbac = d.pop("shouldValidateRbac", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ExecutionPrincipalInfoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ExecutionPrincipalInfoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        execution_principal_info = cls(
            unknown_fields=unknown_fields,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            principal=principal,
            principal_bytes=principal_bytes,
            principal_type_value=principal_type_value,
            principal_type=principal_type,
            should_validate_rbac=should_validate_rbac,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        execution_principal_info.additional_properties = d
        return execution_principal_info

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
