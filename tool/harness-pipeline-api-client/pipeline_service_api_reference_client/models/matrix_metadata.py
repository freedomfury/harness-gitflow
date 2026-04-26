from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.matrix_metadata_all_fields import MatrixMetadataAllFields
    from ..models.matrix_metadata_matrix_values import MatrixMetadataMatrixValues
    from ..models.matrix_metadata_matrix_values_map import MatrixMetadataMatrixValuesMap
    from ..models.parser_matrix_metadata import ParserMatrixMetadata
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="MatrixMetadata")


@_attrs_define
class MatrixMetadata:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        matrix_values_map (MatrixMetadataMatrixValuesMap | Unset):
        matrix_keys_to_skip_in_name_list (list[str] | Unset):
        matrix_values_count (int | Unset):
        matrix_values (MatrixMetadataMatrixValues | Unset):
        matrix_combination_list (list[int] | Unset):
        matrix_combination_count (int | Unset):
        sub_type (str | Unset):
        sub_type_bytes (ByteString | Unset):
        matrix_keys_to_skip_in_name_count (int | Unset):
        node_name_bytes (ByteString | Unset):
        node_name (str | Unset):
        initialized (bool | Unset):
        default_instance_for_type (MatrixMetadata | Unset):
        parser_for_type (ParserMatrixMetadata | Unset):
        serialized_size (int | Unset):
        all_fields (MatrixMetadataAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    matrix_values_map: MatrixMetadataMatrixValuesMap | Unset = UNSET
    matrix_keys_to_skip_in_name_list: list[str] | Unset = UNSET
    matrix_values_count: int | Unset = UNSET
    matrix_values: MatrixMetadataMatrixValues | Unset = UNSET
    matrix_combination_list: list[int] | Unset = UNSET
    matrix_combination_count: int | Unset = UNSET
    sub_type: str | Unset = UNSET
    sub_type_bytes: ByteString | Unset = UNSET
    matrix_keys_to_skip_in_name_count: int | Unset = UNSET
    node_name_bytes: ByteString | Unset = UNSET
    node_name: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: MatrixMetadata | Unset = UNSET
    parser_for_type: ParserMatrixMetadata | Unset = UNSET
    serialized_size: int | Unset = UNSET
    all_fields: MatrixMetadataAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        matrix_values_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matrix_values_map, Unset):
            matrix_values_map = self.matrix_values_map.to_dict()

        matrix_keys_to_skip_in_name_list: list[str] | Unset = UNSET
        if not isinstance(self.matrix_keys_to_skip_in_name_list, Unset):
            matrix_keys_to_skip_in_name_list = self.matrix_keys_to_skip_in_name_list

        matrix_values_count = self.matrix_values_count

        matrix_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matrix_values, Unset):
            matrix_values = self.matrix_values.to_dict()

        matrix_combination_list: list[int] | Unset = UNSET
        if not isinstance(self.matrix_combination_list, Unset):
            matrix_combination_list = self.matrix_combination_list

        matrix_combination_count = self.matrix_combination_count

        sub_type = self.sub_type

        sub_type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sub_type_bytes, Unset):
            sub_type_bytes = self.sub_type_bytes.to_dict()

        matrix_keys_to_skip_in_name_count = self.matrix_keys_to_skip_in_name_count

        node_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_name_bytes, Unset):
            node_name_bytes = self.node_name_bytes.to_dict()

        node_name = self.node_name

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
        if matrix_values_map is not UNSET:
            field_dict["matrixValuesMap"] = matrix_values_map
        if matrix_keys_to_skip_in_name_list is not UNSET:
            field_dict["matrixKeysToSkipInNameList"] = matrix_keys_to_skip_in_name_list
        if matrix_values_count is not UNSET:
            field_dict["matrixValuesCount"] = matrix_values_count
        if matrix_values is not UNSET:
            field_dict["matrixValues"] = matrix_values
        if matrix_combination_list is not UNSET:
            field_dict["matrixCombinationList"] = matrix_combination_list
        if matrix_combination_count is not UNSET:
            field_dict["matrixCombinationCount"] = matrix_combination_count
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if sub_type_bytes is not UNSET:
            field_dict["subTypeBytes"] = sub_type_bytes
        if matrix_keys_to_skip_in_name_count is not UNSET:
            field_dict["matrixKeysToSkipInNameCount"] = matrix_keys_to_skip_in_name_count
        if node_name_bytes is not UNSET:
            field_dict["nodeNameBytes"] = node_name_bytes
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
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
        from ..models.descriptor import Descriptor
        from ..models.matrix_metadata_all_fields import MatrixMetadataAllFields
        from ..models.matrix_metadata_matrix_values import MatrixMetadataMatrixValues
        from ..models.matrix_metadata_matrix_values_map import MatrixMetadataMatrixValuesMap
        from ..models.parser_matrix_metadata import ParserMatrixMetadata
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _matrix_values_map = d.pop("matrixValuesMap", UNSET)
        matrix_values_map: MatrixMetadataMatrixValuesMap | Unset
        if isinstance(_matrix_values_map, Unset):
            matrix_values_map = UNSET
        else:
            matrix_values_map = MatrixMetadataMatrixValuesMap.from_dict(_matrix_values_map)

        matrix_keys_to_skip_in_name_list = cast(list[str], d.pop("matrixKeysToSkipInNameList", UNSET))

        matrix_values_count = d.pop("matrixValuesCount", UNSET)

        _matrix_values = d.pop("matrixValues", UNSET)
        matrix_values: MatrixMetadataMatrixValues | Unset
        if isinstance(_matrix_values, Unset):
            matrix_values = UNSET
        else:
            matrix_values = MatrixMetadataMatrixValues.from_dict(_matrix_values)

        matrix_combination_list = cast(list[int], d.pop("matrixCombinationList", UNSET))

        matrix_combination_count = d.pop("matrixCombinationCount", UNSET)

        sub_type = d.pop("subType", UNSET)

        _sub_type_bytes = d.pop("subTypeBytes", UNSET)
        sub_type_bytes: ByteString | Unset
        if isinstance(_sub_type_bytes, Unset):
            sub_type_bytes = UNSET
        else:
            sub_type_bytes = ByteString.from_dict(_sub_type_bytes)

        matrix_keys_to_skip_in_name_count = d.pop("matrixKeysToSkipInNameCount", UNSET)

        _node_name_bytes = d.pop("nodeNameBytes", UNSET)
        node_name_bytes: ByteString | Unset
        if isinstance(_node_name_bytes, Unset):
            node_name_bytes = UNSET
        else:
            node_name_bytes = ByteString.from_dict(_node_name_bytes)

        node_name = d.pop("nodeName", UNSET)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: MatrixMetadata | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = MatrixMetadata.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserMatrixMetadata | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserMatrixMetadata.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: MatrixMetadataAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = MatrixMetadataAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        matrix_metadata = cls(
            unknown_fields=unknown_fields,
            matrix_values_map=matrix_values_map,
            matrix_keys_to_skip_in_name_list=matrix_keys_to_skip_in_name_list,
            matrix_values_count=matrix_values_count,
            matrix_values=matrix_values,
            matrix_combination_list=matrix_combination_list,
            matrix_combination_count=matrix_combination_count,
            sub_type=sub_type,
            sub_type_bytes=sub_type_bytes,
            matrix_keys_to_skip_in_name_count=matrix_keys_to_skip_in_name_count,
            node_name_bytes=node_name_bytes,
            node_name=node_name,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        matrix_metadata.additional_properties = d
        return matrix_metadata

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
