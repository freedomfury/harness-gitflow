from typing import Literal, cast

RecurrenceType = Literal["Daily", "Monthly", "Weekly", "Yearly"]

RECURRENCE_TYPE_VALUES: set[RecurrenceType] = {
    "Daily",
    "Monthly",
    "Weekly",
    "Yearly",
}


def check_recurrence_type(value: str) -> RecurrenceType:
    if value in RECURRENCE_TYPE_VALUES:
        return cast(RecurrenceType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECURRENCE_TYPE_VALUES!r}")
