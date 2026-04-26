from typing import Literal, cast

PostOverlayInputSetStoreType = Literal["INLINE", "INLINE_HC", "REMOTE"]

POST_OVERLAY_INPUT_SET_STORE_TYPE_VALUES: set[PostOverlayInputSetStoreType] = {
    "INLINE",
    "INLINE_HC",
    "REMOTE",
}


def check_post_overlay_input_set_store_type(value: str) -> PostOverlayInputSetStoreType:
    if value in POST_OVERLAY_INPUT_SET_STORE_TYPE_VALUES:
        return cast(PostOverlayInputSetStoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_OVERLAY_INPUT_SET_STORE_TYPE_VALUES!r}")
