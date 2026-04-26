from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_payload_build_data_case import TriggerPayloadBuildDataCase, check_trigger_payload_build_data_case
from ..models.trigger_payload_source_type import TriggerPayloadSourceType, check_trigger_payload_source_type
from ..models.trigger_payload_type import TriggerPayloadType, check_trigger_payload_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact_data import ArtifactData
    from ..models.artifact_data_or_builder import ArtifactDataOrBuilder
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.manifest_data import ManifestData
    from ..models.manifest_data_or_builder import ManifestDataOrBuilder
    from ..models.parsed_payload import ParsedPayload
    from ..models.parsed_payload_or_builder import ParsedPayloadOrBuilder
    from ..models.parser_trigger_payload import ParserTriggerPayload
    from ..models.trigger_payload_all_fields import TriggerPayloadAllFields
    from ..models.trigger_payload_headers import TriggerPayloadHeaders
    from ..models.trigger_payload_headers_map import TriggerPayloadHeadersMap
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="TriggerPayload")


@_attrs_define
class TriggerPayload:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        parsed_payload (ParsedPayload | Unset):
        changed_files_list (list[str] | Unset):
        headers_map (TriggerPayloadHeadersMap | Unset):
        artifact_data (ArtifactData | Unset):
        manifest_data (ManifestData | Unset):
        type_value (int | Unset):
        headers_count (int | Unset):
        source_type_value (int | Unset):
        artifact_data_or_builder (ArtifactDataOrBuilder | Unset):
        manifest_data_or_builder (ManifestDataOrBuilder | Unset):
        connector_ref_bytes (ByteString | Unset):
        image_path_bytes (ByteString | Unset):
        changed_files_count (int | Unset):
        build_data_case (TriggerPayloadBuildDataCase | Unset):
        parsed_payload_or_builder (ParsedPayloadOrBuilder | Unset):
        type_ (TriggerPayloadType | Unset):
        version (int | Unset):
        image_path (str | Unset):
        initialized (bool | Unset):
        headers (TriggerPayloadHeaders | Unset):
        default_instance_for_type (TriggerPayload | Unset):
        parser_for_type (ParserTriggerPayload | Unset):
        serialized_size (int | Unset):
        connector_ref (str | Unset):
        source_type (TriggerPayloadSourceType | Unset):
        all_fields (TriggerPayloadAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    parsed_payload: ParsedPayload | Unset = UNSET
    changed_files_list: list[str] | Unset = UNSET
    headers_map: TriggerPayloadHeadersMap | Unset = UNSET
    artifact_data: ArtifactData | Unset = UNSET
    manifest_data: ManifestData | Unset = UNSET
    type_value: int | Unset = UNSET
    headers_count: int | Unset = UNSET
    source_type_value: int | Unset = UNSET
    artifact_data_or_builder: ArtifactDataOrBuilder | Unset = UNSET
    manifest_data_or_builder: ManifestDataOrBuilder | Unset = UNSET
    connector_ref_bytes: ByteString | Unset = UNSET
    image_path_bytes: ByteString | Unset = UNSET
    changed_files_count: int | Unset = UNSET
    build_data_case: TriggerPayloadBuildDataCase | Unset = UNSET
    parsed_payload_or_builder: ParsedPayloadOrBuilder | Unset = UNSET
    type_: TriggerPayloadType | Unset = UNSET
    version: int | Unset = UNSET
    image_path: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    headers: TriggerPayloadHeaders | Unset = UNSET
    default_instance_for_type: TriggerPayload | Unset = UNSET
    parser_for_type: ParserTriggerPayload | Unset = UNSET
    serialized_size: int | Unset = UNSET
    connector_ref: str | Unset = UNSET
    source_type: TriggerPayloadSourceType | Unset = UNSET
    all_fields: TriggerPayloadAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        parsed_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parsed_payload, Unset):
            parsed_payload = self.parsed_payload.to_dict()

        changed_files_list: list[str] | Unset = UNSET
        if not isinstance(self.changed_files_list, Unset):
            changed_files_list = self.changed_files_list

        headers_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers_map, Unset):
            headers_map = self.headers_map.to_dict()

        artifact_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.artifact_data, Unset):
            artifact_data = self.artifact_data.to_dict()

        manifest_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manifest_data, Unset):
            manifest_data = self.manifest_data.to_dict()

        type_value = self.type_value

        headers_count = self.headers_count

        source_type_value = self.source_type_value

        artifact_data_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.artifact_data_or_builder, Unset):
            artifact_data_or_builder = self.artifact_data_or_builder.to_dict()

        manifest_data_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manifest_data_or_builder, Unset):
            manifest_data_or_builder = self.manifest_data_or_builder.to_dict()

        connector_ref_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connector_ref_bytes, Unset):
            connector_ref_bytes = self.connector_ref_bytes.to_dict()

        image_path_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_path_bytes, Unset):
            image_path_bytes = self.image_path_bytes.to_dict()

        changed_files_count = self.changed_files_count

        build_data_case: str | Unset = UNSET
        if not isinstance(self.build_data_case, Unset):
            build_data_case = self.build_data_case

        parsed_payload_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parsed_payload_or_builder, Unset):
            parsed_payload_or_builder = self.parsed_payload_or_builder.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        version = self.version

        image_path = self.image_path

        initialized = self.initialized

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        connector_ref = self.connector_ref

        source_type: str | Unset = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type

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
        if parsed_payload is not UNSET:
            field_dict["parsedPayload"] = parsed_payload
        if changed_files_list is not UNSET:
            field_dict["changedFilesList"] = changed_files_list
        if headers_map is not UNSET:
            field_dict["headersMap"] = headers_map
        if artifact_data is not UNSET:
            field_dict["artifactData"] = artifact_data
        if manifest_data is not UNSET:
            field_dict["manifestData"] = manifest_data
        if type_value is not UNSET:
            field_dict["typeValue"] = type_value
        if headers_count is not UNSET:
            field_dict["headersCount"] = headers_count
        if source_type_value is not UNSET:
            field_dict["sourceTypeValue"] = source_type_value
        if artifact_data_or_builder is not UNSET:
            field_dict["artifactDataOrBuilder"] = artifact_data_or_builder
        if manifest_data_or_builder is not UNSET:
            field_dict["manifestDataOrBuilder"] = manifest_data_or_builder
        if connector_ref_bytes is not UNSET:
            field_dict["connectorRefBytes"] = connector_ref_bytes
        if image_path_bytes is not UNSET:
            field_dict["imagePathBytes"] = image_path_bytes
        if changed_files_count is not UNSET:
            field_dict["changedFilesCount"] = changed_files_count
        if build_data_case is not UNSET:
            field_dict["buildDataCase"] = build_data_case
        if parsed_payload_or_builder is not UNSET:
            field_dict["parsedPayloadOrBuilder"] = parsed_payload_or_builder
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version
        if image_path is not UNSET:
            field_dict["imagePath"] = image_path
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if headers is not UNSET:
            field_dict["headers"] = headers
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if connector_ref is not UNSET:
            field_dict["connectorRef"] = connector_ref
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
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
        from ..models.artifact_data import ArtifactData
        from ..models.artifact_data_or_builder import ArtifactDataOrBuilder
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.manifest_data import ManifestData
        from ..models.manifest_data_or_builder import ManifestDataOrBuilder
        from ..models.parsed_payload import ParsedPayload
        from ..models.parsed_payload_or_builder import ParsedPayloadOrBuilder
        from ..models.parser_trigger_payload import ParserTriggerPayload
        from ..models.trigger_payload_all_fields import TriggerPayloadAllFields
        from ..models.trigger_payload_headers import TriggerPayloadHeaders
        from ..models.trigger_payload_headers_map import TriggerPayloadHeadersMap
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _parsed_payload = d.pop("parsedPayload", UNSET)
        parsed_payload: ParsedPayload | Unset
        if isinstance(_parsed_payload, Unset):
            parsed_payload = UNSET
        else:
            parsed_payload = ParsedPayload.from_dict(_parsed_payload)

        changed_files_list = cast(list[str], d.pop("changedFilesList", UNSET))

        _headers_map = d.pop("headersMap", UNSET)
        headers_map: TriggerPayloadHeadersMap | Unset
        if isinstance(_headers_map, Unset):
            headers_map = UNSET
        else:
            headers_map = TriggerPayloadHeadersMap.from_dict(_headers_map)

        _artifact_data = d.pop("artifactData", UNSET)
        artifact_data: ArtifactData | Unset
        if isinstance(_artifact_data, Unset):
            artifact_data = UNSET
        else:
            artifact_data = ArtifactData.from_dict(_artifact_data)

        _manifest_data = d.pop("manifestData", UNSET)
        manifest_data: ManifestData | Unset
        if isinstance(_manifest_data, Unset):
            manifest_data = UNSET
        else:
            manifest_data = ManifestData.from_dict(_manifest_data)

        type_value = d.pop("typeValue", UNSET)

        headers_count = d.pop("headersCount", UNSET)

        source_type_value = d.pop("sourceTypeValue", UNSET)

        _artifact_data_or_builder = d.pop("artifactDataOrBuilder", UNSET)
        artifact_data_or_builder: ArtifactDataOrBuilder | Unset
        if isinstance(_artifact_data_or_builder, Unset):
            artifact_data_or_builder = UNSET
        else:
            artifact_data_or_builder = ArtifactDataOrBuilder.from_dict(_artifact_data_or_builder)

        _manifest_data_or_builder = d.pop("manifestDataOrBuilder", UNSET)
        manifest_data_or_builder: ManifestDataOrBuilder | Unset
        if isinstance(_manifest_data_or_builder, Unset):
            manifest_data_or_builder = UNSET
        else:
            manifest_data_or_builder = ManifestDataOrBuilder.from_dict(_manifest_data_or_builder)

        _connector_ref_bytes = d.pop("connectorRefBytes", UNSET)
        connector_ref_bytes: ByteString | Unset
        if isinstance(_connector_ref_bytes, Unset):
            connector_ref_bytes = UNSET
        else:
            connector_ref_bytes = ByteString.from_dict(_connector_ref_bytes)

        _image_path_bytes = d.pop("imagePathBytes", UNSET)
        image_path_bytes: ByteString | Unset
        if isinstance(_image_path_bytes, Unset):
            image_path_bytes = UNSET
        else:
            image_path_bytes = ByteString.from_dict(_image_path_bytes)

        changed_files_count = d.pop("changedFilesCount", UNSET)

        _build_data_case = d.pop("buildDataCase", UNSET)
        build_data_case: TriggerPayloadBuildDataCase | Unset
        if isinstance(_build_data_case, Unset):
            build_data_case = UNSET
        else:
            build_data_case = check_trigger_payload_build_data_case(_build_data_case)

        _parsed_payload_or_builder = d.pop("parsedPayloadOrBuilder", UNSET)
        parsed_payload_or_builder: ParsedPayloadOrBuilder | Unset
        if isinstance(_parsed_payload_or_builder, Unset):
            parsed_payload_or_builder = UNSET
        else:
            parsed_payload_or_builder = ParsedPayloadOrBuilder.from_dict(_parsed_payload_or_builder)

        _type_ = d.pop("type", UNSET)
        type_: TriggerPayloadType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_trigger_payload_type(_type_)

        version = d.pop("version", UNSET)

        image_path = d.pop("imagePath", UNSET)

        initialized = d.pop("initialized", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: TriggerPayloadHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = TriggerPayloadHeaders.from_dict(_headers)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: TriggerPayload | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = TriggerPayload.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserTriggerPayload | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserTriggerPayload.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        connector_ref = d.pop("connectorRef", UNSET)

        _source_type = d.pop("sourceType", UNSET)
        source_type: TriggerPayloadSourceType | Unset
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = check_trigger_payload_source_type(_source_type)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: TriggerPayloadAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = TriggerPayloadAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        trigger_payload = cls(
            unknown_fields=unknown_fields,
            parsed_payload=parsed_payload,
            changed_files_list=changed_files_list,
            headers_map=headers_map,
            artifact_data=artifact_data,
            manifest_data=manifest_data,
            type_value=type_value,
            headers_count=headers_count,
            source_type_value=source_type_value,
            artifact_data_or_builder=artifact_data_or_builder,
            manifest_data_or_builder=manifest_data_or_builder,
            connector_ref_bytes=connector_ref_bytes,
            image_path_bytes=image_path_bytes,
            changed_files_count=changed_files_count,
            build_data_case=build_data_case,
            parsed_payload_or_builder=parsed_payload_or_builder,
            type_=type_,
            version=version,
            image_path=image_path,
            initialized=initialized,
            headers=headers,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            connector_ref=connector_ref,
            source_type=source_type,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        trigger_payload.additional_properties = d
        return trigger_payload

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
