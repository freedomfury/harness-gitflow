from typing import Literal, cast

DelegateGroupDetailsGroupImplicitSelectorsAdditionalProperty = Literal[
    "DELEGATE_NAME", "GROUP_NAME", "GROUP_SELECTORS", "HOST_NAME", "PROFILE_NAME", "PROFILE_SELECTORS"
]

DELEGATE_GROUP_DETAILS_GROUP_IMPLICIT_SELECTORS_ADDITIONAL_PROPERTY_VALUES: set[
    DelegateGroupDetailsGroupImplicitSelectorsAdditionalProperty
] = {
    "DELEGATE_NAME",
    "GROUP_NAME",
    "GROUP_SELECTORS",
    "HOST_NAME",
    "PROFILE_NAME",
    "PROFILE_SELECTORS",
}


def check_delegate_group_details_group_implicit_selectors_additional_property(
    value: str,
) -> DelegateGroupDetailsGroupImplicitSelectorsAdditionalProperty:
    if value in DELEGATE_GROUP_DETAILS_GROUP_IMPLICIT_SELECTORS_ADDITIONAL_PROPERTY_VALUES:
        return cast(DelegateGroupDetailsGroupImplicitSelectorsAdditionalProperty, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELEGATE_GROUP_DETAILS_GROUP_IMPLICIT_SELECTORS_ADDITIONAL_PROPERTY_VALUES!r}"
    )
