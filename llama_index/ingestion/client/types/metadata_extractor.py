# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from llama_index.bridge.pydantic import pydantic

from ..core.datetime_utils import serialize_datetime
from .metadata_feature_extractor import MetadataFeatureExtractor


class MetadataExtractor(pydantic.BaseModel):
    """
    Metadata extractor.
    """

    extractors: typing.Optional[typing.List[MetadataFeatureExtractor]] = pydantic.Field(
        description="Metadta feature extractors to apply to each node."
    )
    node_text_template: typing.Optional[str] = pydantic.Field(
        description="Template to represent how node text is mixed with metadata text."
    )
    disable_template_rewrite: typing.Optional[bool] = pydantic.Field(
        description="Disable the node template rewrite."
    )
    in_place: typing.Optional[bool] = pydantic.Field(
        description="Whether to process nodes in place."
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
