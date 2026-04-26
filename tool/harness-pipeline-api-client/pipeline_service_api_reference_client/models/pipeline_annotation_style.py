from typing import Literal, cast

PipelineAnnotationStyle = Literal["error", "info", "success", "warning"]

PIPELINE_ANNOTATION_STYLE_VALUES: set[PipelineAnnotationStyle] = {
    "error",
    "info",
    "success",
    "warning",
}


def check_pipeline_annotation_style(value: str) -> PipelineAnnotationStyle:
    if value in PIPELINE_ANNOTATION_STYLE_VALUES:
        return cast(PipelineAnnotationStyle, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PIPELINE_ANNOTATION_STYLE_VALUES!r}")
