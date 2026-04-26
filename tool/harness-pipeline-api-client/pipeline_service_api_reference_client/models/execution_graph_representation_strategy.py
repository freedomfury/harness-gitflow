from typing import Literal, cast

ExecutionGraphRepresentationStrategy = Literal["camelCase"]

EXECUTION_GRAPH_REPRESENTATION_STRATEGY_VALUES: set[ExecutionGraphRepresentationStrategy] = {
    "camelCase",
}


def check_execution_graph_representation_strategy(value: str) -> ExecutionGraphRepresentationStrategy:
    if value in EXECUTION_GRAPH_REPRESENTATION_STRATEGY_VALUES:
        return cast(ExecutionGraphRepresentationStrategy, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXECUTION_GRAPH_REPRESENTATION_STRATEGY_VALUES!r}")
