from typing import Literal, cast

CreateBodyType = Literal["FILE", "FOLDER"]

CREATE_BODY_TYPE_VALUES: set[CreateBodyType] = {
    "FILE",
    "FOLDER",
}


def check_create_body_type(value: str) -> CreateBodyType:
    if value in CREATE_BODY_TYPE_VALUES:
        return cast(CreateBodyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_BODY_TYPE_VALUES!r}")
