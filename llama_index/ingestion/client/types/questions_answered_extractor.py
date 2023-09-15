# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from llama_index.bridge.pydantic import pydantic

from ..core.datetime_utils import serialize_datetime
from .base_llm_predictor import BaseLlmPredictor
from .metadata_mode import MetadataMode


class QuestionsAnsweredExtractor(pydantic.BaseModel):
    """
    Questions answered extractor. Node-level extractor.
    Extracts `questions_this_excerpt_can_answer` metadata field.
    Args:
        llm_predictor (Optional[BaseLLMPredictor]): LLM predictor
        questions (int): number of questions to extract
        prompt_template (str): template for question extraction,
        embedding_only (bool): whether to use embedding only
    """

    is_text_node_only: typing.Optional[bool]
    show_progress: typing.Optional[bool]
    metadata_mode: typing.Optional[MetadataMode]
    llm_predictor: BaseLlmPredictor = pydantic.Field(
        description="The LLMPredictor to use for generation."
    )
    questions: typing.Optional[int] = pydantic.Field(
        description="The number of questions to generate."
    )
    prompt_template: typing.Optional[str] = pydantic.Field(
        description="Prompt template to use when generating questions."
    )
    embedding_only: typing.Optional[bool] = pydantic.Field(
        description="Whether to use metadata for emebddings only."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
