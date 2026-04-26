from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.input_set_summary_response_input_set_type import (
    InputSetSummaryResponseInputSetType,
    check_input_set_summary_response_input_set_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_git_details import EntityGitDetails
    from ..models.input_set_error_wrapper import InputSetErrorWrapper
    from ..models.input_set_summary_response_overlay_set_error_details import (
        InputSetSummaryResponseOverlaySetErrorDetails,
    )
    from ..models.input_set_summary_response_tags import InputSetSummaryResponseTags


T = TypeVar("T", bound="InputSetSummaryResponse")


@_attrs_define
class InputSetSummaryResponse:
    """This is the view of the Input Set Summary.

    Attributes:
        identifier (str | Unset): Input Set Identifier
        name (str | Unset): Input Set Name
        pipeline_identifier (str | Unset): Pipeline Identifier for the entity.
        description (str | Unset): Input Set description
        input_set_type (InputSetSummaryResponseInputSetType | Unset): Type of Input Set. The default value is ALL.
        tags (InputSetSummaryResponseTags | Unset): Input Set tags
        git_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        created_at (int | Unset): Time at which the entity was created
        last_updated_at (int | Unset): Time at which the entity was last updated
        is_outdated (bool | Unset): This field is true if a Pipeline update has made this Input Set invalid, and cannot
            be used for Pipeline Execution
        input_set_error_details (InputSetErrorWrapper | Unset): This contains the error response if the Input Set save
            failed
        overlay_set_error_details (InputSetSummaryResponseOverlaySetErrorDetails | Unset): This contains the invalid
            references in the Overlay Input Set, along with a message why they are invalid
        entity_validity_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        modules (list[str] | Unset): Modules in which the Pipeline belongs
    """

    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    pipeline_identifier: str | Unset = UNSET
    description: str | Unset = UNSET
    input_set_type: InputSetSummaryResponseInputSetType | Unset = UNSET
    tags: InputSetSummaryResponseTags | Unset = UNSET
    git_details: EntityGitDetails | Unset = UNSET
    created_at: int | Unset = UNSET
    last_updated_at: int | Unset = UNSET
    is_outdated: bool | Unset = UNSET
    input_set_error_details: InputSetErrorWrapper | Unset = UNSET
    overlay_set_error_details: InputSetSummaryResponseOverlaySetErrorDetails | Unset = UNSET
    entity_validity_details: EntityGitDetails | Unset = UNSET
    modules: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        pipeline_identifier = self.pipeline_identifier

        description = self.description

        input_set_type: str | Unset = UNSET
        if not isinstance(self.input_set_type, Unset):
            input_set_type = self.input_set_type

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

        created_at = self.created_at

        last_updated_at = self.last_updated_at

        is_outdated = self.is_outdated

        input_set_error_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_set_error_details, Unset):
            input_set_error_details = self.input_set_error_details.to_dict()

        overlay_set_error_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overlay_set_error_details, Unset):
            overlay_set_error_details = self.overlay_set_error_details.to_dict()

        entity_validity_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_validity_details, Unset):
            entity_validity_details = self.entity_validity_details.to_dict()

        modules: list[str] | Unset = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if description is not UNSET:
            field_dict["description"] = description
        if input_set_type is not UNSET:
            field_dict["inputSetType"] = input_set_type
        if tags is not UNSET:
            field_dict["tags"] = tags
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if is_outdated is not UNSET:
            field_dict["isOutdated"] = is_outdated
        if input_set_error_details is not UNSET:
            field_dict["inputSetErrorDetails"] = input_set_error_details
        if overlay_set_error_details is not UNSET:
            field_dict["overlaySetErrorDetails"] = overlay_set_error_details
        if entity_validity_details is not UNSET:
            field_dict["entityValidityDetails"] = entity_validity_details
        if modules is not UNSET:
            field_dict["modules"] = modules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_git_details import EntityGitDetails
        from ..models.input_set_error_wrapper import InputSetErrorWrapper
        from ..models.input_set_summary_response_overlay_set_error_details import (
            InputSetSummaryResponseOverlaySetErrorDetails,
        )
        from ..models.input_set_summary_response_tags import InputSetSummaryResponseTags

        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        description = d.pop("description", UNSET)

        _input_set_type = d.pop("inputSetType", UNSET)
        input_set_type: InputSetSummaryResponseInputSetType | Unset
        if isinstance(_input_set_type, Unset):
            input_set_type = UNSET
        else:
            input_set_type = check_input_set_summary_response_input_set_type(_input_set_type)

        _tags = d.pop("tags", UNSET)
        tags: InputSetSummaryResponseTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = InputSetSummaryResponseTags.from_dict(_tags)

        _git_details = d.pop("gitDetails", UNSET)
        git_details: EntityGitDetails | Unset
        if isinstance(_git_details, Unset):
            git_details = UNSET
        else:
            git_details = EntityGitDetails.from_dict(_git_details)

        created_at = d.pop("createdAt", UNSET)

        last_updated_at = d.pop("lastUpdatedAt", UNSET)

        is_outdated = d.pop("isOutdated", UNSET)

        _input_set_error_details = d.pop("inputSetErrorDetails", UNSET)
        input_set_error_details: InputSetErrorWrapper | Unset
        if isinstance(_input_set_error_details, Unset):
            input_set_error_details = UNSET
        else:
            input_set_error_details = InputSetErrorWrapper.from_dict(_input_set_error_details)

        _overlay_set_error_details = d.pop("overlaySetErrorDetails", UNSET)
        overlay_set_error_details: InputSetSummaryResponseOverlaySetErrorDetails | Unset
        if isinstance(_overlay_set_error_details, Unset):
            overlay_set_error_details = UNSET
        else:
            overlay_set_error_details = InputSetSummaryResponseOverlaySetErrorDetails.from_dict(
                _overlay_set_error_details
            )

        _entity_validity_details = d.pop("entityValidityDetails", UNSET)
        entity_validity_details: EntityGitDetails | Unset
        if isinstance(_entity_validity_details, Unset):
            entity_validity_details = UNSET
        else:
            entity_validity_details = EntityGitDetails.from_dict(_entity_validity_details)

        modules = cast(list[str], d.pop("modules", UNSET))

        input_set_summary_response = cls(
            identifier=identifier,
            name=name,
            pipeline_identifier=pipeline_identifier,
            description=description,
            input_set_type=input_set_type,
            tags=tags,
            git_details=git_details,
            created_at=created_at,
            last_updated_at=last_updated_at,
            is_outdated=is_outdated,
            input_set_error_details=input_set_error_details,
            overlay_set_error_details=overlay_set_error_details,
            entity_validity_details=entity_validity_details,
            modules=modules,
        )

        input_set_summary_response.additional_properties = d
        return input_set_summary_response

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
