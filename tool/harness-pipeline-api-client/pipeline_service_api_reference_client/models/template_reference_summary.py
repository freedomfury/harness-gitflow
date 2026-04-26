from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_template_reference_summary import ParserTemplateReferenceSummary
    from ..models.template_reference_summary_all_fields import TemplateReferenceSummaryAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="TemplateReferenceSummary")


@_attrs_define
class TemplateReferenceSummary:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        name (str | Unset):
        initialized (bool | Unset):
        description (str | Unset):
        default_instance_for_type (TemplateReferenceSummary | Unset):
        parser_for_type (ParserTemplateReferenceSummary | Unset):
        serialized_size (int | Unset):
        name_bytes (ByteString | Unset):
        description_bytes (ByteString | Unset):
        template_ref_bytes (ByteString | Unset):
        version_label (str | Unset):
        version_label_bytes (ByteString | Unset):
        git_branch (str | Unset):
        git_branch_bytes (ByteString | Unset):
        uses (str | Unset):
        uses_bytes (ByteString | Unset):
        icon_name (str | Unset):
        icon_name_bytes (ByteString | Unset):
        template_ref (str | Unset):
        all_fields (TemplateReferenceSummaryAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    name: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    description: str | Unset = UNSET
    default_instance_for_type: TemplateReferenceSummary | Unset = UNSET
    parser_for_type: ParserTemplateReferenceSummary | Unset = UNSET
    serialized_size: int | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    description_bytes: ByteString | Unset = UNSET
    template_ref_bytes: ByteString | Unset = UNSET
    version_label: str | Unset = UNSET
    version_label_bytes: ByteString | Unset = UNSET
    git_branch: str | Unset = UNSET
    git_branch_bytes: ByteString | Unset = UNSET
    uses: str | Unset = UNSET
    uses_bytes: ByteString | Unset = UNSET
    icon_name: str | Unset = UNSET
    icon_name_bytes: ByteString | Unset = UNSET
    template_ref: str | Unset = UNSET
    all_fields: TemplateReferenceSummaryAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        name = self.name

        initialized = self.initialized

        description = self.description

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

        description_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description_bytes, Unset):
            description_bytes = self.description_bytes.to_dict()

        template_ref_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_ref_bytes, Unset):
            template_ref_bytes = self.template_ref_bytes.to_dict()

        version_label = self.version_label

        version_label_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version_label_bytes, Unset):
            version_label_bytes = self.version_label_bytes.to_dict()

        git_branch = self.git_branch

        git_branch_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_branch_bytes, Unset):
            git_branch_bytes = self.git_branch_bytes.to_dict()

        uses = self.uses

        uses_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uses_bytes, Unset):
            uses_bytes = self.uses_bytes.to_dict()

        icon_name = self.icon_name

        icon_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icon_name_bytes, Unset):
            icon_name_bytes = self.icon_name_bytes.to_dict()

        template_ref = self.template_ref

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
        if name is not UNSET:
            field_dict["name"] = name
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if description is not UNSET:
            field_dict["description"] = description
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if description_bytes is not UNSET:
            field_dict["descriptionBytes"] = description_bytes
        if template_ref_bytes is not UNSET:
            field_dict["templateRefBytes"] = template_ref_bytes
        if version_label is not UNSET:
            field_dict["versionLabel"] = version_label
        if version_label_bytes is not UNSET:
            field_dict["versionLabelBytes"] = version_label_bytes
        if git_branch is not UNSET:
            field_dict["gitBranch"] = git_branch
        if git_branch_bytes is not UNSET:
            field_dict["gitBranchBytes"] = git_branch_bytes
        if uses is not UNSET:
            field_dict["uses"] = uses
        if uses_bytes is not UNSET:
            field_dict["usesBytes"] = uses_bytes
        if icon_name is not UNSET:
            field_dict["iconName"] = icon_name
        if icon_name_bytes is not UNSET:
            field_dict["iconNameBytes"] = icon_name_bytes
        if template_ref is not UNSET:
            field_dict["templateRef"] = template_ref
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
        from ..models.parser_template_reference_summary import ParserTemplateReferenceSummary
        from ..models.template_reference_summary_all_fields import TemplateReferenceSummaryAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        name = d.pop("name", UNSET)

        initialized = d.pop("initialized", UNSET)

        description = d.pop("description", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: TemplateReferenceSummary | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = TemplateReferenceSummary.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserTemplateReferenceSummary | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserTemplateReferenceSummary.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        _description_bytes = d.pop("descriptionBytes", UNSET)
        description_bytes: ByteString | Unset
        if isinstance(_description_bytes, Unset):
            description_bytes = UNSET
        else:
            description_bytes = ByteString.from_dict(_description_bytes)

        _template_ref_bytes = d.pop("templateRefBytes", UNSET)
        template_ref_bytes: ByteString | Unset
        if isinstance(_template_ref_bytes, Unset):
            template_ref_bytes = UNSET
        else:
            template_ref_bytes = ByteString.from_dict(_template_ref_bytes)

        version_label = d.pop("versionLabel", UNSET)

        _version_label_bytes = d.pop("versionLabelBytes", UNSET)
        version_label_bytes: ByteString | Unset
        if isinstance(_version_label_bytes, Unset):
            version_label_bytes = UNSET
        else:
            version_label_bytes = ByteString.from_dict(_version_label_bytes)

        git_branch = d.pop("gitBranch", UNSET)

        _git_branch_bytes = d.pop("gitBranchBytes", UNSET)
        git_branch_bytes: ByteString | Unset
        if isinstance(_git_branch_bytes, Unset):
            git_branch_bytes = UNSET
        else:
            git_branch_bytes = ByteString.from_dict(_git_branch_bytes)

        uses = d.pop("uses", UNSET)

        _uses_bytes = d.pop("usesBytes", UNSET)
        uses_bytes: ByteString | Unset
        if isinstance(_uses_bytes, Unset):
            uses_bytes = UNSET
        else:
            uses_bytes = ByteString.from_dict(_uses_bytes)

        icon_name = d.pop("iconName", UNSET)

        _icon_name_bytes = d.pop("iconNameBytes", UNSET)
        icon_name_bytes: ByteString | Unset
        if isinstance(_icon_name_bytes, Unset):
            icon_name_bytes = UNSET
        else:
            icon_name_bytes = ByteString.from_dict(_icon_name_bytes)

        template_ref = d.pop("templateRef", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: TemplateReferenceSummaryAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = TemplateReferenceSummaryAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        template_reference_summary = cls(
            unknown_fields=unknown_fields,
            name=name,
            initialized=initialized,
            description=description,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            name_bytes=name_bytes,
            description_bytes=description_bytes,
            template_ref_bytes=template_ref_bytes,
            version_label=version_label,
            version_label_bytes=version_label_bytes,
            git_branch=git_branch,
            git_branch_bytes=git_branch_bytes,
            uses=uses,
            uses_bytes=uses_bytes,
            icon_name=icon_name,
            icon_name_bytes=icon_name_bytes,
            template_ref=template_ref,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        template_reference_summary.additional_properties = d
        return template_reference_summary

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
