from typing import Literal, cast

CacheResponseMetadataCacheState = Literal["STALE_CACHE", "UNKNOWN", "VALID_CACHE"]

CACHE_RESPONSE_METADATA_CACHE_STATE_VALUES: set[CacheResponseMetadataCacheState] = {
    "STALE_CACHE",
    "UNKNOWN",
    "VALID_CACHE",
}


def check_cache_response_metadata_cache_state(value: str) -> CacheResponseMetadataCacheState:
    if value in CACHE_RESPONSE_METADATA_CACHE_STATE_VALUES:
        return cast(CacheResponseMetadataCacheState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CACHE_RESPONSE_METADATA_CACHE_STATE_VALUES!r}")
