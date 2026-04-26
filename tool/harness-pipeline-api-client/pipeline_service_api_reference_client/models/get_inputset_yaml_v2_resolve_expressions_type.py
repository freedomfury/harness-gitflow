from typing import Literal, cast

GetInputsetYamlV2ResolveExpressionsType = Literal["RESOLVE_ALL_EXPRESSIONS", "RESOLVE_TRIGGER_EXPRESSIONS", "UNKNOWN"]

GET_INPUTSET_YAML_V2_RESOLVE_EXPRESSIONS_TYPE_VALUES: set[GetInputsetYamlV2ResolveExpressionsType] = {
    "RESOLVE_ALL_EXPRESSIONS",
    "RESOLVE_TRIGGER_EXPRESSIONS",
    "UNKNOWN",
}


def check_get_inputset_yaml_v2_resolve_expressions_type(value: str) -> GetInputsetYamlV2ResolveExpressionsType:
    if value in GET_INPUTSET_YAML_V2_RESOLVE_EXPRESSIONS_TYPE_VALUES:
        return cast(GetInputsetYamlV2ResolveExpressionsType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INPUTSET_YAML_V2_RESOLVE_EXPRESSIONS_TYPE_VALUES!r}"
    )
