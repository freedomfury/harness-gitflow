from typing import Literal, cast

ResponseDTOPageGovernanceMetadataStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_GOVERNANCE_METADATA_STATUS_VALUES: set[ResponseDTOPageGovernanceMetadataStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_governance_metadata_status(value: str) -> ResponseDTOPageGovernanceMetadataStatus:
    if value in RESPONSE_DTO_PAGE_GOVERNANCE_METADATA_STATUS_VALUES:
        return cast(ResponseDTOPageGovernanceMetadataStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_GOVERNANCE_METADATA_STATUS_VALUES!r}"
    )
