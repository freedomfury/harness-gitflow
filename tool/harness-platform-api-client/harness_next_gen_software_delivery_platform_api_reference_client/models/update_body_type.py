from typing import Literal, cast

UpdateBodyType = Literal["FILE", "FOLDER"]

UPDATE_BODY_TYPE_VALUES: set[UpdateBodyType] = {
    "FILE",
    "FOLDER",
}


def check_update_body_type(value: str) -> UpdateBodyType:
    if value in UPDATE_BODY_TYPE_VALUES:
        return cast(UpdateBodyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BODY_TYPE_VALUES!r}")
