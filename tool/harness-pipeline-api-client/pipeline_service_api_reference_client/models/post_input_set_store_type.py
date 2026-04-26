from typing import Literal, cast

PostInputSetStoreType = Literal["INLINE", "INLINE_HC", "REMOTE"]

POST_INPUT_SET_STORE_TYPE_VALUES: set[PostInputSetStoreType] = {
    "INLINE",
    "INLINE_HC",
    "REMOTE",
}


def check_post_input_set_store_type(value: str) -> PostInputSetStoreType:
    if value in POST_INPUT_SET_STORE_TYPE_VALUES:
        return cast(PostInputSetStoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_INPUT_SET_STORE_TYPE_VALUES!r}")
